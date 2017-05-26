from __future__ import unicode_literals

import os
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect

from pages.models import Author, ExpPost, Journal
from pages.forms import ContactForm

class ListView(generic.ListView):
    template_name = 'pages/work.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return all relevant experiences"""
        return ExpPost.objects.filter(
            pub_date__lte=timezone.now()
            ).filter(start_date__lte=timezone.now()
            ).order_by('-start_date')

class DetailView(generic.DetailView):
    model = ExpPost
    template_name = 'pages/details.html'

def homepage(request):
    author = get_object_or_404(Author)
    context = {'author': author}
    return render(request, 'pages/homepage.html', context)

@sensitive_post_parameters('contact_email')
@csrf_protect
def contact(request):
    form = ContactForm

    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_subject = form.cleaned_data['subject']
            form_content = form.cleaned_data['content']

            # Email the profile with the
            # contact information
            template = get_template('pages/contact_template.txt')
            context = {'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
            subject = 'New Site Email - ' + form_subject

            try:
                send_mail(subject,
                          content,
                          None,
                          [os.environ['HKG_EMAIL']],
                          fail_silently=False)
                messages.success(request, 'Thank you! Your email has been sent')
                return redirect('contact')
            except:
                messages.error(request, 'Sorry, we were unable to send your email.')
                return redirect('contact')

    return render(request, 'pages/contact.html', {'form': form})
