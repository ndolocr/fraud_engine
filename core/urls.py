from django.urls import path

from core import views

urlpatterns = [
    path('post', views.transactionPost, name='transaction_post')
]