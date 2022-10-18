from django.db import models


class Category(models.Model):
    name = models.CharField('Наименование', max_length=255)
    imgpath = models.CharField('Фото', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField('Наименование', max_length=255)
    description = models.TextField('Описание')
    category = models.ForeignKey(Category, verbose_name='Категория', related_name='courses', on_delete=models.CASCADE)
    logo = models.CharField('Логотип', max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField('Широта', max_length=255)
    longitude = models.CharField('Долгота', max_length=255)
    address = models.CharField('Адрес', max_length=255)
    course = models.ForeignKey(Course, verbose_name='Ветки', related_name='branches', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ветка'
        verbose_name_plural = 'Ветки'

    def __str__(self):
        return self.address


class Contact(models.Model):
    contact_choices = (
        (1, 'Phone'),
        (2, 'Facebook'),
        (3, 'Email')
    )
    type = models.IntegerField('Тип', choices=contact_choices, default=1)
    value = models.CharField('Значение', max_length=255)
    course = models.ForeignKey(Course, verbose_name='Контакты', related_name='contacts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.value
