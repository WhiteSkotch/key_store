from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('add_money/', views.add_money, name='add_money'),
    path('get_money/', views.get_money, name='get_money'),
    path('add_money/', views.add_money_view, name='add_money_view'),
    path('get_trans/', views.get_trans, name='get_trans'),
]