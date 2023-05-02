from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth import login,authenticate,logout
from django.contrib import  messages
from . models import *
from django.contrib.auth.models import User


def home(request):
    ev = addevent.objects.filter(latest_event=1) 
    return render(request,'events/index.html',{"event":ev})

def signup_page(request):
    if request.method == 'POST':
        u = request.POST['username']
        e = request.POST['email']
        p = request.POST['password']
        if User.objects.filter(username = u).exists():
            messages.info('already exists username')
        else:
            u = User.objects.create_user(username=u,email=e,password=p)
            u.save()
            return redirect('login')
    
    return render(request,'login/signup.html')

def login_page(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request,username=u,password=p)
        if user is not None:
           login(request,user)
           return redirect('dashboard')
        else:
            messages.error(request,'incorrect username or password ')
            return redirect('login')
    return render(request,'login/login.html')

def logout_page(request):
    if request.user.is_authenticated:
       logout(request)    
       return redirect('home')
    

def dashboard(request):
     if request.user.is_authenticated:
         return render(request,'login/dashboard.html')
     else:
         return redirect('home')
     
def regiserlist(request):
    if request.user.is_authenticated:
         e = registerevent.objects.all()
         return render(request,'login/registerlist.html',{"event":e})
    else:
         return redirect('login')
    
def regdata(request,name):
    if request.user.is_authenticated:
        
        data = registerevent.objects.filter(eventname_id=name)
        return render(request,'login/registerdata.html',{"data":data})
    else:
        return redirect('login')

   

def upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            y = request.POST['year']
            d = request.POST['desc']
            u = events_year.objects.create(year=y,desc=d)
            u.save()
            messages.info(request,'Sucessfully Created Folder')
            return redirect('uploadfile')
        
    else:
        return redirect('home')
    return render(request,'login/upload.html')



def upload_events(request):
    if request.user.is_authenticated:
          if request.method == 'POST':
            ye  = request.POST['year']
            year = events_year.objects.get(id=ye)
            en = request.POST['ename']
            ed = request.POST['date']
            edesc = request.POST['desc']
            ef = request.FILES['file']
            uf = upload_event.objects.create(events_years=year,event_name=en,event_date=ed,event_desc=edesc,event_file=ef)
            uf.save()
            messages.info(request,'Sucessfully Added file')
            return redirect('uploadfile')
    else:
        return redirect('home')
    return render(request,'login/uploadfile.html',{"years":events_year.objects.all()})

def eventsdata(request):
    if request.user.is_authenticated:
        data = events_year.objects.all()
        return render(request,"login/eventsdata.html",{'data':data})

    else:
        return redirect('home')
    
def view_data(request,rid):
     if request.user.is_authenticated:
      event = upload_event.objects.filter(events_years_id=rid)
      return render(request,'login/data.html',{"event":event,"year":rid})
     else:
         return redirect('login')  

def event_post(request):
   
    event = addevent.objects.filter(status=0)

    return render(request,'events/events.html',{"event":event})

def event_details(request,ename):
    if(addevent.objects.filter(ename=ename)):
     details = addevent.objects.filter(ename=ename)
     return render(request,"events/event_details.html",{"details":details})

def regisert_event(request,ename,eid):
    if(addevent.objects.filter(ename=ename)):
        if request.method == 'POST':
            ed  = request.POST['edetails']
            eid = addevent.objects.get(event_name=ed)
            fullname = request.POST['fullname']
            email = request.POST['email']
            phoneno = request.POST['phone']
            rollno = request.POST['rollno']
            clg    = request.POST['clgname']
            dept   = request.POST['dept']
            reg = registerevent.objects.create(eventname=eid,fullname=fullname,email=email,phoneno=phoneno,rollno=rollno,collegename=clg,dept=dept)
            reg.save()
            return redirect('events')
    
    return render(request,'events/register.html',{"events":addevent.objects.all()})


def announcement(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ei = request.FILES['event_img']
            en = request.POST['eventname']
            iu =  request.POST['issuses']
            desc = request.POST['event_desc']
            ev  = request.POST['event']
            
            ea = event_announcement.objects.create(post_img=ei, event_name=en,issuses=iu,desc=desc,event=ev)
            ea.save()
            messages.success(request,'successfully added')


    else:
        redirect('login')
    return render(request,'login/ea.html')