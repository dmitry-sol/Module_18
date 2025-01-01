from django.urls import path
from .views import index, page1, page2

urlpatterns = [
    path('', index, name='fourth_index'),
    path('page1', page1, name='fourth_page1'),
    path('page2', page2, name='fourth_page2'),
]