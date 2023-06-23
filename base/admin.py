from django.contrib import admin

from .models import Medicine, Pharmacy

admin.site.register(Pharmacy)
admin.site.register(Medicine)
