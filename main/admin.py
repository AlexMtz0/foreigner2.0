from django.contrib import admin
from .models import Casas

class CasasAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Casas, CasasAdmin)
# Register your models here.
