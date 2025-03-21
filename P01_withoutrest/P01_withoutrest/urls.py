"""
URL configuration for P01_withoutrest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.emp_data_view),
    path('json/', views.json_view),
    path('json1/', views.django_json_view),
    path('jsoncbv/', views.JsonCBV.as_view()),
    path('jsoncbv1/', views.JsonCBV1.as_view()),
    path('jsoncbv2/', views.JsonCBV1.as_view()),
]
