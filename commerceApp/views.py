from django.shortcuts import render,redirect
from .forms import Featured_Products
from .forms import Sales_Information
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def p1(request):
    
    context=Featured_Products.objects.filter(name='pant') | Featured_Products.objects.filter(name='green shirt')
    return render(request,'p1.html',{'context':context})

def shop(request):
    return render(request,'shop.html')
def blog(request):
    return render(request,'blog.html')
def login(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')
def contacts(request):
    return render(request,'contacts.html')
def cart(request):
    return render(request,'cart.html')
def signup(request):
    return render(request,'signup.html')
def login1(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
         
            auth.login(request,user)
          
            return redirect('p1')
        else:
            messages.info(request,'Credentials are invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
def signup1(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if(password==password2):
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return  redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already used')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not the same')
            return redirect('signup')
    else:
        return redirect('signup')


def viewall(request):
    if request.method == 'POST':
        name = request.POST['brandname']
        images = Featured_Products.objects.filter(name=name)
        return render(request, 'filtering.html', {'images': images})
    else:
        return render(request, 'p1.html')



def addingcart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Featured_Products.objects.get(id=product_id)
        cart_products = request.session.get('cart_products', [])
        cart_products.append({
            'id': product.id,
            'name': product.name,
            'price': product.cost,
            'image': product.image.url,
        })
        request.session['cart_products'] = cart_products
    return redirect('cart')
def cart(request):
    cart_products = request.session.get('cart_products', [])
    total_price = sum([p['price'] for p in cart_products])
    return render(request, 'cart.html', {'cart_products': cart_products, 'total_price': total_price})

   


def sale(request):
    if request.method == 'POST':
        context=Sales_Information.objects.all()
        return render(request,'sales.html',{'context':context})




from django.utils import timezone
from .models import Sales_Information

def sales(request):
    current_time = timezone.now()
    ongoing_sales = Sales_Information.objects.filter(date_starts__lte=current_time, date_ends__gte=current_time)
    context = {'ongoing_sales': ongoing_sales}
    return render(request, 'p1.html', context)

def viewal(request):
    context=Featured_Products.objects.all()
    return render(request,'viewall.html',{'context':context})





    