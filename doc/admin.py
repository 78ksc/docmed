from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Presc)
admin.site.register(Inves)
admin.site.register(Docsuggest)