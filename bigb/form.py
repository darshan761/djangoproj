from django import forms
from .models import user

class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput()) 
	confirm_password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = user
		fields = ['name','address','mobile_no','username','password','confirm_password']

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")
		if password != confirm_password:
			self.add_error('confirm_password', "Password does not match")

class LoginForm(forms.ModelForm):
	"""docstring for RegisterForm"""
	password = forms.CharField(widget= forms.PasswordInput()) 
	class Meta:
		model = user
		fields = ['username','password']
			
		