from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns("solver.views",
	url(r"^upload/$", "solver_file_upload"),
)
