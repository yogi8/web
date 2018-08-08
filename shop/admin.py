from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']             #things need to be displayed while creating a category.
    prepopulated_fields = {'slug': ('name',)}   #autofills slug field with name.
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock','available', 'created', 'updated']  #things need to be displayed while creating a product.
    list_filter = ['available', 'created', 'updated']     #autofills slug field with name.
    list_editable = ['price', 'stock', 'available']       #helps in editing the fields on the display itself.
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

