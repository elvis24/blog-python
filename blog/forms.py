from django import forms

from.models import Post

class PostCrearForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content')
