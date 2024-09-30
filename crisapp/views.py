from django.shortcuts import render,redirect,HttpResponse
from .models import NewsletterSubscription  # Assuming you have a model defined for subscriptions
# Create your views here.

from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Process the form data, e.g., send an email
            send_mail(
                f'Contact Form Submission from {name}',
                f'Message: {message}\nPhone: {phone}\nEmail: {email}',
                'proyectodigitalmexico@gmail.com',  # From email
                ['proyectodigitalmexico@gmail.com'],  # To email
                fail_silently=False,
            )
            
            
            messages.success(request, 'Email Sent! (Mensaje Enviado)')
            return redirect('inicio')
    else:
        form = ContactForm()

    return render(request, 'enviar_email.html', {'form': form})



def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Process the form data, e.g., send an email
            send_mail(
                f'Contact Form Submission from {name}',
                f'Message: {message}\nPhone: {phone}\nEmail: {email}',
                'proyectodigitalmexico@gmail.com',  # From email
                ['proyectodigitalmexico@gmail.com'],  # To email
                fail_silently=False,
            )
            
            
            messages.success(request, 'Email Sent! (Mensaje Enviado)')
            return redirect('inicio')
    else:
        form = ContactForm()

    return render(request, 'inicio.html', {'form': form})



def politica_privacidad(request):
    return render(request ,'politica_privacidad.html')


def terminos_condiciones(request):
    return render(request ,'terminos_condiciones.html')

def about_us(request):
    return render(request,'about_us.html')





# views.py




from .models import NewsletterSubscription

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            subscription = NewsletterSubscription(email=email)
            subscription.save()
            messages.success(request, "Thank you for subscribing to our newsletter!")
            return redirect('inicio')  # Change this to an existing view name

        messages.error(request, "Invalid email address.")

    return redirect('inicio')  # Change this accordingly

