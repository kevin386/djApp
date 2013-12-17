#-*- coding:utf-8 -*-
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext


def thanks(request):
	return render_to_response("contact_thanks.html")


def contact(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.addpend('Enter a subject')
		if not request.POST.get('message',''):
			errors.append('Enter a message')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address')
		if not errors:
			send_mail(
					request.POST.get('subject'),
					request.POST.get('message'),
					request.POST.get('email'),#源邮件地址
					["null_386@qq.com"],#目标邮件地址
					fail_silently=False)
			return HttpResponseRedirect('/contact/thanks/')
	return render_to_response('contact_form.html',{'errors':errors,
		'subject':request.POST.get('subject',''),
		'message':request.POST.get('message',''),
		'email':request.POST.get('email',''),
		},
		#加入下面参数避免出现csrf错误
		context_instance=RequestContext(request))
