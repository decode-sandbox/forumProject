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
