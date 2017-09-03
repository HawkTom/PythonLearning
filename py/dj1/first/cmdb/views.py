from django.shortcuts import render
from cmdb import models
from django.shortcuts import HttpResponse
# Create your views here.

user_list = [
    {"user":"jack", "psd":"abc"},
    {"user":"marry", "psd":"xyz"},
]
def home(Request):
    global user_list
    if Request.method == "POST":
            username = Request.POST.get("username", None)
            password = Request.POST.get("password", None)
            models.UserInfo.objects.create(user = username, pwd = password)
            user_list = models.UserInfo.objects.all()
    #return HttpResponse('Hello World')
    return render(Request, "index.html", {"data": user_list})