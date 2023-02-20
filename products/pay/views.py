import stripe

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Item


class Products(TemplateView):
    template_name = 'base.html'
    context_object_name = 'Товары'

    def get_context_data(self, **kwargs):
        product = Item.objects.get(name="Test Product")
        context = super(Products, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class Success(TemplateView):
    template_name = 'success.html'


class Cancel(TemplateView):
    template_name = 'cancel.html'


stripe.api_key = settings.STRIPE_SECRET_KEY


def get_coupon():
    return stripe.Coupon.create(
        percent_off=50,
    )


class CreateCheckoutSession(View):

    def post(self, requests, *args, **kwargs):
        products_id = self.kwargs['pk']
        products = Item.objects.get(id=products_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000/'

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],

            line_items=[
                {
                    'price_data': {

                        'currency': 'usd',
                        'unit_amount': products.price,
                        'product_data': {
                            'name': products.name},
                    },
                    'quantity': 1,
                },
            ],

            mode='payment',
            discounts=[{
                'coupon': get_coupon(),
            }],

            success_url=YOUR_DOMAIN + 'success/',
            cancel_url=YOUR_DOMAIN + 'cancel/',
        )
        # return redirect(checkout_session.url, code=303)
        return JsonResponse({
            'id': checkout_session.id
        })
