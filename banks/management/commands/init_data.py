from django.core.management.base import BaseCommand
from banks.models import Bank, Branch


class Command(BaseCommand):
    help = 'Initialize the database with sample bank and branch data'

    def handle(self, *args, **options):
        self.stdout.write('Initializing database with sample data...')

        # Clear existing data
        Branch.objects.all().delete()
        Bank.objects.all().delete()

        # Create sample banks
        banks_data = [
            {'name': 'State Bank of India', 'code': 'SBI'},
            {'name': 'HDFC Bank', 'code': 'HDFC'},
            {'name': 'ICICI Bank', 'code': 'ICICI'},
            {'name': 'Axis Bank', 'code': 'AXIS'},
            {'name': 'Punjab National Bank', 'code': 'PNB'},
        ]

        banks = {}
        for bank_data in banks_data:
            bank = Bank.objects.create(**bank_data)
            banks[bank_data['code']] = bank
            self.stdout.write(f'Created bank: {bank.name}')

        # Create sample branches
        branches_data = [
            {
                'bank': banks['SBI'],
                'name': 'Mumbai Main Branch',
                'ifsc': 'SBIN0000001',
                'address': '123 Fort Area, Mumbai',
                'city': 'Mumbai',
                'state': 'Maharashtra'
            },
            {
                'bank': banks['SBI'],
                'name': 'Delhi Connaught Place',
                'ifsc': 'SBIN0000002',
                'address': '456 CP, New Delhi',
                'city': 'Delhi',
                'state': 'Delhi'
            },
            {
                'bank': banks['HDFC'],
                'name': 'Bangalore Koramangala',
                'ifsc': 'HDFC0000001',
                'address': '789 Koramangala, Bangalore',
                'city': 'Bangalore',
                'state': 'Karnataka'
            },
            {
                'bank': banks['HDFC'],
                'name': 'Chennai Anna Nagar',
                'ifsc': 'HDFC0000002',
                'address': '321 Anna Nagar, Chennai',
                'city': 'Chennai',
                'state': 'Tamil Nadu'
            },
            {
                'bank': banks['ICICI'],
                'name': 'Pune Camp',
                'ifsc': 'ICIC0000001',
                'address': '654 Camp Area, Pune',
                'city': 'Pune',
                'state': 'Maharashtra'
            },
            {
                'bank': banks['ICICI'],
                'name': 'Hyderabad Gachibowli',
                'ifsc': 'ICIC0000002',
                'address': '987 Gachibowli, Hyderabad',
                'city': 'Hyderabad',
                'state': 'Telangana'
            },
            {
                'bank': banks['AXIS'],
                'name': 'Kolkata Park Street',
                'ifsc': 'UTIB0000001',
                'address': '147 Park Street, Kolkata',
                'city': 'Kolkata',
                'state': 'West Bengal'
            },
            {
                'bank': banks['AXIS'],
                'name': 'Ahmedabad CG Road',
                'ifsc': 'UTIB0000002',
                'address': '258 CG Road, Ahmedabad',
                'city': 'Ahmedabad',
                'state': 'Gujarat'
            },
            {
                'bank': banks['PNB'],
                'name': 'Jaipur MI Road',
                'ifsc': 'PUNB0000001',
                'address': '369 MI Road, Jaipur',
                'city': 'Jaipur',
                'state': 'Rajasthan'
            },
            {
                'bank': banks['PNB'],
                'name': 'Lucknow Hazratganj',
                'ifsc': 'PUNB0000002',
                'address': '741 Hazratganj, Lucknow',
                'city': 'Lucknow',
                'state': 'Uttar Pradesh'
            },
        ]

        for branch_data in branches_data:
            branch = Branch.objects.create(**branch_data)
            self.stdout.write(f'Created branch: {branch.name} ({branch.ifsc})')

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {Bank.objects.count()} banks and {Branch.objects.count()} branches'
            )
        )
