from django.conf.urls import url
from slot import views

urlpatterns=[
    url('addslot/',views.addslot),
    url('slot/(?P<idd>\w+)',views.slot),

]