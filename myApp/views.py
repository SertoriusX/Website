from django.shortcuts import render,get_list_or_404
from .models import yugioh
from django.core.paginator import Paginator

# Create your views here.

def cards(request,*args,**kwargs):
    cards = yugioh.objects.all()
    paginator = Paginator(cards, 16)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    cards = paginator.get_page(page_number) 
    return render(request,'myApp/card.html',{'cards':cards}) 

def detail(request,cards_id,*args,**kwargs):
    cards = get_list_or_404(yugioh,id=cards_id)
    return render(request,'myApp/detail.html',{'cards':cards}) 


def home(response):
    return render(response,'myApp/home.html')