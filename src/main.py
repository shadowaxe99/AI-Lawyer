
import tensorflow as tf
from contract_generator import ContractGenerator
from contract_editor import ContractEditor

def main():
    # Load the trained model
    model = tf.keras.models.load_model('../models/contract_model.h5')

    # Initialize the contract generator and editor
    contract_generator = ContractGenerator(model)
    contract_editor = ContractEditor(model)

    # Generate a new contract
    new_contract = contract_generator.generate_contract()

    # Edit the contract
    edited_contract = contract_editor.edit_contract(new_contract)

    # Print the edited contract
    print(edited_contract)

if __name__ == "__main__":
    main()
