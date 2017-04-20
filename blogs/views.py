from django.utils import timezone

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView,ListView
from blogs.models import Books, Author
import pdb

# Create your views here.

class Bookslist(ListView):
    template_name = 'blogs/list.html'
    model = Books
    # queryset = Books.objects.all()
    context_object_name = 'my_favorite_books'

class BooksDetail(DetailView):
    template_name = 'blogs/detail.html'
    model = Books
    context_object_name = 'my_favorite_book'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BooksDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Books.objects.all()
        return context

class BooksSmartList(ListView):
    template_name = 'blogs/list.html'

    queryset = Books.objects.filter()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BooksSmartList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.self.name
        return context

class AuthorDetailView(DetailView):
    queryset = Author.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(AuthorDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object


