from django.db import models
from django.utils import timezone
from django.core.urlsolvers import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null =True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approbve_comments=True)
    
      
    def get_absolute_url(self):
        return reverse('post_details',kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title

class Comment(model.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=250)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approbve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment= True
        self.save()
    
    def get_absolute_url(self):
        return reverse('post_list')


    def __str__(self):
        return self.title