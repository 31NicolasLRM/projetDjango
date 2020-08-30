from django.contrib import admin

# Register your models here.
from .models import *

class StudentAdmin(admin.ModelAdmin):
  list_display = ("first_name","last_name", "email", "phone")

class CursusAdmin(admin.ModelAdmin):
  fields = ['scholar_year', 'name', 'year_from_bac']

class PresenceAdmin(admin.ModelAdmin):
  fields = ['reason', 'isMissing', 'date', 'student']

admin.site.register(Student, StudentAdmin)
admin.site.register(Cursus, CursusAdmin)
admin.site.register(Presence, PresenceAdmin)