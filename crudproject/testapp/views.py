from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.db.models import Q
from django.db.models import Avg,Sum,Min,Max,Count
from django.db.models.functions import Lower
# Create your views here.
def retrieve_view(request):
    avg=Employee.objects.all().aggregate(Avg('esal'))
    max=Employee.objects.all().aggregate(Max('esal'))
    min=Employee.objects.all().aggregate(Min('esal'))
    sum=Employee.objects.all().aggregate(Sum('esal'))
    count=Employee.objects.all().aggregate(Count('esal'))
    employees=Employee.objects.get_emp_sorted_by('ename')
    my_dict={'avg':avg,'max':max,'min':min,'sum':sum,'count':count}
    return render(request,'testapp/home.html',{'employees':employees})
def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/create.html',{'form':form})
def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')
def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/ ')
    return render(request,'testapp/update.html',{'employee':employee})
