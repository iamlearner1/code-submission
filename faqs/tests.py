from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.", language="en")

    def test_translation(self):
        translated_text = self.faq.get_translation("hi")
        self.assertIsInstance(translated_text, str)
