from django.db import models

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=40)
	question= models.CharField(max_length=200)
	domain=models.CharField(max_length=30)
	def __str__(self): #this specifies what should appear when posts are listed on browser.
		return self.title
	class Meta: #meta is used to specify the name that will appear on browser. This is to avoid double s since the model's name is plural
		verbose_name_plural = "Questions"
		db_table="question"