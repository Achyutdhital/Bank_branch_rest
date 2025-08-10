from django.db import models


class Bank(models.Model):
    """Bank model representing a financial institution."""
    id = models.BigIntegerField(primary_key=True)  # Using BigIntegerField to match original data
    name = models.CharField(max_length=49)  # Matching original max length
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'banks'
        ordering = ['name']

    def __str__(self):
        return self.name


class Branch(models.Model):
    """Branch model representing a bank branch."""
    ifsc = models.CharField(max_length=11, primary_key=True)  # IFSC as primary key
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')
    branch = models.CharField(max_length=74)  # Using 'branch' to match original data
    address = models.CharField(max_length=195)  # Using CharField with specific length
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)  # Added district field from original
    state = models.CharField(max_length=26)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'branches'
        ordering = ['bank__name', 'branch']
        indexes = [
            models.Index(fields=['city']),
            models.Index(fields=['state']),
            models.Index(fields=['district']),
        ]

    def __str__(self):
        return f"{self.branch} - {self.bank.name}"
