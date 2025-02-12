from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListApi, book_list_view, BookDetailApiView, \
    BookUpdateview, BookDeleteView, BookCreatApiView, BookListCreateApiView, \
    BookUpdateDeleteView, BookViewset

router = SimpleRouter()
router.register('books', BookViewset, basename='books')

urlpatterns = [
    # path('books/', BookListApi.as_view(),),
    # path('booklistcreate/', BookListCreateApiView.as_view(),),
    # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteView.as_view(),),
    # path('books/create/', BookCreatApiView.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view(),),
    # path('books/<int:pk>/delete/', BookDeleteView.as_view(),),
    # path('books/<int:pk>/update/', BookUpdateview.as_view()),
]


urlpatterns = urlpatterns + router.urls


