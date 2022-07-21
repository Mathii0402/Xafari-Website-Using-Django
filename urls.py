from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('form1/',views.form1, name='form1'),
    path('new/',views.new,name='view'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('technology/',views.technology, name='technology'),
    path('about/',views.about, name='about'),
    path('book/',views.book,name='book'),
    path('register/',views.register,name='register')
]