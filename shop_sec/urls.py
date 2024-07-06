from django.contrib import admin
from django.urls import path,include
from shop_sec import views 
from django.contrib.auth import views as auth_views
from .views import ProductDetail,ViewToCart,AboutPage,Contact,Complain,PlaceOrders,Success

urlpatterns = [
    path('',views.index,name='index'),
    path('about',AboutPage.as_view(),name='about'),
    path('contact',Contact.as_view(),name='contact'),
    path('search',views.search,name='search'),
    path('prod_name/<int:pk>',ProductDetail.as_view(),name='productview'),
    path('add-to-cart/<int:id>',views.cart,name='cartty'),
    path('view-cart/<str:username>/',ViewToCart.as_view(),name='viewcart'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('order/<int:id>/<str:prod_name>/',PlaceOrders.as_view(),name='order'),
    path('success/<int:pk>/',Success.as_view(),name='success'),
    path('complain_received/',Complain.as_view(),name='complain'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'),name='password_reset_complete'),
    path('password_reset_confirm/<uidb64>,<token>',auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'),name='password_reset_confirm'),

]
