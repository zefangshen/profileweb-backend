# factories generating test data 
from faker import Faker
from factory import LazyFunction, SubFactory
from factory.django import DjangoModelFactory

from pages.models import Person, Subscriber, Query, Position, Address, Email, \
    WebLink, PhoneNumber, News, Publication, Project, Talk
from utils.test import text_of_length, sample_choice, fake_image, fake_date

fake = Faker()

# factories, they will be used in many
class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person
    
    first_name = LazyFunction(fake.first_name)
    last_name = LazyFunction(fake.last_name)
    role = LazyFunction(sample_choice(Person.ROLE_CHOICES))
    photo = LazyFunction(fake_image(size=(200, 200)))
    headline = LazyFunction(text_of_length(128))
    bio_short = LazyFunction(text_of_length(256))
    bio = LazyFunction(text_of_length(512))
    copyright_date = LazyFunction(fake_date())
    updated_on = LazyFunction(fake_date())

class SubscriberFactory(DjangoModelFactory):
    class Meta:
        model = Subscriber

    email = LazyFunction(fake.email)
    subscribed_on = LazyFunction(fake_date())

class QueryFactory(DjangoModelFactory):
    class Meta:
        model = Query

    name = LazyFunction(fake.name)
    email = LazyFunction(fake.email)
    message = LazyFunction(text_of_length(128))

class PositionFactory(DjangoModelFactory):
    class Meta:
        model = Position
    
    person = SubFactory(PersonFactory)
    title = LazyFunction(fake.job)
    institution = LazyFunction(fake.company)
    type = LazyFunction(sample_choice(Position.POSITION_TYPES))

class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address
    
    position = SubFactory(Position)
    street_address = LazyFunction(fake.street_address)
    city = LazyFunction(fake.city)
    state = LazyFunction(fake.state)
    postcode = LazyFunction(fake.postcode)
    country = LazyFunction(fake.country)

class EmailFactory(DjangoModelFactory):
    class Meta:
        model = Email
    
    person = SubFactory(PersonFactory)
    type = LazyFunction(sample_choice(Email.TYPE_CHOICES))
    institution = LazyFunction(fake.company)
    address = LazyFunction(fake.email)

class WebLinkFactory(DjangoModelFactory):
    class Meta:
        model = WebLink
    
    person = SubFactory(Person)
    name = LazyFunction(fake.last_name)
    url = LazyFunction(fake.url)
    icon = LazyFunction(fake_image(size=(20, 20)))

class PhoneNumberFactory(DjangoModelFactory):
    class Meta:
        model = PhoneNumber
    
    person = SubFactory(Person)
    number = LazyFunction(fake.phone_number)
    type = LazyFunction(sample_choice(PhoneNumber.TYPE_CHOICES))

class NewsFactory(DjangoModelFactory):
    class Meta:
        model = News
    
    person = SubFactory(Person)
    date = LazyFunction(fake_date())
    content = LazyFunction(text_of_length(200))
    url = LazyFunction(fake.url)

class PublicationFactory(DjangoModelFactory):
    class Meta:
        model = Publication
    
    person = SubFactory(PersonFactory)
    title = LazyFunction(text_of_length(100))
    authors = LazyFunction(fake.name)
    summary = LazyFunction(text_of_length(100))
    abstract = LazyFunction(text_of_length(256))
    doi = LazyFunction(fake.url)
    url = LazyFunction(fake.url)
    image = LazyFunction(fake_image(size=(400, 400)))
    date = LazyFunction(fake_date())
    type = LazyFunction(sample_choice(Publication.TYPE_CHOICES))
    publisher = LazyFunction(fake.company)
    featured = LazyFunction(fake.boolean)
    highlighted = LazyFunction(fake.boolean)

class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project

    person = SubFactory(Person)
    name = LazyFunction(fake.company)
    summary = LazyFunction(text_of_length(50))
    description = LazyFunction(text_of_length(100))
    image = LazyFunction(fake_image(size=(200, 200)))
    start_date = LazyFunction(fake_date())
    end_date = LazyFunction(fake_date())
    role = LazyFunction(fake.job)
    status = LazyFunction(sample_choice(Project.STATUS_CHOICES))
    url = LazyFunction(fake.url)
    featured = LazyFunction(fake.boolean)
    highlighted = LazyFunction(fake.boolean)

class TalkFactory(DjangoModelFactory):
    class Meta:
        model = Talk
    
    person = SubFactory(PersonFactory)
    title = LazyFunction(text_of_length(100))
    image = LazyFunction(fake_image(size=(200, 200)))
    summary = LazyFunction(text_of_length(300))
    description = LazyFunction(text_of_length(300))
    date = LazyFunction(fake_date())
    venue = LazyFunction(fake.address)
    type = LazyFunction(sample_choice(Talk.TYPE_CHOICES))
    status = LazyFunction(sample_choice(Talk.STATUS_CHOICES))
    url = LazyFunction(fake.url)
    featured = LazyFunction(fake.boolean)
    highlighted = LazyFunction(fake.boolean)