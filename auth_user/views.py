from django.shortcuts import render

from .forms import FormUser
# Create your views here.



def register_user(request):
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
        
    else:
        form = FormUser()
    return render(request,'registration/register.html',{"form":form})