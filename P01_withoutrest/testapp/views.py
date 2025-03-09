from django.shortcuts import render
from django.http import HttpResponse

import json


# Create your views here.
def emp_data_view(request):
    
    emp_data={
        'eno': 100,
        'ename': 'Durga',
        'esal': 75000,
        'eaddr': 'Bengluru',
        'designation': 'Software Engineer',
        'department': 'Engineering',
        'hire_date': '2023-01-15',
        'email': 'durga.prasad@company.com',
        'phone': '555-123-4567'
    }

    res = f"""
    Employee Number: {emp_data['eno']}
    Name: {emp_data['ename']}
    Salary: {emp_data['esal']}
    Address: {emp_data['eaddr']}
    Designation: {emp_data['designation']}
    Department: {emp_data['department']}
    Hire Date: {emp_data['hire_date']}
    Email: {emp_data['email']}
    Phone: {emp_data['phone']}
    """

    return HttpResponse(res)


def json_view(request):
    emp_data={
        'eno': 100,
        'ename': 'Durga',
        'esal': 75000,
        'eaddr': 'Bengluru',
        'designation': 'Software Engineer',
        'department': 'Engineering',
        'hire_date': '2023-01-15',
        'email': 'durga.prasad@company.com',
        'phone': '555-123-4567'
        }

    json_data=json.dumps(emp_data)
    
    return HttpResponse(content=json_data, content_type='application/json')


from django.http import JsonResponse

def django_json_view(request):
    emp_data={
        'eno': 100,
        'ename': 'Durga prasad',
        'esal': 75000,
        'eaddr': 'Bengluru',
        'designation': 'Java Trainer',
        'department': 'Engineering',
        'hire_date': '2023-01-15',
        'email': 'durga.prasad@company.com',
        'phone': '555-123-4567'
    }

    return JsonResponse(emp_data)






from django.views.generic import View

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
            emp_data={
            'eno': 100,
            'ename': 'Durga',
            'esal': 75000,
            'eaddr': 'Bengluru'
            }

            return JsonResponse(emp_data)
    

class JsonCBV1(View):
    def get(self, _request, *_args, **_kwargs):
            json_data=json.dumps({'msg':'This is msg from get'})
            return HttpResponse(content=json_data, content_type='application/json')
    def post(self, _request, *_args, **_kwargs):
            json_data=json.dumps({'msg':'This is msg from post'})
            return HttpResponse(content=json_data, content_type='application/json')
    def put(self, _request, *_args, **_kwargs):
            json_data=json.dumps({'msg':'This is msg from put'})
            return HttpResponse(content=json_data, content_type='application/json')
    def delete(self, _request, *_args, **_kwargs):
            json_data=json.dumps({'msg':'This is msg from delete'})
            return HttpResponse(content=json_data, content_type='application/json')




from testapp.mixins import HttpResponseMixins


class JsonCBV2(HttpResponseMixins,View):
    def get(self, _request, *_args, **_kwargs):
            json_data=json.dumps({'msg':'This is msg from get'})
            return self.render_to_http_response(json_data)
    
    def post(self, _request, *_args, **_kwargs):
            json_data=json.dumps({'msg':'This is msg from post'})
            return self.render_to_http_response(json_data)
    
    def put(self, _request, *_args, **_kwargs):
            json_data=json.dumps({'msg':'This is msg from put'})
            return self.render_to_http_response(json_data)
    
    def delete(self, _request, *_args, **_kwargs):
            json_data=json.dumps({'msg':'This is msg from delete'})
            return self.render_to_http_response(json_data)
    

    