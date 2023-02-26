from django.db import models
from django.contrib.auth.models import User


class KhachHang(models.Model):
    ho = models.CharField(max_length=255,blank=False) #blank=False để điền thông tin có giá trị
    ten = models.CharField(max_length=255,blank=False)
    email= models.EmailField(unique=True) # unique=True =đăng ký bằng email độc quyền duy nhất,báo nếu trùng email
    mat_khau = models.CharField(max_length=50,blank=False)
    dien_thoai = models.CharField(max_length=20)
    dia_chi =   models.TextField()

    def __str__(self):
        return self.ten
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT) # onetoone copy từng field từ mẹ cho table con-(User cho Customer),  
    dien_thoai = models.CharField(max_length=20) # Foreignkey= one to many - 1 model mẹ có thể có nhiều trong models con
    dia_chi =   models.TextField()               # manytomany 1 models mẹ có thể có nhiều models id khác

    def __str__(self):
        return f'{self.user.username} and {self.dien_thoai}'

    class Meta:
        db_table = u'customers'    