from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse
import stripe
from rms.settings import *
from .forms import UserPaymentForm



stripe.api_key = STRIPE_SECRET_KEY
BASE_URL = 'http://127.0.0.1:8000/'

def payment_view(request):
    if request.method == "POST":
        form = UserPaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            try:
                session = stripe.checkout.Session.create(
                    payment_method_types=["card", 'us_bank_account'],
                    line_items=[{
                        "price_data": {
                            "currency": "usd",
                            "product_data": {
                                "name": "Lease",
                            },
                            "unit_amount": int(amount * 100),
                        },
                        "quantity": 1,
                    }],
                    mode="payment",
                    success_url = BASE_URL+'payment_successful/',
                    cancel_url = BASE_URL+'payment_cancelled/',
                )
                
                return redirect(session.url)
                
            except stripe.error.StripeError as e:
                return render(request, "payments/payment_form.html", {"form": form, "error": str(e)})

    else:
        form = UserPaymentForm()
    
    return render(request, "payments/payment_form.html", {"form": form, "stripe_public_key": STRIPE_SECRET_KEY})


def stripe_onfig(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

def subscription_view(request):
    subscription= {
        'basic':"prod_RvcLGWeBxWfGnh",
        'standard':'prod_Rw52cPKyGVGF5X',
        'pro':"prod_Rw53VeS9OnawRQ"
    }
    
    
    
    if request.method =="POST":
        price_id =request.POST.get('price_id')
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    'price':price_id,
                    'quantity':1,
                }
                ],
            
            payment_method_types=['card', 'us_bank_account'],
            mode='subscription',
            success_url = BASE_URL+'payment_successful/',
            cancel_url = BASE_URL+'payment_cancelled/',
            metadata={
                "user_id":request.user.id,
            }
        )
        return redirect(checkout_session.url, code=303)
    
    
    return render(request, 'payments/subscription.html', {'subscription': subscription} )

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = STRIPE_ENDPOINT_SECRET
    try:
        event = stripe.Webhook.construct_event(payload,sig_header,endpoint_secret)
    except:
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout_session.completed':
        print(event)
        print('payment ws succesful')
    return HttpResponse(status=200 )

def create_subscription(request):
    checkout_session_id = request.GET.get('session_id', None)
    return redirect('my_sub')

def my_sub_view(request):
    return render(request, 'payments/my_sub.html')


def payment_successful(request):
    return render(request, 'payments/success.html')

def payment_cancelled(request):
    return render(request, 'payments/cancel.html')