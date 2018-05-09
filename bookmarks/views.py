from django.shortcuts import render
from .models import Bookmark

def index(request):
	context = {}

	# TODO: biz logic

	return render(request, 'bookmarks/index.html', context)
