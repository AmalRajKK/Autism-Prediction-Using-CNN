from django.shortcuts import render
from book.models import Book
from slot.models import Slot
# Create your views here.
def book_dr(request,idd):
    ss=request.session["u_id"]
    obb=Slot.objects.get(slot_id=idd)
    context={
        's':obb,
    }
    if request.method=="POST":
        obj=Book()
        obj.user_id=ss
        obj.slot_id=idd
        obj.date=request.POST.get('date')
        obj.status="Pending"
        obj.save()
    return render(request,'book/book_dr.html',context)


def viewandmngbook(request):
    ss = request.session["u_id"]
    obj=Book.objects.filter(slot__dr_id=ss)
    context={
        'a':obj
    }
    return render(request,'book/view&managebooking.html',context)


def viewapprovebook(request):
    ss=request.session["u_id"]
    obj=Book.objects.filter(status='Approved',user_id=ss)
    context={
        'b':obj
    }
    return render(request,'book/viewapprovedbooking.html',context)

def approve(request,idd):
    obj=Book.objects.get(book_id=idd)
    obj.status='Approved'
    obj.save()
    return viewandmngbook(request)

def reject(request,idd):
    obj=Book.objects.get(book_id=idd)
    obj.status='Rejected'
    obj.save()
    return viewandmngbook(request)

def gives(request,idd):
    ss=request.session["u_id"]
    obj=Slot.objects.filter(dr_id=ss)
    context={
        'z':obj
    }
    if request.method=="POST":
        obj=Book.objects.get(book_id=idd)
        obj.slot_id=request.POST.get('slot')
        obj.date=request.POST.get('date')
        obj.save()
        return viewandmngbook(request)
    return render(request,'book/giveslot.html',context)