import unittest
from django.test import TestCase
from ipdb import set_trace
from ..serializers import LayoutSerializer, PersonInfoSerializer, \
    UserBioSerializer
from ..models import Person
from utils.factories import PersonFactory, WebLinkFactory, PositionFactory, \
    AddressFactory, EmailFactory

@unittest.skip('passed')
class PersonSerialTestCase(TestCase):
    def setUp(self):
        self.person = PersonFactory()
        self.person.role = 'user'
        self.person.save()
        self.serializer = PersonInfoSerializer(self.person)
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

@unittest.skip('passed')
class LayoutSerializerTestCase(TestCase):
    def setUp(self):
        self.person = PersonFactory()
        self.person.role = 'user'
        self.person.save()
        self.links = WebLinkFactory.create_batch(5, person=self.person)

    def test_item(self):
        serializer = LayoutSerializer(self.person)
        data = serializer.data
        set_trace()
        self.assertIn('first_name', data.keys())
        self.assertIn('weblinks', data.keys())
        self.assertIsInstance(data['weblinks'], list)

class UsrBioSerializerTestCase(TestCase):
    def setUp(self):
        # user
        self.person = PersonFactory()
        self.person.role = 'user'
        self.person.save()

        # position
        self.position = PositionFactory(person=self.person)
        self.position.type = 'primary'
        self.position.save()

        # address
        self.address = AddressFactory(position=self.position)
        # email
        self.email = EmailFactory(person=self.person)
        self.email.type = 'primary'
        self.email.save()
        # weblinks
        self.links = WebLinkFactory.create_batch(5, person=self.person)

    def test_item(self):
        serializer = UserBioSerializer(self.person)
        data = serializer.data
        self.assertIn('first_name', data.keys())
        self.assertIn('email', data.keys())
        self.assertIn('weblinks', data.keys())
        self.assertIsInstance(data['weblinks'], list)
        self.assertIsInstance(data['address'], dict)
        self.assertIn('city', data['address'].keys())
