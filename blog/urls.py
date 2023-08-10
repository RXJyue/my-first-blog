from django.urls import path, include
from django.contrib import admin

from django.contrib.auth.views import LoginView

from . import views

app_name = "blog"
urlpatterns = [
    path("admin/", admin.site.urls),
    # path('accounts/login/',LoginView.as_view(),name="login"),
    # path("",include('blog.urls')),

    path("", views.IndexView.as_view(), name="index"),
    path("", views.post_list, name="post_list"),
    # path(r'^post/(?P<blog_id>[0-9]+)/$', views.DetailView.as_view(), name='post_detail'),
    path("<int:pk>/", views.DetailView.as_view(), name="post_detail"),
]
