from django.db import models

# Create your models here.

class Job(models.Model):

    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    summary = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)

    topics = models.ManyToManyField('Topic', blank=True, related_name='jobs')

    def __str__(self):
        return self.title

class Topic(models.Model):

    title = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
