from django.contrib import admin
from .models import Bank, Branch


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['ifsc', 'branch', 'city', 'district', 'state', 'bank']
    list_filter = ['city', 'district', 'state', 'bank', 'created_at']
    search_fields = ['ifsc', 'branch', 'city', 'district', 'state']
    readonly_fields = ['created_at', 'updated_at']
    list_select_related = ['bank']
