from django import forms
from . models import Contact


class FormContact(forms.ModelForm):
    name = forms.CharField(max_length=150, label= "Name", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name',
        'required': 'required',
    }))
    email = forms.EmailField(label= "Email",widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email',
        'required': 'required'
    }))
    subject = forms.CharField(max_length=20, label="Subject", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject',
        'required': 'required'
    }))
    message = forms.CharField( label="Message", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'rows': '5',
        'required': 'required',
    }))

    class Meta: #class dùng để lưu các thông tin vào model mình chọn,vd: model Contact
        model = Contact
        fields = '__all__' # lưu tất cả các fields đã điền thông tin vào model Contact ,có thể lưu số lượng fields muốn lưu.
