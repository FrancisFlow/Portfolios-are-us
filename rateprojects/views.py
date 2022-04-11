from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm, UpdateUserProfileForm, NewProjectForm
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
    current_user=request.user
    if request.method=='POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=current_user
            project.save()
        return redirect('home')
    else:
        form=NewProjectForm()
    return render(request, 'new_project.html', {'form':form})

# user registration, loging and logout functions.

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

#end user authentication functions.


def profile(request):
    """
    Allow users to view profile information
    """
    projects=Project.objects.all().order_by('date_posted')
    return render(request, 'profile.html', {'projects':projects} )


def update_profile(request):
    """
    Form for updating user profile information
    """
    if request.method == 'POST':
        prof_form=UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return redirect('profile')
    else:
        prof_form=UpdateUserProfileForm(instance=request.user.profile)
    
    params={
        'form':prof_form,
    }

    return render(request, 'update_profile.html', params)



def single_project(request, project_name):
    project=Project.objects.get(project_name=project_name)
    return render(request, 'single_project.html', {'project':project})



def search_results(request):
    if 'projects' in request.GET and request.GET['projects']:
        search_term=request.GET.get("projects")
        searched_projects=Project.search_by_name(search_term)
        message=f'{search_term}'

        return render(request, 'search.html', {'message': message, "projects":searched_projects})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html', {'message': message, "projects":searched_projects})