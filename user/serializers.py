from rest_framework import serializers
from .models import User, Contact, Spam

class UserSeri(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id','username','phone',"email","password")
        extra_kwargs ={'password':{'write_only':True}}

    def create(self, validated_data):
        user= User.objects.create_user(**validated_data)
        return user
    
class ContactSeri(serializers.ModelSerializer):
    class Meta:
        model= Contact
        fields = ('id','name','phone')

class SpamSeri(serializers.ModelSerializer):
    class Meta:
        model= Spam
        fields = ('id','phone')

class SearchSeri(serializers.ModelSerializer):
    spam_count = serializers.SerializerMethodField()
   
    class Meta:
        model= User
        fields =('id','username','phone','spam_count')

    def get_spam_count(sefl,obj):
        return Spam.objects.filter(phone=obj.phone).count()