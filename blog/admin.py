from django.contrib import admin
from .models import Post



# Register your models here.
admin.site.register(Post)

admin.site.site_header = "Monitor Tool Backend administration"
admin.site.site_title = "Monitor tool"