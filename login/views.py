from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.template import context
from .forms import SignupForm, LoginForm


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if form.is_valid():
            form.save()
            if password == confirm_password:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "email already exist")
                    return redirect('signup')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'username already exits')
                    return redirect('signup')
                else:
                    form = User.objects.create_user(username=username, email=email, password=password)
                    form.save()
                    return redirect('login')
            else:
                messages.info(request, "incorrect password")
                return redirect('signup')
    context = {'signup': form}
    return render(request, 'signup.html', context)


def login(request):
    user = LoginForm(request.POST)
    context = {'login': user}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/laundry')
        else:
            messages.info(request, "wrong username or password")
            return redirect('login')
    else:
        return render(request, 'login.html', context)
