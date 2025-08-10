import csv
import os
from django.core.management.base import BaseCommand
from django.db import transaction
from banks.models import Bank, Branch


class Command(BaseCommand):
    help = 'Load real bank and branch data from the CSV file'

    def handle(self, *args, **options):
        self.stdout.write('Loading real bank and branch data...')

        # Path to the CSV file
        csv_file_path = os.path.join('bank_branches.csv')
        
        if not os.path.exists(csv_file_path):
            self.stdout.write(
                self.style.ERROR(
                    'CSV file not found. Please make sure bank_branches.csv is in the project root.'
                )
            )
            return

        # Clear existing data
        with transaction.atomic():
            Branch.objects.all().delete()
            Bank.objects.all().delete()

            banks_created = {}
            branches_created = 0

            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    bank_id = int(row['bank_id'])
                    bank_name = row['bank_name']
                    
                    # Create bank if it doesn't exist
                    if bank_id not in banks_created:
                        bank, created = Bank.objects.get_or_create(
                            id=bank_id,
                            defaults={'name': bank_name}
                        )
                        if created:
                            banks_created[bank_id] = bank
                            self.stdout.write(f'Created bank: {bank_name} (ID: {bank_id})')
                        else:
                            banks_created[bank_id] = bank
                    
                    # Create branch
                    try:
                        branch = Branch.objects.create(
                            ifsc=row['ifsc'],
                            bank=banks_created[bank_id],
                            branch=row['branch'],
                            address=row['address'],
                            city=row['city'],
                            district=row['district'],
                            state=row['state']
                        )
                        branches_created += 1
                        
                        if branches_created % 1000 == 0:
                            self.stdout.write(f'Created {branches_created} branches...')
                            
                    except Exception as e:
                        self.stdout.write(
                            self.style.WARNING(
                                f'Error creating branch {row["ifsc"]}: {e}'
                            )
                        )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully loaded {len(banks_created)} banks and {branches_created} branches'
            )
        )
