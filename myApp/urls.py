from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Index"),
    path('card/',views.cards,name="Card"),
    path('detail/<int:cards_id>/',views.detail,name="detail"),

    path('home/',views.home,name="Home"),



]
