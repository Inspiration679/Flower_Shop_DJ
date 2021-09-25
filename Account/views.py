from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from Cart.models import UserCart

def SignIn(request):
    sign_in = AuthenticationForm()
    template = "signIn.html"
    context = {"sign_in": sign_in, "path": "css/account/account.css", }
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

            context.update({"sign_in": sign_in})
            return render(request, template, context)
    else:
        return render(request, template, context)


def SignUp(request):
    sign_up = SignUpForm()
    template = "signUp.html"
    context = {"sign_up": sign_up, "path": "css/account/account.css", }
    if request.method == "POST":
        sign_up = SignUpForm(data=request.POST)

        if sign_up.is_valid():
            new_user = sign_up.save(commit=False)

            new_user.set_password(sign_up.cleaned_data['password'])
            new_user.save()
            new_cart=UserCart.objects.create(cart_slug=new_user.id,user_name=new_user.username)
            new_cart.save()
            return redirect("show_sign_in")
        else:
            context.update({"sign_up": sign_up})
            return render(request, template, context)
    else:
        return render(request, template, context)


def LogOut(request):
    logout(request)
    return redirect("show_home")
