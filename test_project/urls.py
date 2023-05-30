from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal_acc/', include('django.contrib.auth.urls')),
    path('personal_acc/', include('personal_acc.urls')),
    path('', include('accounts.urls'))
]
