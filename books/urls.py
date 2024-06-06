from .views import BookList, BookDetailView
from django.urls import path


urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
]