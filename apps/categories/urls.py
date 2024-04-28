from django.urls import path

from apps.categories.views import category_page


urlpatterns = [
    path('category-page/', category_page, name='category_page')
]