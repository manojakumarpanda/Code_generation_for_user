from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import User_codes,profile

# Register your models here.

class Code_Admin(ImportExportModelAdmin):
    list_display = ['id','codes']

class profile_Admin(admin.ModelAdmin):
    list_display = ['id','pid','full_name']

admin.site.register(User_codes,Code_Admin)
admin.site.register(profile,profile_Admin)
