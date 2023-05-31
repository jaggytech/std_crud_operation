from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

def home(request):
    std=Student.objects.all()

    return render(request,"std/home.html",{'std':std})

def add_student(request):
    if request.method=='POST':
        #print("Student details")
        #retreive the data from form
        std_roll=request.POST.get("std_roll")
        std_name=request.POST.get("std_name")
        std_email=request.POST.get("std_email")
        std_address=request.POST.get("std_address")

        # create a object for Model
        s=Student()
        s.roll=std_roll
        s.name=std_name
        s.email=std_email
        s.address=std_address


        # Save the data to DB
        s.save()
        return redirect("/std/home")

    return render(request,"std/add_student.html",{})

def delete_std(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()

    return redirect("/std/home")

def update_std(request,roll):
    st=Student.objects.get(pk=roll)
    return render(request,"std/update_std.html", {'st':st})

def do_update_std(request,roll):
    if request.method=='POST':
        std_roll=request.POST.get("std_roll")
        std_name=request.POST.get("std_name")
        std_email=request.POST.get("std_email")
        std_address=request.POST.get("std_address")

        s=Student.objects.get(pk=roll)
        s.roll=std_roll
        s.name=std_name
        s.email=std_email
        s.address=std_address

        s.save()

        return redirect("/std/home")
    