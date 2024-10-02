from django.shortcuts import render,redirect
from .forms import PostrForm
from .models import Post
# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = PostrForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form = PostrForm()
        print('methdo post na')
    return render(request,'add_post.html',{'form':post_form})


def edit_post(request,id):
    post = Post.objects.get(pk=id)
    post_form = PostrForm(instance=post)
    print(post)
    if request.method == 'POST':
        post_form = PostrForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')

    return render(request,'add_post.html',{'form':post_form})


def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')