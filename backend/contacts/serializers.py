from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelField):
    class Meta:
        model = Contact
        fields = '__all__'