from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterCustomerForm


# Create your views here.


# Registering customers


def register_customer(request):
    if request.method == "POST":
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.save()
            messages.success(
                request, "account has been successfully registered. login to countinue."
            )
            return redirect("login")
        else:
            messages.warning(
                request, "something went wrong. please check the form's inputs."
            )
            return redirect("register-customer")

    else:
        form = RegisterCustomerForm()
        context = {"form": form}
        return render(request, "users/register_customer.html", context)


# login


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, "login was successful.")
            return redirect("dashboard")
        else:
            messages.warning(request, "something went wrong.")
            return redirect("login")

    else:
        return render(request, "users/login.html")


# logout user


def logout_user(request):
    logout(request)
    messages.info(request, "you have successfully loged out.")
    return redirect("home")
