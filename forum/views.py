from django.shortcuts import render

def home(request):
	postes = ['rouge', 'orange', 'jaune']
	cats = ['TECHNO', 'POLITIQUE', 'GAMING', 'DROLE', 'BRICOLAGE', 'DEV']

	return render(request,'forum/home.html', locals())


def postesOfCategorie(request, catID):
	return render('categories.html')

def Poste(request):
        return render(request,'forum/Poste.html')

def coP1(request):
        return render(request,'forum/coP1.html')

def comment(request):
        return render(request,'forum/comment.html')
