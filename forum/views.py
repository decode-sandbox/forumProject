from forum.models import Categorie
from forum.models import User
from django.contrib.auth.models import User as AuthUser
from django.shortcuts import render, redirect
# from django.core.paginator import Paginator
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as new_login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError



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
	if request.method == "POST":
		form_fields = request.POST.dict()
		username = form_fields["name"]
		paswrd = form_fields["paswrd"]
		user = authenticate(username=username,password=paswrd)
		if user:
			new_login(request,user)
			return redirect(home)
		else:
			return render(request,'forum/login.html',{"error":True})
	else:	
		return render(request,'forum/login.html')


def register(request):
	if request.method == "POST":
		form_values = request.POST.dict()
		name = form_values['name']
		names = form_values["names"]
		email = form_values['email']
		username = form_values['username']
		paswrd = form_values['paswrd']
		confirm_paswrd = form_values['confirm_paswrd']
		profil = form_values['resume']
		error = "Password don't match!"
		if paswrd == confirm_paswrd:
			try:
				user = AuthUser.objects.create_user(username,email,paswrd)
			except IntegrityError:
				error = f"Username{username} already exist"
			else:
				User(user=user).save()
				new_login(request,user)
				return redirect(home)
		return render(request, 'forum/register.html',{"error" : error} )
	else:
		return render(request, 'forum/register.html')

	return render(request,'forum/register.html')
def postesOfCategorie(request, catID):
	return render('categories.html')

@login_required(login_url='/forum/login')
def Poste(request):
        return render(request,'forum/Poste.html')
@login_required(login_url='/forum/login')
def coP(request):
        return render(request,'forum/cop.html')

@login_required(login_url='/forum/login')
def comment(request):
        return render(request,'forum/comment.html')
