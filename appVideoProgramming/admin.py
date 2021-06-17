from django.contrib import admin

from .models import videoSite
from embed_video.admin import AdminVideoMixin



class videoAdmin(AdminVideoMixin, admin.ModelAdmin):
    fields = ('title_video', 'image_video', 'video', 'redactor_text')#для создания обьекта
    list_display = ('title_video', 'date_video', 'adminShowImage', 'video')#для отображения обьекта
 
admin.site.register(videoSite, videoAdmin)