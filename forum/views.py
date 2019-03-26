from django.shortcuts import render
from forum.models import Categorie


def home(request):

	categorie = {
		'label' : "",
		'postes' : []
	}
	
	cats = Categorie.objects.all()

	postes_of_categorie = []
	categories = []

	for cat in cats:
		#postes_of_categorie.append(cat.post_set.all())

		categorie = {
			'label' : cat.label,
			'postes' : cat.post_set.all() 
			}
		categories.append(categorie)


	return render(request,'forum/home.html', locals())

def login(request):
	return render(request,'forum/login.html')

def register(request):
	return render(request,'forum/register.html')

def postesOfCategorie(request, catID):
	return render('categories.html')

def Poste(request):
        return render(request,'forum/Poste.html')

def coP(request):
        return render(request,'forum/cop.html')

def comment(request):
        return render(request,'forum/comment.html')
