from .views import BookList, BookDetailView, SearchResultsListView
from django.urls import path


urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results')
]