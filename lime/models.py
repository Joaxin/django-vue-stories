from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager


class Message(models.Model):

    author =  models.CharField('作者', max_length=200, default ="mxh-cp-stories")

    created = models.DateTimeField('date created',auto_now_add=True)
    updated = models.DateTimeField('date updated',auto_now=True)

    tags=TaggableManager(verbose_name='标签', blank=True)

    content = models.TextField(max_length=2000)
    
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ['id']

    def __str__(self):
        return '%s (%s)' % (self.author,self.content)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
