from rest_framework import serializers
from .models import Vacancy
#serializers проекта

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = [
            'id',
            'name',
            'salary_level',
            'experience',
            'city'
        ]
