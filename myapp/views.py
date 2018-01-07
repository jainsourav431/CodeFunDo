# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template.context import RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect , get_object_or_404
from .models import UserProfile,Project,UserChat,GroupDiscussion
from django.contrib.auth.models import User
import datetime
from django.core.files.storage import FileSystemStorage
from django.utils import six
from django.contrib.auth.decorators import login_required 


# Create your views here.

def login_user(request):
		if not request.user.is_authenticated:
			print("hi")
			if request.method == "POST":
				username = request.POST['name']
				password = request.POST['password']
				user = authenticate(username=username , password=password)
				print(username)
				# print(password)
				login(request,user)
				if request.user.is_authenticated:
					return redirect('myapp:home')
				else:
					return render(request, 'myapp/login.html', {'error_message': 'Invalid login'})
			else:
				print("else")
				return render(request, 'myapp/login.html', {'error_message': 'Invalid login'})
		else:
			return redirect('myapp:home')

@login_required(login_url='myapp:login')
def home(request):
	context = {}
	context['username'] = request.user.username
	print("tired " +request.user.username)
	context['projects'] = Project.objects.all()
	return render(request,'myapp/index1.html',context)

def register(request):
	return render(request,'myapp/register.html')


def save(request):
	if request.method == "POST":
		name = request.POST['name']
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		image = request.FILES['image']
		gender = request.POST['gender']
		age = request.POST['age']
		college = request.POST['college']
		branch = request.POST['branch']
		user = User.objects.create_user(
			username = username,
			password = password,
			email=email
			)
		user.save()
		object1 = UserProfile(name = name , user=user ,profileImage = image,age =age,gender=gender,college=college,branch=branch)
		object1.save()
		return render(request,'myapp/login.html')

@login_required(login_url='myapp:login')
def addproject(request,username):
	print(request.user.username)
	return render(request,'myapp/addproject.html',{'username': username})

@login_required(login_url='myapp:login')
def saveproject(request,username):
	if request.method=="POST":
		print("Not")
		name = request.POST['name']
		description = request.POST['description']
		maincategory = request.POST['maincategory']
		subcategory = request.POST['subcategory']
		now = datetime.datetime.now()
		userr=request.user
		username=request.user.username
		print("username = "+ username)
		object1 = Project(projectName = name,projectDescripton = description,user=userr,mainCategory=maincategory,subCategory=subcategory,date=now,members=userr.username)
		object1.save()
		return redirect('myapp:home')
	else:
		return redirect('myapp:home')



def logout_user(request):
	logout(request)
	return redirect('myapp:login')

def profile(request,username):
	user =request.user
	context ={}
	context['projects'] = Project.objects.filter(user=user)
	context['userprofile'] = UserProfile.objects.get(user=user)
	return render(request,'myapp/profile.html',context)

def deleteproject(request,projectName):
	user =request.user
	object1=Project.objects.get(user=user,projectName=projectName)
	object1.delete()
	context ={}
	context['projects'] = Project.objects.filter(user=user)
	context['userprofile'] = UserProfile.objects.get(user=user)
	return render(request,'myapp/profile.html',context)

def description(request,projectName):
	context={}
	projects = Project.objects.filter(projectName=projectName)
	print("project "+str(len(projects)))
	owners = UserProfile.objects.get(user = projects[0].user)
	context['projects']=projects
	context['owners'] = owners
	return render(request,'myapp/description.html',context)



def displaymembers(request,projectName):
	context={}
	projects = Project.objects.filter(projectName=projectName)
	members = projects[0].members
	allmembers = members.split(';')
	print(allmembers)
	context['members']=allmembers
	context['projectName'] =projectName
	context['username']=request.user.username
	return render(request,'myapp/displaymembers.html',context)


def addrequest(request,projectName,username):
	projects = Project.objects.filter(projectName=projectName)
	check=0
	print(username)
	if projects[0].requests != "":
		allrequests = projects[0].requests.split(";")
		for i in (allrequests):
			print("Name = "+ i)
			if i ==username:
				check=1
				break;
		if check==1:
			return redirect('myapp:home')
		else:
			allmembers =projects[0].members.split(";") 
			for i in (allmembers):
				print("Name = "+ i)
				if i ==username:
					check=1
					break;
		if check==1:
			return redirect('myapp:home')
			requests = projects[0].requests+";"+username
	else:
		allmembers =projects[0].members.split(";") 
		for i in (allmembers):
			print("Name = "+ i)
			if i ==username:
				check=1
				break;
		if check==1:
			return redirect('myapp:home')
		requests=username
	members = projects[0].members
	projectName = projects[0].projectName
	projectDescripton = projects[0].projectDescripton
	subcategory = projects[0].subCategory
	maincategory = projects[0].mainCategory
	likes = projects[0].likes
	dates = projects[0].date
	user =projects[0].user
	projects[0].delete()
	newproject = Project(projectName=projectName,projectDescripton=projectDescripton,user=user,mainCategory=maincategory,subCategory=subcategory,likes=likes,members=members,requests=requests,date=dates)
	newproject.save()
	return redirect('myapp:home')

def approverequests(request,projectName):
	projects = Project.objects.filter(projectName=projectName)
	requests = projects[0].requests
	allrequest = requests.split(";")
	print(len(allrequest))
	print(allrequest)
	if allrequest[0] != "":
		context = {}
		context['allrequest']=allrequest
		context['project']=projectName
		return render(request,'myapp/approverequest.html',context)
	else:
		context ={}
		context['projects'] = Project.objects.filter(user=request.user)
		context['userprofile'] = UserProfile.objects.get(user=request.user)
		return render(request,'myapp/profile.html',context)





def addmembertoproject(request,projectName,username):
	projects = Project.objects.filter(projectName=projectName)
	members = projects[0].members+";"+username
	requests = projects[0].requests
	listofrequests = requests.split(";")
	print("len = " + str(len(listofrequests)))
	newrequests = ""
	for i in range(len(listofrequests)):
		if listofrequests[i] != username:
			print("Ans= "+ listofrequests[i])
			newrequests=newrequests+listofrequests[i]
	print("len = " + str(len(newrequests)))
	projectName = projects[0].projectName
	projectDescripton = projects[0].projectDescripton
	subcategory = projects[0].subCategory
	maincategory = projects[0].mainCategory
	likes = projects[0].likes
	dates = projects[0].date
	user =projects[0].user
	projects[0].delete()
	newproject = Project(projectName=projectName,projectDescripton=projectDescripton,user=user,mainCategory=maincategory,subCategory=subcategory,likes=likes,members=members,requests=newrequests,date=dates)
	newproject.save()
	projects = Project.objects.filter(projectName=projectName)
	requests = projects[0].requests
	allrequest = requests.split(";")
	context = {}
	context['allrequest']=allrequest
	context['project']=projectName
	context ={}
	context['projects'] = Project.objects.filter(user=request.user)
	context['userprofile'] = UserProfile.objects.get(user=request.user)
	return render(request,'myapp/profile.html',context)



def myproject(request):
	username = request.user.username
	ans =[]
	context={}
	projects = Project.objects.all()
	for i in range(len(projects)):
		allmembers =projects[i].members.split(";")
		for j in allmembers:
			if j== username:
				ans.append(projects[i])
				break;
	context['projects'] = ans
	return render(request,'myapp/myproject.html',context)


def creategroupchat(request,projectName):
	context={}
	projects = Project.objects.filter(projectName=projectName)
	members = projects[0].members
	allmembers = members.split(';')
	context['username'] =request.user.username
	context['allmembers'] = allmembers
	context['projectName'] = projectName
	chats  = GroupDiscussion.objects.filter(projectName=projectName).order_by('datetime')
	# orderedchats = chats.objects.order_by(datetime)
	context['chats']=chats
	print(chats)
	return render(request,'myapp/groupchat.html',context)


def savechat(request,projectName,username):
	context={}
	message = request.POST['message']
	object1 = GroupDiscussion(user=request.user,projectName= projectName,message=message,datetime=datetime.datetime.now())
	object1.save()
	context['username'] =request.user.username
	context['projectName'] = projectName
	chats  = GroupDiscussion.objects.filter(projectName=projectName).order_by('datetime')
	context['chats']=chats
	return render(request,'myapp/groupchat.html',context)


def searchresult(request,domain):
	context={}
	objects = Project.objects.filter(mainCategory=domain)
	context['projects']=objects
	context['username']=request.user.username
	return render(request,'myapp/index1.html',context)












	



















