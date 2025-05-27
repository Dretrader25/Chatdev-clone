import unittest
from unittest import mock
import markdown2

# Adjust imports based on your project structure
# Assuming agent files are in the root directory for now
from pm import PMAgent
from architect import ArchitectAgent
from frontend import FrontendAgent

class TestFormatting(unittest.TestCase):

    @mock.patch('google.generativeai.GenerativeModel')
    def test_pm_agent_formatting(self, MockGenerativeModel):
        # Configure the mock
        mock_model_instance = MockGenerativeModel.return_value
        mock_response = mock.Mock()
        markdown_text = "# Test Header\n*italic text*\n**bold text**\n- Item 1\n- Item 2"
        mock_response.text = markdown_text
        mock_model_instance.generate_content.return_value = mock_response

        # Call the agent
        state = {"input": "Test input for PM"}
        result = PMAgent(state)

        # Assertions
        expected_html = markdown2.markdown(markdown_text)
        self.assertEqual(result["pm_output"], expected_html)
        self.assertEqual(result["input"], expected_html) # PMAgent also modifies 'input'

    @mock.patch('google.generativeai.GenerativeModel')
    def test_architect_agent_formatting(self, MockGenerativeModel):
        # Configure the mock
        mock_model_instance = MockGenerativeModel.return_value
        mock_response = mock.Mock()
        markdown_text = "## Architect Plan\n> Blockquote\n`inline code`"
        mock_response.text = markdown_text
        mock_model_instance.generate_content.return_value = mock_response

        # Call the agent
        state = {"input": "Test input for Architect"}
        result = ArchitectAgent(state)

        # Assertions
        expected_html = markdown2.markdown(markdown_text)
        self.assertEqual(result["architect_output"], expected_html)
        self.assertEqual(result["input"], expected_html) # ArchitectAgent also modifies 'input'

    @mock.patch('google.generativeai.GenerativeModel')
    def test_frontend_agent_formatting(self, MockGenerativeModel):
        # Configure the mock
        mock_model_instance = MockGenerativeModel.return_value
        mock_response = mock.Mock()
        markdown_text = "### Frontend Details\n* List item 1\n* List item 2\n\n```python\nprint('Hello')\n```"
        mock_response.text = markdown_text
        mock_model_instance.generate_content.return_value = mock_response

        # Call the agent
        state = {"input": "Test input for Frontend"}
        result = FrontendAgent(state)

        # Assertions
        expected_html = markdown2.markdown(markdown_text)
        self.assertEqual(result["frontend_output"], expected_html)

if __name__ == '__main__':
    unittest.main()
