from django.shortcuts import render

# Create your views here.
from user.models import User
from doctor.models import Doctor


def admin(request):
    return render(request,'temp/admin.html')

def user(request):
    ss=request.session["u_id"]
    aa=User.objects.get(user_id=ss)
    context={
        'k':aa
    }
    return render(request,'temp/user.html',context)

def doctor(request):
    ss = request.session["u_id"]
    aa = Doctor.objects.get(dr_id=ss)
    context = {
        'b': aa
    }
    return render(request,'temp/doctor.html',context)

def home(request):
    return render(request,'temp/home.html')