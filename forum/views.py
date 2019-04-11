from forum.models import Categorie
from forum.models import Post

from forum.models import User
from django.contrib.auth.models import User as AuthUser
from django.shortcuts import render, redirect
# from django.core.paginator import Paginator
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as new_login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.template.context_processors import csrf
from django.http import HttpResponse



the_user=User()

def home(request):

	categorie = {
		'label' : "",
		'postes' : []
	}
	
	cats = Categorie.objects.all()

	postes_of_categorie = []
	categories = []			

	# return HttpResponse("Salut, {0} !".format(request.user.username))

	for cat in cats:
		#postes_of_categorie.append(cat.post_set.all())

		categorie = {
			'label' : cat.label,
			'postes' : cat.post_set.all() 
			}
		categories.append(categorie)

	
	poste_no_cat=[]
	for p in Post.objects.all():
		if p.categorie is None:
			poste_no_cat.append(p)

	categorie = {
			'label' : "Autre",
			'postes' : poste_no_cat
			}
	categories.append(categorie)

	return render(request,'forum/home.html', locals())

def home1(request):
	return render(request,'forum/home1.html')

def login(request):
	if request.method == "POST":
		form_fields = request.POST.dict()
		username = form_fields["name"]
		paswrd = form_fields["paswrd"]
		user = authenticate(username=username,password=paswrd)
		the_user = user
		if user:
			the_user = user
			new_login(request,user)
			return redirect(home)
		else:
			return render(request,'forum/login.html',{"error":True})
	else:	
		return render(request,'forum/login.html')


def register(request):
	if request.method == "POST":
		form_values = request.POST.dict()
		name = form_values['name']#nom
		names = form_values["names"]#prenom
		email = form_values['email']
		username = form_values['username']
		paswrd = form_values['paswrd']
		confirm_paswrd = form_values['confirm_paswrd']
		profil = form_values['resume']
		error = "Password don't match!"
		if paswrd == confirm_paswrd:
			try:
				user = AuthUser.objects.create_user(username=username,email=email,password=paswrd,first_name=names,last_name=name)
			except IntegrityError:
				error = f"Username{username} already exist"
			else:
				User(user=user).save()
				new_login(request,user)
				return redirect(home1)
		return render(request, 'forum/register.html',{"error" : error} )
	else:
		return render(request, 'forum/register.html')

	return render(request,'forum/register.html')

def postesOfCategorie(request, catID):
	return render('categories.html')

@login_required(login_url='/forum/login')
def Poste(request):
	if request.method == "POST":
		form_values = request.POST.dict()
		title = form_values['title']
		description = form_values["description"]
		#paylaod = form_values['paylaod']

		#the_user.save()
		user=User.objects.get(user__username=request.user.username)
		# return HttpResponse("hi, {0} !".format(user))
		post = Post.objects.create(title=title, description=description, user=user)
		post.save()
		error = ""
		#return render(request,'forum/cop.html')
		return redirect(coP)

	else:
		return render(request,'forum/Poste.html')

	return render(request,'forum/Poste.html')

@login_required(login_url='/forum/login')
def coP(request):
	user_post=[]
	user=User.objects.get(user__username=request.user.username)
	for post in Post.objects.filter(user=user):
		user_post.append(post)
	
	return render(request,'forum/cop.html',locals())

@login_required(login_url='/forum/login')
def comment(request):
    return render(request,'forum/comment.html')

def Logout(request):
	logout(request)
	return redirect(login)

