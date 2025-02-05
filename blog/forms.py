from django import forms
from blog.models import Blog, BlogCategory


class BlogCreateForm(forms.ModelForm):

    category = forms.ModelChoiceField(
        queryset=BlogCategory.objects.all(), 
        widget=forms.Select(attrs={
        'class' : 'form-control'
    }),
        empty_label=None
    )

    class Meta:
        model = Blog
        fields = (
            'title',
            'description',
            'category',
            'image'
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description',
                'rows': 3
            })
            

        }