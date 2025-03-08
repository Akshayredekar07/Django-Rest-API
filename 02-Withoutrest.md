
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