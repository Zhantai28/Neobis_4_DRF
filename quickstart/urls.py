from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('courses/', views.Course_list.as_view()),
    path('courses/<int:pk>/', views.Course_detail.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)
