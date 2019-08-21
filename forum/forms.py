from django import forms
from .models import Post,Comment,Category
import datetime

class CommentForm(forms.ModelForm):
    # email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','rows': 5,
                              'cols': 30,'style': 'width: 20em;','placeholder':'comment'}))
    class Meta:
        model = Comment

        fields = ('content',)


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    date = forms.DateField(initial=datetime.date.today,
                           widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = Post
        fields = ('title','desc','category','date')

class CategoryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}))

    class Meta:
        model = Category
        fields = ('title',)



