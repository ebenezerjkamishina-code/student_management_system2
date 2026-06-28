from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student
from django.contrib import messages




@login_required
def home(request):
    return render(request, 'students/home.html')



@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.created_by = request.user
            student.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})





def courses(request):
    return render(request, 'students/placeholder.html', {'title': 'Courses'})

def results_page(request):
    return render(request, 'students/placeholder.html', {'title': 'Results'})

def past_papers_page(request):
    return render(request, 'students/placeholder.html', {'title': 'Past Papers'})
def resources_page(request):
    return render(request, 'students/placeholder.html', {
        'title': 'Resources',
        'content': 'Textbooks, guides, syllabus and study materials will appear here.'
    })

def elearning_page(request):
    return render(request, 'students/placeholder.html', {
        'title': 'E-Learning', 
        'content': 'Online lessons, video lectures and Moodle links go here.'
    })

def assignments_page(request):
    return render(request, 'students/placeholder.html', {
        'title': 'Assignments',
        'content': 'Submit and track all your coursework assignments here.'
    })
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import StudentRegisterForm

def register_student(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # auto login after register
            messages.success(request, 'Registration successful.')
            return redirect('home')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = StudentRegisterForm()
    return render(request, 'students/register.html', {'form': form})

def login_student(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        messages.error(request, 'Invalid Reg Number or Password')
    else:
        form = AuthenticationForm()
    return render(request, 'students/login.html', {'form': form})

def logout_student(request):
    logout(request)
    return redirect('home')