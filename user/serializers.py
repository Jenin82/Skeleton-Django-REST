from rest_framework.serializers import ModelSerializer
# from user.models import Todo
from django.contrib.auth.models import User
from rest_framework import  serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# class TodoSerializer(ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = '__all__'
    
# Token serialization
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    
# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data['username'], password=validated_data['password']
        )

