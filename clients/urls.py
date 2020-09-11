from django.urls import path

from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView, 
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
)

urlpatterns = [
    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('', ClientListView.as_view(), name='client_list'),
    path('new/comment/', CommentCreateView.as_view(), name='comment_new'),
    path('<int:pk>/comment/delete/',
         CommentDeleteView.as_view(), name='comment_delete'),
    path('<int:pk>/comment/edit/',
         CommentUpdateView.as_view(), name='comment_edit'),
    ]



