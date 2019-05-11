from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','bio','email_id','gender','date_of_birth']