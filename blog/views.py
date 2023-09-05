from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect

from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import UploadFileForm

from django.contrib.auth.models import User


from django.db.models import Count,Avg,Max

# Create your views here.
class IndexView(generic.ListView):
    template_name = "blog/index.html"
    #template_name = "registration/login.html"
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


@login_required
def index(request):
    all_posts_list = Post.objects.order_by("published_date")
    # template = loader.get_template("polls/index.html")
    context = {
        "all_posts_list": all_posts_list
    }
    return render(request, "blog/index.html", context)

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        'published_date')
    return render(request,'blog/post_list.html',{'posts':posts})

@login_required
def post_detail(request,blog_id):
    post = get_object_or_404(Post,pk=blog_id)
    return render(request,'blog/post_detail.html',{'post':post})

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/url")
    else:
        form = UploadFileForm()
    return render(request,"upload.html",{"form":form})

def dashboard(request):
    user_count = User.objects.count()
    task_count = Post.objects.count()

    latest_date = Post.objects.aggregate(latest_date=Max('published_date'))['latest_date']

    avg_length = Post.objects.aggregate(text_avg=Avg(len('text')))['text_avg']

    hardest_author = Post.objects.all().filter(author=1).count()

    context = {'user_count': user_count, 'task_count': task_count,
               'latest_date':latest_date, 'avg_len':avg_length,
               'hardest_author':hardest_author,}
    return render(request, 'blog/dashboard.html', context)