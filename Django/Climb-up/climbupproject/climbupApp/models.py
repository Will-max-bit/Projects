from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()# allowing the user to add images to their post
    post_image = models.ImageField(upload_to='post_images/', null=True, blank=True)# ties the post to a city in the database for sorting
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='posts')# ties user to their posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_posts')
    attendees = models.ManyToManyField(User, related_name='attending_posts', blank=True) # ties user(s) attending status to individual posts
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)# ties user(s) likes to individual posts
    created_date = models.DateTimeField(default=timezone.now)
    scheduled_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title + 'by' + self.author.username + 'on' + self.created_date.strftime('%b %d %Y')
    
    # model for comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')# post ties the comment to a particular post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_authors')# foreign key to the user, tying the user to their comments
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)# comments are auto-accepted, select default to false if comments should be approved before posting to page

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return 'Comment {} by {}'. format(self.body, self.author)
    