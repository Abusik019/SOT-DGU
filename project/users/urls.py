from django.urls import path
from django.views.generic import TemplateView

from .views import DocumentsList, PresentationView, VideoView, MetodView, ContestView


app_name = 'users'


urlpatterns = [
    path('contacts/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
    path('documents/', DocumentsList.as_view(), name='documents'),
    path('instruct/', TemplateView.as_view(template_name='instruct_mat.html'), name='instruct'),
    path('presentations/', PresentationView.as_view(), name='presentations'),
    path('videomat/', VideoView.as_view(), name='videomat'),
    path('metodmat/', MetodView.as_view(), name='metodmat'),
    path('contests/', ContestView.as_view(), name='contests'),
]
