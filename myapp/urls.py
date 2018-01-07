from django.conf.urls import url
from django.contrib import admin
from .import views

app_name ='myapp'

urlpatterns = [
    url(r'^login/$', views.login_user,name='login'),
    url(r'^logout/$', views.logout_user,name='logout'),
    url(r'^home/$', views.home,name='home'),
    url(r'^register/$', views.register,name='register'),
    url(r'^save/$', views.save,name='save'),
    url(r'^(?P<username>[\w-]+)/addproject/$', views.addproject,name='addproject'),
    url(r'^(?P<username>[\w-]+)/saveproject/$', views.saveproject,name='saveproject'),
    url(r'^(?P<username>[\w-]+)/profile/$', views.profile,name='profile'),
    url(r'^(?P<projectName>[\w-]+)/delete/$', views.deleteproject,name='deleteproject'),
    url(r'^(?P<projectName>[\w-]+)/description/$', views.description,name='description'),
    url(r'^(?P<projectName>[\w-]+)/(?P<username>[\w-]+)/addrequest/$', views.addrequest,name='addrequest'),
    url(r'^(?P<projectName>[\w-]+)/displaymembers/$', views.displaymembers,name='displaymembers'),
    url(r'^(?P<projectName>[\w-]+)/approverequests/$', views.approverequests,name='approverequests'),
    url(r'^(?P<projectName>[\w-]+)/(?P<username>[\w-]+)/addmembertoproject/$', views.addmembertoproject,name='addmembertoproject'),
    url(r'^myproject/$', views.myproject,name='myproject'),
    url(r'^(?P<projectName>[\w-]+)/creategroupchat/$', views.creategroupchat,name='creategroupchat'),
    url(r'^(?P<projectName>[\w-]+)/(?P<username>[\w-]+)/savechat/$', views.savechat,name='savechat'),
    url(r'^(?P<domain>[\w-]+)/search/$', views.searchresult,name='search'),







]
