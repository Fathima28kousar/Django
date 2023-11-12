from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, Blogcomment
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def blogHome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= Blogcomment.objects.filter(post=post)
    context={'post':post, 'comments': comments}
    return render(request, "blog/blogpost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)

        comment=Blogcomment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request,"Your comment has been posted successfully")
        
    return redirect(f"/{post.slug}/")

