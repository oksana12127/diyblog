from django.test import TestCase

# Create your tests here.

from blog.models import Blog, Bloger, Comment, User
from django.urls import reverse
import datetime


class BlogListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_blogs = 7
        test_author = Bloger.objects.create(bloger_name='John', nik_name='smith2')
        for blog_num in range(number_of_blogs):
            Blog.objects.create(title='Isecream %s' % blog_num, summary='Isecream is good %s' % blog_num,
                                author=test_author, )
        # print(Blog.objects.create(title='Isecream %s' % blog_num, summary='Isecream is good %s' % blog_num, author=test_author , ))

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/blogs/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blogs'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blogs'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'blog/blog_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('blogs'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['blog_list']) == 5)

    def test_lists_all_blogs(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('blogs') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['blog_list']) == 2)
        # print(resp)


class BlogerListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_blogers = 7

        for bloger_num in range(number_of_blogers):
            Bloger.objects.create(bloger_name='John %s' % bloger_num, nik_name='smith2 %s' % bloger_num, bio='123')
            # print(number_of_blogers)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/blogers/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blogers'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blogers'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'blog/bloger_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('blogers'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['bloger_list']) == 5)

    def test_lists_all_blogers(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('blogers') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['bloger_list']) == 2)
        # print(resp)


class CommentCreateViewTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()

        # Создание объекта Comment для для пользователя test_user1
        test_author = Bloger.objects.create(bloger_name='John', nik_name='smith2')
        return_date = datetime.datetime.now()
        self.test_blog = Blog.objects.create(title='Isecream ', summary='Isecream is good ',
                                             author=test_author, )

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('comment_create', kwargs={'pk': self.test_blog.pk, }))
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(resp.url.startswith('/accounts/login/'))

    def test_HTTP404_for_invalid_book_if_logged_in(self):
        import uuid
        test_uid = 55555555555  # unlikely UID to match our comment!
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('comment_create', kwargs={'pk': test_uid, }))
        self.assertEqual(resp.status_code, 404)


def test_uses_correct_template(self):
    login = self.client.login(username='testuser1', password='12345')
    print(reverse('comment_create', kwargs={'pk': self.test_blog.pk, }))
    resp = self.client.get(reverse('comment_create', kwargs={'pk': self.test_blog.pk, }))
    self.assertEqual(resp.status_code, 200)

    # Check we used correct template
    self.assertTemplateUsed(resp, 'blog/comment_form.html')


def test_redirects_to_author_create_on_success(self):
    login = self.client.login(username='testuser1', password='12345')

    resp = self.client.post(reverse('comment_create', kwargs={'pk': self.test_blog.pk, }),
                            data={"author": 'test_user1', "moment": 'return_date',
                                  "summary": 'qwerty', },
                            )
    self.assertEqual(resp.status_code, 302)
    self.assertRedirects(resp, reverse('blog-detail', kwargs={'pk': self.test_blog.pk, }))
