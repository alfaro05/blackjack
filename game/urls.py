from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('game', views.game, name="game"),
    path('next_round', views.next_round, name="next_round")
]
urlpatterns += staticfiles_urlpatterns()