from django.shortcuts import render
#---------------------
#新增
from django.http import HttpResponse
from . models import User
#------------------------
# Create your views here.
def user(request):
    return render(request, 'user01.html')
def add(request): #form的add方法
    name = request.POST.get('username')
    password = request.POST.get('passwd')
    user = User()
    user.username = name
    user.passwd = password
    user.save() #有真正存到db
    return HttpResponse('新增成功！')
    
def getAllUser(request): #取得所有user
    userList = User.objects.all()
    return render(request, 'userList.html',{'users':userList})