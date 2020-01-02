"""smls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('slms/', include('blog.urls', namespace='blog')),
    path('slms-shop/', include('shop.urls', namespace='shop')),
    path("slms-students/", include('students.urls', namespace='students')),
    path("slms-staffs/", include('staffs.urls', namespace='staffs')),
    path('slms-account/', include('register.urls', namespace= 'register')),
    path('slms_shopping_cart/', include('cart.urls', namespace='cart')),
    path("slms/", include('django.contrib.auth.urls')),
  path("paystack", include(('paystack.urls', 'paystack'),namespace='paystack')),
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
