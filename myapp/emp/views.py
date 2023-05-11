from django.shortcuts import render,redirect
from django.http import HttpResponse
#import emp model in this view
from .models import Emp
# Create your views here.

def emp_home(request):
    #return HttpResponse("Student Home Page")
    emps=Emp.objects.all()

    return render(request,"emp/home.html", {'emps':emps})

def add_emp(request):
    if request.method=="POST":
        #print("data coming")

        #fetch all the data
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        #craete a object of model class
        #object.coln
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        #for working need to check if working is true then he is an employe 
        if emp_working is None:
            e.working=False
        else:
            e.working=True

        # save the data
        e.save()
        return redirect("/emp/home")

    return render(request,"emp/add_emp.html", {})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{'emp':emp})
    
def do_update_emp(request,emp_id):
    #fetch the data
    if request.method=="POST":

        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

    #create object of Models
        e=Emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department

        if emp_working is None:
            e.working=False
        else:
            e.working=true
        e.save()
        return redirect("/emp/home")

