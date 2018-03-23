from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    site_id = models.CharField(max_length=200, default='', unique=True)
    title = models.CharField(max_length=200, default='')
    content = models.TextField()
    is_viewed = models.BooleanField(default=False)
    is_clicked = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    view_date = models.DateTimeField('date viewed', auto_now=True)


    def __str__(self):
        return '{}: {}'.format(self.site_id, self.title)
