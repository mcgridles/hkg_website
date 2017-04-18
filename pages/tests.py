from __future__ import unicode_literals

import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Author, ExpPost

def create_post(title, post_type, days):
    """
    Creates a post with the given 'title' of the given 'post_type' and published
    the given number of 'days' offset to now (negative for posts published in the past,
    positive for posts that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return ExpPost.objects.create(title=title, post_type=post_type, pub_date=time)

class ExpPostViewTests(TestCase):
    def test_work_view_with_no_posts(self):
        """
        If no post exists, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('pages:work'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts were found.")
        self.assertQuerysetEqual(response.context['work_list'], [])

    def test_work_view_with_past_post(self):
        """
        Posts with a pub_date in the past should be displayed on the page.
        """
        create_post(title='Past post', post_type='work', days=-10)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(
            response.context['work_list'],
            ['<ExpPost: Past post>']
        )

    def test_work_view_with_future_post(self):
        """
        Posts with a pub_date in the future should not be displayed.
        """
        create_post(title='Future post', post_type='work', days=10)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(response.context['work_list'], [])
        self.assertContains(response, 'No posts were found.')


def create_author(name, age):
    """
    Creates a site author with the given 'name'
    """
    return Author.objects.create(name=name, age=age)

class AuthorViewTests(TestCase):
    def test_aboutMe_view_with_no_author(self):
        """
        If no author exists, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('pages:aboutMe'))
        self.assertEqual(response.status_code, 404)

    def test_aboutMe_with_author(self):
        """
        Author should be displayed on the page.
        """
        name = 'Henry Gridley'
        create_author(name=name, age=20)
        response = self.client.get(reverse('pages:aboutMe'))
        self.assertContains(response, name)
