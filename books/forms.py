from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserForm(UserCreationForm):
	
	class Meta(UserCreationForm):
		model = Profile
		fields = ['username','first_name','last_name','password1','password2','email','date_of_birth','bio']