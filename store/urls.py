"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from appStoreV2.views.productView import product_api_view, product_detail_view
from appStoreV2.views.clientView import client_api_view, client_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('producto/', include('appStoreV2.views.urls'))
    # path('producto/', ProductAPIView.as_view()),
    path('producto/', product_api_view),
    path('producto/<int:pk>/', product_detail_view),
    path('client/', client_api_view),
    path('client/<int:pk>/', client_detail_view),
]
