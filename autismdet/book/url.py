from django.conf.urls import url
from book import views

urlpatterns=[
    url('book/(?P<idd>\w+)',views.book_dr),
    url('manage/',views.viewandmngbook),
    url('approved/',views.viewapprovebook),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject),
    url('gives/(?P<idd>\w+)',views.gives)
]