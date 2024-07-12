from pathlib import Path
import unittest
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from pages.models import Person
from utils.factories import PersonFactory, PositionFactory, AddressFactory, \
    WebLinkFactory, NewsFactory, PublicationFactory, ProjectFactory, \
    TalkFactory
from ipdb import set_trace

# @unittest.skip('passed')
class PersonInfoAPITestCase(APITestCase):
    def setUp(self):
        # populate the database
        # person
        self.person = PersonFactory()
        self.person.role='user'
        self.person.save()

        # position
        self.position = PositionFactory(person=self.person)
        self.position.type = 'primary'
        self.position.save()

        # address
        self.address = AddressFactory(position=self.position)

        # weblinks
        self.weblinks = WebLinkFactory.create_batch(5, person=self.person)


    def test_get(self):
        # fields: first_name, middle_name, last_name,
        # bio_short, copyright_year, updated_on  
        # position {title, institution},
        # address {city, state, country}, photo, headline,
        # weblinks {name, url, icon}
        # related Models: Person, Position, Address, WebLink, 
        ownerinfo_url = reverse('owner-info')
        response = self.client.get(ownerinfo_url)
        data = response.data
        # print(response.data)
        self.assertIn('first_name', data.keys())
        self.assertIn('photo', data.keys())
        self.assertIn('weblinks', data.keys())
        self.assertEqual(len(data['weblinks']), 5)
    
    def tearDown(self):
        if self.person.photo:
            Path(self.person.photo.path).unlink()
    
        for weblink in self.weblinks:
            if weblink.icon:
                Path(weblink.icon.path).unlink()

@unittest.skip('passed')
class NewsAPITestCase(APITestCase):
    def setUp(self):
        self.person = PersonFactory()
        self.person.role='user'
        self.person.save()

        self.news_items = NewsFactory.create_batch(20, person=self.person)

    def test_get(self):
        news_url = reverse('news')
        response = self.client.get(news_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data
        for news in data:
            self.assertIn('date', news.keys())
            self.assertNotEqual(news['content'], '')
            self.assertIn('http', news['url'])
    
    def tearDown(self):
        if self.person.photo:
            Path(self.person.photo.path).unlink()

@unittest.skip('passed')
class HighlightPublicationViewCase(APITestCase):
    def setUp(self):
        self.person = PersonFactory()
        self.person.role='user'
        self.person.save()

        # publications
        self.publications = PublicationFactory.create_batch(
            20, person=self.person
        )

    def test_get(self):
        url = reverse('highlight-publication')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(len(response.data), 20)
        for pub in response.data:
            self.assertIn('id', pub.keys())
            self.assertIn('title', pub.keys())
            self.assertIn('summary', pub.keys())
            self.assertIn('image', pub.keys())
    
    def tearDown(self):
        for pub in self.publications:
            if pub.image:
                Path(pub.image.path).unlink()

@unittest.skip('passed')
class HighlightProjectViewCase(APITestCase):
    def setUp(self):
        self.person = PersonFactory()
        self.person.role='user'
        self.person.save()

        # publications
        self.projects = ProjectFactory.create_batch(
            20, person=self.person
        )

    def test_get(self):
        url = reverse('highlight-project')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(len(response.data), 20)
        for pub in response.data:
            self.assertIn('id', pub.keys())
            self.assertIn('name', pub.keys())
            self.assertIn('summary', pub.keys())
            self.assertIn('image', pub.keys())
    
    def tearDown(self):
        for p in self.projects:
            if p.image:
                Path(p.image.path).unlink()

class HighlightTalkViewCase(APITestCase):
    def setUp(self):
        self.person = PersonFactory()
        self.person.role='user'
        self.person.save()

        # publications
        self.talks = TalkFactory.create_batch(
            20, person=self.person
        )

    def test_get(self):
        url = reverse('highlight-talk')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(len(response.data), 20)
        for t in response.data:
            self.assertIn('id', t.keys())
            self.assertIn('name', t.keys())
            self.assertIn('summary', t.keys())
            self.assertIn('image', t.keys())
    
    def tearDown(self):
        for t in self.talks:
            if t.image:
                Path(t.image.path).unlink()