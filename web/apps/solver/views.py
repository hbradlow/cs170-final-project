from django.http import HttpResponse
from  django.shortcuts import *
from django.core.urlresolvers import reverse

import forms

def solver_file_upload(request):
	form = forms.SolverFileForm(request.POST)
	print form
	if form.is_valid():
		return HttpResponse("SDLKFJSDLFKJ")
	else:
		return HttpResponseRedirect(reverse("home"))
