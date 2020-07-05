from django.test import TestCase
from blog.models import Bloger, Blog, Comment

class BlogerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Bloger.objects.create(bloger_name='Big', nik_name='Bob')

    def test_bloger_name_label(self):
        author = Bloger.objects.get(id=1)
        field_label = author._meta.get_field('bloger_name').verbose_name
        self.assertEquals(field_label, 'bloger name')

    def test_nik_name_label(self):
        author = Bloger.objects.get(id=1)
        field_label = author._meta.get_field('nik_name').verbose_name
        self.assertEquals(field_label, 'nik name')

    def test_bio_label(self):
        author = Bloger.objects.get(id=1)
        field_label = author._meta.get_field('bio').verbose_name
        self.assertEquals(field_label, 'bio')

    def test_bloger_name_max_length(self):
        author = Bloger.objects.get(id=1)
        max_length = author._meta.get_field('bloger_name').max_length
        self.assertEquals(max_length, 200)

    def test_nik_name_max_length(self):
        author = Bloger.objects.get(id=1)
        max_length = author._meta.get_field('nik_name').max_length
        self.assertEquals(max_length, 200)


    def test_bio_max_length(self):
        author = Bloger.objects.get(id=1)
        max_length = author._meta.get_field('bio').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_bloger_name_comma_nik_name(self):
        author = Bloger.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.bloger_name, author.nik_name)
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url_for_bloger(self):
        author = Bloger.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/blog/bloger/1')

class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Blog.objects.create(title='icecream')

    def test_blog_name_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')


    def test_date_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

    def test_author_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_summary_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_summary_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('summary').max_length
        self.assertEquals(max_length, 1000)

    def test_object_name_is_title(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = blog.title
        self.assertEquals(expected_object_name, str(blog))

    def test_get_absolute_url_for_blog(self):
        blog = Blog.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(blog.get_absolute_url(), '/blog/blog-detail/1')

class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Comment.objects.create(summary='chocco ok')
        Blog.objects.create(title='icecream')

    def test_comment_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_summary_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_moment_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('moment').verbose_name
        self.assertEquals(field_label, 'moment')

    def test_date_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

    def test_blog_comment_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('blog_comment').verbose_name
        self.assertEquals(field_label, 'blog comment')

    def test_object_name_is_summary_comma_author(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = '%s, %s' % (comment.summary, comment.author)
        self.assertEquals(expected_object_name, str(comment))

    def test_get_absolute_url_for_comment(self):
        blog_comment = Blog.objects.get(id=1)
        # title = Blog.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(blog_comment.get_absolute_url(), '/blog/blog-detail/1')

