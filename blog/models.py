from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth import get_user_model

import os
import uuid

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


def user_dict_path(instance,filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10],ext)
    return os.path.join("files",filename)

#class File(models.Model):
    #file = models.FileField(upload_to=user_dict_path(),null=True)
    #upload_method = models.CharField(max_length=50,verbose_name="upload method")

User = get_user_model()