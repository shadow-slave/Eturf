from django.shortcuts import render,redirect
from. models import *
from User_App.models import *
from Manager_App.models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


@login_required(login_url='adminlogin')
def adminview(request):
    countman=Manager_Signup.objects.all().count()
    countcontact=contact_dbs.objects.all().count()
    countturf=turf_dbs.objects.all().count()
    countloc=LocMan.objects.all().count()
    countuser=Signup.objects.all().count()
    countbooking=BookTurf.objects.all().count()
    return render(request,'admin_view.html',{'countloc':countloc,'countturf':countturf,'countuser':countuser,'countman':countman,'countcontact':countcontact,'countbooking':countbooking})

def adminlogin(request):
    return render(request,'admin_login.html')

def adlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username_a'] = username
            request.session['password_a'] = password
            return redirect('adminview')
        else:
            return render(request,'admin_login.html', {'msg':'Sorry Invalid User Credentials'})
    else:
        return render(request, 'admin_login.html')

def adlogout(request):
    del request.session['username_a']
    del request.session['password_a']
    logout(request)
    return redirect('adminlogin')

@login_required(login_url='adminlogin')
def addlocation(request):
    return render(request,'add_location.html')

def regloc(request):
    if request.method=='POST':
        loc=request.POST['loc']
        locimage=request.FILES['locimage']
        data=LocMan(locimage=locimage,loc=loc)
        data.save()
    return redirect('viewlocations')

@login_required(login_url='adminlogin')
def addturf(request):
    locations=LocMan.objects.all()
    manager=Manager_Signup.objects.filter(status=1)
    return render(request,'add_turf.html',{'locations':locations,'manager':manager})

@login_required(login_url='adminlogin')
def viewlocations(request):
    data=LocMan.objects.all()
    return render(request,'view_locations.html',{'data':data})

@login_required(login_url='adminlogin')
def editloc(request,id):
    data=LocMan.objects.filter(id=id)
    return render(request,'edit_location.html',{'data':data})


def updateloc(request,id):
    if request.method=='POST':
        loc=request.POST['loc']
        try:
            img_c=request.FILES['locimage']
            fs=FileSystemStorage()
            file=fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file=LocMan.objects.get(id=id).locimage
        LocMan.objects.filter(id=id).update(loc=loc,locimage=file)
    return redirect('viewlocations')

def deleteloc(request,id):
    LocMan.objects.filter(id=id).delete()
    return redirect('viewlocations')

dict={}

def regturf(request):
    if request.method=='POST':
        tname=request.POST['tname']
        tprice=request.POST['tprice']
        tstime=request.POST['tstime']
        tetime=request.POST['tetime']
        tloc=request.POST['tloc']
        tmanagerid=request.POST['tmanager']
        tarea=request.POST['tarea']
        taddress=request.POST['taddress']
        features=request.POST.getlist('class')
        global dict
        lst2=[]
        for i in features:
            pass
        dict[tname]=features
        print(dict)
        timage1=request.FILES['timage1']
        timage2=request.FILES['timage2']
        timage3=request.FILES['timage3']
        data=turf_dbs(tname=tname,tprice=tprice,tstime=tstime,tetime=tetime,tloc=tloc,tmanagerid=Manager_Signup.objects.get(id=tmanagerid),tarea=tarea,taddress=taddress,features=features,timage1=timage1,timage2=timage2,timage3=timage3)
        data.save()
    return redirect('viewturfs')

@login_required(login_url='adminlogin')
def viewturfs(request):
    data=turf_dbs.objects.all()
    global dict
    data1=dict
    return render(request,'view_turfs.html',{'data':data,'data1':data1})


@login_required(login_url='adminlogin')
def editturf(request,id):
    locations=LocMan.objects.all()
    manager=Manager_Signup.objects.filter(status=1)
    data=turf_dbs.objects.filter(id=id)
    return render(request,'edit_turf.html',{'data':data,'locations':locations,'manager':manager})


def updateturf(request,id):
    if request.method=='POST':
        tname=request.POST['tname']
        tprice=request.POST['tprice']
        tstime=request.POST['tstime']
        tetime=request.POST['tetime']
        tmanagerid=request.POST['tmanager']
        tloc=request.POST['tloc']
        tarea=request.POST['tarea']
        taddress=request.POST['taddress']
        features=request.POST.getlist('class')
        global dict
        lst2=[]
        for i in features:
            lst2.append(i)
        dict[tname]=[lst2]
        print(dict)
        try:
            img_c1=request.FILES['timage1']
            fs1=FileSystemStorage()
            file1=fs1.save(img_c1.name, img_c1)

            img_c2=request.FILES['timage2']
            fs2=FileSystemStorage()
            file2=fs2.save(img_c2.name, img_c2)

            img_c3=request.FILES['timage3']
            fs3=FileSystemStorage()
            file3=fs3.save(img_c3.name, img_c3)

        except MultiValueDictKeyError:
            file1=turf_dbs.objects.get(id=id).timage1
            file2=turf_dbs.objects.get(id=id).timage2
            file3=turf_dbs.objects.get(id=id).timage3
        turf_dbs.objects.filter(id=id).update(tname=tname,tprice=tprice,tstime=tstime,tetime=tetime,tloc=tloc,tmanagerid=Manager_Signup.objects.get(id=tmanagerid),tarea=tarea,taddress=taddress,features=features,timage1=file1,timage2=file2,timage3=file3)
    return redirect('viewturfs')

@login_required(login_url='adminlogin')
def deleteturf(request,id):
    # global dict
    # tname=turf_dbs.objects.filter(id=id).values('tname')
    # del dict[tname]
    turf_dbs.objects.filter(id=id).delete()
    return redirect('viewturfs')

@login_required(login_url='adminlogin')
def viewuser(request):
    data=Signup.objects.all()
    return render(request,'view_user.html',{'data':data})

@login_required(login_url='adminlogin')
def deleteuser(request,id):
    Signup.objects.filter(id=id).delete()
    return redirect('viewuser')

@login_required(login_url='adminlogin')
def viewcontact(request):
    data=contact_dbs.objects.all()
    return render(request,'view_contactus.html',{'data':data})

@login_required(login_url='adminlogin')
def deletecontact(request,id):
    contact_dbs.objects.filter(id=id).delete()
    return redirect('viewcontact')

@login_required(login_url='adminlogin')
def deleteall(request,id):
    if id=='contact':
        contact_dbs.objects.all().delete()
        return redirect('viewcontact')
    elif id=='users':
        Signup.objects.all().delete()
        return redirect('viewuser')
    elif id=='locations':
        LocMan.objects.all().delete()
    elif id=='turfs':
        turf_dbs.objects.all().delete()
    else:
        return redirect('adminview')
    
@login_required(login_url='adminlogin')
def viewmrequest(request):
    data=Manager_Signup.objects.filter(status=0)
    return render(request,'view_mrequest.html',{'data':data})

def approve_mreq(request,id):
    Manager_Signup.objects.filter(id=id).update(status=1)
    return redirect('viewmrequest')

def decline_mreq(request,id):
    Manager_Signup.objects.filter(id=id).update(status=3)
    return redirect('viewmrequest')
   
@login_required(login_url='adminlogin')
def viewamrequest(request):
    data=Manager_Signup.objects.filter(status=1)
    return render(request,'view_amrequest.html',{'data':data})

@login_required(login_url='adminlogin')
def viewdmrequest(request):
    data=Manager_Signup.objects.filter(status=3)
    return render(request,'view_dmrequest.html',{'data':data})

@login_required(login_url='adminlogin')
def viewbooking(request):
    data=BookTurf.objects.all()
    return render(request,'view_booking.html',{'data':data})