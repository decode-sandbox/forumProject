"""forumProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path


from . import views

urlpatterns = [
    path('',views.home), 
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('Poste',views.Poste,name='poste'),
    path('coP',views.coP,name='cop'),
    path('edit_post/<id>/<action>',views.edit_post,name='edit_post'),
    path('edit_comment/<id_post>/<id>/<action>',views.edit_comment,name='edit_comment'),
    path('comment/<id>',views.comment,name='comment'),
    path('like/<post_id>/<id>/<typ>',views.like,name='like'),
    path('posts',views.post_with_more_upvote,name='posts'),
    path('comment',views.comment,name='comment'),
    path('home1',views.home1,name='home1'),
    path('logout',views.Logout,name='logout'),
]

