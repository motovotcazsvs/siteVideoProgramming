from django import forms

from .models import videoSite


class videoForm(forms.ModelForm):
    class Meta:
        model = videoSite
        fields = ('title_video', 'image_video', 'video', 'redactor_text')
        