
### **Steps to Create a Django Project and an App**  

#### **1. Create a Django Project**  
Open your terminal or command prompt and run:  
```sh
django-admin startproject P01_withoutrest
```
This creates a new Django project named **P01_withoutrest**.  

#### **2. Navigate to the Project Directory**  
Move into the newly created project directory:  
```sh
cd P01_withoutrest
```

#### **3. Create a Django App**  
Run the following command to create a new app inside the project:  
```sh
python manage.py startapp testapp
```
This creates an app named **testapp** within the project.

#### **4. Register the App in `settings.py`**  
Open `P01_withoutrest/settings.py` and add `'testapp',` inside the `INSTALLED_APPS` list:  
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testapp',  # Add this line
]
```

#### **5. Run the Development Server**  
Start the Django development server:  
```sh
python manage.py runserver
```
This will start the server at `http://127.0.0.1:8000/`.  

---

### **Project Structure After Creation**  
```
P01_withoutrest/
│── manage.py
│── P01_withoutrest/
│   │── __init__.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│── testapp/  # Newly created app
│   │── migrations/
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── tests.py
│   │── views.py
```
---

### **`*args` vs `**kwargs` in Python**

### `*args` → **Variable Length Positional Arguments**  

### Explanation:
- `*args` allows us to pass a variable number of positional arguments to a function.
- Internally, `*args` collects all values into a **tuple**.
- Useful when the number of arguments is unknown beforehand.

### Example 1: Summing Numbers  
```python
def calculate_sum(*args):
    total = sum(args)
    print("Total Sum:", total)

calculate_sum()
calculate_sum(5, 10)
calculate_sum(3, 7, 2, 8, 10)
```
#### Output:
```
Total Sum: 0
Total Sum: 15
Total Sum: 30
```

### Example 2: Joining Strings  
```python
def concatenate_strings(*args):
    result = " ".join(args)
    print("Concatenated String:", result)

concatenate_strings("Hello", "World")
concatenate_strings("Python", "is", "awesome!")
```
#### Output:
```
Concatenated String: Hello World
Concatenated String: Python is awesome!
```


## `**kwargs` → **Variable Length Keyword Arguments**  

### Explanation:
- `**kwargs` allows us to pass a variable number of **keyword arguments** (key-value pairs) to a function.
- Internally, `**kwargs` collects all key-value pairs into a **dictionary**.
- Useful when we want to handle named arguments dynamically.

### Example 1: Printing Student Details  
```python
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Tanvi", age=20, grade="A")
student_info(name="Rohit", age=22, department="Computer Science")
```
#### Output:
```
name: Tanvi
age: 20
grade: A

name: Rohit
age: 22
department: Computer Science
```

### Example 2: Merging Dictionaries  
```python
def merge_dicts(defaults, **kwargs):
    defaults.update(kwargs)
    return defaults

default_settings = {"theme": "light", "language": "English"}
user_settings = merge_dicts(default_settings, theme="dark", font_size=14)

print(user_settings)
```
#### Output:
```
{'theme': 'dark', 'language': 'English', 'font_size': 14}
```


## **Using `*args` and `**kwargs` Together**
### Example: Flexible Function Parameters  
```python
def display_info(*args, **kwargs):
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)

display_info(10, 20, 30, name="Om", age=25)
```
#### Output:
```
Positional Arguments: (10, 20, 30)
Keyword Arguments: {'name': 'Om', 'age': 25}
```
---

### **Mixin (Mixed In)**  

- Mixins are a special type of inheritance in Python.  
- It is a **limited version of multiple inheritance**.  
- In multiple inheritance, we can create objects for the parent class, and the parent class can extend other classes. But in Mixins:  
  - The **parent class cannot be instantiated**.  
  - The **parent class must be a direct child of `object`**, meaning it cannot extend other classes.  
- In multiple inheritance, the parent class can contain instance variables. But in Mixins:  
  - The **parent class cannot contain instance variables**, only **class-level static variables**.  
- The **main purpose** of the parent class in Mixins is to provide **functions** to child classes.  


### **Differences Between Mixins and Multiple Inheritance**  

| **Mixins** | **Multiple Inheritance** |
|------------|-------------------------|
| Parent class instantiation is **not** possible. | Parent class instantiation is **possible**. |
| Contains only **instance methods**, but **not instance variables**. | Contains both **instance methods** and **instance variables**. |
| Methods are useful **only for child classes**. | Methods are useful for **both parent and child classes**. |
| Parent class must be a **direct child of `object`**. | Parent class can extend **any other class** (not necessarily `object`). |

---

### **Important Notes on Mixins**  

1) **Mixins are reusable classes in Django.**  
2) **Mixins are available only in languages that support multiple inheritance**, like **Python, Ruby, Scala, etc.**  
3) **Mixins are not applicable for Java and C#**, because these languages **do not support multiple inheritance**.  

---

### **Writing CBV (Class-Based View) Using Mixin Class**  

#### **Mixin Class (`mixins.py`)**  
```python
from django.http import JsonResponse

class JsonResponseMixin(object):
    def render_to_json_response(self, context, **kwargs):
        return JsonResponse(context, **kwargs)
```

#### **Class-Based View (CBV) Using Mixin**  
```python
from testapp.mixins import JsonResponseMixin
from django.views import View

class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        employee_data = {
            'eno': 100,
            'ename': 'Durga',
            'esal': 1000,
            'eaddr': 'Hyderabad'
        }
        return self.render_to_json_response(employee_data)
```
