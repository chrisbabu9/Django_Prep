from django.test import TestCase

from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is test data!")
    def test_model_content(self):
        self.assertEqual(self.post.text,"This is test data!")        