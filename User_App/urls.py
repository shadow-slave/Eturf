from django.urls import path
from. import views
urlpatterns = [
    path('',views.uindex,name='uindex'),
    path('usearch',views.usearch,name='usearch'),
    path('searchresult',views.searchresult,name='searchresult'),
    path('search_feature',views.search_feature,name='search_feature'),
    path('locationresult/<str:id>/',views.locationresult,name='locationresult'),
    path('ulogin',views.ulogin,name='ulogin'),
    path('uregister',views.uregister,name='uregister'), #register page
    path('reguser',views.reguser,name='reguser'), #register function
    path('publicdata',views.publicdata,name='publicdata'),
    path('ulogout',views.ulogout,name='ulogout'),
    path('contact',views.contact,name='contact'),
    path('regcontact',views.regcontact,name='regcontact'),
    path('singleview/<int:id>/',views.singleview,name='singleview'),
    path('booknow/<int:id>/',views.booknow,name='booknow'),
    path('regbooking/<int:id>/',views.regbooking,name='regbooking'),
    path('bookinghistory',views.bookinghistory,name='bookinghistory'),
    path('error',views.error,name='error'),
    path('pay_success',views.pay_success,name='pay_success'),


]
