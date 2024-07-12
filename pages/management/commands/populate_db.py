from pathlib import Path
from typing import Any
from ipdb import set_trace
from django.core.management.base import BaseCommand
from utils.factories import PersonFactory, PositionFactory, AddressFactory, \
    EmailFactory, WebLinkFactory, PhoneNumberFactory, NewsFactory, \
    PublicationFactory, ProjectFactory, TalkFactory
from utils.test import fake_image


class Command(BaseCommand):
    help = 'populate the db with Factory boy for development'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        # person
        person = PersonFactory()
        person.role = 'user'
        person.save()

        positions = PositionFactory.create_batch(3, person=person)
        for i, position in enumerate(positions):
            if i == 0:
                # for first position set to primary
                position.type = 'primary'
            else:
                # rest set as other
                position.type = 'other'
            position.save()

            # add address to position
            AddressFactory(position=position)

        emails = EmailFactory.create_batch(3, person=person)
        for i, email in enumerate(emails):
            if i == 0:
                email.type = 'primary'
            else:
                email.type = 'other'
            email.save()

        PhoneNumberFactory.create_batch(3, person=person)

        WebLinkFactory.create_batch(5, person=person)
        NewsFactory.create_batch(20, person=person)
        PublicationFactory.create_batch(20, person=person)
        ProjectFactory.create_batch(10, person=person)
        TalkFactory.create_batch(10, person=person)
    
        self.stdout.write('Database populated')
