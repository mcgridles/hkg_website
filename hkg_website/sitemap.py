from django.contrib import sitemaps
from django.urls import reverse
from django.utils import timezone
from pages.models import ExpPost

class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ['home', 'pages:work', 'contact', ]

    def location(self, item):
        return reverse(item)

class ExpPostSitemap(sitemaps.Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return ExpPost.objects.filter(pub_date__lte=timezone.now()
                ).filter(start_date__lte=timezone.now())

    def lastmod(self, obj):
        return obj.pub_date
