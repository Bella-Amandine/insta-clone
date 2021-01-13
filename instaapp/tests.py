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

