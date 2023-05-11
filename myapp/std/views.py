from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def home(request):
    std=Student.objects.all()
    return render(request,"std/home.html",{'std':std})

def add_std(request):
    if request.method=='POST':
        
        #fetch the data from form
        std_roll=request.POST.get("std_roll")
        std_name=request.POST.get("std_name")
        std_email=request.POST.get("std_email")
        std_address=request.POST.get("std_address")
        std_phone=request.POST.get("std_phone")
        

        #create a object of model
        std=Student()
        std.roll=std_roll
        std.name=std_name
        std.email=std_email
        std.address=std_address
        std.phone=std_phone

        #save the data
        std.save()
        return redirect("/std/home")

    return render(request,"std/add_emp.html",{})

def delete_std(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect("/std/home")

def update_std(request,roll):
    std=Student.objects.get(pk=roll)
    return render(request,"std/update_std.html", {'std':std})

def do_update_std(request,roll):
    if request.method=='POST':
        std_roll=request.POST.get("std_roll")
        std_name=request.POST.get("std_name")
        std_email=request.POST.get("std_email")
        std_address=request.POST.get("std_address")
        std_phone=request.POST.get("std_phone")

        s=Student.objects.get(pk=roll)
        s.roll=std_roll
        s.name=std_name
        s.email=std_email
        s.address=std_address
        s.phone=std_phone

        s.save()
        return redirect("/std/home")
    
