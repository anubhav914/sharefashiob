from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from accounts.forms import RegistrationForm
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
import pdb

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			# messages.info(request, "Thanks for registering. You are now logged in.")
			new_user = authenticate(username= request.POST['email'],
                                 	password= request.POST['password1'])
			login(request, new_user)
			return HttpResponseRedirect('/dashboard/')
	else:
		form = RegistrationForm()
	token = {}
	token.update(csrf(request))
	print token
	token['form'] = form
	return render_to_response('accounts/register.html', token)
