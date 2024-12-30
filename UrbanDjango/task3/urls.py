from django.urls import path
from .views import index, page1, page2  # Импортируем представления

urlpatterns = [
    path('', index, name='third_index'), # Главная страница
    path('page1.html', page1, name='page1'),  # Первая страница
    path('page2.html', page2, name='page2'),  # Вторая страница
]