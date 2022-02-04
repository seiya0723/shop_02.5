from django import forms
from .models import CategoryCreation, CommentCreation

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryCreation
        fields = ['name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentCreation
        fields = ['category', 'username', 'topic', 'comment', ]