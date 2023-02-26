from django.contrib import admin
from . import models



#admin.site.register(models.Category)
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin): 
    search_fields = ['name']
    ordering = ['name'] #đặt tên biến theo đúng mặc định của model admin
    list_display = ['name','slug'] #đặt tên biến theo đúng mặc định của model admin

@admin.register(models.SubCategory)
class SubcategoreAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category']
    prepopulated_fields= {     #tạo thêm subcategory tự động thêm slug( chỉ dùng tiếng việt không dấu)
        'slug': ['name']
    }
    ordering = ['name'] # ordering dùng để hiện mũi tên sắp xếp thứ tự
    list_display = ['category_name','name','image','slug'] 
    search_fields = ['name']

    def category_name(self, subcategory):
        return subcategory.category.name

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['subcategory']
    ordering = ['name','viewed']
    list_display = ['name','price','viewed','viewed_status','subcategory_name']     
    list_filter = ['public_day','subcategory'] #tạo filter danh mục
    list_per_page = 10 # phân trang
    list_editable = ['price'] # biến cho phép chỉnh sửa thông tin bên ngoài không cần bấm vào form
    search_fields = ['name__startswith'] # tìm kiếm theo giá trị,__startswith bắt đầu chữ tìm kiếm,__endswith kết thúc bằng từ tìm kiếm.thêm i đầu start để nhận hoa thường.

    def subcategory_name(self, product):
        return product.subcategory.name 
    @admin.display(ordering='viewed') # sắp xếp theo model có sẵn
    def viewed_status(self, product):
        if product.viewed == 0:
            return "no"
        return "yes"    
