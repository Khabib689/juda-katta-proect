from django.urls import path
from .views import home_page_view, all_news, detail , contact_us

urlpatterns = [
    path('', home_page_view, name='home_page_view'),
    path('news/', all_news, name='all_news'),
    path('news/<int:pk>/', detail, name='news_detail'),
    path('contact-us/', contact_us.as_view(), name='contact_us')
]
 