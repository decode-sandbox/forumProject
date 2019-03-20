from django.db import models
from django.utils import timezone

class Like(models.Model):
	"""docstring for Like"""
	num = models.IntegerField()
	def __str__(self):
		return self.num

class User(models.Model):
	"""This class is used to get all informations about the User"""
	names = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	login = models.CharField(max_length=45)
	passwd = models.CharField(max_length=45)
	inscription_date = models.DateTimeField(default=timezone.now,verbose_name="Date d'inscription")
	photo = models.CharField(max_length=200)
	like = models.OneToOneField(Like, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.login

class Post(models.Model):
	"""docstring for post"""
	title = models.CharField(max_length=45)
	description = models.TextField()
	creation = models.CharField(max_length=45)
	status = models.CharField(max_length=10)
	payload = models.CharField(max_length=200)
	categorie = models.ForeignKey('Categorie',on_delete=models.CASCADE)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	like = models.OneToOneField(Like, on_delete=models.CASCADE)
	def __str__(self):
		return self.title

class Comment(models.Model):
	"""docstring for Comment"""
	message = models.TextField()
	crud_date = models.DateTimeField(default=timezone.now, verbose_name="Creation, update, delete.. date")
	payload = models.CharField(max_length=45)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	def __init__(self):
		return self.message

class Categorie(models.Model):
	"""docstring for Categorie"""
	label = models.CharField(max_length=45)
	def __str__(self):
		return self.label

		
		
		
		

