from django import forms

class Post(forms.Form):
title = forms.CharField(max_length=100)
description = forms.CharField(widget=forms.Textarea)
date = forms.DateTimeField
categorie = forms.BooleanField(required=False)
photo = forms.ImageField()


