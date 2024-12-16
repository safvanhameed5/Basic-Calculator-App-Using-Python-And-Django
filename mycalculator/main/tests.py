from django.test import TestCase
from django.urls import reverse
from .forms import HomeForm

class CalculatorViewTest(TestCase):
    def test_addition(self):
        """Test addition operation."""
        response = self.client.post(reverse('homepage'), {
            'number1': 10, 'number2': 5, 'number3': 3, 'number4': 2,
            'add': 'Add'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Result :')
        self.assertIn('result', response.context)
        self.assertEqual(response.context['result'], 20)

    def test_subtraction(self):
        """Test subtraction operation."""
        response = self.client.post(reverse('homepage'), {
            'number1': 20, 'number2': 5, 'number3': 3, 'number4': 2,
            'sub': 'Subtract'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Result :')
        self.assertIn('result', response.context)
        self.assertEqual(response.context['result'], 10)

    def test_multiplication(self):
        """Test multiplication operation."""
        response = self.client.post(reverse('homepage'), {
            'number1': 2, 'number2': 3, 'number3': 4, 'number4': 5,
            'mul': 'Multiply'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Result :')
        self.assertIn('result', response.context)
        self.assertEqual(response.context['result'], 120)

    def test_division(self):
        """Test division operation."""
        response = self.client.post(reverse('homepage'), {
            'number1': 100, 'number2': 2, 'number3': 5, 'number4': 2,
            'div': 'Divide'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Result :')
        self.assertIn('result', response.context)
        self.assertEqual(response.context['result'], 5.0)

class CalculatorFormTest(TestCase):
    def test_valid_form(self):
        """Test form validation with valid data."""
        form = HomeForm(data={'number1': 10, 'number2': 20, 'number3': 30, 'number4': 40})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test form validation with invalid data."""
        form = HomeForm(data={'number1': 'invalid', 'number2': 'invalid'})
        self.assertFalse(form.is_valid())
