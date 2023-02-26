from django import forms
from django.contrib.auth.models import User
from .models import KhachHang , Customer


class FormDangKy(forms.ModelForm):
    ho = forms.CharField(max_length=255,label='Họ', widget= forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Họ",
        "required": "required",
    }))
    ten = forms.CharField(max_length=255,label='Tên', widget= forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Tên",
        "required": "required",
    }))
     
    email = forms.EmailField(label= "Email",widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email",
        "required": "required",
    }))

    mat_khau = forms.CharField(label= "Mật Khẩu", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Mật Khẩu",
        "required": "required",
    }))

    xac_nhan_mat_khau = forms.CharField(label= "Xác Nhận Mật Khẩu", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Xác Nhận Mật Khẩu",
        "required": "required",
    }))

    dien_thoai = forms.CharField(max_length=20, label=" Điện Thoại", widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Điện Thoại",
        "required": "required",
    }))

    dia_chi = forms.CharField(label=" Địa Chỉ", widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Địa Chỉ",
        "row": "3",
    }))

    class Meta:
        model = KhachHang
        fields = "__all__" # có thể dùng list lưu 1 số fields ['ho','ten',....]


class FormUser(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Username", widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username",
        "required": "required",
    }))   

    email = forms.EmailField(label= "Email",widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email",
        "required": "required",
    }))

    last_name = forms.CharField(max_length=255, label="Họ", widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Họ",
        "required": "required",
    }))

    first_name = forms.CharField(max_length=255, label="Tên", widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Tên",
        "required": "required",
    }))

    password = forms.CharField(label= "Mật Khẩu", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Mật Khẩu",
        "required": "required",
    }))

    confirm_password = forms.CharField(label= "Xác Nhận Mật Khẩu", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Xác Nhận Mật Khẩu",
        "required": "required",
    }))

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password')


class FormCustomer(forms.ModelForm):  
    dien_thoai = forms.CharField(max_length=20, label=" Điện Thoại", widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Điện Thoại",
        "required": "required",
    }))

    dia_chi = forms.CharField(label=" Địa Chỉ", widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Địa Chỉ",
        "row": "3",
    }))

    class Meta:
        model = Customer
        exclude = ('user',) # exclude khai báo những fields sẽ không lấy trong model


   
