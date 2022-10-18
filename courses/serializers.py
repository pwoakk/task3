from rest_framework import serializers

from courses.models import *


class ContactSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ('contact_choice', 'value')


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Category
        fields = ('name',)


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address',)


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, required=True)
    branches = BranchSerializer(many=True, required=True)
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'logo', 'category', 'contacts', 'branches')



