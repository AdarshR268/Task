from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def admin_logout(request):
    logout(request)
    return redirect('login')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_student')
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'login.html')

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        course_interest = request.POST.get('course_interest')
        status = request.POST.get('status')
        
        # Check for duplicate email
        if Student.objects.filter(email=email).exists():
            messages.error(request, f'A student with the email {email} already exists.')
            # Re-render form retaining the filled data
            context = {
                'name': name,
                'email': email,
                'course_interest': course_interest,
                'status': status
            }
            return render(request, 'home.html', context)
        
        Student.objects.create(
            name=name,
            email=email,
            course_interest=course_interest,
            status=status
        )
        messages.success(request, 'Student added successfully!')
        return redirect('list_students')
        
    return render(request, 'home.html')

def list_students(request):
    query = request.GET.get('course', '')
    if query:
        students = Student.objects.filter(course_interest__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'list.html', {'students': students, 'query': query})
