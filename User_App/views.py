from django.shortcuts import render,redirect
from Admin_App.models import *
from. models import *
from django.db.models import Q
from django.contrib import messages
import datetime
import stripe
from django.conf import settings

# Create your views here.
def uindex(request):
    countturf=turf_dbs.objects.all().count()
    countloc=LocMan.objects.all().count()
    countuser=Signup.objects.all().count()
    countbooking=BookTurf.objects.all().count()
    locations=LocMan.objects.all()
    return render(request,'index.html',{'locations':locations,'countuser':countuser,'countbooking':countbooking,'countloc':countloc,'countturf':countturf})

def usearch(request):
    locations=LocMan.objects.all()
    return render(request,'search.html',{'locations':locations})

def searchresult(request):
    locations=LocMan.objects.all()
    return render(request,'search_result.html',{'locations':locations})

def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        posts = turf_dbs.objects.filter(tloc=search_query)
        locations=LocMan.objects.all()
        if LocMan.objects.filter(loc=search_query).exists():
            return render(request, 'search_result.html', {'query':search_query, 'posts':posts,'locations':locations})
        else:
            return render(request, 'search.html',{'msg':"No Such Location"})
    else:
        return render(request, 'search.html',{'msg':"No Such Location"})
    
def locationresult(request,id):
    posts = turf_dbs.objects.filter(tloc=id)
    locations=LocMan.objects.all()
    return render(request, 'location_result.html', {'posts':posts,'locations':locations})

def ulogin(request):
    locations=LocMan.objects.all()
    return render(request,'ulogin.html',{'locations':locations})

def uregister(request):
    locations=LocMan.objects.all()
    return render(request,'uregister.html',{'locations':locations})

def reguser(request):
    if request.method=='POST':
        name=request.POST['name']
        num=request.POST['num']
        email=request.POST['email']
        password=request.POST['password']
        if Signup.objects.filter(Q(email=email) | Q(name=name) ).exists():
            return render(request,'uregister.html',{'msg':"Registered User. Click Login Below"})
        else:
            data=Signup(name=name,num=num,email=email,password=password)
            data.save()
    return redirect('ulogin')

def publicdata(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        if Signup.objects.filter(name=name,password=password).exists():
            data=Signup.objects.filter(name=name,password=password).values('email','num','id').first()
            request.session['u_name']=name
            request.session['u_password']=password
            request.session['u_email']=data['email']
            request.session['u_num']=data['num']
            request.session['u_id']=data['id']
            return redirect('uindex')
        else:
            return render(request,'ulogin.html',{'msg':"Invalid User Credentials"})
    else:
        return redirect('ulogin')

def ulogout(request):
    del request.session['u_name']
    del request.session['u_id']
    del request.session['u_num']
    del request.session['u_email']
    del request.session['u_password']
    return redirect('uindex')


def contact(request):
    locations=LocMan.objects.all()
    return render(request,'contact.html',{'locations':locations})

def regcontact(request):
    if request.method=='POST':
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        usubject=request.POST['usubject']
        umessage=request.POST['umessage']
        data=contact_dbs(uname=uname,uemail=uemail,usubject=usubject,umessage=umessage)
        data.save()
        messages.success(request,"Your message has been sent. Thank you!")
    return redirect('uindex')

def singleview(request,id):
    locations=LocMan.objects.all()
    data=turf_dbs.objects.filter(id=id)
    return render(request,'single_view.html',{'locations':locations,'data':data})

def booknow(request,id):
    locations=LocMan.objects.all()
    data=turf_dbs.objects.filter(id=id)
    # t=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    book=BookTurf.objects.all()
    s_time=turf_dbs.objects.filter(id=id).values('tstime')
    return render(request,'booknow.html',{'locations':locations,'data':data,'s_time':s_time,'book':book})

stripe.api_key=settings.STRIPE_SECRET_KEY
def regbooking(request,id):
    if request.method=='POST':
        user_id=request.session.get('u_id')
        bookingdate=request.POST['bookingdate']
        mid=request.POST['mid']
        bstime=request.POST['bstime']
        betime=request.POST['betime']
        duration=request.POST['duration']
        btotal=request.POST['btotal']
        request.session['u_mid']=mid
        request.session['u_tid']=id
        request.session['u_bookingdate']=bookingdate
        request.session['u_duration']=duration
        request.session['u_bstime']=bstime
        request.session['u_betime']=betime
        request.session['u_btotal']=btotal
        data1=turf_dbs.objects.filter(id=id)
        locations=LocMan.objects.all()
        if BookTurf.objects.filter(turfid=id,bookingdate=bookingdate,bstime=bstime).exists():
            return render(request,'booking_full.html',{'data1':data1,'locations':locations})
        elif Signup.objects.filter(id=user_id).exists():
            product = turf_dbs.objects.get(id=id)
            session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items=[{
                'price_data':{
                    'currency': 'inr',
                    'product_data':{
                        'name': product.tname,
                    },
                    'unit_amount':int(btotal)*100,
                   
                },
                'quantity':1,
            }],
            mode='payment',
            success_url = "http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url = "http://127.0.0.1:8000/pay_cancel",
            # client_reference_id=product_id,
            )
            return redirect(session.url, code=303)
            
            # return redirect('bookinghistory')
        else:
            return render(request,'ulogin.html',{'msg':"Please Login To Book At UrTurf"})
    return redirect('uindex')

def pay_success(request):
    id=request.session.get('u_tid')
    bookingdate=request.session.get('u_bookingdate')
    mid=request.session.get('u_mid')
    bstime=request.session.get('u_bstime')
    betime=request.session.get('u_betime')
    duration=request.session.get('u_duration')
    btotal=request.session.get('u_btotal')
    # plan_id = session.client_reference_id
    u_id = request.session.get('u_id')
    if Signup.objects.filter(id=u_id).exists():
        data=BookTurf(userid=Signup.objects.get(id=u_id),turfid=turf_dbs.objects.get(id=id),mid=Manager_Signup.objects.get(id=mid),bookingdate=bookingdate,bstime=bstime,betime=betime,duration=duration,btotal=btotal)
        data.save()
        del request.session['u_mid']
        del request.session['u_tid']
        del request.session['u_bookingdate']
        del request.session['u_duration']
        del request.session['u_bstime']
        del request.session['u_betime']
        del request.session['u_btotal']
        return redirect('bookinghistory')

def error(request):
    locations=LocMan.objects.all()
    return render(request,'error.html',{'locations':locations,})
    
def bookinghistory(request):
    locations=LocMan.objects.all()
    user_id=request.session.get('u_id')
    if BookTurf.objects.filter(userid=user_id).exists():
        data=BookTurf.objects.filter(userid=user_id)
        return render(request,'booking_history.html',{'locations':locations,'data':data})
    else:
        return redirect('error')
    
# def bookingfull(request,id):
#     locations=LocMan.objects.all()
#     data=turf_dbs.objects.filter(id=id)
#     return render(request,'booking_full.html',{'locations':locations,'data':data})