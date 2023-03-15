from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'email' , 'content']
        labels = {
           'title':'タイトル',
           'email': 'メールアドレス',
           'content':'内容',
        }