from django.shortcuts import render
from .forms import ContactForm, ContactForm1
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
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
                to=['pawanacharya1979@gmail.com']
            )
            email.send()
            messages.success(request, 'Thank You! for contacting us, we will get back to you soon.')
            return HttpResponseRedirect('/home/')
    else:
        form = ContactForm()
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
                to=['pawanacharya1979@gmail.com']
            )
            email.send()
            messages.success(request, 'Thank You! for contacting us, we will get back to you soon.')
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    return render(request, 'trustee/contact.html', {'form': form})


def quiz(request):
    return render(request, 'trustee/Onlinequiz.html')