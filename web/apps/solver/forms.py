from django import forms

class SolverFileForm(forms.Form):
	file = forms.FileField()
