# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	name = models.CharField(max_length=100,default="ram")
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	profileImage=models.FileField(default='jon.jpg')
	age  = models.IntegerField(default =0)
	gender = models.CharField(max_length= 1, default='M')
	college = models.CharField(max_length=100 , default="NITW")
	branch = models.CharField(max_length=100,default="CSE")

class GroupDiscussion(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	projectName = models.CharField(max_length=100,default="")
	datetime = models.DateTimeField(auto_now_add = True)
	message = models.CharField(max_length=250)

class Project(models.Model):
	projectName = models.CharField(max_length=100)
	projectDescripton = models.CharField(max_length =500)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	mainCategory = models.CharField(max_length =50)
	subCategory = models.CharField(max_length=50)
	likes = models.IntegerField(default=0)	
	members = models.CharField(max_length=500,default="")
	requests = models.CharField(max_length=500,default="")
	# groupDiscussion = models.ForeignKey(GroupDiscussion,on_delete=models.CASCADE)
	date = models.DateField()



class UserChat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    senderUser = models.ForeignKey(User,related_name='messages_sent',on_delete=models.CASCADE)
    recieverUser = models.ForeignKey(User,related_name='messages_recieved',on_delete=models.CASCADE)
    message = models.CharField(max_length=200)


