from cProfile import Profile
from django.contrib import admin
from .models import Category, Product,Comment,Profile,Application


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','created']
    list_filter = ['created']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Application)

