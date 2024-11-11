from django.urls import path

from core import views

urlpatterns = [
    path('post', views.transactionPost, name='transaction_post'),
    path('post_v2', views.transactionPost_v2, name='transaction_post_v2')
]