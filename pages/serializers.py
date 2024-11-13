from rest_framework import serializers
from .models import Person, Position, Address, Email, WebLink, PhoneNumber, \
    News, Publication, Project, Talk, Subscriber, Query
from utils.helpers import split_date
from ipdb import set_trace


# =====
# general serializers
class WebLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebLink
        fields = ['id', 'name', 'url', 'icon']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['city', 'state', 'province', 'country']

class LayoutSerializer(serializers.ModelSerializer):
    weblinks = WebLinkSerializer(many=True, read_only=True)
    copyright_year = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = [
            'first_name', 'middle_name', 'last_name', 'copyright_year',
            'updated_on', 'weblinks'
        ]

    def get_copyright_year(self, instance):
        return instance.copyright_date.year

    def get_updated_on(self, instance):
        return {
            'year': instance.updated_on.year,
            'month': instance.updated_on.month,
            'day': instance.updated_on.day,
        }

class UserBioSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    institution = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    weblinks = WebLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = [
            'photo', 'first_name', 'middle_name', 'last_name', 'position',
            'institution', 'address', 'email', 'weblinks', 'bio_short'
        ]

    def get_position(self, instance):
        position = instance.positions.get(type='primary') 
        return position.title

    def get_institution(self, instance):
        position = instance.positions.get(type='primary') 
        return position.institution

    def get_address(self, instance):
        position = instance.positions.get(type='primary') 
        address = AddressSerializer(position.address)
        fields = ['city', 'state', 'province', 'country']
        return {key: address.data[key] for key in fields }
    
    def get_email(self, instance):
        email = instance.emails.get(type='primary')
        return email.address

class NewsSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = ['id', 'date', 'content', 'url']

    def get_date(self, instance):
        year = str(instance.date.year)[-2:]
        month = str(instance.date.month)
        month = '0' +  month if len(month) == 1 else month
        day = str(instance.date.day)
        day = '0' + day if len(day) == 1 else day
        return {'year': year, 'month': month,'day': day}

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['email']

# ==============================================================================
# separation line

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['title', 'institution']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['city', 'state', 'province', 'country']


class HighlightPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'title', 'summary', 'image']

class HighlightProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'summary', 'image']

class HighlightTalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ['id', 'title', 'summary', 'image']

# =====
# page specific serializers


# Home page serializers
class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'first_name', 'middle_name', 'last_name', 'photo', 'headline',
            'bio_short', 'copyright_year', 'updated_on'
        ]

    copyright_year = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_copyright_year(self, instance):
        return instance.copyright_date.year

    def get_updated_on(self, instance):
        return {
            'year': instance.updated_on.year,
            'month': instance.updated_on.month,
            'day': instance.updated_on.day,
        }



# =====
# about page serializers

# =====
# publication page serializers

# =====
# project page serializers

# =====
# talk page serializers

# =====
# other serializers






class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'



class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'




class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'
