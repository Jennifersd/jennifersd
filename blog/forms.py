from django import forms
from .models import Comment, Post

#class PostForm(forms.ModelForm):
#    class Meta:
#        model = Post
#        fields = ('title', 'text', ) # Añadir las categorias en el futuro
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'email', 'body')
        labels = {
            'user': 'Indica tu nombre o tu alias',
            'email': 'Indica tu email',
            'body': 'Indica tu comentario',
        }
        
        widgets = {
            'user' : forms.TextInput(attrs = {'placeholder': 'Indica tu nombre o tu alias'}),
            'email': forms.TextInput(attrs = {'placeholder': 'Indica tu email'}),
            'body': forms.Textarea(attrs = {'placeholder': 'Indica tu comentario'}),
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content' , 'image' , 'category' , 'seo_title' , 'seo_description' , 'status')