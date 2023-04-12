from django.shortcuts import render,HttpResponse
from .models import EMP,Role
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')

def allemp(request):
    # role=Role.objects.all()
    # context={'role':role}
    emp=EMP.objects.all()
    context={'emp':emp}
    return render(request,'all_emp.html',context)

    # return render(request,'jj.html',context)
def addemp(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        dept=request.POST['dept']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=int(request.POST['role'])
        phone=int(request.POST['phone'])
        print(role,'-----------')
        new_emp=EMP(name=fname,lname=lname,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added Successfully')
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        pass

def kk(request):
    pass

def removeemp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_deleted=EMP.objects.get(id=emp_id)
            emp_to_be_deleted.delete()
            return HttpResponse('Deleted Successfully')
        except:
            return HttpResponse('Enter Valid emp')
    emp=EMP.objects.all()
    context={'emp':emp}
    return render(request,'remove_emp.html',context)
