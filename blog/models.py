from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User


# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="", null=True, blank=True)
    moment = models.DateTimeField(default=datetime.datetime.now, editable=True, blank=True)
    date = models.DateField(default=datetime.date.today, editable=True, blank=True)
    blog_comment = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
    likes = models.IntegerField(verbose_name='Нравится', default=0)
    dislikes = models.IntegerField(verbose_name='Не нравится', default=0)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return '%s, %s' % (self.summary, self.author)

    def get_absolute_url(self):
        # print(reverse('blog-detail', args=[str(self.blog_comment.pk)]))
        return reverse('blog-detail', args=[str(self.blog_comment.pk)])


class Blog(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    author = models.ForeignKey('Bloger', related_name='bs', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a description of blog")

    class Meta:
        ordering = ["-date"]

    # def display_comment(self):
    #     """
    #
    #     """
    #     return ', '.join([comment.name for comment in self.comment.all()[:3]])
    #
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('blog-detail', args=[str(self.id)])


class Bloger(models.Model):
    """
    Model representing an author.
    """
    bloger_name = models.CharField(max_length=200)
    nik_name = models.CharField(max_length=200, unique=True)
    bio = models.TextField(max_length=100, help_text="Enter a biogrephy of bloger")
    image = models.ImageField(upload_to='media/', default='no photo', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('bloger-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.bloger_name, self.nik_name)
