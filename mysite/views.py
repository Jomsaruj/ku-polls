from django.shortcuts import redirect

__author__      = "Saruj Sattayanurak"

def index(request):
    """
    Redirect to the polls index
    """
    return redirect("polls:index")
