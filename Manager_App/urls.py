from django.urls import path
from. import views

urlpatterns = [
    path('managerview',views.managerview,name='managerview'),
    path('requestview',views.requestview,name='requestview'),
    path('managersignup',views.managersignup,name='managersignup'),
    path('registermanager',views.registermanager,name='registermanager'),
    path('managerlogin',views.managerlogin,name='managerlogin'),
    path('mpublicdata',views.mpublicdata,name='mpublicdata'),
    path('mlogout',views.mlogout,name='mlogout'),
    path('approvebooking/<int:id>/',views.approvebooking,name='approvebooking'),
    path('declinebooking/<int:id>/',views.declinebooking,name='declinebooking'),
    path('approved_view',views.approved_view,name='approved_view'),
    path('declined_view',views.declined_view,name='declined_view'),
    path('allturf',views.allturf,name='allturf'),
]
