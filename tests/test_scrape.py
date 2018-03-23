import pytest
from extract.models import Topic, Listing
from extract.management.commands.scrape import Command


@pytest.mark.django_db
def test_initial_db():
    qs = Topic.objects.filter(is_active=True)
    assert qs.count() == 1, "2 active topics expected"
    t = Topic.objects.get(pk=2)
    assert t.listing_set.count() == 1, 'Second topic shall have one dummy listing'


@pytest.mark.django_db
def test_scrape_local(testdata):
    t = Topic.objects.get(pk=1)
    scraper = Command()

    assert scraper.scrape_topic(t, testdata.uri('minitools.html'), follow=False) == 35
    assert scraper.scrape_topic(t, testdata.uri('minitools.html'), follow=False) == 0, 'No new articles shall be found'


@pytest.mark.django_db
def test_scrape_real(testdata):
    t = Topic.objects.get(pk=2)
    scraper = Command()

    assert scraper.scrape_topic(t, t.url) > 0
    # no new articles shall be found (although there is a chance that new listing will be added in between the calls)
    assert scraper.scrape_topic(t,t.url) == 0, 'No new articles shall be found '

@pytest.mark.django_db
def test_scrape_all(testdata):
    scraper = Command()
    assert scraper.scrape_all() > 0
