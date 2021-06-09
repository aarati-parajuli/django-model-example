from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .models import tbl_Login



def index(request):
    return render(request,'form.html')
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = tbl_Login()
        user.email = email
        user.password = password
        user.save()
        return redirect('/')
    else:
        return render(request, 'form.html')

def sign(request):
    return render(request,'sign.html')
def two(request):
    return render(request,'two.html')
