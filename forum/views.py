from forum.models import User, Post, Comment, Like,Categorie
from django.contrib.auth.models import User as AuthUser
from django.shortcuts import render, redirect
# from django.core.paginator import Paginator
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as new_login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.template.context_processors import csrf
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator,EmptyPage	




the_user=User()

def home(request):

	categorie = {
		'label' : "",
		'postes' : []
	}
	
	cats = Categorie.objects.all()
	nbCat=cats.count()+1
	nbPost=Post.objects.all().count()
	nbCom=Comment.objects.all().count()

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
				# user=User(username,first_name="names",last_name="name",email="email",password="paswrd")
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

		user=User.objects.get(user__username=request.user.username)
		try:
			myfile = request.FILES['picture']
		except KeyError:
			post = Post.objects.create(title=title, description=description, user=user)
		else:
			myfile = request.FILES['picture']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)
			paylaod=uploaded_file_url
			post = Post.objects.create(title=title, description=description, user=user, payload=paylaod)
		
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

def comment(request,id):
	# return HttpResponse("id, {0} !".format(id))
	post=Post.objects.get(id=id)
	coms = post.comment_set.all()
	coms_like=[]
	post_like = post.like_set.all().count()

	for c in coms:
		com_like = {
				'com' : c,
				'like' : c.like_set.all().count()
				}
		coms_like.append(com_like)

	if request.method == "POST":
		form_values = request.POST.dict()
		message = form_values["comment"]
		#paylaod = form_values['paylaod']
		
		user=User.objects.get(user__username=request.user.username)
		# return HttpResponse("hi, {0} !".format(user))
		comme = Comment.objects.create(message=message,post=post, user=user)

		return redirect(comment,id)

	else:
		return render(request,'forum/comment.html', locals())

	return render(request,'forum/comment.html', locals())

@login_required(login_url='/forum/login')
def like(request,post_id,id,typ):
	#return HttpResponse("id, {0} !".format(id))
	user=User.objects.get(user__username=request.user.username)
	if typ == "postt":
		try:
			l=Like.objects.get(user=user, poste=Post.objects.get(id=id))

		except Like.DoesNotExist:
			try:
				Like.objects.create(poste=Post.objects.get(id=id), user=user)
			except IntegrityError:
				return HttpResponse("tyintegrytié")
			else:
				redirect(comment,post_id)

		except MultipleObjectsReturned:
				redirect(comment,post_id)
		#else:
			#return HttpResponse("vous avez deja liké ce post")
			

	elif typ == "commentt":
		try:
			l=Like.objects.get(user=user, comment=Comment.objects.get(id=id))

		except Like.DoesNotExist:
			try:
				Like.objects.create(comment=Comment.objects.get(id=id), user=user)
			except IntegrityError:
				return HttpResponse("tyintegrytié")
			else:
				redirect(comment,post_id)

		except MultipleObjectsReturned:
				redirect(comment,post_id)
		#else:
			#return HttpResponse("vous avez deja liké ce commentaire")
		
		
	else:
		return HttpResponse("type error must be post or comment not .%s.." %(typ))
	
	return redirect(comment,post_id)


def edit_post(request, id, action):
	post = Post.objects.get(id=id)
	if action == "edit":
		title=post.title
		description=post.description
		#form = JournalForm(initial={'title': title})

		if request.method == "POST":
			form_values = request.POST.dict()
			title = form_values['title']
			description = form_values["description"]
			#paylaod = form_values['paylaod']

			#the_user.save()
			user=User.objects.get(user__username=request.user.username)
			# return HttpResponse("hi, {0} !".format(user))
			post.title=title
			post.description=description
			post.save()
			error = ""
			#return render(request,'forum/cop.html')
			return redirect(coP)

		else:
			return render(request,'forum/edit_post.html', locals())

		return render(request,'forum/edit_post.html', locals())

	elif action == "delete":
		post.delete()
		return redirect(coP)
	else:
		return HttpResponse("type error must be post or comment not .%s.." %(action))

def edit_comment(request,id_post, id, action):
	com = Comment.objects.get(id=id)
	post = Post.objects.get(id=id_post)
	if action == "edit":
		message=com.message
		#form = JournalForm(initial={'title': title})

		if request.method == "POST":
			form_values = request.POST.dict()
			nmessage = form_values["comment"]
			com.message=nmessage
			com.save()

			return redirect(comment,id_post)

		else:
			return render(request,'forum/edit_comment.html', locals())
		return redirect(comment,id_post)

	elif action == "delete":
		com.delete()
		return redirect(comment,id_post)
	else:
		return HttpResponse("type error must be post or comment not .%s.." %(action))

def post_with_more_upvote(request,page=1):
	my_dict={}
	liste = []
	
	for posts in Post.objects.all():
		yo = Like.objects.filter(poste__title=posts.title)
		my_dict[posts] = yo
		liste.append(posts)
		#ya = QuerySet [<Like: Like object (2)>]
	p = Paginator(liste,10)
	yi = p.num_pages
	try:
		pos = p.page(page)
	except EmptyPage:
		pos = p.page(paginator.num_pages)


	return render(request,'forum/post_plus_upvote.html',locals())

def Logout(request):
	logout(request)
	return redirect(login)

