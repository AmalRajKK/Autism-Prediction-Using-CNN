from django.shortcuts import render
from slot.models import Slot
from book.models import Book
# Create your views here.
def addslot(request):
    obk=""
    ss=request.session["u_id"]
    if request.method=='POST':
        obj=Slot()
        obj.dr_id=ss
        obj.slot_number=request.POST.get('sno')
        obj.from_field=request.POST.get('from')
        obj.to=request.POST.get('to')
        obj.save()
        obk="success"
    context={
        'msg':obk
    }
    return render(request,'slot/add_slot.html',context)


def slot(request,idd):
    obj=Slot.objects.filter(dr_id = idd)
    context={
        'k':obj
    }
    return render(request,'slot/slot.html',context)
