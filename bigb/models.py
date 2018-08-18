from django.db import models
from django.core.validators import RegexValidator,MaxValueValidator, MinValueValidator 
# Create your models here.
class bigb(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	def __str__(self):
	    return self.title
class user(models.Model):
	"""docstring for ClassName"""
	name = models.CharField(max_length = 20)
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 10)
	address = models.CharField(max_length = 500)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	mobile_no = models.CharField(validators=[phone_regex], max_length=17, blank=True)		
	def __str__(self):
		return self.name

class Item(models.Model):
	"""docstring for Item"""
	userid = models.ForeignKey(user,on_delete=models.CASCADE)
	name = models.CharField(max_length = 20)
	price = models.IntegerField(default=1,
        validators=[MaxValueValidator(1000), MinValueValidator(1)])
	qty = models.IntegerField(default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)])
		
    

	
 		
		
