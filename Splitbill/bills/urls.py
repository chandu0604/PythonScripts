from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('bill_entry/', views.bill_entry),
    path('bill_entry_submit', views.bill_entry_submit),
    path('share_bill/', views.share_bill),
    path('monthly_bill/', views.monthly_bill)

]
