from django.test import TestCase
from banks.models import Bank, Branch


class BankModelTest(TestCase):
    """Test cases for Bank model."""
    
    def setUp(self):
        self.bank = Bank.objects.create(
            id=1,
            name='Test Bank'
        )
    
    def test_bank_creation(self):
        """Test bank creation."""
        self.assertEqual(self.bank.name, 'Test Bank')
        self.assertEqual(self.bank.id, 1)
        self.assertTrue(self.bank.created_at)
        self.assertTrue(self.bank.updated_at)
    
    def test_bank_str_method(self):
        """Test bank string representation."""
        self.assertEqual(str(self.bank), 'Test Bank')


class BranchModelTest(TestCase):
    """Test cases for Branch model."""
    
    def setUp(self):
        self.bank = Bank.objects.create(
            id=1,
            name='Test Bank'
        )
        self.branch = Branch.objects.create(
            ifsc='TEST0000001',
            bank=self.bank,
            branch='Test Branch',
            address='123 Test Street',
            city='Test City',
            district='Test District',
            state='Test State'
        )
    
    def test_branch_creation(self):
        """Test branch creation."""
        self.assertEqual(self.branch.branch, 'Test Branch')
        self.assertEqual(self.branch.ifsc, 'TEST0000001')
        self.assertEqual(self.branch.bank, self.bank)
        self.assertEqual(self.branch.district, 'Test District')
        self.assertTrue(self.branch.created_at)
        self.assertTrue(self.branch.updated_at)
    
    def test_branch_str_method(self):
        """Test branch string representation."""
        self.assertEqual(str(self.branch), 'Test Branch - Test Bank')
    
    def test_branch_unique_ifsc(self):
        """Test branch IFSC uniqueness."""
        with self.assertRaises(Exception):
            Branch.objects.create(
                ifsc='TEST0000001',
                bank=self.bank,
                branch='Another Branch',
                address='456 Another Street',
                city='Another City',
                district='Another District',
                state='Another State'
            )
    
    def test_bank_branch_relationship(self):
        """Test bank-branch relationship."""
        self.assertEqual(self.bank.branches.count(), 1)
        self.assertEqual(self.bank.branches.first(), self.branch)
