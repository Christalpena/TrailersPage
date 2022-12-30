from django.shortcuts import render,redirect
from .models import TrailersInf
from django.http import HttpResponseRedirect

# Create your views here.

def main(request):
    return render(request,"main.html")

def trailerspage(request):
   data = TrailersInf.objects.all()
   return render(request,"trailerspage.html",{"data":data})

def search(request):

    data = request.GET['search']
    data = TrailersInf.objects.filter(title__icontains = data)
    
    return render(request,"searchpageresult.html",{"data":data})
def trailersinf(request,title):
    trailer = TrailersInf.objects.filter(title = title).first()

    return render(request,"trailersinf.html",{"trailer":trailer})
    





        
