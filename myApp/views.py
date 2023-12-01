from django.shortcuts import render,get_list_or_404
from .models import yugioh,yugioh1
from django.core.paginator import Paginator

# Create your views here.

def cards(request,*args,**kwargs):
    cards = yugioh.objects.all()
    paginator = Paginator(cards, 16)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    cards = paginator.get_page(page_number) 
    return render(request,'myApp/card.html',{'cards':cards}) 

def detail(request,card_id,*args,**kwargs):
    card = get_list_or_404(yugioh,id=card_id)
    return render(request,'myApp/detail.html',{'cards':card}) 


def home(response):
    return render(response,'myApp/home.html')