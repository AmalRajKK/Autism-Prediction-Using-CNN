from django.shortcuts import render
# from feedback.models import Feedback
from feedback.models import Feedback
from book.models import Book
from feedback.models import Autistic
from feedback.models import Notautistic
# Create your views here.
def viewandgivefeed(request):
    # ss = request.session["u_id"]
    # a=Book.objects.filter(slot__dr_id=ss)
    # ls=a.values_list('slot__dr_id')
    # print(ls)
    # obj=Feedback.objects.filter(book__slot__dr_id__in=ls)
    obj = Feedback.objects.all()
    context={
        'e':obj
    }
    return render(request,'feedback/view&givefeedback.html',context)

def viewdrfeed(request):
    # ss = request.session["u_id"]
    obj=Feedback.objects.all()
    context={
        'f':obj
    }
    return render(request,'feedback/view_dr_feedback.html',context)


def viewfeedadmin(request):
    obj=Feedback.objects.all()
    context={
        'g':obj
    }
    return render(request,'feedback/viewfeedback_admin.html',context)

def autistic(request,idd):
    ss = request.session["u_id"]
    obj=Feedback.objects.get(feedback_id=idd)
    obj.feedback='Autistic'
    obj.dr_id=ss
    obj.save()

    obk=Autistic()
    obk.image=obj.image
    obk.result=obj.feedback
    obk.save()
    return viewandgivefeed(request)

def notautistic(request,idd):
    ss = request.session["u_id"]
    obj=Feedback.objects.get(feedback_id=idd)
    obj.feedback='Not Autistic'
    obj.dr_id=ss
    obj.save()

    obk = Notautistic()
    obk.image = obj.image
    obk.result = obj.feedback
    obk.save()
    return viewandgivefeed(request)


def managedata(request):
    ab =Autistic.objects.all()
    context = {
        'w': ab
    }
    return render(request,'feedback/managedata.html',context)

def managedata2(request):
    ab =Notautistic.objects.all()
    context = {
        'w': ab
    }
    return render(request,'feedback/managedata2.html',context)


def delete(request,idd):
    obj=Autistic.objects.get(aut_is=idd)
    obj.delete()
    return managedata(request)

def delete2(request,itt):
    obj=Notautistic.objects.get(notaut_id=itt)
    obj.delete()
    return managedata2(request)