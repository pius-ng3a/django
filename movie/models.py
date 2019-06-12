from django.db import models
from time import time
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.
class Manager(models.Model):
	"""docstring for Person"""
	manager_name = models.CharField(max_length=30)
	experience=models.FloatField(blank=True, null=True,) #stores working experience in years
	#phone = models.CharField(max_length=15)
	# def __init__(self, arg):
	# 	super(Person, self).__init__()
	# 	self.arg = arg

def get_upload_file_name(instance,filename): #function to rename files and give a unique name
	return "uploaded_files/%s_%s"%(str(time()).replace('.','_'),filename)
class Movie(models.Model):
	"""movie object ot be played by users"""
	name=models.CharField(max_length=50 )
	movie_type = models.CharField(max_length=30)
	studio = models.CharField(max_length=25)
	manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
	created_at = models.DateField(blank=True,null=True)
	updated_at= models.DateField(blank=True, null=True)
	icon =models.ImageField(upload_to=get_upload_file_name,default="default.png",blank=True)
	video = models.FileField(upload_to=get_upload_file_name)
	likes = models.IntegerField(default=0)
	def __unicode__(self):
		return self.name
	# def __init__(self, arg):
	# 	super(Movie, self).__init__()
	# 	self.arg = arg
	# 	
class MovieForm(ModelForm):
	"""docstring for MovieForm"""
	class Meta:
		model = Movie
		fields = ['name','movie_type','studio','manager','created_at','icon','video','updated_at']
class AddMovie(ModelForm):
	"""docstring for AddMovie"""
	def __init__(self, arg):
		super(AddMovie, self).__init__()
		self.arg = arg
		