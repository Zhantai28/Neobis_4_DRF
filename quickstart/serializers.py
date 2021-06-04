from rest_framework import serializers
from .models import Course, Contact, Branch


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['type', 'value']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['latitude', 'longitude', 'address']


class CourseSerializer(serializers.ModelSerializer):

    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        contacts = validated_data.pop('contacts')
        branches = validated_data.pop('branches')
        course = Course.objects.create(**validated_data)
        for course_data in contacts:
            Course.objects.create(course=course, **course_data)
        for course_data in branches:
            Course.objects.create(course=course, **course_data)
        return course
