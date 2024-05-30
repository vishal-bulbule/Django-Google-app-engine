# test

Creating a simple notes application using Django involves several steps. Below is a step-by-step guide to help you get started:

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
         <title>Notes</title>
     </head>
     <body>
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
     </head>
     <body>
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
         <title>New Note</title>
     </head>
     <body>
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
