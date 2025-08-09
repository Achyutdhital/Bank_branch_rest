from rest_framework import serializers
from .models import Bank, Branch


class BankSerializer(serializers.ModelSerializer):
    """Serializer for Bank model."""
    
    class Meta:
        model = Bank
        fields = ['id', 'name', 'code', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class BranchListSerializer(serializers.ModelSerializer):
    """Serializer for Branch model in list views."""
    bank_name = serializers.CharField(source='bank.name', read_only=True)
    bank_code = serializers.CharField(source='bank.code', read_only=True)
    
    class Meta:
        model = Branch
        fields = ['id', 'name', 'ifsc', 'city', 'state', 'bank_name', 'bank_code']


class BranchDetailSerializer(serializers.ModelSerializer):
    """Serializer for Branch model in detail views."""
    bank = BankSerializer(read_only=True)
    
    class Meta:
        model = Branch
        fields = ['id', 'name', 'ifsc', 'address', 'city', 'state', 'bank', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class BankWithBranchesSerializer(serializers.ModelSerializer):
    """Serializer for Bank model with branches."""
    branches = BranchListSerializer(many=True, read_only=True)
    branch_count = serializers.IntegerField(source='branches.count', read_only=True)
    
    class Meta:
        model = Bank
        fields = ['id', 'name', 'code', 'branch_count', 'branches', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
