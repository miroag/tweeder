import bs4
import requests
from requests_file import FileAdapter

from django.core.management.base import BaseCommand, CommandError
from extract.models import Topic, Listing


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        return self.scrape_all()

    @staticmethod
    def _soup(url):
        """
        Simple wrapper to BeautifulSoup object from url
        :param url:
        :return: BeautifulSoup
        """

        s = requests.Session()
        s.mount('file://', FileAdapter())

        r = s.get(url)
        r.raise_for_status()
        # force encoding into utf-8 as sometimes airbase comes back in 'ISO-8859-1'
        r.encoding = 'utf-8'
        return bs4.BeautifulSoup(r.text, 'html.parser')

    def scrape_all(self):
        new_articles = 0
        qs = Topic.objects.filter(is_active=True)
        for t in qs:
            self.stdout.write('Scraping "{}"'.format(t.name))
            new_articles += self.scrape_topic(t, t.url)
        self.stdout.write(self.style.SUCCESS('Scraped {} new articles in {} topics'.format(new_articles, qs.count())))

    def scrape_topic(self, t, url, follow=True):
        soup = self._soup(url)

        title = soup.title.text
        articles = soup.find_all('article')

        new_articles = 0
        for a in articles:
            _id = a.get('id')
            # skip creation of the new listing in the db if it's been already scraped
            if t.listing_set.filter(site_id=_id).count() > 0:
                continue
            # listing title
            lt = a.find('h3', class_='listed-adv-item-title').text
            l = Listing(site_id=_id, title=lt, content=str(a), topic_id=t.pk)
            l.save()
            new_articles += 1

        self.stdout.write('Scraped {} new articles from {} on page {}'.format(new_articles, len(articles), url))

        # It's very likely that if all items on the page already scraped, then there is nothing to be found further
        if follow and new_articles > 0:
            next_page = soup.find('a', class_='next ui-button-secondary')
            if next_page:
                self.stdout.write(('Found next page ... '))
                new_articles += self.scrape_topic(t, 'https://www.2dehands.be/' + next_page.get('href'), follow=follow)

        return new_articles
