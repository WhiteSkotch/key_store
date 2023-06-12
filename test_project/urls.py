from django.contrib import admin
from django.urls import path, include
from personal_acc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal_acc/', include('django.contrib.auth.urls')),
    path('personal_acc/', include('personal_acc.urls')),
    path('logout', views.logout_view, name='logout'),
    path('', include('accounts.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    # path('get_money/', views.get_money, name='get_money'),
]
