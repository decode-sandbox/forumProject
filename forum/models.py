from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as AuthUser



class User(models.Model):
	"""This class is used to get all informations about the User"""
	user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
	# name = models.CharField(max_length=45)
	# surname = models.CharField(max_length=45)
	# email = models.CharField(max_length=45)
	# login = models.CharField(max_length=45)
	# passwd = models.CharField(max_length=45)
	# inscription_date = models.DateTimeField(default=timezone.now,verbose_name="Date d'inscription")
	photo = models.ImageField(max_length=200, null=True)
	
	def __str__(self):
		return self.user.username

class Post(models.Model):
	"""docstring for post"""
	title = models.CharField(max_length=45)
	description = models.TextField()
	crud_date = models.DateTimeField(default=timezone.now, verbose_name="Creation, update, delete.. date")
	status = models.CharField(max_length=10, default="open")
	payload = models.CharField(max_length=200, null=True)
	
	categorie = models.ForeignKey('Categorie',null=True, on_delete=models.SET_NULL)
	user = models.ForeignKey('User', on_delete=models.CASCADE)

	class Meta:
		verbose_name = "un poste"
		ordering = ['crud_date']

	def __str__(self):
		return self.title



class Comment(models.Model):
	"""docstring for Comment"""
	message = models.TextField()
	crud_date = models.DateTimeField(default=timezone.now, verbose_name="Creation, update, delete.. date")
	payload = models.CharField(max_length=45, null=True)

	post = models.ForeignKey('Post', null=True, on_delete=models.CASCADE)
	com = models.ForeignKey('Comment', null=True, on_delete=models.CASCADE)

	def __init__(self):
		return self.message

	class Meta:
		verbose_name = "un commentaire"
		ordering = ['crud_date']

	def __str__(self):
		return self.title
 
class Categorie(models.Model):
	"""docstring for Categorie"""
	label = models.CharField(max_length=45)
	def __str__(self):
		return self.label

class Like(models.Model):
	"""docstring for Like"""
	#num = models.IntegerField()

	poste = models.OneToOneField(Post, null=True, on_delete=models.CASCADE)
	comment = models.OneToOneField(Comment, null=True, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete=models.CASCADE)


	