from django.urls import path
from .views import home_page_view, all_news, detail , contact_us, categories_list, category_news

urlpatterns = [
    path('', home_page_view, name='home_page_view'),
    path('news/', all_news, name='all_news'),
    path('news/<int:pk>/', detail, name='news_detail'),
    path('contact-us/', contact_us.as_view(), name='contact_us'),
    path('categories/', categories_list, name='categories'),
    path('category_news/<str:name>', category_news, name='category_news')
]
 