
### **Steps to Create a Django Project and an App**  

#### **1. Create a Django Project**  
Open your terminal or command prompt and run:  
```sh
django-admin startproject P02_crud_without_rest
```
This creates a new Django project named **P01_withoutrest**.  

#### **2. Navigate to the Project Directory**  
Move into the newly created project directory:  
```sh
cd P02_crud_without_rest
```

#### **3. Create a Django App**  
Run the following command to create a new app inside the project:  
```sh
python manage.py startapp testapp
```
This creates an app named **testapp** within the project.

#### **4. Register the App in `settings.py`**  
Open `P02_crud_without_rest/settings.py` and add `'testapp',` inside the `INSTALLED_APPS` list:  
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


### **Status Codes**

Status code represents the status of HttpResponse. The following are various possible status codes:

- **1XX → Informational**  
- **2XX → Successful**  
- **3XX → Redirection**  
- **4XX → Client Error**  
- **5XX → Server Error**  



#### **1XX → Informational**  
These indicate that the request has been received and is being processed.  
- **100 Continue** → The server has received the request headers, and the client should continue sending the body.  
- **101 Switching Protocols** → The client has requested the server to switch protocols, and the server agrees.  
- **102 Processing** → The server is still processing the request but has not completed it yet.  
- **103 Early Hints** → Used to return response headers before the final HTTP message.

#### **2XX → Successful**  
- **200 OK** → The request was successful.  
- **201 Created** → A new resource has been successfully created.  
- **204 No Content** → The request was successful, but there is no response body.  

#### **3XX → Redirection**  
- **301 Moved Permanently** → The resource has been permanently moved to a new URL.  
- **302 Found** → The resource is temporarily available at a different location.  
- **304 Not Modified** → The resource has not been modified since the last request (used for caching).  

#### **4XX → Client Error**  
- **400 Bad Request** → The request is malformed and cannot be processed.  
- **401 Unauthorized** → Authentication is required but missing or invalid.  
- **403 Forbidden** → The client does not have permission to access the resource.  
- **404 Not Found** → The requested resource could not be found on the server.  
- **429 Too Many Requests** → The client has sent too many requests in a short period.  

#### **5XX → Server Error**  
- **500 Internal Server Error** → A generic server error.  
- **502 Bad Gateway** → The server received an invalid response from an upstream server.  
- **503 Service Unavailable** → The server is temporarily unavailable due to maintenance or overload.  
- **504 Gateway Timeout** → The upstream server did not respond in time.  
