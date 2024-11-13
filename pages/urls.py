from django.urls import path
from .api_views import LayoutView, UserBioView, PersonInfoView, NewsView, \
    SubscriberView, HighlightPublicationView, HighlightProjectView, HighlightTalkView

urlpatterns = [
    path('layout/', LayoutView.as_view(), name='layout'),
    path('user-bio/', UserBioView.as_view(), name='user-bio'),
    path('news/', NewsView.as_view(), name='news'),
    path('subscribe/', SubscriberView.as_view(), name='subscribe'),
    path('owner-info/', PersonInfoView.as_view(), name='owner-info'),
    path(
        'highlight-publication/', HighlightPublicationView.as_view(),
        name='highlight-publication'
    ),
    path(
        'highlight-project/', HighlightProjectView.as_view(),
        name='highlight-project'
    ),
    path(
        'highlight-talk/', HighlightProjectView.as_view(),
        name='highlight-talk'
    ),
]
