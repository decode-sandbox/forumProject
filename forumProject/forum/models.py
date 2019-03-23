from django.db import models


class Poste(models.Model):
	"""This class is used to get all informations about the User"""
	title = models.CharField(max_length=45)
	post = models.TextField()
	date = models.DateField()
	
	
