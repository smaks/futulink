from django import forms
from .models import Post, Comment, Tag
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'category', 'tags', 'body')
        
        widgets = {'body': SummernoteWidget(), 'tags': forms.CheckboxSelectMultiple}

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
