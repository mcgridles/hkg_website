from __future__ import unicode_literals

import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from unittest import skip, skipIf, skipUnless

from .models import Author, ExpPost, Image, Journal

DEBUG = False

def create_author(name, age):
    """
    Creates a site author with the given 'name'
    """
    return Author.objects.create(name=name, age=age, picture='hkg_portrait.png')

class HomepageViewTests(TestCase):
    def test_homepage_view_with_no_author(self):
        """
        If no author exists, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 404)

    def test_homepage_with_author(self):
        """
        Author should be displayed on the page.
        """
        create_author(name='Henry Gridley', age=20)
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Henry Gridley')

def create_post(title, post_type, days=-1, start=-1):
    """
    Creates a post with the given 'title' of the given 'post_type' and published
    the given number of 'days' offset to now (negative for posts published in the past,
    positive for posts that have yet to be published).
    """
    pub_time = timezone.now() + datetime.timedelta(days=days)
    start_time = timezone.now() + datetime.timedelta(days=start)
    return ExpPost.objects.create(title=title, post_type=post_type,
        pub_date=pub_time, start_date=start_time,
        marquee='hkg_portrait.png')

class ListViewTests(TestCase):
    def test_list_view_with_no_posts(self):
        """
        If no post exists, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('pages:work'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts were found.")
        self.assertQuerysetEqual(response.context['post_list'], [])

    def test_list_view_with_past_post(self):
        """
        Posts with a pub_date in the past should be displayed on the page.
        """
        create_post(title='Past post', post_type='work', days=-10)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(
            response.context['post_list'],
            ['<ExpPost: Past post>']
        )

    def test_list_view_with_future_post(self):
        """
        Posts with a pub_date in the future should not be displayed.
        """
        create_post(title='Future post', post_type='work', days=10)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(response.context['post_list'], [])
        self.assertContains(response, 'No posts were found.')

    def test_list_view_with_future_and_past_post(self):
        """
        Posts with a pub_date in the future should not be displayed but
        posts with a pub_date in the past should be displayed.
        """
        create_post(title='Future post', post_type='work', days=10)
        create_post(title='Past post', post_type='work', days=-10)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(
            response.context['post_list'],
            ['<ExpPost: Past post>']
        )

    def test_list_view_with_multiple_past_posts(self):
        """
        More than one post can be displayed at a time as long as the pub_date
        is in the past.
        """
        create_post(title='Past post 1', post_type='work', days=-10)
        create_post(title='Past post 2', post_type='work', days=-20)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(
            response.context['post_list'],
            ['<ExpPost: Past post 2>', '<ExpPost: Past post 1>'],
            ordered=False
        )

    def test_list_view_with_future_start_date(self):
        """
        Jobs and projects that are expected to be started in the future should
        not be posted until they are started.
        """
        create_post(title='Work post', post_type='work', days=-10, start=10)
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(response.context['post_list'], [])
        self.assertContains(response, 'No posts were found.')

    def test_list_view_with_different_post_types(self):
        """
        Both work and job posts should be displayed, as long as the start date
        is in the past.
        """
        create_post(title='Work post', post_type='work')
        create_post(title='Project post', post_type='project')
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(
            response.context['post_list'],
            ['<ExpPost: Work post>', '<ExpPost: Project post>']
        )

class ImageModelTests(TestCase):
    def test_post_with_no_images(self):
        """
        Posts with no images associated with them should return an empty Queryset.
        """
        create_post(title='Test post', post_type='work')
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(response.context['post_list'][0].image_set.all(), [])

    def test_post_with_image(self):
        """
        Posts with an image should not break the site.
        More specific tests to come.
        """
        post = create_post(title='Test post', post_type='work')
        post.image_set.create(title='Test image', img='hkg_portrait.png')
        response = self.client.get(reverse('pages:work'))
        self.assertQuerysetEqual(
            response.context['post_list'][0].image_set.all(),
            ['<Image: Test image>']
        )

class DetailViewTest(TestCase):
    def test_detail_with_no_journals(self):
        """
        Posts not containing journals should not display journal section.
        """
        post = create_post(title='Test post', post_type='work')
        response = self.client.get(reverse('pages:details', kwargs={'pk':post.id}))
        self.assertNotContains(response, 'Journal')

    def test_detail_with_journals(self):
        """
        Posts containing journals should display journal section.
        """
        post = create_post(title='Test post', post_type='work')
        post.journal_set.create(title='Test journal', post=post,
            pub_date=timezone.now(), author='Henry Gridley', text='test')
        response = self.client.get(reverse('pages:details', kwargs={'pk':post.id}))
        self.assertContains(response, 'Journal')

class ContactPageTest(TestCase):
    def test_base_contact_page(self):
        """
        Contact page should not contain any messages when first loaded.
        """
        response = self.client.get(reverse('contact'))
        self.assertNotContains(response, 'Thank you!')
        self.assertNotContains(response, 'Sorry')
