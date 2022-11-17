from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def todolist(request):
    context = {
        'welcome_text':"Welcome From Todo List Page."
        }
    return render(request, 'todolist.html', context)

def contact(request):
    context = {
        'welcome_text':"Welcome From Contact Page."
        }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'welcome_text':"Welcome From About Us Page."
        }
    return render(request, 'about.html', context)