from django.shortcuts import render
from user.models import User
from login.models import Login

# Create your views here.
def registeruser(request):
    obk=""
    if request.method=="POST":
        obj=User()
        obj.user_name=request.POST.get('uname')
        obj.mail_id=request.POST.get('mail')
        obj.phone_number=request.POST.get('phn')
        obj.address=request.POST.get('add')
        obj.password=request.POST.get('pswd')
        obj.save()
        ob = Login()
        ob.username = obj.mail_id
        ob.password = obj.password
        ob.user_type = 'user'
        ob.u_id = obj.user_id
        ob.save()
        obk="success"
    context={
        'msg':obk
    }
    return render(request,'user/register_user.html',context)