from django import forms
from core.models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'email',
            'message'
        )
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control'
            }),
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'rows' : 5,
                'cols' : 30
            })
        }

    def clean(self):
            
            value = self.cleaned_data['email']
            if not value.endswith('gmail.com'):
                raise forms.ValidationError('Email must be gmail.com!')
            return super().clean()
    
        
    def clean_first_name(self):
            name = self.cleaned_data['first_name']
            return name.lower()