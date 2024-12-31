from django.urls import path
from .views import index, page1, page2  # Импортируем представления

urlpatterns = [
    path('', index, name='third_index'), # Главная страница
    path('page1', page1, name='third_page1'),  # Первая страница
    path('page2', page2, name='third_page2'),  # Вторая страница
]