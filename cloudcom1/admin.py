from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
	"""docstring for QuestionAdmin"""
	fieldsets=[
	("Title",{'fields':['title']}),
	("Question",{'fields':['question']}),
	("Knowledge Domain ",{'fields':['domain']}),
	]
# class ChoiceInline(admin.StackedInline):
# 	"""docstring for ChoiceInline"""
# 	model =Choice
# 	extra = 3
# 	]
# #inlines = [ChoiceInline]

# Register your models here.
#model registration
admin.site.register(Question,QuestionAdmin)

