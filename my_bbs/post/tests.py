import unittest

from django.contrib.auth.models import User
from django.test import TestCase

from post.models import Topic


"""
class SimpleTest(TestCase):
    def test_addition(self):
        def addition(x, y):
            return x + y
        self.assertEqual(addition(1, 1), 2)


    def test_post_topic_model(self):
        user = User.objects.create_user(username='username', password='password')
        topic = Topic.objects.create(
            title='test topic', content='first test topic', user=user
        )
        self.assertTrue(topic is not None)
        self.assertEqual(Topic.objects.count(), 1)
        topic.delete()
        self.assertEqual(Topic.objects.count(), 0)


    def test_topic_detail_view(self):
        user = User.objects.create_user(username='username', password='password')
        topic = Topic.objects.create(
            title='test topic', content='first test topic', user=user
        )
        response = self.client.get('/post/topic/%d/' % topic.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], topic.id)
"""

"""
class SimpleTest(TestCase):
    @classmethod
    def setUpClass(cls):
        print('running setUpClass')
    
    @classmethod
    def tearDownClass(cls):
        print('running tearDownClass')

    # 团子注：这里其实跟 python 一般的命名方式不太一样，setUp 应为 set_up
    def setUp(self):
        print('running setUp')
        self.user = User.objects.create_user(username='username', password='password')
    
    def test_post_topic_model(self):
        print('running test_post_topic_model')
        topic = Topic.objects.create(
            title='test topic', content='first test topic', user=self.user
        )
        self.assertTrue(topic is not None)
        self.assertEqual(Topic.objects.count(), 1)
        topic.delete()
        self.assertEqual(Topic.objects.count(), 0)
    
    def test_topic_detail_view(self):
        print('running test_topic_detail_view')
        topic = Topic.objects.create(
            title='test topic', content='first test topic', user=self.user
        )
        response = self.client.get('/post/topic/%d/' % topic.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], topic.id)
    
    def tearDown(self):
        print('running tearDown')
"""


class SimpleTest(TestCase):
    @unittest.skip('skip test a')
    def test_a(self):
        print('running test a')
    
    @unittest.skipIf(2 > 1, 'skip test b')
    def test_b(self):
        print('running test b')
    
    @unittest.skipUnless(2 < 1, 'skip test c')
    def test_c(self):
        print('running test c')
