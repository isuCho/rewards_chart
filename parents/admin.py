from django.contrib import admin

from .models import Child, Parent, Task

admin.site.register(Child)
admin.site.register(Parent)
admin.site.register(Task)