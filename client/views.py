from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Client

# error
def log(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')
        try:
            Auser = User.objects.get(username=uname)
        except User.DoesNotExist:
            # Handle the case where the user does not exist
            return render(request, 'client/login.html', {'msg': 'User not found'})

        Auser = authenticate(request , username = uname , password = pass1)
        if Auser is not None:
            login(request, Auser)
            return redirect('home')
    con={

    }
    return render(request,'client/login.html',con)

def register(request):
    # form = UserCreationForm()
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST) #make all one by one loke username email pass etc so that we can access
        uname = request.POST.get('username')
        # pass1 = request.POST.get('password')
        
        
        if form.is_valid():
            form.save()
            try:
                obj = User.objects.get(username = uname)
                Client.objects.create(user=obj).save()
            except User.DoesNotExist:
                return render(request, 'client/register.html', {'msg': 'User not found'})
            print(obj)
            login(request,obj)
            return redirect('home')

    con={
        'form':form,
    }
    return render(request,'client/register.html',con)

def logo(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return render(request,'client/logout.html')

def account(request):
    obj = User.objects.get(username = request.user)
    profile = Client.objects.get(user = obj.id)

    if request.method == 'POST':
            # Update the profile fields as needed
            if obj.email is not '':
                obj.email = request.POST.get('email')
            if profile.phone is not '':
                profile.phone = request.POST.get('phone') 
            if profile.state is not '':
                profile.state = request.POST.get('state')
            if profile.city is not '':
                profile.city = request.POST.get('city')
            if profile.pincode is not '':
                profile.pincode = request.POST.get('pincode')
            if profile.area is not '':
                profile.area = request.POST.get('area')
            if profile.dob is not '':
                profile.dob = request.POST.get('dob')
            profile.save()
            return redirect('home')
    con = {
        'profile':profile,
    }
    return render(request,'client/account.html',con)

from django.shortcuts import render, redirect
from .models import Client

def accountEdit(request):
    # Get the current user
    user = request.user

    try:
        # Try to get the user's profile
        profile = Client.objects.get(user=user)

        if request.method == 'POST':
            # Update the profile fields as needed
            profile.phone = request.POST.get('phone')  # Replace with the actual field names
            profile.state = request.POST.get('state')
            profile.city = request.POST.get('city')
            profile.pincode = request.POST.get('pincode')
            profile.area = request.POST.get('area')
            profile.dob = request.POST.get('dob')
            profile.save()
            return redirect('home')
    except Client.DoesNotExist:
        # Handle the case where the profile doesn't exist for the user
        # You can create a new profile here or return an error
        pass

    # Return the view with the updated or unmodified profile
    context = {'profile': profile}  # Pass any additional data needed for the view
    return render(request, 'client/accountedit.html', context)
