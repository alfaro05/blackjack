from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def game(request):
    cards_dict = {"key":"value"}
    return render(request, "game.html",cards_dict)