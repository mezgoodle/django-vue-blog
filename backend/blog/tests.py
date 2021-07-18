from django.test import TestCase
from django.conf import settings
from .models import Profile, Tag, Post

class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(
            name='test name',
        )

    def test_name_content(self):
        tag = Tag.objects.get(id=1)
        expected_object_name = tag.name
        self.assertEquals(expected_object_name, 'test name')


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Profile.objects.create(
            user=settings.AUTH_USER_MODEL,
            website='https://github.com',
            bio='my test bio'
        )

    def test_website_content(self):
        profile = Profile.objects.get(id=1)
        expected_object_website = profile.website
        self.assertEquals(expected_object_website, 'https://github.com')

    def test_bio_content(self):
        profile = Profile.objects.get(id=1)
        expected_object_bio = profile.bio
        self.assertEquals(expected_object_bio, 'my test bio')


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Profile.objects.create(
            user=settings.AUTH_USER_MODEL,
            website='https://github.com',
            bio='my test bio'
        )
        Tag.objects.create(
            name='test name',
        )
        profile = Profile.objects.get(id=1)
        tag = Tag.objects.get(id=1)
        Post.objects.create(
            title='Test title',
            slug='test-title',
            body='Test body',
            author=profile,
            tags=tag
        )

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = post.website
        self.assertEquals(expected_object_title, 'Test title')

    def test_bodt_content(self):
        post = Post.objects.get(id=1)
        expected_object_body = post.body
        self.assertEquals(expected_object_body, 'Test body')
