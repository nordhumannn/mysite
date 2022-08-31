from django.urls import path
from .views import customer, customer_general

urlpatterns = [
    path('<int:customer_number>/', customer),
    path('', customer_general),
]