from django.contrib import admin

from .models import Toilet,Review,User
# Register your models here.
admin.site.register(Toilet)
admin.site.register(Review)
admin.site.register(User)
