from django.shortcuts import render,redirect
from Admin_App.models import *
from User_App.models import *
from. models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def managerview(request):
    mid=request.session.get('m_id')
    count=BookTurf.objects.filter(status=0,mid=mid)
    data=turf_dbs.objects.filter(tmanagerid=mid)
    countbooking=BookTurf.objects.filter(mid=mid).count()
    countturf=turf_dbs.objects.all().count()
    mname=request.session.get('m_name')
    if Manager_Signup.objects.filter(mname=mname).exists():
        return render(request,'manager_view.html',{'data':data,'count':count,'cb':countbooking,'ct':countturf})
    else:
        return redirect('managerlogin')
    
def requestview(request):
    mid=request.session.get('m_id')
    data=BookTurf.objects.filter(status=0,mid=mid)
    count=BookTurf.objects.filter(status=0,mid=mid)
    mname=request.session.get('m_name')
    if Manager_Signup.objects.filter(mname=mname).exists():
        return render(request,'request_view.html',{'data':data,'count':count})
    else:
        return redirect('managerlogin')
    
def managersignup(request):
    loc=LocMan.objects.all()
    return render(request,'manager_signup.html',{'loc':loc})

def registermanager(request):
    if request.method=='POST':
        mname=request.POST['mname']
        memail=request.POST['memail']
        mphone=request.POST['mphone']
        mloc=request.POST['mloc']
        mpass=request.POST['mpass']
        data=Manager_Signup(mname=mname,memail=memail,mphone=mphone,mloc=mloc,mpass=mpass)
        data.save()
    return redirect('managerlogin')

def managerlogin(request):
    return render(request,'manager_login.html')


def mpublicdata(request):
    if request.method=='POST':
        mname=request.POST.get('mname')
        mpass=request.POST.get('mpass')
        if Manager_Signup.objects.filter(mname=mname,mpass=mpass,status=0).exists():
            return render(request,'manager_login.html',{'msg':"Manager Not Approved Yet"})
        elif Manager_Signup.objects.filter(mname=mname,mpass=mpass,status=1).exists():
            data=Manager_Signup.objects.filter(mname=mname,mpass=mpass).values('memail','mphone','id').first()
            request.session['m_name']=mname
            request.session['m_password']=mpass
            request.session['m_email']=data['memail']
            request.session['m_phone']=data['mphone']
            request.session['m_id']=data['id']
            return redirect('managerview')      
        elif Manager_Signup.objects.filter(mname=mname,mpass=mpass,status=3).exists():
                return render(request,'manager_login.html',{'msg':"Manager Not Approved"})
        else:
            return render(request,'manager_login.html',{'msg':"Invalid User Credentials"})
    else:
        return redirect('managerlogin')

def mlogout(request):
    mname=request.session.get('m_name')
    if Manager_Signup.objects.filter(mname=mname).exists():
        del request.session['m_name']
        del request.session['m_id']
        del request.session['m_phone']
        del request.session['m_email']
        del request.session['m_password']
        return redirect('managerlogin')
    else:
        return redirect('managerlogin')

def approvebooking(request,id):
    mname=request.session.get('m_name')
    if Manager_Signup.objects.filter(mname=mname).exists():
        BookTurf.objects.filter(id=id).update(status=1)
        return redirect('requestview')
    else:
        return redirect('managerlogin')

def declinebooking(request,id):
    BookTurf.objects.filter(id=id).update(status=2)
    return redirect('requestview')

def approved_view(request):
    mid=request.session.get('m_id')
    data=BookTurf.objects.filter(status=1,mid=mid)
    count=BookTurf.objects.filter(status=0,mid=mid)
    mname=request.session.get('m_name')
    if Manager_Signup.objects.filter(mname=mname).exists():
        return render(request,'approved_bookings.html',{'data':data,'count':count})
    else:
        return redirect('managerlogin')

def declined_view(request):
    mid=request.session.get('m_id')
    count=BookTurf.objects.filter(status=0,mid=mid)
    data=BookTurf.objects.filter(status=2,mid=mid)
    mname=request.session.get('m_name')
    if Manager_Signup.objects.filter(mname=mname).exists():
        return render(request,'declined_bookings.html',{'data':data,'count':count})
    else:
        return redirect('managerlogin')
    
def allturf(request):
    mid=request.session.get('m_id')
    mname=request.session.get('m_name')
    data=turf_dbs.objects.all()
    if Manager_Signup.objects.filter(mname=mname).exists():
        return render(request,'allturf.html',{'data':data})
    else:
        return redirect('managerlogin')