from django.shortcuts import render
from django.shortcuts import render_to_response
from forum.models import Comment, Like, Post

def home(request):
	postes = ['rouge', 'orange', 'jaune']
	cats = ['TECHNO', 'POLITIQUE', 'GAMING', 'DROLE', 'BRICOLAGE', 'DEV']

	return render(request,'forum/home.html', locals())


def postesOfCategorie(request, catID):
	return render('categories.html')

def Poste(request):
            if request.method == 'POST': # S'il s'agit d'une requête POST
            form = Post(request.POST, request.FILES) # Nous reprenons les données
            if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            # Ici nous pouvons traiter les données du formulaire
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            categorie = form.cleaned_data['categorie']
            photo = form.cleaned_data['photo']
            form.save()
            # Nous pourrions ici envoyer l'e-mail grâce aux donnéesque nous venons de récupérer
            envoi = True
            GET
            else: # Si ce n'est pas du POST, c'est probablement une requête
            form = Post()
            # Nous créons un formulaire vide
            return render(request, 'forum/Poste.html', locals())




def comment(request):
        return render(request,'forum/comment.html')

def coP(request):
        coP = Poste.objects.all()
        return render(request,'forum/cop.html',{ 'coP':coP})
