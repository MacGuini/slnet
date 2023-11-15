from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm, LoginForm

# Create your views here.

def loginUser(request):
    
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Username forced lower case to prevent repeat users
            username = request.POST['username'].lower()
            password = request.POST['password']

            # Check if the user exists
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                messages.error(request, 'User does not exist.')
                return render(request, 'accounts/login.html', {'form':form})

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            # Checks if user exists
            if user is not None:
                # Check if the user is active
                if user.is_active:
                    # creates a session for the users in the database
                    login(request, user)
                    
                    # returns the user if there is a next route. Otherwise, the user is redirected to the accounts page.
                    return redirect(request.GET['next'] if 'next' in request.GET else 'index')
                else:
                    messages.errors(request, 'User is inactive')
            else:
                messages.error(request, 'Invalid password')
            
            
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form':form})



def logoutUser(request):
    logout(request)
    return redirect('index')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # Instead of committing data to database, it suspends it temporarily
            user.username = user.username.lower() # Ensures all usernames are lower case to prevent duplicates with different cases.
            user.save() # Finally saves
            
            messages.success(request, 'User account was created')

            login(request, user) # Logs user in
            return redirect('edit-account')
        else:
            messages.success(request, "An error has occured during registration")

    
    context = {'page':page, 'form':form}
    return render (request, 'accounts/create_account.html', context)

@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)

    
    context = {'form':form}
    return render(request, 'accounts/edit_account.html', context)
