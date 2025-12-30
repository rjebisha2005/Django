from rest_framework import serializers

from.models import Student_ser

class studentserilizer(serializers.Modelserilizer):
    class Meta:
        queryset=Student_ser.objects. all()
        serializer_class=studentserilizer
        
