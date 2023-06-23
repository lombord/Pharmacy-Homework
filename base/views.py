from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse


from .models import *

# Create your views here.


def homePage(request: HttpRequest):
    pharmacies = None
    if request.POST.get('pk'):
        from django.db.models import F
        med = Medicine.objects.get(pk=request.POST.get('pk'))
        pharmacies = med.pharmacies.all().order_by(
            F('coefficient') + F('distance') * .01)
    meds = Medicine.objects.all()
    context = {'meds': meds, 'pharmacies': pharmacies}
    return render(request, 'base/home.html', context)
