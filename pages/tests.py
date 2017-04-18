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
        If no work post exists, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('pages:work'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts were found.")
        self.assertQuerysetEqual(response.context['work_list'], [])

    def test_work_view_with_past_post(self):
        """
        Work posts with a pub_date in the past should be displayed on the page.
        """
        create_post(title='Past post', post_type='work', days=-10)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(
            response.context['work_list'],
            ['<ExpPost: Past post>']
        )

    def test_work_view_with_future_post(self):
        """
        Work posts with a pub_date in the future should not be displayed.
        """
        create_post(title='Future post', post_type='work', days=10)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(response.context['work_list'], [])
        self.assertContains(response, 'No posts were found.')

    def test_work_view_with_future_and_past_post(self):
        """
        Work posts with a pub_date in the future should not be displayed but
        posts with a pub_date in the past should be displayed.
        """
        create_post(title='Future post', post_type='work', days=10)
        create_post(title='Past post', post_type='work', days=-10)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(
            response.context['work_list'],
            ['<ExpPost: Past post>']
        )

    def test_work_view_with_multiple_past_posts(self):
        """
        More than one work post can be displayed at a time as long as the pub_date
        is in the past.
        """
        create_post(title='Past post 1', post_type='work', days=-10)
        create_post(title='Past post 2', post_type='work', days=-20)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(
            response.context['work_list'],
            ['<ExpPost: Past post 2>', '<ExpPost: Past post 1>'],
            ordered=False
        )

    def test_work_view_with_project_posts(self):
        """
        Project posts should be exluded from work_list.
        """
        create_post(title='Project post', post_type='project', days=-10)
        create_post(title='Work post', post_type='work', days=-10)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(
            response.context['work_list'],
            ['<ExpPost: Work post>']
        )

    def test_project_view_with_no_posts(self):
        """
        If no project post exists, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('pages:projects'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No projects were found.")
        self.assertQuerysetEqual(response.context['project_list'], [])

    def test_project_view_with_past_post(self):
        """
        Project posts with a pub_date in the past should be displayed on the page.
        """
        create_post(title='Past post', post_type='project', days=-10)
        response = self.client.get(reverse('pages:projects'))
        self.assertQuerysetEqual(
            response.context['project_list'],
            ['<ExpPost: Past post>']
        )

    def test_project_view_with_future_post(self):
        """
        Project posts with a pub_date in the future should not be displayed.
        """
        create_post(title='Future post', post_type='project', days=10)
        response = self.client.get(reverse('pages:projects'))
        self.assertQuerysetEqual(response.context['project_list'], [])
        self.assertContains(response, 'No projects were found.')
    def test_project_view_with_future_and_past_post(self):
        """
        Project posts with a pub_date in the future should not be displayed but
        posts with a pub_date in the past should be displayed.
        """
        create_post(title='Future post', post_type='project', days=10)
        create_post(title='Past post', post_type='project', days=-10)
        response = self.client.get(reverse('pages:projects'))
        self.assertQuerysetEqual(
            response.context['project_list'],
            ['<ExpPost: Past post>']
        )

    def test_project_view_with_multiple_past_posts(self):
        """
        More than one project post can be displayed at a time as long as the pub_date
        is in the past.
        """
        create_post(title='Past post 1', post_type='project', days=-10)
        create_post(title='Past post 2', post_type='project', days=-20)
        response = self.client.get(reverse('pages:projects'))
        self.assertQuerysetEqual(
            response.context['project_list'],
            ['<ExpPost: Past post 2>', '<ExpPost: Past post 1>'],
            ordered=False
        )

    def test_project_view_with_project_posts(self):
        """
        Work posts should be exluded from project_list.
        """
        create_post(title='Project post', post_type='project', days=-10)
        create_post(title='Work post', post_type='work', days=-10)
        response = self.client.get(reverse('pages:projects'))
        self.assertQuerysetEqual(
            response.context['project_list'],
            ['<ExpPost: Project post>']
        )


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
