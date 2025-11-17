import unittest
# The model module is imported from the 'src' directory
from src.model import load_model, get_response
import torch

class TestModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # load_model returns only (model, tokenizer).
        # We determine the device from the loaded model.
        cls.model, cls.tokenizer = load_model()
        cls.device = cls.model.device

    def test_factual_query(self):
        prompt = "What is the capital of France?"
        # Corrected call: get_response does not need the device as an explicit argument.
        resp = get_response(prompt, self.model, self.tokenizer, max_length=50)
        
        # Test: Check if the response contains the expected answer (Paris)
        self.assertIn("paris", resp.lower(), "The model failed to identify the capital of France.")

    def test_code_generation(self):
        prompt = "Write a Python function to calculate the factorial of a number."
        # Corrected call: get_response does not need the device as an explicit argument.
        resp = get_response(prompt, self.model, self.tokenizer, max_length=200)
        
        # Test: Check for key elements of a Python function definition
        self.assertIn("def", resp, "Response did not contain function definition keyword 'def'.")
        self.assertIn("factorial", resp, "Response did not contain the function name 'factorial'.")
        
        # Test: Check for logic keywords (for, while, or return)
        self.assertTrue(
            any(keyword in resp for keyword in ["for", "while", "return"]),
            "Response did not contain logic keywords (for, while, or return)."
        )

if __name__ == '__main__':
    unittest.main()