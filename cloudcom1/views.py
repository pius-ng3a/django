from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import generic
from . models import Question
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
		
def homey(request):
	latest_questions = Question.objects.order_by('domain')[:3]
	output = ','.join([q.question for q in latest_questions])
	return HttpResponse(output)
def detail(request,question_id):
	question = Question.objects.get(id =question_id)
	return HttpResponse("<h1>Looking at question %s  which is: </h1> <br/><p> %s </p> ." %(question_id,question.question))
def vote(request,question_id):
	return HttpResponse("You want to vote question %s." %question_id)
class GetRescentQuestions(generic.ListView):
	"""docstring for GetRescentQuestions"""
	template_name = 'home.html'
	context_object_name ="latest_questions"
	def get_latest_questions(self):
		return Question.objects.order_by('id',descending)[:5]
