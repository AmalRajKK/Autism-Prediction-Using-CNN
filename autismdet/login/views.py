from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login

# Create your views here.
def login(request):
    if request.method == "POST":
        eml = request.POST.get("unm")
        passwoed = request.POST.get("psw")
        obj = Login.objects.filter(username=eml, password=passwoed)
        print(len(obj))
        tp = ""
        for ob in obj:
            tp = ob.user_type
            uid = ob.u_id
            if tp == "doctor":
                request.session["u_id"] = uid
                return  HttpResponseRedirect('/temp/doctor/')
            elif tp == "user":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/user/')
            elif tp == "admin":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/admin/')
            else:
                objlist="user name or password incorrect...plese try again...!"
                context = {
                    'msg':objlist,
                }
                return render(request,'login/login.html',context)

    return render(request,'login/login.html')