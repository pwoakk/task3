from rest_framework import serializers

from courses.models import *


class ContactSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ('type', 'value')

    def get_type(self, obj):
        return obj.type

    def get_contact_choice(self, obj):
        return obj.get_contact_choice_display()


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

    def create(self, validated_data):
        cat_data = validated_data.pop('category')
        cont_data = validated_data.pop('contacts')
        br_data = validated_data.pop('branches')
        cat_value = cat_data['name']
        course = Course.objects.create(**validated_data, category=Category.objects.get(name=cat_value))
        for contact in cont_data:
            Contact.objects.create(course=course, **contact)
        for branch in br_data:
            Branch.objects.create(course=course, **branch)
        return course




