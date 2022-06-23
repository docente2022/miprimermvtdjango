from django.contrib import admin
from .models import familiar
# Register your models here.

class FamiliarAdmin(admin.ModelAdmin):
    list_display= ("nombre", "edad", "fecha_nac")
    
    
    
admin.site.register(familiar, FamiliarAdmin)