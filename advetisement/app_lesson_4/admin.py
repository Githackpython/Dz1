from django.contrib import admin
from .models import Advetisement
class AdvetisementAdmin(admin.ModelAdmin):
    pass
admin.site.register(Advetisement,AdvetisementAdmin)



