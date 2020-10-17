from django.contrib import admin
from .models import Dogs


class DogsAdmin(admin.ModelAdmin):
    model = Dogs


admin.site.register(Dogs, DogsAdmin)
