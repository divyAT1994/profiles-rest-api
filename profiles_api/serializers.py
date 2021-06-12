from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer): #they are similar to Django forms
    """Serializes a name field for testing out an APIView post calls"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password' : {
                'write_only' : True, #Only write to passwords and you cant retrieve it
                'style' : {
                    'input_type' : 'password'
                } #Make the field obfuscated so that nobody sees your password
            }
        }

    def create(self,validated_data):
        """Create and return a new user using the custom User Profile model"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
