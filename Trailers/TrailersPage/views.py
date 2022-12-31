from django.shortcuts import render
from .models import TrailersInf


# Create your views here.

def main(request):
    return render(request,"main.html")

def trailerspage(request):
   data = TrailersInf.objects.all()
   return render(request,"trailerspage.html",{"data":data})

def search(request):
    data = request.GET['search']
    data = TrailersInf.objects.filter(title__icontains = data)
    return render(request,"trailerspage.html",{"data":data})

def trailersinf(request,title):
    trailer = TrailersInf.objects.filter(title = title).first()
    return render(request,"trailersinf.html",{"trailer":trailer})

def romancetrailers(request):
    data = TrailersInf.objects.filter(category = 'Romance')
    return render(request,"trailerspage.html",{"data":data})

def actiontrailers(request):
    data = TrailersInf.objects.filter(category = 'Action')
    return render(request,"trailerspage.html",{"data":data})

def fantasytrailers(request):
    data = TrailersInf.objects.filter(category = 'Fantasy')
    return render(request,"trailerspage.html",{"data":data})
    
def suspensetrailers(request):
    data = TrailersInf.objects.filter(category = 'Suspense')
    return render(request,"trailerspage.html",{"data":data})
    





        
