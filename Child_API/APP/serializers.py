from django.contrib.auth.models import User
from rest_framework import serializers, validators
from .models import child,manual,auto



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), f"A user with that Email already exists."
                    )
                ],
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )
        return user
    
class MDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = manual
        fields =("child_id","Date","Manual_height","Manual_weight")
    
class ADataSerializer(serializers.ModelSerializer):
    class Meta:
        model = auto
        fields =("child_id","Date","Auto_height","Auto_weight")
    
class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = child
        fields =("id","User_id","First_name","Last_name","Gender","date_of_birth","Organization","Father_name","Father_mobile","Mother_name","State","District","Taluk","Village")
    