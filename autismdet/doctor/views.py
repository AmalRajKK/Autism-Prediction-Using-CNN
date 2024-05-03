from django.shortcuts import render
from doctor.models import Doctor

# Create your views here.
from login.models import Login


def dr_register(request):
    obk=""
    if request.method=='POST':
        obj=Doctor()
        obj.name=request.POST.get('drname')
        obj.specilization=request.POST.get('spl')
        obj.dr_address=request.POST.get('draddress')
        obj.dr_contactnumber=request.POST.get('drnumber')
        obj.mailaddress=request.POST.get('mail')
        obj.cirtificare=request.POST.get('cirtificate')
        obj.hospital_name=request.POST.get('name')
        obj.hospital_address=request.POST.get('address')
        obj.hospital_contact_number=request.POST.get('number')
        obj.password=request.POST.get('pswd')
        obj.save()
        obk="success"
    context={
        'msg':obk
    }

    return render(request,'doctor/dr_register.html',context)



def manage_dr(request):
    obj=Doctor.objects.all()
    context={
        'c':obj
    }
    return render(request,'doctor/manage_dr.html',context)


def viewandbookdr(request):
    # obj=Doctor.objects.all()
    obj =Doctor.objects.filter(status='Approved')
    context={
        'd':obj
    }
    return render(request,'doctor/view&book_dr.html',context)

def approve(request,idd):
    obj=Doctor.objects.get(dr_id=idd)
    obj.status='Approved'
    obj.save()
    ob=Login()
    ob.username=obj.mailaddress
    ob.password=obj.password
    ob.user_type='doctor'
    ob.u_id=obj.dr_id
    ob.save()
    return manage_dr(request)

def reject(request,idd):
    obj=Doctor.objects.get(dr_id=idd)
    obj.status='Rejected'
    obj.save()
    return manage_dr(request)