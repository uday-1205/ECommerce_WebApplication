from django.urls import path
from . import views

urlpatterns = [
    path('', views.p1, name='p1'),
    path('shop', views.shop, name='shop'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('login1', views.login1, name='login1'),
    path('signup1', views.signup1, name='signup1'),
    path('viewall', views.viewall, name='viewall'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('cart', views.cart, name='cart'),
    path('filtering', views.viewall, name='filtering'),
    path('addingcart', views.addingcart, name='addingcart'),
    path('sale',views.sale,name='sale'),
    path('sales',views.sales,name='sales'),
     path('viewal', views.viewal, name='viewal'),
]




