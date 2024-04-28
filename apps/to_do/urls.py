from django.urls import path

from apps.to_do.views import home_page, add_todo_page, add_todo, delete_page, edit_page


urlpatterns = [
    path('', home_page, name='home_page'),
    path('add-page/', add_todo_page, name='add_todo_page'),
    path('create-page/', add_todo, name='add_todo'),
    path('delete-page/<int:pk>/', delete_page, name='delete_page'),
    path('edit-page/<int:pk>/', edit_page, name='edit_page')
]