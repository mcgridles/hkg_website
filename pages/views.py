from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse

from .models import Author, ExpPost

class WorkView(generic.ListView):
    template_name = 'pages/work.html'
    context_object_name = 'work_list'

    def get_queryset(self):
        """Return all relevant experiences"""
        return ExpPost.objects.filter(
            pub_date__lte=timezone.now()
            ).filter(start_date__lte=timezone.now()
            ).exclude(post_type='project').order_by('-start_date')

class ProjectView(generic.ListView):
    template_name = 'pages/projects.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """Return all relevant projects"""
        return ExpPost.objects.filter(
            pub_date__lte=timezone.now()
            ).filter(start_date__lte=timezone.now()
            ).filter(post_type='project').order_by('-start_date')

class DetailView(generic.DetailView):
    model = ExpPost
    template_name = 'pages/details.html'

def index(request):
    return render(request, 'pages/index.html')

def aboutMe(request):
    author = get_object_or_404(Author, pk=1)
    context = {'author': author}
    return render(request, 'pages/aboutMe.html', context)
