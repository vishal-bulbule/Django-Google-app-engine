# Deploy Django Notes application on Google App Engine with CloudSQL(MySQL)

Learn how to deploy your Django application on Google App Engine, integrate it with Cloud SQL, and map it to a custom domain in this comprehensive tutorial. I'll guide you step-by-step through the entire process, from setting up your Google Cloud environment to configuring your Django app for production. Whether you're a beginner or an experienced developer, this video will help you get your Django project up and running smoothly on Google Cloud Platform.

Refer youtube Video for this project
 [![YouTube](https://img.shields.io/badge/YouTube-Video-red)](https://youtu.be/z8AUu0C8aKo)
 
## Topics Covered:

- Build and Test Django App in Local
- Setting up Google App Engine
- Deploy Django App on Google App Engine
- Connecting Django to Cloud SQL (MySQL)
- Mapping a custom domain to your app


<img width="636" alt="image" src="https://github.com/vishal-bulbule/Django-Google-app-engine/assets/143475073/1ecd1e87-cb7f-4ebf-b0cc-dcda3979be3f">


### Step 1: Set Up Your Django Project

1. **Install Django:**
   ```sh
   pip install django
   ```

2. **Create a New Django Project:**
   ```sh
   django-admin startproject notes_project
   cd notes_project
   ```

3. **Start the Development Server:**
   ```sh
   python manage.py runserver
   ```

### Step 2: Create the Notes App

1. **Create a New Django App:**
   ```sh
   python manage.py startapp notes
   ```

2. **Add the App to Installed Apps:**
   Edit `notes_project/settings.py` and add `'notes'` to the `INSTALLED_APPS` list:
   ```python
   INSTALLED_APPS = [
       ...
       'notes',
   ]
   ```

### Step 3: Define the Note Model

1. **Create the Note Model:**
   Edit `notes/models.py` to define the Note model:
   ```python
   from django.db import models

   class Note(models.Model):
       title = models.CharField(max_length=200)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return self.title
   ```

2. **Create and Apply Migrations:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

### Step 4: Create the Note Views

1. **Create Views for Listing, Creating, and Viewing Notes:**
   Edit `notes/views.py` to add the necessary views:
   ```python
   from django.shortcuts import render, get_object_or_404, redirect
   from .models import Note
   from .forms import NoteForm

   def note_list(request):
       notes = Note.objects.all()
       return render(request, 'notes/note_list.html', {'notes': notes})

   def note_detail(request, pk):
       note = get_object_or_404(Note, pk=pk)
       return render(request, 'notes/note_detail.html', {'note': note})

   def note_create(request):
       if request.method == 'POST':
           form = NoteForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('note_list')
       else:
           form = NoteForm()
       return render(request, 'notes/note_form.html', {'form': form})
   ```

### Step 5: Create the Forms

1. **Create a Form for the Note Model:**
   Create `notes/forms.py`:
   ```python
   from django import forms
   from .models import Note

   class NoteForm(forms.ModelForm):
       class Meta:
           model = Note
           fields = ['title', 'content']
   ```

### Step 6: Create the URLs

1. **Define URLs for the Notes App:**
   Create `notes/urls.py`:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.note_list, name='note_list'),
       path('<int:pk>/', views.note_detail, name='note_detail'),
       path('new/', views.note_create, name='note_create'),
   ]
   ```

2. **Include Notes URLs in the Project URLs:**
   Edit `notes_project/urls.py`:
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('notes/', include('notes.urls')),
   ]
   ```

### Step 7: Create Templates

1. **Create Templates Directory and Templates:**
   Create a directory `notes/templates/notes/` and add the following HTML files:

   - `note_list.html`:
     ```html
     <!DOCTYPE html>
      <html> 
      <head>
          <title>{{ note.title }}</title>
          <style>
              body {font-family: Arial, sans-serif;}
              .header {background-color: #362264;color: white;padding: 5px;text-align: center;}
              .container {padding: 20px;}
              form {margin-top: 20px;}
          </style>
      </head>    
      <body>
          <div class="header">
               <h1>TechTrapture Notes</h1>
          </div>
          <h1>Notes</h1>
          <ul>
              {% for note in notes %}
              <li><a href="{% url 'note_detail' note.pk %}">{{ note.title }}</a></li>
              {% endfor %}
          </ul>
          <a href="{% url 'note_create' %}">Add a new note</a>
      </body>
      </html>
     ```

   - `note_detail.html`:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <title>{{ note.title }}</title>
       <style>
         body {font-family: Arial, sans-serif;}
         .header {background-color: #362264;color: white;padding: 5px;text-align: center;}
         .container {padding: 20px;}
         form {margin-top: 20px;}
     </style>
     </head>
      <body>
          <div class="header">
              <h1>TechTrapture Notes</h1>
          </div>
          <h1>{{ note.title }}</h1>
          <p>{{ note.content }}</p>
          <p><a href="{% url 'note_list' %}">Back to Notes</a></p>
      </body>
     </html>
     ```

   - `note_form.html`:
     ```html
         <!DOCTYPE html>
         <html>
         
         <head>
             <title>{{ note.title }}</title>
           <style>
               body {font-family: Arial, sans-serif;}
               .header {background-color: #362264;color: white;padding: 5px;text-align: center;}
               .container {padding: 20px;}
               form {margin-top: 20px;}
           </style>
               
         </head>
         
         <body>
             <div class="header">
                 <h1>TechTrapture Notes</h1>
             </div>
             <h1>New Note</h1>
             <form method="post">
                 {% csrf_token %}
                 {{ form.as_p }}
                 <button type="submit">Save</button>
             </form>
         </body>
         
         </html>
     ```

### Step 8: Run the Application

1. **Start the Development Server:**
   ```sh
   python manage.py runserver
   ```

2. **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:8000/notes/` to see your notes application in action.

### Conclusion

You've now created a simple notes application with Django that allows you to list, view, and create notes. This basic setup can be expanded with additional features like updating and deleting notes, user authentication, and more advanced styling with CSS frameworks like Bootstrap.


To deploy your Django application on Google App Engine , follow these steps:

### Step 1: Set Up Your Django Project for Deployment

1. **Create CloudSQL MySQL Instance**
   Ensure you have CloudSQL MySQL Instance created and one database for application is created.

2. **Update `settings.py`:**
   Add the necessary configurations for static files and allowed hosts.
   ```python
       DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/tt-dev-001:us-central1:dev',
            'PORT' : '3306',
            'USER': 'root',
            'PASSWORD': 'mysql',
            'NAME': 'appdb',
        }
      }
   ```

3. **Create `requirements.txt`:**
   Generate a `requirements.txt` file for the dependencies.
   ```sh
      Django
      mysqlclient
   ```

4. **Download and install the Cloud SQL Auth Proxy to your local machine.**
   Right-click https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.11.3/cloud-sql-proxy.x64.exe and select Save Link As to download the Cloud SQL Auth Proxy. Rename the file to cloud-sql-proxy.exe.
   In seperate terminal run Cloud SQL Auth Proxy
   ```sh
      ./cloud-sql-proxy PROJECT_ID:REGION:INSTANCE_NAME
   ```
 5. **Run the Django migrations to set up your models on New Database i.e Cloud SQL.**
   ```sh
      python manage.py makemigrations
      python manage.py migrate
  ```
 Now run and Test Application locally

  **Start the Development Server:**
   ```sh
   python manage.py runserver
   ```

 **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:8000/notes/` to see your notes application in action.

6. **Create `app.yaml`:**
   Create an `app.yaml` file in your project's root directory.
   ```yaml
      runtime: python39
      service: noteapp
   ```
7. **Create `main.py`:**
   Add the necessary configurations for static files and allowed hosts.
   ```python
      from notes_project.wsgi import application
      app = application
   ```

### Step 2: Deploy to Google App Engine

1. **Install Google Cloud SDK:**
   If you haven’t already, install the Google Cloud SDK by following the [installation guide](https://cloud.google.com/sdk/docs/install).

2. **Initialize Your Google Cloud Project:**
   ```sh
   gcloud init
   ```

3. **Authenticate Your Google Cloud Account:**
   ```sh
   gcloud auth login
   ```

4. **Set the Project:**
   ```sh
   gcloud config set project YOUR_PROJECT_ID
   ```

5. **Deploy Your Application:**
   Deploy your application to Google App Engine.
   ```sh
   gcloud app deploy
   ```

6. **Browse Your Application:**
   Open your browser to view the deployed application.
   ```sh
   gcloud app browse
   ```

To Map custom Domain Use  Below Link - [Mapping custom Domain to Google App Engine](https://cloud.google.com/appengine/docs/legacy/standard/python/mapping-custom-domains)

### Conclusion

This guide walks you through setting up a Django application for deployment on Google App Engine. It includes steps for configuring your Django project, preparing it for deployment, and deploying it using the Google Cloud SDK. By following these steps, you can ensure your application is ready for a scalable and reliable deployment on Google App Engine.

<img width="746" alt="image" src="https://github.com/vishal-bulbule/Django-Google-app-engine/assets/143475073/79ade334-5e0d-4dc3-b312-1ae25acf11e4">


