import os
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template import loader

from celery import shared_task


@shared_task
def send_activation_code(subject, to_email, activation_code, action, template):
    from_email = settings.EMAIL_HOST_USER
    context = {
        'user_address': to_email,
        'site_link': os.environ.get('SITE_URL') + action + '/' + str(activation_code)
    }
    body = loader.render_to_string(template, context)
    email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
    email_message.content_subtype = "html"
    email_message.send()
