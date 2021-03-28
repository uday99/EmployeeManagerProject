from  rest_framework import serializers
from .models import Manager,Employee


class ManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True, style={"input_type": 'password'})

    class Meta:
        model=Manager
        fields = ['email', 'firstname', 'lastname', 'password', 'address', 'dob', 'company'
                  ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if Manager.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return Manager.objects.create(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True,style={"input_type":'password'})

    class Meta:
        model=Manager
        fields=('email','password')


class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields=('email',)



class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True, style={"input_type": 'password'})

    class Meta:
        model=Employee
        fields=['id','email', 'firstname', 'lastname', 'password', 'address', 'dob', 'company','mobile','city']
