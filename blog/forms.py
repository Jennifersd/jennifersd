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
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content' , 'image' , 'category' , 'seo_title' , 'seo_description' , 'status')