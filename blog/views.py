from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import Post

wall = "/img/wall.jpg"
tracks = "/img/bg.jpg"

def index(request):
	post_list = Post.objects.all()
	context = {'post_list': post_list, 'current_year':date.today(), 'background_image':wall}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	context = {'post': post, 'current_year':date.today(), 'background_image':wall}
	return render(request, 'blog/post.html', context)

def contact(request):
	context = {'current_year':date.today(), 'background_image':wall}
	return render(request, 'blog/contact.html', context)


