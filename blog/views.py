from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import Post

def index(request):
	post_list = Post.objects.all()
	context = {'post_list': post_list, 'current_year':date.today()}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	context = {'post': post, 'current_year':date.today()}
	return render(request, 'blog/post.html', context)

def contact(request):
	context = {'current_year':date.today()}
	return render(request, 'blog/contact.html', context)


