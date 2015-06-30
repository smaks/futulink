#blog models
from django.db import models
from django.db.models import permalink
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('blog.Category')
    tags = models.ManyToManyField('blog.Tag')

    def publish(self):
        self.published_date = timezone.now()

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return self.slug

    @permalink
    def get_absolute_url(self):
        return ('view_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return self.slug

    @permalink
    def get_absolute_url(self):
        return ('view_category', None, { 'slug': self.slug })

class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.slug

