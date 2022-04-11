from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project, Profile
# Create your views here.
@login_required(login_url='/login/')
def home(request):
    """
    View function for the home page
    """
    projects=Project.objects.all().order_by('date_posted')
    users=User.objects.exclude(id=request.user.id).all()
    current_user=request.user
    return render(request, 'home.html', {'projects':projects, 'users':users, "current_user":current_user})


@login_required(login_url='/login')
def new_post(request):
    # current_user=request.user
    # if request.method=='POST':
    pass

def register_request(request):
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, "User registration successful.")
            return redirect("/login")
        messages.error(request, "User registration failed. Invalid information")
    form=NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect("/")

            else:
                messages.error(request, "Invalid username or password.")
            
        else:
            messages.error(request, "Invalid username or password.")
    form=AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")



def profile(request):
    return render(request, 'profile.html')