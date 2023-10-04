from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				messages.info(request, 'You are not authorized to view this screen')
				return HttpResponseRedirect(reverse('location'),"You are not authorized to view this screen")
				
		return wrapper_func
	return decorator