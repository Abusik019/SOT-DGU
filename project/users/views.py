from django.views.generic import ListView

from .models import Documents, Presentation, Video, Metodics, Contest


class DocumentsList(ListView):
    queryset = Documents.objects.all()
    template_name = 'documents.html'
    context_object_name = 'documents'


class PresentationView(ListView):
    queryset = Presentation.objects.all()
    template_name = 'presentations.html'
    context_object_name = 'presentations'


class MetodView(ListView):
    queryset = Metodics.objects.all()
    template_name = 'metodmat.html'
    context_object_name = 'metods'


class VideoView(ListView):
    queryset = Video.objects.all()
    template_name = 'videomat.html'
    context_object_name = 'videos'


class ContestView(ListView):
    queryset = Contest.objects.all()
    template_name = 'contests.html'
    context_object_name = 'contests'

