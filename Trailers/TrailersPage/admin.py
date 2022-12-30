from django.contrib import admin
from .models import TrailersInf
# Register your models here.

class Trailer(admin.ModelAdmin):
    list_display =('title','year','director')

admin.site.register(TrailersInf,Trailer)