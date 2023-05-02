from django.db import models
import datetime
import os


class events_year(models.Model):
    year = models.CharField(max_length=50,null=False,blank=False)
    desc = models.CharField(max_length=150,null=False,blank=False)

    def __str__(self) :
        return  self.year
    class Meta:
        db_table = 'years'
      

def getfilename(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join("uploads/",new_filename)

class upload_event(models.Model):
    events_years = models.ForeignKey(events_year,on_delete=models.CASCADE )
    event_name = models.CharField(max_length=50,null=False,blank=False)
    event_date = models.DateField(null=False,blank=False)
    event_desc = models.CharField(max_length=50,null=False,blank=False)
    event_file = models.FileField(upload_to=getfilename,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return  self.event_name
    class Meta:
        db_table = 'events'
       

class addevents(models.Model):
   

    event_name =  models.CharField(max_length=50,null=False,blank=False)
    event_date = models.DateField(null=False,blank=False)
    small_desc = models.CharField(max_length=250,null=False,blank=False)
    event_type = models.CharField(max_length=50,null=False,blank=False)
    event_image = models.ImageField(upload_to=getfilename,null=True,blank=True)
    latest_event =  models.BooleanField(default=False,help_text="o-default,1-latest")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) :
        return  self.event_name
    class Meta:
        db_table = 'event'
       
class eventdetails(models.Model):
   
    addevent = models.ForeignKey(addevents, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=False,blank=False)
    last_date = models.DateField(null=False,blank=False)
    auditorium = models.CharField(max_length=50,null=False,blank=False)
    img = models.ImageField(upload_to=getfilename,null=True,blank=True)
    clg_name = models.CharField(max_length=50,null=False,blank=False)
    desc =models.CharField(max_length=550,null=False,blank=False)
    invitation = models.FileField(upload_to=getfilename,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return  self.name
    class Meta:
        db_table = 'eventdetail'

class eventregisteration(models.Model):
    eventreg = models.ForeignKey(eventdetails,on_delete=models.CASCADE)
    full_name =  models.CharField(max_length=50,null=False,blank=False)
    email  =    models.CharField(max_length=50,null=False,blank=False)
    phone_number = models.IntegerField()
    roll_no = models.IntegerField(null=False,blank=False)
    college_name= models.CharField(max_length=50,null=False,blank=False)
    dept = models.CharField(max_length=50,null=False,blank=False)
    address = models.CharField(max_length=350,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return  self.dept
    class Meta:
        db_table = 'register'

        
class addevent(models.Model):
    ename =  models.CharField(max_length=50,null=False,blank=False)
    event_name =  models.CharField(max_length=150,null=False,blank=False)
    event_type =  models.CharField(max_length=50,null=False,blank=False)
    event_date =  models.DateField(null=False,blank=False)
    last_date  =  models.DateField(null=False,blank=False)
    auditorium =  models.CharField(max_length=50,null=False,blank=False)
    timing     = models.CharField(max_length=50,null=False,blank=False)
    small_desc =  models.CharField(max_length=450,null=False,blank=False)
    desc =        models.CharField(max_length=1000,null=False,blank=False)
    post_img    = models.ImageField(upload_to=getfilename,null=True,blank=True)
    event_img   = models.ImageField(upload_to=getfilename,null=True,blank=True)
    invitation   = models.FileField(upload_to=getfilename,null=True,blank=True)
    latest_event = models.BooleanField(default=False,help_text="o-default,1-Trending")
    status = models.BooleanField(default=False,help_text="o-show,1-hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return  self.event_name
    class Meta:
        db_table = 'addevent'

class registerevent(models.Model):
    eventname = models.ForeignKey(addevent, on_delete=models.CASCADE)
    post_img    = models.ImageField(upload_to=getfilename,null=True,blank=True)
    fullname  =  models.CharField(max_length=50,null=False,blank=False)
    email     =  models.CharField(max_length=50,null=False,blank=False)
    phoneno =    models.IntegerField(null=False,blank=False)
    rollno    =   models.CharField(max_length=50,null=False,blank=False)
    collegename  =  models.CharField(max_length=50,null=False,blank=False)
    dept         =  models.CharField(max_length=50,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return  self.dept
    class Meta:
        db_table = 'registerevent'

class event_announcement(models.Model):
    post_img    = models.ImageField(upload_to=getfilename,null=True,blank=True)
    event_name =  models.CharField(max_length=150,null=False,blank=False)
    issuses =  models.CharField(max_length=150,null=False,blank=False)
    desc =        models.CharField(max_length=1000,null=False,blank=False)
    event =  models.CharField(max_length=150,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False,help_text="o-show,1-hidden")

    def __str__(self) :
        return  self.event_name
    class Meta:
        db_table = 'eventannouncement'

   
   
