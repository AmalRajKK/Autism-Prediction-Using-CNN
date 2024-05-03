from django.conf.urls import url
from feedback import views

urlpatterns=[
    url('viewandfeedback/',views.viewandgivefeed),
    url('viewdrfeed/',views.viewdrfeed),
    url('viewfeedadmin/',views.viewfeedadmin),
    url('autistic/(?P<idd>\w+)',views.autistic),
    url('notau/(?P<idd>\w+)',views.notautistic),
    url('managedata/',views.managedata),
    url('managedata2/',views.managedata2),
    url('delete/(?P<idd>\w+)',views.delete),
    url('delete2/(?P<itt>\w+)',views.delete2)
]