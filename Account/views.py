from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def SignIn(request):
    sign_in = AuthenticationForm()
    template = "signIn.html"
    if request.method == "POST":
        sign_in = AuthenticationForm(data=request.POST)
        if sign_in.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("show_home")
        else:
            return render(request, template, context={"sign_in": sign_in, "path": "css/account/account.css", })
    else:
        return render(request, template, context={"sign_in": sign_in, "path": "css/account/account.css", })


def SignUp(request):
    sign_up = SignUpForm()
    template = "signUp.html"
    if request.method == "POST":
        sign_up = SignUpForm(data=request.POST)
        print(sign_up.errors)
        if sign_up.is_valid():
            new_user = sign_up.save(commit=False)
            new_user.set_password(sign_up.cleaned_data['password'])
            new_user.save()
            return redirect("show_sign_in")
        else:
            return render(request, template, context={"sign_up": sign_up, "path": "css/account/account.css", })
    else:
        return render(request, template, context={"sign_up": sign_up, "path": "css/account/account.css", }
                      )


def LogOut(request):
    logout(request)
    return redirect("show_home")
