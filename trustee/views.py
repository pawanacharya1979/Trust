from django.shortcuts import render
from .forms import HomeForm, ContactForm1
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('Name')
            email = form.cleaned_data.get('Email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('Message')
            body = {'Name': name, 'Email': email,'subject': subject, 'Message': message},

            email = EmailMessage(
                'Contact From',
                str(body),
                to=['parvaaz.academy@gmail.com']
            )
            email.send()
            messages.success(request, 'Thank You! for contacting us, we will get back to you soon.')
            return HttpResponseRedirect('/')
    else:
        form = HomeForm()
    return render(request, 'trustee/home.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm1(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('Name')
            email = form.cleaned_data.get('Email')
            phone = form.cleaned_data.get('Phone')
            message = form.cleaned_data.get('Message')
            body = {'Name': name, 'Email': email,'Phone': phone, 'Message': message},

            email = EmailMessage(
                'Contact From',
                str(body),
                to=['parvaaz.academy@gmail.com']
            )
            email.send()
            messages.success(request, 'Thank You! for contacting us, we will get back to you soon.')
            return HttpResponseRedirect('/contact-us/')
    else:
        form = ContactForm1()
    return render(request, 'trustee/contact.html', {'form': form})


def quiz(request):
    return render(request, 'trustee/Onlinequiz.html')


def tution(request):
    return render(request,'trustee/tution.html')


def about(request):
    return render(request,'trustee/aboutus.html')


def uqaab(request):
    return render(request,'trustee/uqaab.html')


def leadership(request):
    return render(request,'trustee/leadership.html')


def support(request):
    return render(request,'trustee/supportteam.html')


def donate(request):
    return render(request,'trustee/donate.html')


def madrasa(request):
    return render(request,'trustee/Madrasa.html')