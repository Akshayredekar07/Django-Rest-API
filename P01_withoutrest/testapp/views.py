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

