from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
        else:
            return HttpResponse('usuário incorreto')
            
    return render(request,'registration/login.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(email = email).exists()
        if not user:
            user = User.objects.create_user(username=username,password=password,email=email)
        else:
            return HttpResponse('email já cadastrado')
    return render(request,'registration/register.html')