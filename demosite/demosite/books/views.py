from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
from demosite.books.models import Book

def search_form(request):
	return render_to_response("search_form.html")

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q :
			errors.append('Please input a search term.')
		elif len(q) > 20:
			errors.append("Please input at most 20 characters.")
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html',{'books':books,'query':q})
	return render_to_response('search_form.html', {'errors':errors})
