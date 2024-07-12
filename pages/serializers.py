from rest_framework import serializers
from .models import Person, Position, Address, Email, WebLink, PhoneNumber, \
    News, Publication, Project, Talk, Subscriber, Query
from utils.helpers import split_date
from ipdb import set_trace

# =====
# general serializers
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['title', 'institution']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['city', 'state', 'province', 'country']

class WebLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebLink
        fields = ['id', 'name', 'url', 'icon']

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

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'date', 'content', 'url']



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



class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'
