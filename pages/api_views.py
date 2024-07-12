from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Person
from .serializers import PersonInfoSerializer, PositionSerializer, \
    AddressSerializer, WebLinkSerializer, NewsSerializer, \
    HighlightPublicationSerializer, HighlightProjectSerializer
from ipdb import set_trace

# =====
# home page
class PersonInfoView(APIView):
    def get(self, request):
        # there should be only one user
        person = Person.objects.get(role='user')
        basic_data = PersonInfoSerializer(person).data

        # position and address
        position = person.positions.get(type='primary')
        position_data = PositionSerializer(position).data
        address_data = AddressSerializer(position.address).data

        # weblinks
        weblinks = person.weblinks.all()
        weblink_data = {'weblinks': WebLinkSerializer(weblinks, many=True).data}

        data = basic_data  | position_data | address_data | weblink_data

        return Response(data, status=status.HTTP_200_OK)


class NewsView(APIView):
    def get(self, request):
        person = Person.objects.get(role='user')
        news_items = person.news_items.all()
        data = NewsSerializer(news_items, many=True).data

        return Response(data, status=status.HTTP_200_OK)


class HighlightPublicationView(APIView):
    def get(self, request):
        person = Person.objects.get(role='user')
        publications = person.publications.filter(highlighted=True)

        data = HighlightPublicationSerializer(publications, many=True).data

        return Response(data, status=status.HTTP_200_OK)

class HighlightProjectView(APIView):
    def get(self, request):
        person = Person.objects.get(role='user')
        projects = person.projects.filter(highlighted=True)

        data = HighlightProjectSerializer(projects, many=True).data

        return Response(data, status=status.HTTP_200_OK)

class HighlightTalkView(APIView):
    def get(self, request):
        person = Person.objects.get(role='user')
        talks = person.talks.filter(highlighted=True)

        data = HighlightProjectSerializer(talks, many=True).data

        return Response(data, status=status.HTTP_200_OK)

class AboutView(APIView):
    def get(self, request):
        data = {'message', 'Hello'}
        return Response(data, status=status.HTTP_200_OK)

class PublicationView(APIView):
    def get(self, request):
        data = {'message', 'Hello'}
        return Response(data, status=status.HTTP_200_OK)

class ProjectView(APIView):
    pass

class TalkView(APIView):
    pass

class ContactView(APIView):
    pass

class SubscribeView(APIView):
    pass
