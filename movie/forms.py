from django import forms
from .models import Movie,Manager

def get_upload_file_name(instance,filename): #function to rename files and give a unique name
    return "uploaded_files/%s_%s"%(str(time()).replace('.','_'),filename)
class AddMovieForm(forms.ModelForm):
    # name = forms.CharField(max_length=50)
    # movie_type = forms.CharField(max_length=30)
    # studio = forms.CharField(max_length=25)
    manager = forms.CharField(max_length= 25)
    # created_at = forms.DateField()
    # updated_at= forms.DateField()
    # icon =forms.ImageField()
    # video = forms.FileField()
    class Meta:
        model = Movie
        fields = ['name','movie_type','studio','manager','created_at','icon','video','updated_at']

    def clean(self):
        cleaned_data = super(AddMovieForm, self).clean()
        name = cleaned_data.get('name')
        movie_type = cleaned_data.get('movie_type')
        studio = cleaned_data.get('studio')
        created_at = cleaned_data.get('created_at')
        icon = cleaned_data.get('icon')
        video = cleaned_data.get('video')
        updated_at = cleaned_data.get('updated_at')
        manager = cleaned_data.get('manager')
        if not name and not movie_type and not video and not icon and not created_at and not studio:
            raise forms.ValidationError('You have to write something!')
    def save(self, commit=True):
        manager_fetched, experience = Manager.objects.get_or_create(
            manager_name=self.cleaned_data['manager'],
            defaults={'experience': 1}
        )
        self.cleaned_data['manager'] = manager_fetched.id
        return super(AddMovieForm, self).save(commit)