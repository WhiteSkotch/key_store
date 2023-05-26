from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from personal_acc.views import *

urlpatterns = [
    path('games/', get_games, name='games'),
    path('games/<int:pk>/', game_detail, name='game_detail'),
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),

]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

