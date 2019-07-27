from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone

from .models import Post, FreeQuote, Newletter
from .forms import PostForm, FreequoteForm, NewletterForm



def home(request):
    sub_form = NewletterForm(request.POST or None)
    if request.method == "POST":
        if sub_form.is_valid():
            sub_form.save()
            sub_form = NewletterForm()  
    return render(request, 'home.html', {'sub_form': sub_form})	

def about(request):
    sub_form = NewletterForm(request.POST or None)
    if request.method == "POST":
        if sub_form.is_valid():
            sub_form.save()
            sub_form = NewletterForm()  
    return render(request, 'about.html', {'sub_form': sub_form})

def service(request):
    sub_form = NewletterForm(request.POST or None)
    if request.method == "POST":
        if sub_form.is_valid():
            sub_form.save()
            sub_form = NewletterForm()  
    return render(request, 'service.html', {'sub_form': sub_form})


def portfolio(request):
    sub_form = NewletterForm(request.POST or None)
    if request.method == "POST":
        if sub_form.is_valid():
            sub_form.save()
            sub_form = NewletterForm()  
    return render(request, 'portfolio.html', {'sub_form': sub_form})	

def contact(request):
    form = PostForm(request.POST or None)
    success = False
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = PostForm()
            success =True
            messages.success(request, 'Your Message has been submitted, our team will be intouch soon.')
    sub_form = NewletterForm(request.POST or None)
    if request.method == "POST":
        if sub_form.is_valid():
            sub_form.save()
            sub_form =NewletterForm()            
    return render(request, 'contact.html', {'form': form, 'sub_form': sub_form})


def newletter_view(request):
    form = NewletterForm(request.POST or None)
    success =False
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = NewletterForm()
            success = True
            messages.success(request, 'Newletter request has been submitted')    
    return render(request, 'newletter.html', {'form': form})
# Create your views here.
