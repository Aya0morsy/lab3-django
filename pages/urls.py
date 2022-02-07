from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('checklogin',views.checklogin,name='checklogin'),
    path('logout',views.logout,name='logout'),
    path('addtrainee',views.addtrainee,name='addtrainee'),
    path('addtrack',views.addtrack,name='addtrack'),
    path('index',views.index,name='index'),
    path('track111',views.track111,name='track111'),
    path('update/<int:id>',views.update,name='update'),
    path('actupdate/<int:id>',views.actupdate,name='actupdate'),
    path('dell/<int:id>',views.dell,name='dell')
    
]
