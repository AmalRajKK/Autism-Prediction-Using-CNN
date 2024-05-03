from django.conf.urls import url
from doctor import views

urlpatterns=[
    url('drredister/',views.dr_register),
    url('managedr/',views.manage_dr),
    url('view&bookdr/',views.viewandbookdr),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject),

]