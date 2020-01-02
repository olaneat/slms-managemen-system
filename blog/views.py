from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.

def index(request):
    post = Post.objects.all()
    return render(request, 'blog/slms_index.html', {'post': post})

def post_detail(request, slug, year, month, day):
    detail = get_object_or_404(Post, slug = slug,
                                created__year =year,
                                created__month=month,
                                created__day =day)
    new_comment = None
    comments = detail.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form(commit=False)
            new_comment.detail = detail
            new_comment.save()
    else:
        new_comment = CommentForm()
    return render(request, 'blog/post_detail.html', {'comments':comments,
                                                    'new_comment' : new_comment,
                                                    'comment_form': comment_form})