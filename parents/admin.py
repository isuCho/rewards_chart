from django.contrib import admin

from .models import Child, Parent

admin.site.register(Child)
admin.site.register(Parent)