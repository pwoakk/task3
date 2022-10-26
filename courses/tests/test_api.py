from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Category, Course
from courses.serializers import CourseSerializer


class CourseApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='test_category_name', imgpath='test_category_imgpath')
        Course.objects.create(name='test_name', description='test_desc', category=test_category, logo='test_path')

    def test_get(self):
        category = Category.objects.get(id=1)
        course = Course.objects.get(id=1)
        course_2 = Course.objects.create(id=2, name='test_name_2', description='test_desc_2', category=category, logo='test_path_2')
        serializer_data = CourseSerializer([course, course_2], many=True).data
        url = reverse('courses-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

