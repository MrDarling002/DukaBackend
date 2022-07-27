from cProfile import Profile
import profile
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import render, redirect, reverse
from .models import Cart, Category, Comment, Product
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models.deletion import ProtectedError
from .forms import ApplicationForm
from django.core.files.storage import FileSystemStorage
from .translit import translit
from random import randint
from django.utils import timezone




#Главная страница продуктов
def index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(moderate=1).order_by('-created')
    return render(request,'index.html',{'categories': categories,'products': products})

#Все продукты
def all(request):
    categories = Category.objects.all()
    products = Product.objects.filter(moderate=1).order_by('-created')
    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'all.html',{'page_obj':page_obj})

def category(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug__exact=slug)
    product=Product.objects.filter(category=category)
    return render(request,'category.html', {'categories':categories,'category':category,'product':product})

def contact(request):
    categories = Category.objects.all()
    form = ApplicationForm(request.POST)
    is_succes=False
    if request.method =='POST' and form.is_valid():
        instance=form.save(commit=False)
        is_succes=True
        form.save()
        form=ApplicationForm()
    return render(request,'contact.html',{'is_succes':is_succes,'form':form,})

#Открыть продукт
def product_detail(request,slug):
    category = Category.objects.all()
    product = get_object_or_404(Product,slug=slug)
    comment = Comment.objects.filter().order_by('-date')
    products = Product.objects.order_by('-created')[:4]
    return render(request,'product_detail.html',{'product': product, 'comment':comment,'products':products,'category':category})


#поиск
def search_function(request):
    categories = Category.objects.all()
    query = request.GET.get('search')
    search_obj = Product.objects.filter(Q(name__icontains=query))
    context = {'query': query, 'search_obj':search_obj}
    return render(request, 'search.html', context)

#Регистрация
def register(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user=register_form.save()
            profile=Profile()
            profile.user=user
            return redirect('index')
        else:
            return HttpResponse('Попробуй снова')
    register_form=RegisterForm()
    return render(request,'register/register.html',{'register_form':register_form})

#Логин
def login(request):
    categories = Category.objects.all()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            _login (request,user)
            return redirect('index')
    return render(request,'register/login.html')

#Выход из аккаунта
def logout(request):
    _logout(request)
    return redirect('index')

#Создание продукта
def create_product(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        categories = Category.objects.all()
        context = {'categories':categories}
        if request.method == "POST":
            product = Product()
            product.user = request.user
            product.name = request.POST.get('title')
            product.description = request.POST.get('description')
            new_slug = translit(request.POST.get('title'))
            if Product.objects.filter(slug__exact=new_slug).exists():
                product.slug = new_slug + '' + str(timezone.now().format('Y-m-d_H-i-s')) + '' + str(randint(1, 100))
            else:
                product.slug = new_slug
            if request.FILES.get('image', False) != False:
                myfile = request.FILES.get('image')
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                product.image = filename
            product.phone = request.POST.get('phone')
            product.price = request.POST.get('price')
            product.city = request.POST.get('city')
            product.country = request.POST.get('country')
            product.save()
            category_ids = request.POST.getlist('categories[]')
            for id in category_ids:
                product.category.add(id)
            return redirect('index')
        return render(request, 'create_product.html', context)
    return redirect('login')
    
#Удаление продукта
def product_delete(request, id):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('index')
    return redirect('login')

def product_edit(request, id):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        users = User.objects.all()
        categories = Category.objects.all()
        context = {'product':product, 'users':users,'categories':categories}
        if request.method == "POST":
            product.name = request.POST.get('name')
            product.description = request.POST.get('description')
            if request.FILES.get('image', False) != False:
                myfile = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                product.image = filename
            product.price = request.POST.get('price')
            product.save()
            # category_ids = request.POST.getlist('categories[]')
            # product.category.set(category_ids)
            return redirect('profile')
        return render(request, 'product_edit.html', context)    
    return redirect('login')

#Комментарии
def comment(request, slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug__exact=slug)
    if request.method == 'POST':
        product.comment_set.create(author = request.user, text = request.POST.get('text'))
        return redirect(reverse('product_detail', kwargs = {'slug': product.slug}))
    return redirect(reverse('product_detail', kwargs = {'slug': product.slug}))


def cart(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        product = Cart.objects.filter(user=request.user)
        paginator = Paginator(product, 12)
        page_number = request.GET.get('page')
        product = paginator.get_page(page_number)
        return render(request, 'cart.html',{'product':product})
    return redirect('login')

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        if not request.user.cart_set.filter(product = product).exists():
            item = Cart()
            item.product = product
            item.user = request.user
            item.save()
            return redirect('index')
    return redirect('register')

def delete_cart(request, item_id):
    item = Cart.objects.get(id=item_id)
    if request.user.is_authenticated:
        item.delete()
        return redirect('cart')
    return redirect('register')

def profile(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            user.first_name = request.POST.get('first_name') 
            user.last_name = request.POST.get('last_name') 
            if request.POST.get('password') != '':
                user.password = make_password(request.POST.get('password'))
            user.email = request.POST.get('email')
            user.save()
            return redirect('profile')
        return render(request, 'profile.html')
    return redirect('register')

def user_product(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        product = request.user.product_set.filter(moderate=1).order_by('-created')
        paginator = Paginator(product, 12)
        page_number = request.GET.get('page')
        product = paginator.get_page(page_number)
        return render(request, 'profile.html', {'page_number':page_number,'product':product})
    return redirect('login')