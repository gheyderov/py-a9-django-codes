import time
from celery import shared_task
from core.models import Subscriber
from product.models import Product
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

@shared_task
def send_mail_to_subscribers():
    email_list = Subscriber.objects.values_list('email', flat=True)
    products = Product.objects.all()[:3]

    message = render_to_string('includes/email_to_subscribers.html', {
                'products' : products
            })
    mail = EmailMultiAlternatives(
        subject='Lates Products',
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=email_list

    )
    mail.content_subtype = 'html'
    mail.send()
    


@shared_task
def export_data():
    print('Process start!')
    time.sleep(10)
    print("Process end")


