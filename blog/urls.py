
from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index,name='index'),
    path('product_detail/<slug:slug>', views.product_detail,name='product_detail'),  
    path('search/', views.search_function, name='search'),  
    path('category/<slug:slug>/',views.category,name = 'category'),
    path('all/',views.all,name='all'),
    path('register/', views.register, name='register'),
    path('index/<slug:slug>/comment/', views.comment, name='comment'),
    path('cart/',views.cart,name='cart'),
    path('cart/add/<int:product_id>/', views.add_cart , name= 'add_cart'),
    path('cart/detele/<int:item_id>/', views.delete_cart, name= 'delete_cart'),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('create_product',views.create_product,name='create_product'),
    path('product_delete/<int:id>',views.product_delete,name='product_delete'),
    path('profile/product_edit/<int:id>/', views.product_edit , name = 'product_edit'),
    path('profile/',views.profile, name='profile'),
    path('profile/product/', views.user_product,name = 'profile'),
    path('contact/', views.contact,name = 'contact'),
]
