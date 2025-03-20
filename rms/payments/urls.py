from django.urls import path
from .views import *

urlpatterns = [
    path('',subscription_view, name='subscription'),
    path('payment/', payment_view, name='user_payment'),path('stripe_webhook', stripe_webhook, name='stripe_webhook'),
    path('create/', create_subscription, name='create_subscription'),
    path('payment_successful/', payment_successful, name='payment_successful'),
    path('payment_cancelled/', payment_cancelled,name="payment_cancelled" ),
    path('my_sub/', my_sub_view, name='my_sub_view')
]
