from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Post

# Create your tests here.
class ProfileTestCase(TestCase):

    #Setup method
    def setUp(self):
        self.new_user = User(username = "amandine")
        self.new_user.save()

        self.new_profile = Profile(profile_photo='default.jpg', bio='blablabla', name='Amandine', user = self.new_user)

    def tearDown(self):
        Profile.objects.all().delete()
    
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_profile_method(self):
        self.new_profile.save_profile()
        profiles = Profile.get_all_profiles()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profiles = Profile.get_all_profiles()
        self.assertTrue(len(profiles) == 0)

class PostTestCase(TestCase):

    #setup method
    def setUp(self):
        self.new_user = User(username = "amandine")
        self.new_user.save()

        self.new_profile = Profile(profile_photo='default.jpg', bio='blablabla', name='Amandine', user = self.new_user)
        self.new_profile.save_profile()

        self.post_test = Post(image='post1.png', image_name='post1', caption='my post test', user=self.new_profile)

    def tearDown(self):
        Post.objects.all().delete()
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.post_test, Post))

    def test_save_post_method(self):
        self.post_test.save_post()
        posts = Post.get_all_posts()
        self.assertTrue(len(posts) > 0)

    def test_delete_post_method(self):
        self.post_test.save_post()
        Post.delete_post(self.post_test.id)
        posts = Post.get_all_posts()
        self.assertTrue(len(posts) == 0)
