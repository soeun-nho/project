from django import forms
from .models import Post, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm#w장고제공


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title','content', 'photo']
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['comment']
