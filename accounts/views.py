from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def signin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user= auth.authenticate(username=name,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'invalid credentials')
            messages.add_message(request, messages.INFO, 'invalid credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')



def home(request):
    try:
        if auth._get_user_session_key(request):
            return render(request, 'index.html')
    except:
        return redirect('signin')

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('signup') #if we get error we should return to same page not to home page
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('signin')

        else:
            messages.info(request, 'password not matching')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request, 'signup.html')


def signout(request):
    auth.logout(request)
    return redirect('/')
