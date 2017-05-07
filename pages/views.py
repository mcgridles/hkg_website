from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

from .models import Author, ExpPost, Journal
from pages.forms import ContactForm

class WorkView(generic.ListView):
    template_name = 'pages/work.html'
    context_object_name = 'work_list'

    def get_queryset(self):
        """Return all relevant experiences"""
        return ExpPost.objects.filter(
            pub_date__lte=timezone.now()
            ).filter(start_date__lte=timezone.now()
            ).filter(post_type='work').order_by('-start_date')

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
    journals = Journal.objects.filter(
                pub_date__lte=timezone.now()
                ).order_by('-pub_date')[:5]
    context = {'journals': journals}
    return render(request, 'pages/index.html', context)

def homepage(request):
    author = get_object_or_404(Author, pk=1)
    context = {'author': author}
    return render(request, 'pages/homepage.html', context)

def contact_submit(request):
    context = {}
    return render(request, 'pages/contact_submit.html', context)

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('pages/contact_template.txt')
            context = {'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremai@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact_submit')

    return render(request, 'pages/contact.html', {'form': form_class})
