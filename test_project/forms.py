# coding: utf-8

from django import forms

class CommentForm(forms.Form):
    question=forms.CharField(widget=forms.Textarea(attrs={'cols':80, 'rows':5}))