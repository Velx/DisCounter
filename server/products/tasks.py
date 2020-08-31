import requests
import json
import re
import time
import os
from decimal import Decimal
from django.utils.timezone import datetime, timedelta
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template import loader
from django.db.models import Q, F
from django.conf import settings
from bs4 import BeautifulSoup
from discounter.celery import app
from .models import Products
from fcm_django.models import FCMDevice
from django.contrib.auth import get_user_model

@app.task
def check_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0',
    }
    http = requests.get(url, headers=headers)
    soup = BeautifulSoup(http.text, 'lxml')
    all_scripts = soup.find_all('script')
    data = re.search(r'data: \{.+\},', all_scripts[-3].contents[0], flags=re.M).group(0)
    data = json.loads(data[6:-1])
    product_id = data['actionModule']['productId']
    title = data['titleModule']['subject'][0:200]
    image = data['imageModule']['imagePathList'][0]
    if data['quantityModule'].get("activity"):
        normal_price = Decimal(data['priceModule']['minAmount']['value']).quantize(Decimal('.01'))
        try:
            minimum = Decimal(data['priceModule']['minActivityAmount']['value']).quantize(Decimal('.01'))
        except KeyError:
            minimum = None
    else:
        normal_price = minimum = None
    return product_id, title, image, normal_price, minimum


@app.task
def cron_price():
    to_check = Products.objects.all()
    for product in to_check:
        _, _, _, product.price, product.current_price = check_price(product.ali_url)
        product.save(update_fields=['price', 'current_price'])
        time.sleep(1)
    users = get_user_model().objects.filter(products__current_price__isnull=False).distinct()
    datatuple = []
    for user in users.filter(e_notifications=True):
        count = user.products.filter(current_price__isnull=False).count()
        datatuple.append((count, user.email))
    if datatuple:
        send_mass_html_mail.delay(datatuple)
    for device in FCMDevice.objects.filter(user__in=users):
        device.send_message(
            title="Products with discount in your list",
            body="There are products from your list that are currently sold at a discount",
            time_to_live=604800,
            click_action=os.environ.get('SITE_URL')
        )


@app.task
def send_mass_html_mail(datatuple, fail_silently=False, user=settings.EMAIL_HOST_USER,
                        password=settings.EMAIL_HOST_PASSWORD, connection=None):
    connection = connection or get_connection(
        username=user, password=password, fail_silently=fail_silently)
    messages = []
    from_email = settings.EMAIL_HOST_USER
    subject = 'Products with discount in your list'
    for count, recipient in datatuple:
        text = '1 product' if count == 1 else f'{count} products'
        context = {
            'count': text,
            'site_link': os.environ.get('SITE_URL')
        }
        body = loader.render_to_string('users/notification_email.html', context)
        message = EmailMultiAlternatives(subject, body, from_email, [recipient])
        message.content_subtype = "html"
        messages.append(message)
    return connection.send_messages(messages)