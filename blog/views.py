from django.shortcuts import render

# Create your views here.

from .models import Comment, Blog, Bloger
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404



def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_comments = Comment.objects.all().count()
    num_blogs = Blog.objects.all().count()
    num_blogers = Bloger.objects.count()  # Метод 'all()' применен по умолчанию.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_comments': num_comments, 'num_blogs': num_blogs,
                 'num_blogers': num_blogers, 'num_visits':num_visits},
    )


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 2




class BlogDetailView(generic.DetailView):
    model = Blog
    # paginate_by = 5



class BlogerListView(generic.ListView):
    model = Bloger
    paginate_by = 2



class BlogerDetailView(generic.DetailView):
    model = Bloger


# class AuthorCreate(CreateView):
#     model = Author
#     # fields = ['name']
#
#     def form_valid(self, for:
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)



class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['summary']

    def form_valid(self, form):
        """

        Добавьте автора и связанный блог, чтобы сформировать данные, прежде чем задавать их действительными (чтобы они сохранялись в модели)
        """
        # Добавить зарегистрированного пользователя как автора комментария
        form.instance.author = self.request.user
        # Связать комментарий с блогом на основе переданного идентификатора
        # print('FORM VALID', self.kwargs['pk'])
        form.instance.blog_comment = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Вызвать поведение проверки формы суперкласса
        return super(CommentCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blog_diskr'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        print('context:', context)
        return context


    # def likes(self, **kwargs):
    #     context = super(CommentCreate, self).get_context_data(**kwargs)
    #     context['blog_diskr'] = get_object_or_404(Comment, pk=self.kwargs['pk'])
    #     return context + 1


class CommentLikeView(generic.DetailView):
    model = Comment

    def likes(self, **kwargs):
        try:
            comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
            comment.likes += 1
            comment.save()
        except ObjectDoesNotExist:
            return Http404
        # return redirect(request.GET.get('next', '/'))
