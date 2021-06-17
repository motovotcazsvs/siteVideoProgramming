import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe

from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField

class videoSite(models.Model):
    title_video = models.CharField("Название видео", max_length = 200)
    redactor_text = RichTextField(blank = True, null = True)
    date_video = models.DateTimeField('дата публикации', auto_now_add = True, db_index = True, )
    image_video = models.ImageField(blank = True, upload_to = 'images/', verbose_name = 'изображение')
    video = EmbedVideoField(blank = True, verbose_name = 'адрес видео')

    def __str__(self):
        return self.title_video

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def adminShowImage(self):
        if self.image_video:
           return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(self.image_video.url))
           #return u'< img src="%s" width="100"/>' % self.image_video.url
        else:
            return '(Нет изображения)'
    adminShowImage.short_description = 'Изображение'
    adminShowImage.allow_tags = True
        