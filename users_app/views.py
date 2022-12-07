from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            # register_form.save()
            messages.success(request, ("Your Account Has Been Created Successfully, Login To Get Started!"))
            return redirect('register')
    else:
        register_form = UserCreationForm()
    return render(request, 'register.html', {'register_form': register_form})