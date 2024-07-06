from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from shop_sec.models import Product,Contact,Add,Orders
from math import ceil
from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic import (DetailView,ListView,TemplateView,CreateView,
                                  DeleteView)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


def index(request):
    cat=Product.objects.values('category')
    item=[]
    dogs={items['category'] for items in cat}
    for send_items in dogs:
        prod =Product.objects.filter(category=send_items)
        n=len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        item.append([prod,range(1,nSlides),n])
    
    
    params = {'product': item}
    return render(request, 'shop/index.html', params)


class Contact(LoginRequiredMixin,CreateView):
    template_name='shop/contact.html'
    model = Contact
    fields=['name','email','phone','description']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user=self.request.user
        return super().form_valid(form)

class Complain(TemplateView):
    template_name='shop/contact_received.html'

def tracker(requests):
    return render(requests, 'shop/tracker.html')

def searchMatch(query,item):
    if query in item.Description.lower() or query in item.prod_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(requests):
    query= requests.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'product': allProds}
    
    return render(requests, 'shop/search.html',params)


class ProductDetail(DetailView):
    model=Product
    template_name='shop/prod.html'
    context_object_name='product'


class AboutPage(TemplateView):
    template_name='shop/about.html'


def cart(requests,id):   
    try:
        
        pro=Product.objects.get(id=id)
        val=Add.objects.get(prod_name=pro,user=requests.user)
        if (pro.prod_name == val.prod_name):
            messages.success(requests,'Items already in your cart')
            pass
            
    except Exception as e:
        product=Product.objects.get(id=id)
        abs=Add(category=product.category,sub_category=product.sub_category,prod_name=product.prod_name,Description=product.Description,price=product.price,img=product.img,discount=product.discount,user=requests.user)
        abs.save()
        
    
    return redirect("index")


class ViewToCart(LoginRequiredMixin,ListView):
    model=Add
    template_name='shop/cart.html'
    context_object_name='product'

    def get_queryset(self) -> QuerySet[Any]:
        data=Add.objects.filter(user=self.request.user)
        return data
        


def remove(requests,id):
    product=Add.objects.filter(id=id)
    product.delete()
    messages.success(requests,'Item has been removed from your cart')
    return redirect('viewcart',requests.user)


class PlaceOrders(CreateView):
    model=Orders
    fields=['name','maddress','caddress','email','phone','quantity']
    template_name='shop/order.html'
    

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user=self.request.user
        form.instance.product_name=self.kwargs.get('prod_name')
        return super().form_valid(form)


class Success(TemplateView):
    template_name='shop/success.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        order=Orders.objects.get(id=self.kwargs.get('pk'))
        context['prod_name']=order.product_name
        context['quantity']=order.quantity
        prod_obj=Add.objects.get(prod_name=order.product_name,user=self.request.user)
        prod_price=prod_obj.price
        context['total_amount']=int(prod_price*order.quantity)
        context['prod_id']=order.id
        return context

def logout_view(request):
    logout(request)
    messages.success(request,"You have been logout successfully")
    return redirect('index')