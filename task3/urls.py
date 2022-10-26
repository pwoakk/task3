from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from courses.views import CoursesListAPI, CourseView, CoursesDetailAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    re_path(r'^course/$', CoursesListAPI.as_view(), name='courses-list'),
    re_path(r'^course/(?P<pk>[0-9]+)/$', CoursesDetailAPI.as_view(), name='course-detail'),
]
