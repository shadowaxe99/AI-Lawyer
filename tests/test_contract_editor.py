
import unittest
from src.contract_editor import ContractEditor

class TestContractEditor(unittest.TestCase):

    def setUp(self):
        self.editor = ContractEditor()

    def test_edit_contract(self):
        original_contract = "This contract is between X and Y."
        edited_contract = self.editor.edit_contract(original_contract, 'X', 'Z')
        self.assertEqual(edited_contract, "This contract is between Z and Y.")

    def test_undo_edit(self):
        original_contract = "This contract is between X and Y."
        edited_contract = self.editor.edit_contract(original_contract, 'X', 'Z')
        reverted_contract = self.editor.undo_edit()
        self.assertEqual(reverted_contract, original_contract)

if __name__ == '__main__':
    unittest.main()

