from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def signin(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)
        if(user is not None):
            auth.login(request,user)           
            return redirect('/database/dashboard')
        else:
            messages.info(request,'invalid credential')
            return redirect('/register/signin')
    else:
        return render(request,'login.html')


def signup(request):
    if(request.method == 'POST'):
        fname = request.POST['firstname'].upper()
        lname = request.POST['lastname'].upper()
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pass']
        password1 = request.POST['pass1'] 

        if(password == password1):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'username already taken')
                return redirect('/register/signup')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'email taken')
                return redirect('/register/signup')
            else:               
                user = User.objects.create_user(username=username,email=email,password=password,first_name=fname,last_name=lname)        
                user.save()
        else:
            messages.info(request,'password not matching')
            return redirect('/register/signup')       
                
        return redirect('/register/signin')

    else:            
        return render(request, 'registration.html')

def signout(request):
    auth.logout(request)
    return redirect('/')