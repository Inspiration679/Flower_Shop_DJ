from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


# Create your views here.

# def signUpView(request):
#     print(request.form["btn"])
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             signup_user = User.objects.get(username=username)
#             user_group = Group.objects.get(name='User')
#             user_group.user_set.add(signup_user)
#             return redirect("Home")
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


def signView(request):
    # if request.method == "POST":
    #     form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         username = request.POST["username"]
    #         password = request.POST["password"]
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect("Home")
    # else:
    #     form = AuthenticationForm()

    if request.method == 'POST':
        form2 = SignUpForm(request.POST)
        if form2.is_valid():
            form2.save()
            username = form2.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(signup_user)
            return redirect("Home")
    else:
        form2 = SignUpForm()
    return render(request, "login.html",
                  {"path": "css/login_registration/login_registration.css",
                   "title": "Account", "form2": form2})
