"""
URL configuration for the Django project. Includes URL patterns for the home page, search functionality, prompt list, prompt deletion, and admin site.
"""

from django.contrib import admin

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('search_landing/', views.search_landing, name='search_landing'),
    path('contact_info/', views.contact_info, name='contact_info'),

    path('make_search/', views.make_search, name='make_search'),
    path('prompt_list/', views.prompt_list, name='prompt_list'),
    path('prompt_list/<int:pk>/', views.delete_prompt, name='delete_prompt'),
    path('show_result/<int:prompt_id>/', views.show_result, name='show_result'),

    path('gen_biz_docs/', views.gen_biz_docs, name='gen_biz_docs'),

    path('ppxt_support/', views.ppxt_support, name='ppxt_support'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
