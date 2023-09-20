
import unittest
from src.contract_generator import ContractGenerator

class TestContractGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = ContractGenerator()

    def test_generate_contract(self):
        contract = self.generator.generate_contract()
        self.assertIsNotNone(contract)

    def test_generate_contract_length(self):
        contract = self.generator.generate_contract()
        self.assertGreater(len(contract), 0)

if __name__ == '__main__':
    unittest.main()
