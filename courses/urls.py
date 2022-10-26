from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from courses.views import CourseView, CoursesListAPI

router = routers.DefaultRouter()
router.register(r'courses', CourseView)

urlpatterns = [
    path('', include(router.urls)),
]
