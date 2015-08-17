from django.shortcuts import render

from blog.models import Post

def index(request):
	posts = Post.objects.all()
	return render(request, "index.html", {
		"posts": posts
	})
