from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        name = request.POST['name']

        contacts = Contact(user_id=user_id, email=email, subject=subject, message=message, name=name)

        contacts.save()

        send_mail(
            'Pizzeria message',
            name + ' send you a message: ' + subject + '.\n' + message +
            '\nFor more information, check the administration panel on your website.',
            'rekrutacja.jarocin@gmail.com',
            ['klimak.nowi@gmail.com'],
            fail_silently=True
        )

        messages.success(request, ' Your request has been submitted.')
        return render(request, 'contacts/contact.html')
    else:
        return render(request, 'contacts/contact.html')
