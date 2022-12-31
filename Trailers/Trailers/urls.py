"""Trailers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TrailersPage.views import trailerspage,trailersinf,search,romancetrailers,actiontrailers,fantasytrailers,suspensetrailers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trailerspage/',trailerspage, name = "trailerspage"),
    path('searchpageresult/',search, name="filterTrailers"),
    path('trailerinf/<str:title>',trailersinf,name= "trailersinf"),
    path('RomanceTrailers/',romancetrailers, name="Romance"),
    path('ActionTrailers/',actiontrailers, name="Action"),
    path('FantasyTrailers/',fantasytrailers, name="Fantasy"),
    path('SportsTrailers/',suspensetrailers, name="Suspense"),

]
