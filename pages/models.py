from pathlib import Path
from django.db import models
# from utils.helpers import FileCleanupMixin
# from django.db.models.signals import post_delete, pre_save
# from django.dispatch import receiver
from ipdb import set_trace

# Create your models here.

class Person(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('example', 'Example')
    ]

    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(blank=True, max_length=32)
    last_name = models.CharField(max_length=32)
    role = models.CharField(default='user', max_length=16, choices=ROLE_CHOICES)
    photo = models.ImageField(upload_to='person/')
    headline = models.TextField(blank=True, max_length=256)
    bio_short = models.TextField(max_length=1204)
    bio = models.TextField(max_length=1204)
    copyright_date = models.DateField()
    updated_on = models.DateField()

    # related fields
    # positions < Position
    # emails < Email
    # weblinks < WebLink
    # phone_numbers < PhoneNumber
    # news_items < News
    # publications < Publication 
    # project < Project
    # talks < Talk

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Position(models.Model):
    # Person < Position

    POSITION_TYPES = [
        ('primary', 'Primary'),
        ('fulltime', 'Fulltime'),
        ('part-time', 'Part time'),
        ('voluntary', 'Voluntary'),
        ('self-employed', 'Self-employed'),
        ('other', 'Other'),
    ]

    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="positions")
    title = models.CharField(max_length=32)
    institution = models.CharField(max_length=32)
    type = models.CharField(default='primary', choices=POSITION_TYPES, max_length=64)

    # relational fields
    # address < Address

class Address(models.Model):
    position = models.OneToOneField(Position, on_delete=models.CASCADE, related_name="address") 
    street_address = models.CharField(max_length=128)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=16)
    province = models.CharField(max_length=32)
    postcode = models.CharField(max_length=8)
    country = models.CharField(max_length=32)

class Email(models.Model):
    TYPE_CHOICES = [
        ('primary', 'Primary'),
        ('other', 'Other'),
    ]

    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="emails")
    type = models.CharField(choices=TYPE_CHOICES, max_length=16)
    institution = models.CharField(max_length=64)
    address = models.EmailField(max_length=128)

class WebLink(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="weblinks")
    name = models.CharField(max_length=32)
    url = models.URLField(max_length=256)
    icon = models.ImageField(upload_to='icons/')

class PhoneNumber(models.Model):
    TYPE_CHOICES = [
        ('office', 'Office Phone'),
        ('mobile', 'Mobile'),
    ]
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="phone_numbers")
    number = models.CharField(max_length=32)
    type = models.CharField(default='office', choices=TYPE_CHOICES, max_length=8)

class News(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="news_items")
    date = models.DateField()
    content = models.TextField(max_length=512) 
    url = models.URLField(max_length=128)


class Publication(models.Model):
    TYPE_CHOICES = [
        ('preprint', 'Preprint'),
        ('journal', 'Journal'),
        ('conference', 'Conference'),
        ('report', 'Report'),
        ('other', 'Other')
    ]
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="publications")
    title = models.TextField(max_length=512)
    authors = models.TextField(max_length=512)
    summary = models.TextField(max_length=512)
    abstract = models.TextField(max_length=1024)
    doi = models.URLField(max_length=128)
    url = models.URLField(max_length=128)
    image = models.ImageField(upload_to='publications')
    date = models.DateField()
    type = models.CharField(default='preprint', choices=TYPE_CHOICES, max_length=16)
    publisher = models.CharField(max_length=64)
    featured = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)

class Project(models.Model):    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('lts', 'Long-term support'),
        ('deprecated', 'Deprecated'),
    ]
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=64)
    summary = models.TextField(blank=True, max_length=512)
    description = models.TextField(max_length=1024)
    image = models.ImageField(upload_to='projects/')
    start_date = models.DateField()
    end_date = models.DateField()
    role = models.CharField(max_length=16)
    status = models.CharField(default='active', choices=STATUS_CHOICES, max_length=16)
    url = models.URLField()
    featured = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)

class Talk(models.Model):
    TYPE_CHOICES = [
        ('keynote', 'Keynote'),
        ('conference', 'Conference'),
        ('poster', 'Poster'),
        ('public', 'Public'),
    ]
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
    ]
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="talks")
    title = models.TextField(max_length=128)
    summary = models.TextField(max_length=512)
    description = models.TextField(max_length=1024)
    image = models.ImageField(upload_to='talks/')
    date = models.DateField()
    venue = models.CharField(max_length=128)
    type = models.CharField(default='conference', choices=TYPE_CHOICES, max_length=16)
    status = models.CharField(default='completed', choices=TYPE_CHOICES, max_length=16)
    url = models.URLField()
    featured = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)

class Subscriber(models.Model):
    email = models.EmailField(max_length=128)
    subscribed_on = models.DateField()

class Query(models.Model):
    OCCUPATION_CHOICES = [
        ('researcher', 'Researcher'),
        ('developer', 'Developer'),
        ('student', 'Student'),
        ('other', 'Please specify'),
    ]
    TYPE_CHOICES = [
        ('collaboration', 'Seek collaboration'),
        ('interest', 'Interested in my work'),
        ('consultancy', 'Consultation in AI application or research'),
        ('other', 'Please specify'),
    ]

    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    occupation = models.CharField(default='researcher', choices=OCCUPATION_CHOICES, max_length=32)
    occupation_other = models.CharField(blank=True, max_length=32)
    type = models.CharField(default='collaboration', choices=TYPE_CHOICES, max_length=32)
    type_other = models.CharField(blank=True, max_length=32)
    message = models.TextField(max_length=512)

# =====
# automated file delete or change management
"""
@receiver(post_delete)
def delete_file_on_delete(sender, instance, **kwargs):
    # delete file when instance is deleted
    if isinstance(instance, FileCleanupMixin):
        instance.delete_attached_files()

@receiver(pre_save)
def delete_file_on_change(sender, instance, **kwargs):
    # remove old file when a new file is attached.
    set_trace()
    if instance(instance, FileCleanupMixin):
        # sender keeps the original instance
        # instance is the current
        try:
            old_instance = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            return
        
        for field in instance._meta.fields:
            if isinstance(field, models.FileField):
                old_file = getattr(old_instance, field.name)
                new_file = getattr(instance, field.name)
                if old_file and old_file != new_file:
                    Path(old_file.path).unlink()
"""