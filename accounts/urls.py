from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from personal_acc.views import *

urlpatterns = [
    path('games/', get_games, name='games'),
    path('games/<int:pk>/', game_detail, name='game_detail'),
    path('home/', home, name='home'),
    path('aboutstore/', aboutstore, name='aboutstore'),
    path('agreement/', agreement, name='agreement'),
    path('guarantees/', guarantees, name='guarantees'),
    path('refund/', refund, name='refund'),
    path('support/', support, name='support'),




]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

