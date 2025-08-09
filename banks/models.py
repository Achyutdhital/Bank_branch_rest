from django.db import models


class Bank(models.Model):
    """Bank model representing a financial institution."""
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'banks'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})"


class Branch(models.Model):
    """Branch model representing a bank branch."""
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=11, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'branches'
        ordering = ['bank__name', 'name']
        indexes = [
            models.Index(fields=['ifsc']),
            models.Index(fields=['city']),
            models.Index(fields=['state']),
        ]

    def __str__(self):
        return f"{self.name} - {self.bank.name}"
