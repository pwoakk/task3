from django.test import TestCase

from courses.models import Category, Course


class CourseModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='test_category_name', imgpath='test_category_imgpath')
        Course.objects.create(name='test_name', description='test_desc', category=test_category, logo='test_path')

    def test_name(self):
        course = Course.objects.get(id=1)
        fl = course._meta.get_field('name').verbose_name
        self.assertEqual(fl, 'Наименование')

    def test_desc(self):
        course = Course.objects.get(id=1)
        fl = course._meta.get_field('description').verbose_name
        self.assertEqual(fl, 'Описание')

    def test_logo(self):
        course = Course.objects.get(id=1)
        fl = course._meta.get_field('logo').verbose_name
        self.assertEqual(fl, 'Логотип')

    def test_name_max_length(self):
        course = Course.objects.get(id=1)
        ml = course._meta.get_field('name').max_length
        self.assertEqual(ml, 255)

    def test_logo_max_length(self):
        course = Course.objects.get(id=1)
        ml = course._meta.get_field('logo').max_length
        self.assertEqual(ml, 255)
