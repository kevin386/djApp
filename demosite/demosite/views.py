#-*- coding:utf-8 -*-
from django.http import HttpResponse,Http404
import datetime
#from django.template import Template,Context
#from django.template.loader import get_template
from django.shortcuts import render_to_response

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
	#now = datetime.datetime.now()
	#html = "<html><body>It is now %s.</body></html>" % now
	#t = Template("<html><body>It is now {{ current_date }}.</body></html>")
	#t = get_template('current_datetime.html') 
	#html = t.render(Context({'current_date':now}))
	#return HttpResponse(html)
	#return render_to_response('current_datetime.html',{'current_date':now})
	current_date = datetime.datetime.now()
	return render_to_response('current_datetime.html', locals())

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	#html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset,dt)
	#return HttpResponse(html)
	return render_to_response('hours_ahead.html',locals())

def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k,v in values:
		html.append('<tr><td>%s</td><td><%s></td><tr>' % (k,v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

