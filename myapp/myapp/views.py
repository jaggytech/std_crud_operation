from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    isActive=True
    #accessing data from form
    if request.method=='POST':
        check=request.POST.get('check')
        print(check)
        if check is None: isActive=False
        else:isActive=True
    date=datetime.datetime.now()
    
    name="JaggyTech"
    list_of_programs=[
        'wap to print hello world',
        'wap to check prime number',
        'wap to check armstronog number',
        'wap to print all the prime numbers'
    ]
    student={
        'student_name':"Jagesh",
        'student_college':"msb",
        'city':"bbsr"
    }
    print("function called from view")
    # return HttpResponse("<h1> Hello this is index page </h1>")

    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,"home.html",data)
def about(request):
   # return HttpResponse("<h1> This is about page. </h1> ")
    return render(request,"about.html", {})
def services(request):
   # return HttpResponse("<h1> This is services page. </h1>")
    return render(request,"services.html", {})
    