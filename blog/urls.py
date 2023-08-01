from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("", views.post_list, name="post_list"),
    #path(r'^post/(?P<blog_id>[0-9]+)/$', views.DetailView.as_view(), name='post_detail'),
    path("<int:pk>/",views.DetailView.as_view(),name="post_detail"),
]
