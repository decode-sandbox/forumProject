from django.shortcuts import render

def home(request):
	postes = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo',
'violet']
	cats = ['TECHNO', 'POLITIQUE', 'GAMING', 'DROLE', 'BRICOLAGE', 'DEV']

	return render(request,'forum/home.html', locals())

def base(request):
	
	return render(request, 'base.html')

def postesOfCategorie(request, catID):
	return render('categories.html')

def login(request):
	return render(request,'forum/login.html')
<<<<<<< HEAD

def register(request):
	return render(request,'forum/register.html')
=======
>>>>>>> c471ecd9856d00c0963cd44e7d0dddac3b0b5401
