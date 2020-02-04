from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """serializer for the users objects"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password','name')

        extra_kwargs = {'password':{'write_only':True , 'min_length':5}}


        def create(self, validated_data):
            """create a new user with encrypted password and return it"""

            user = get_user_model().objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password'],
                **validated_data
                )

            return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """validate and authenticate the user"""
        user = authenticate(
            request=self.context.get('request'),
            username=attrs.get('email'),
            password=attrs.get('password')
        )

        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs




