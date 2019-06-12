from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
# admin.site.register(Movie)
# admin.site.register(Person)

class MovieAdmin(admin.ModelAdmin):
	"""docstring for MovieAdmin"""
	fieldsets=[
	("Name",{'fields':['name']}),
	("Movie Type",{'fields':['movie_type']}),
	("Studio",{'fields':['studio']}),
	("Manager",{'fields':['manager']}),
	("Created At ",{'fields':['created_at']}),
	("Icon ",{'fields':['icon']}),
	("Movie",{'fields':['video']}),
	]
class ManagerAdmin(admin.ModelAdmin):
	"""docstring for PersonAdmin"""
	fieldsets=[
	("Manager",{'fields':['manager_name']}),
	("Working Experience",{'fields':['experience']}),
	]
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Movie,MovieAdmin)
#admin.site.site_header = "Aministration Dashboard" # this changes the default title
