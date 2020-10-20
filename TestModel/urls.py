from django.urls import path, re_path
from . import testdb, search, test

urlpatterns = [
    # db
    path('testdb/', testdb.testdb),
    path('add/', testdb.add),

    # search
    path('search-form/', search.search_form),
    path('search/', search.search),
    path('search-post/', search.search_post),

    # test
    path('post/', test.testPost)
]
