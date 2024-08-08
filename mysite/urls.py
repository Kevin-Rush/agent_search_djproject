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
    path('make_search/', views.make_search, name='make_search'),
    path('prompt_list/', views.prompt_list, name='prompt_list'),
    path('prompt_list/<int:pk>/', views.delete_prompt, name='delete_prompt'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
