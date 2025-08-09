from django.contrib import admin
from .models import Bank, Branch


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'code']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ifsc', 'city', 'state', 'bank']
    list_filter = ['city', 'state', 'bank', 'created_at']
    search_fields = ['name', 'ifsc', 'city', 'state']
    readonly_fields = ['created_at', 'updated_at']
    list_select_related = ['bank']
