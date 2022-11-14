from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Contact

# Create your views here.
def a(request):
    return HttpResponse("a 응답!")
def contact(request,no):
    con=Contact.objects.get(id=no)
    return HttpResponse(con.name)