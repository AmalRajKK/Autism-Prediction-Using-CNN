from django.conf.urls import url
from temp import views

urlpatterns=[
    url('admin/',views.admin),
    url('user/',views.user),
    url('doctor/',views.doctor),
    url('home/',views.home),
]