from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
class HomePage(TemplateView):
	"""docstring for HomePage: this is the global home page for the app"""
	template_name = 'home.html'
	# def __init__(self, arg):
	# 	super(HomePage, self).__init__()
	# 	self.arg = arg
class AboutPage(TemplateView):
	"""docstring for AboutPage"""
	template_name ="about.html"
	# def __init__(self, arg):
	# 	super(AboutPage, self).__init__()
	# 	self.arg = arg
		
def home(request):
	return HttpResponse("cloudcom1 App")
