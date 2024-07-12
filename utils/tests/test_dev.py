import unittest
import datetime
from django.test import TestCase
from pages.models import Person
from utils.test import sample_choice, fake_image, fake_date
from ipdb import set_trace
import types

@unittest.skip('passed')
class SampleChoiceTestCase(TestCase):
    def setUp(self):
        self.choices = Person.ROLE_CHOICES
    
    def test_sample_choice(self):
        all_choices = [x[0] for x in self.choices]
        set_trace()
        self.assertIn(sample_choice(self.choices)(), all_choices)

@unittest.skip('passed')
class FakeImageTestCase(TestCase):
    def test_fake_image(self):
        image_fn = fake_image(name="image.png")
        self.assertIsInstance(image_fn, types.FunctionType)
        self.assertEqual(image_fn().name , 'image.png')

@unittest.skip('passed')
class FakeDateTestCase(TestCase):
    def test_fake_date(self):
        date_fn = fake_date()
        self.assertIsInstance(date_fn, types.FunctionType)
        self.assertIsInstance(date_fn(), datetime.date)
