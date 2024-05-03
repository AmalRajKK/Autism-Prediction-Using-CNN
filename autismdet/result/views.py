from django.shortcuts import render
from result.models import Result
# Create your views here.

def viewresult(request):
    ss=request.session["u_id"]
    obj=Result.objects.filter(book__user_id=ss)
    context={
        'h':obj
    }
    return render(request,'result/viewresult.html',context)


def viewresultadmin(request):
    obj=Result.objects.all()
    context={
        'j':obj
    }
    return render(request,'result/viewresult_admin.html',context)

