from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='photos/', default='default.png')
    bio = models.TextField(default="My Bio", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

    @classmethod
    def get_all_profiles(cls):
        return cls.objects.all()

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    image_name = models.CharField(max_length=30, blank=True)
    caption = models.CharField(max_length=200, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    def save_post(self):
        self.save()

    @property
    def get_all_comments(self):
        return self.comments.all()

    @classmethod
    def delete_post(cls, image_id):
        cls.objects.filter(id = image_id).delete()
    
    @classmethod
    def update_caption(cls,image_id, entered_caption):
        cls.objects.filter(id = image_id).update(caption = entered_caption)

    @classmethod
    def get_single_post(cls, image_id):
        found_image = cls.objects.get(pk = image_id)
        return found_image

    @classmethod
    def get_all_posts(cls):
        return cls.objects.all()

    def get_number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')


class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followers = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
