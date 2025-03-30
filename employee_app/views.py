from django.shortcuts import render,HttpResponse
from .models import Employee
from datetime import datetime

from django.db.models import Q
# Create your views here.


def index(request):
    return render(request,'index.html')


def all_emp(request):
    obj =Employee.objects.all()
    context = {
        'emps':obj

    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        f = request.POST['first_name']
        l = request.POST['last_name']
        s = int(request.POST['salary'])
        b = int(request.POST['bonus'])
        p = int(request.POST['phone'])
        d = int(request.POST['dept'])
        r = int(request.POST['role'])
        
        obj = Employee(first_name= f , last_name=l,salary=s,bonus=b,phone=p,dept_id=d,role_id=r,hire_date= datetime.now() )
        obj.save()
        return HttpResponse("Employee added Successfully")
    elif request.method=='GET':   
        return render(request,'add_emp.html')

    else :
        return  HttpResponse('An Exception occured! Employee Has Not Been Added')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please  Enter A Valid Emp Id")
    emps= Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name :
            emps = emps.filter(Q(first_name__icontains =name) | Q(last_name__icontains=name))
            
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            
            emps = emps.filter(role__name__icontains=role)



            
        context = {
            'emps':emps
        }
        return render(request,'view_all_emp.html',context)
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return render(request,'filter_emp.html')