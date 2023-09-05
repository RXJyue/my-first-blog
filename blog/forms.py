from django import forms

from .models import Post


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    class Meta:
        model = Post
        fields = ('title', 'text',)
