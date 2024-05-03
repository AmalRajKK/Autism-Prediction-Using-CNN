from django.conf.urls import url
from user import views

urlpatterns=[
    url('reguser/',views.registeruser)

]