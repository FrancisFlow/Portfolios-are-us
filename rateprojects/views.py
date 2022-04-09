from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')


def register_request(request):
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, "User registration successful.")
            return redirect("main:home")
        messages.error(request, "User registration failed. Invalid information")
    form=NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form":form})