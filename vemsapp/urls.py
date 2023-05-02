from django.contrib import admin
from django.urls import path
from vemsapp import views
urlpatterns = [
   path('',views.home,name="home"),
   path('login',views.login_page,name="login"),
   path('signup',views.signup_page,name="signup"),
   path('logout',views.logout_page,name="logout"),
   path('dashboard',views.dashboard,name="dashboard"),
   path('registerlist',views.regiserlist,name="registerlist"),
   path('registerlist/<str:name>',views.regdata,name="registerlist"),
   path('upload',views.upload,name="upload"),
   path('uploadfile',views.upload_events,name="uploadfile"),
   path('eventsdata',views.eventsdata ,name="eventsdata"),
   path('eventsdata/<rid>',views.view_data,name="eventsdata"),
   path('events',views.event_post,name="events"),
   path('events/<str:ename>',views.event_details,name="events"),
   path('events/<str:ename>/<eid>',views.regisert_event,name="events"),
   path('announcement',views.announcement,name="announcement"),

  
 

]