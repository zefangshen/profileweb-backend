import unittest
from django.test import TestCase
from ipdb import set_trace
from ..serializers import PersonHomeSerializer
from ..models import Person
from utils.factories import PersonFactory

@unittest.skip('passed')
class PersonSerialTestCase(TestCase):
    def setUp(self):
        self.person = PersonFactory()
        self.person.role = 'user'
        self.person.save()
        self.serializer = PersonHomeSerializer(self.person)
        self.data = self.serializer.data
    
    def test_contain_fields(self):
        selected_fields = [
            'first_name', 'middle_name', 'last_name', 'photo', 'headline',
            'bio_short', 'copyright_year', 'updated_on'
        ]
        self.assertEqual(
            set(self.data.keys()),
            set(selected_fields)
        )
    
    def test_field_value(self):
        self.assertEqual(
            self.person.first_name, self.data['first_name']
        )
        self.assertEqual(
            set(self.data['updated_on'].keys()),
            set(['year', 'month', 'day'])
        )
