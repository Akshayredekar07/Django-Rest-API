from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.EmployeeCBV.as_view()),  
    path('api1/<int:id>/', views.EmployeeCBV1.as_view()),  
    path('api2/<int:id>/', views.EmployeeCBV2.as_view()),  
]
