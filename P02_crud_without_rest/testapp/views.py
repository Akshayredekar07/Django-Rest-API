from django.http import HttpResponse, JsonResponse
from django.views import View
import json
from testapp.models import Employee  
import requests

class EmployeeCBV(View):
    def get(self, request, *args, **kwargs):  
        # Accept 'id' parameter from URL
        try:
            emp = Employee.objects.get(1)
            emp_data = {
                'eno': emp.eno,
                'ename': emp.ename,
                'esal': emp.esal,
                'eaddr': emp.eaddr,
            }
            return JsonResponse(emp_data) 
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
        

class EmployeeCBV1(View):
    def get(self, request, id, *args, **kwargs):  
        # Accept 'id' parameter from URL
        try:
            emp = Employee.objects.get(id=id)
            emp_data = {
                'eno': emp.eno,
                'ename': emp.ename,
                'esal': emp.esal,
                'eaddr': emp.eaddr,
            }
            return JsonResponse(emp_data) 
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)


from django.core.serializers import serialize


class EmployeeCBV2(View):
    def get(self,request,id,*args, **kwargs):
        emp=Employee.objects.get(id=id)
        json_data=serialize('json',[emp,]) 
        return JsonResponse(json_data, content_type='application/json')
    

