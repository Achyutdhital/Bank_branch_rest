from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from banks.models import Bank, Branch


class BankAPITest(TestCase):
    """Test cases for Bank API endpoints."""
    
    def setUp(self):
        self.client = APIClient()
        self.bank1 = Bank.objects.create(name='State Bank of India', code='SBI')
        self.bank2 = Bank.objects.create(name='HDFC Bank', code='HDFC')
        
        self.branch1 = Branch.objects.create(
            bank=self.bank1,
            name='Mumbai Branch',
            ifsc='SBIN0000001',
            address='123 Fort Area, Mumbai',
            city='Mumbai',
            state='Maharashtra'
        )
        self.branch2 = Branch.objects.create(
            bank=self.bank2,
            name='Delhi Branch',
            ifsc='HDFC0000001',
            address='456 CP, New Delhi',
            city='Delhi',
            state='Delhi'
        )
    
    def test_bank_list_api(self):
        """Test GET /api/banks/"""
        url = reverse('bank-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['name'], 'HDFC Bank')
        self.assertEqual(response.data['results'][1]['name'], 'State Bank of India')
    
    def test_bank_detail_api(self):
        """Test GET /api/banks/{id}/"""
        url = reverse('bank-detail', kwargs={'id': self.bank1.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'State Bank of India')
        self.assertEqual(response.data['code'], 'SBI')
    
    def test_bank_branches_api(self):
        """Test GET /api/banks/{id}/branches/"""
        url = reverse('bank-branches', kwargs={'bank_id': self.bank1.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Mumbai Branch')
        self.assertEqual(response.data['results'][0]['bank_name'], 'State Bank of India')


class BranchAPITest(TestCase):
    """Test cases for Branch API endpoints."""
    
    def setUp(self):
        self.client = APIClient()
        self.bank = Bank.objects.create(name='Test Bank', code='TEST')
        
        self.branch1 = Branch.objects.create(
            bank=self.bank,
            name='Mumbai Branch',
            ifsc='TEST0000001',
            address='123 Test Street, Mumbai',
            city='Mumbai',
            state='Maharashtra'
        )
        self.branch2 = Branch.objects.create(
            bank=self.bank,
            name='Delhi Branch',
            ifsc='TEST0000002',
            address='456 Test Street, Delhi',
            city='Delhi',
            state='Delhi'
        )
    
    def test_branch_list_api(self):
        """Test GET /api/branches/"""
        url = reverse('branch-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_branch_detail_api(self):
        """Test GET /api/branches/{id}/"""
        url = reverse('branch-detail', kwargs={'id': self.branch1.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Mumbai Branch')
        self.assertEqual(response.data['ifsc'], 'TEST0000001')
        self.assertEqual(response.data['bank']['name'], 'Test Bank')
    
    def test_branch_search_by_ifsc(self):
        """Test GET /api/branches/search/?ifsc={code}"""
        url = reverse('branch-search')
        response = self.client.get(url, {'ifsc': 'TEST0000001'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['branch']['name'], 'Mumbai Branch')
        self.assertEqual(response.data['branch']['ifsc'], 'TEST0000001')
    
    def test_branch_search_by_city(self):
        """Test GET /api/branches/search/?city={city}"""
        url = reverse('branch-search')
        response = self.client.get(url, {'city': 'Mumbai'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['branches']), 1)
        self.assertEqual(response.data['branches'][0]['city'], 'Mumbai')
    
    def test_branch_search_no_params(self):
        """Test branch search without parameters."""
        url = reverse('branch-search')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
    
    def test_branch_search_not_found(self):
        """Test branch search with non-existent data."""
        url = reverse('branch-search')
        response = self.client.get(url, {'ifsc': 'NONEXISTENT'})
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('message', response.data)


class APIOverviewTest(TestCase):
    """Test cases for API overview endpoint."""
    
    def setUp(self):
        self.client = APIClient()
    
    def test_api_overview(self):
        """Test GET /api/"""
        url = reverse('api-overview')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Banks', response.data)
        self.assertIn('Branches', response.data)
