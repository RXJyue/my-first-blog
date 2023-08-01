from django.shortcuts import render, get_object_or_404
from django.views import generic

from django.utils import timezone

from .models import Post

# Create your views here.
class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "all_posts_list"

    def get_queryset(self):
        """return the last five published questions."""
        return Post.objects.filter(published_date__lte=timezone.now()).order_by(
            "published_date")


class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now())


def index(request):
    all_posts_list = Post.objects.order_by("published_date")
    # template = loader.get_template("polls/index.html")
    context = {
        "all_posts_list": all_posts_list
    }
    return render(request, "blog/index.html", context)


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        'published_date')
    return render(request,'blog/post_list.html',{'posts':posts})


def post_detail(request,blog_id):
    post = get_object_or_404(Post,pk=blog_id)
    return render(request,'blog/post_detail.html',{'post':post})