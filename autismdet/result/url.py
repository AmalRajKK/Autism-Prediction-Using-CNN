from django.conf.urls import url
from result import views

urlpatterns=[
    url('viewresult/',views.viewresult),
    url('viewresultadmin/',views.viewresultadmin),


]