from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .models import Faculty
from .forms import  FacultyForm
 
# Create your views here.

def faculty(request):
    faculties = Faculty.objects.all()
    context={'faculties': faculties}
    return render(request,'faculty_app/Scrollable-Faculty.html',context)


def loginPage(request):
    faculty = FacultyForm()
    
    if request.method == 'POST':
        
        faculty = FacultyForm(request.POST)
        email=request.POST['email']
        password=request.POST['password']

        user = auth.authenticate(email=email,password=password)

        if user is not None:
           auth.login(request,user)
           messages.success(request, 'You are logged in')
           return redirect('dashboard')
        else:
           messages.error(request, 'Invalid login credentials !')
           return redirect('login')        
       
    return render(request,'faculty_app/login.html')

def dashboard(request):
   return render(request,"faculty_app/dashboard.html") 

def add_faculty(request):  
    faculty = FacultyForm()
    if request.method == 'POST':
        faculty = FacultyForm(request.POST)
        if faculty.is_valid():
            faculty.save()
            return redirect('faculty')         
    return render(request,"faculty_app/add_form.html",{'form':faculty})


def viewFaculty(request,pk):  
    faculties = Faculty.objects.get(id=pk)
    form=FacultyForm(instance=faculties)
    
    context = {'form':form} 
    return render(request,'faculty_app/view_form.html', context)


def updateFaculty(request,pk):  
    faculties = Faculty.objects.get(id=pk)
    form=FacultyForm(instance=faculties)
               
    if request.method == 'POST':
        form = FacultyForm(request.POST,instance=faculties)                
        if form.is_valid():              
            form.save()  
            return redirect('faculty')        
    context = {'form':form}    
    return render(request,'faculty_app/edit2_form.html', context)


def deleteFaculty(request,pk):
      
    faculties = Faculty.objects.get(id=pk)
                       
    if request.method == 'POST':
        faculties.delete()
        return redirect('faculty')
        
    context = {'obj':faculties} 
    
    return render(request,'faculty_app/delete_template.html', context)
