from pathlib import Path
import datetime

from ipdb import set_trace
import unittest
from factory import LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from web.settings import BASE_DIR, MEDIA_ROOT
from pages.models import Person, Subscriber, Query, Position, Address, Email, \
    WebLink, PhoneNumber, News, Publication, Project, Talk
from utils.test import text_of_length, sample_choice, fake_image, fake_date
from utils.factories import PersonFactory, SubscriberFactory, QueryFactory, \
    PositionFactory, AddressFactory, EmailFactory, WebLinkFactory, \
    PhoneNumberFactory, NewsFactory, PublicationFactory, ProjectFactory, \
    TalkFactory

# instance to create fake data

# ==============================================================================
# independent models


@unittest.skip('passed')
class PersonTestCase(TestCase):
    def setUp(self):
        self.person = PersonFactory()

    def test_creation(self):
        self.assertNotEqual(self.person.first_name, '')
        self.assertIsInstance(self.person.copyright_date, datetime.date)
        self.assertTrue((MEDIA_ROOT / self.person.photo.name).exists())
        self.assertGreaterEqual(self.person.copyright_date.month, 1)
        self.assertLessEqual(self.person.copyright_date.month, 12)
    
    def tearDown(self):
        for instance in Person.objects.all():
            if instance.photo:
                Path(instance.photo.path).unlink()

@unittest.skip('passed')
class SubscriberTestCase(TestCase):
    def setUp(self):
        self.sub = SubscriberFactory()
    
    def test_creation(self):
        self.assertIn("@", self.sub.email)
        self.assertIsInstance(self.sub.subscribed_on, datetime.date)

@unittest.skip('passed')
class QueryTestCase(TestCase):
    def setUp(self):
        self.query = QueryFactory()
    
    def test_creation(self):
        self.assertNotEqual(self.query.name, "")
        self.assertIn("@", self.query.email)
        self.assertIn(".com", self.query.email)

# ==============================================================================
# relational models

@unittest.skip('passed')
class PersonPositionTestCase(TestCase): 
    def setUp(self):
        self.person = PersonFactory()
        self.positions = PositionFactory.create_batch(3, person=self.person)
    
    def test_position_creation(self):
        position = self.positions[0]
        position_types = [x[0] for x in Position.POSITION_TYPES]
        self.assertNotEqual(position.title, '')
        self.assertIn(position.type, position_types)
        self.assertNotEqual(position.institution, '')

    def test_person_position(self):
        self.assertEqual(self.person.positions.count(), 3)
        for position in self.positions:
            self.assertIn(position, self.person.positions.all())

    def tearDown(self):
        for instance in Person.objects.all():
            if instance.photo:
                Path(instance.photo.path).unlink()

@unittest.skip('passed')
class PersonPositionAddressTestCase(TestCase): 
    def setUp(self):
        self.person = PersonFactory()
        self.position = PositionFactory(person=self.person)
        self.address = AddressFactory(position=self.position)
        # self.addresses = AddressFactory.create_batch(3, position=self.position)
    
    def test_address_creation(self):
        self.assertNotEqual(self.address.street_address, '')
        self.assertNotEqual(self.address.country, '')

    def test_person_position_address(self):
        self.assertEqual(self.person.positions.count(), 1)
        self.assertIsInstance(
            self.address.position.person, Person
        )

    def tearDown(self):
        for instance in Person.objects.all():
            if instance.photo:
                Path(instance.photo.path).unlink()

@unittest.skip('passed')
class EmailTestCase(TestCase): 
    def setUp(self):
        self.person = PersonFactory()
        self.emails = EmailFactory.create_batch(3, person=self.person)
    
    def test_email_creation(self):
        email = self.emails[0]
        self.assertNotEqual(email.address, '')
        self.assertIn('@', email.address)

    def test_person_position(self):
        self.assertEqual(self.person.emails.count(), 3)
        for email in self.emails:
            self.assertIn(email, self.person.emails.all())

@unittest.skip('passed')
class PersonWebLinkTestCase(TestCase): 
    def setUp(self):
        self.person = PersonFactory()
        self.weblinks = WebLinkFactory.create_batch(3, person=self.person)
    
    def test_weblink_creation(self):
        for weblink in self.weblinks:
            self.assertNotEqual(weblink.name, '')
            self.assertIn('http', weblink.url)
            self.assertTrue(
                Path(
                    MEDIA_ROOT/weblink.icon.name
                ).exists()
            )

    def test_person_weblink_relationship(self):
        self.assertEqual(self.person.weblinks.count(), 3)
        for weblink in self.weblinks:
            self.assertIn(weblink, self.person.weblinks.all())

    def tearDown(self):
        # remove person photos
        for instance in Person.objects.all():
            if instance.photo:
                Path(instance.photo.path).unlink()
    
        # remove web icons
        for instance in WebLink.objects.all():
            if instance.icon:
                Path(instance.icon.path).unlink() 

@unittest.skip('passed')
class PersonPhoneNumberTestCase(TestCase): 
    def setUp(self):
        self.person = PersonFactory()
        self.numbers = PhoneNumberFactory.create_batch(3, person=self.person)
    
    def test_phone_number_creation(self):
        choices = [x[0] for x in PhoneNumber.TYPE_CHOICES]
        for number in self.numbers:
            self.assertNotEqual(number.number, '')
            self.assertIn(number.type, choices)

    def test_person_phone_number_relationship(self):
        self.assertEqual(self.person.phone_numbers.count(), 3)
        for number in self.numbers:
            self.assertIn(number, self.person.phone_numbers.all())

    def tearDown(self):
        # remove person photos
        for instance in Person.objects.all():
            if instance.photo:
                Path(instance.photo.path).unlink()

@unittest.skip('passed')
class PersonNewsTestCase(TestCase): 
    def setUp(self):
        self.person = PersonFactory()
        self.news_items = NewsFactory.create_batch(3, person=self.person)
    
    def test_news_creation(self):
        for news in self.news_items:
            self.assertGreaterEqual(news.date.year, 1900)
            self.assertLessEqual(news.date.year, 2024)
            self.assertNotEqual(news.content, '')
            self.assertIn('http', news.url)

    def test_person_news_relationship(self):
        self.assertEqual(self.person.news_items.count(), 3)
        for news in self.news_items:
            self.assertIn(news, self.person.news_items.all())

    def tearDown(self):
        for instance in Person.objects.all():
            if instance.photo:
                Path(instance.photo.path).unlink()

@unittest.skip('passed')
class PersonPublicationTestCase(TestCase): 
    def setUp(self):
        self.person = PersonFactory()
        self.publications = PublicationFactory.create_batch(10, person=self.person)
    
    def test_publication_creation(self):
        for publication in self.publications:
            self.assertNotEqual(publication.title, '')
            self.assertNotEqual(publication.authors, '')
            self.assertNotEqual(publication.summary, '')
            self.assertNotEqual(publication.abstract, '')
            self.assertIn('http', publication.doi)
            self.assertIn('http', publication.url)
            self.assertTrue((MEDIA_ROOT/publication.image.name).exists())
            self.assertIsInstance(publication.featured, bool)
            self.assertIsInstance(publication.highlighted, bool)

    def test_person_publication(self):
        self.assertEqual(self.person.publications.count(), 10)
        for publication in self.publications:
            self.assertIn(publication, self.person.publications.all())

    def tearDown(self):
        for instance in Person.objects.all():
            if instance.photo:
                Path(instance.photo.path).unlink()

        for instance in Publication.objects.all():
            if instance.image:
                Path(instance.image.path).unlink()

@unittest.skip('passed')
class PersonProjectTestCase(TestCase): 
    def setUp(self):
        self.person = PersonFactory()
        self.projects = ProjectFactory.create_batch(5, person=self.person)
    
    def test_project_creation(self):
        statuses = [x[0] for x in Project.STATUS_CHOICES]
        for project in self.projects:
            self.assertNotEqual(project.name, '')
            self.assertNotEqual(project.description, '')
            self.assertTrue((MEDIA_ROOT/project.image.name).exists())
            self.assertLessEqual(project.start_date.year, 2024)
            self.assertNotEqual(project.role, '')
            self.assertIn(project.status, statuses)
            self.assertIn('http', project.url)
            self.assertIsInstance(project.featured, bool)
            self.assertIsInstance(project.highlighted, bool)

    def test_person_project(self):
        self.assertEqual(self.person.projects.count(), 5)
        for project in self.projects:
            self.assertIn(project, self.person.projects.all())

    def tearDown(self):
        for instance in Person.objects.all():
            if instance.photo:
                Path(instance.photo.path).unlink()

        for instance in Project.objects.all():
            if instance.image:
                Path(instance.image.path).unlink()

@unittest.skip('passed')
class PersonTalkTestCase(TestCase): 
    def setUp(self):
        self.person = PersonFactory()
        self.talks = TalkFactory.create_batch(5, person=self.person)
    
    def test_talk_creation(self):
        type_choices = [x[0] for x in Talk.TYPE_CHOICES]
        status_choices = [x[0] for x in Talk.STATUS_CHOICES]
        for talk in self.talks:
            self.assertNotEqual(talk.title, '')
            self.assertTrue((MEDIA_ROOT/talk.image.name).exists())
            self.assertNotEqual(talk.summary, '')
            self.assertNotEqual(talk.description, '')
            self.assertLessEqual(talk.date.year, 2024)
            self.assertNotEqual(talk.venue, '')
            self.assertIn(talk.type, type_choices)
            self.assertIn(talk.status, status_choices)
            self.assertIsInstance(talk.featured, bool)
            self.assertIsInstance(talk.highlighted, bool)

    def test_person_talk(self):
        self.assertEqual(self.person.talks.count(), 5)
        for talk in self.talks:
            self.assertIn(talk, self.person.talks.all())

    def tearDown(self):
        for instance in Person.objects.all():
            if instance.photo:
                Path(instance.photo.path).unlink()
        
        for instance in Talk.objects.all():
            if instance.image:
                Path(instance.image.path).unlink()

# =====
# test file auto delete and change: django-cleanup
@unittest.skip('pass')
class FileFieldManageTestCase():
    def setUp(self):
        self.person = PersonFactory()

    def test_change(self):
        old_img_path = Path(self.person.photo.path)
        self.person.photo = fake_image(size=(50, 50))
        self.person.save()
        new_img_path = Path(self.person.photo.path)

        self.assertNotEqual(old_img_path, new_img_path)
        self.assertFalse(old_img_path.exists())
        self.assertTrue(new_img_path.exists())

    def test_delete(self):
        img_path = Path(self.person.photo.path)
        self.person.delete()
        self.assertFalse(img_path.exists())

