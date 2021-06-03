from django.db.models import fields
from rest_framework import serializers
from .models import Course
from quickstart import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description',
                  'category', 'logo', 'contacts', 'branches']
