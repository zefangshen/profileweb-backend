from django.urls import path
from .api_views import PersonInfoView, NewsView, HighlightPublicationView, \
    HighlightProjectView, HighlightTalkView

urlpatterns = [
    path('owner-info/', PersonInfoView.as_view(), name='owner-info'),
    path('news/', NewsView.as_view(), name='news'),
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
