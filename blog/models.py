from django.db import models
from organizer.models import Startup, Tag
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, blank=True, related_name='blog_posts')

    def __str__(self):
        return "{} on {}".format(self.title, self.pub_date.strftime('%Y-%m-%d'))
    
    def get_archive_year_url(self):
        return reverse('blog_post_archive_year', kwargs={'year': self.pub_date.year})
    
    def get_archive_month_url(self):
        return reverse('blog_post_archive_month', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month})


    class Meta:
          verbose_name = 'Blog Post'
          ordering = ['-pub_date', 'title']
          get_latest_by = 'pub_date'
          #permissions = [
          #  ("can_create_post", "Can create a new blog post"),
           # ("can_edit_post", "Can edit an existing blog post"),
           # ("can_delete_post", "Can delete a blog post"),
           # ("view_future_post","Can view unpublished Post"),
       # ]

    def get_update_url(self):
        return reverse('blog_post_update', kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        return reverse('blog_post_delete', kwargs={'slug': self.slug})
    
    def get_absolute_url(self):
	    return reverse('blog_post_detail', kwargs={'slug': self.slug})




    
