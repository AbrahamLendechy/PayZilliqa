# test_payzilliqawallet.py
"""
Tests for PayZilliqaWallet module.
"""

import unittest
from payzilliqawallet import PayZilliqaWallet

class TestPayZilliqaWallet(unittest.TestCase):
    """Test cases for PayZilliqaWallet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PayZilliqaWallet()
        self.assertIsInstance(instance, PayZilliqaWallet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PayZilliqaWallet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
