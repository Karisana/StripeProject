from django.urls import path, include

# from products import settings
from .views import product_list, CreateCheckoutSession, Cancel, Success

urlpatterns = [
    path('', product_list, name='base'),
    path('create-checkout-session/<pk>', CreateCheckoutSession.as_view(), name='create-checkout-session'),
    path('cancel/', Cancel.as_view(), name='cancel'),
    path('success/', Success.as_view(), name='success'),

]
