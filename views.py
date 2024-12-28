from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"app/base.html")


from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        author = request.POST.get('author')
        text = request.POST.get('text')
        if author and text:
            Comment.objects.create(post=post, author=author, text=text)
            return redirect('post_detail', post_id=post.id)

    comments = post.comments.all()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})
