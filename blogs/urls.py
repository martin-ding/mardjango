from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$',views.index,name='blog_index'),
    # url(r'hello/$',views.index,name='hello'),
    url(r'^books/$',views.Bookslist.as_view()),
    url(r'^books/(?P<pk>\d+)/$',views.BooksDetail.as_view()),
    url(r"^books/(?P<slug_topic_name>[\w-]+)/$",views.BooksSmartList.as_view())
]