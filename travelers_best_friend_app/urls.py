from django.urls import path
from travelers_best_friend_app import views

urlpatterns = [
    path('', views.homepage, name='homepage')
]
