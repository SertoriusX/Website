from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="index"),
    path('card/',views.cards,name="card"),
    path('detail/<int:card_id>/',views.detail,name="detail"),
    path('home/',views.home,name="Home"),



]
