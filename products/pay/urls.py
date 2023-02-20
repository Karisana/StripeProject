from django.urls import path, include

# from products import settings
from .views import Products, CreateCheckoutSession, Cancel, Success

urlpatterns = [
    path('', Products.as_view(), name='base'),
    path('create-checkout-session/<pk>', CreateCheckoutSession.as_view(), name='create-checkout-session'),
    path('cancel/', Cancel.as_view(), name='cancel'),
    path('success/', Success.as_view(), name='success'),

]
