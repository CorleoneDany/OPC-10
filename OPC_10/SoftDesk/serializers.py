from rest_framework.serializers import ModelSerializer
from .models import User, Contributor, Project, Issue, Comment
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:

        model = User
        fields = '__all__'
        read_field_only = ['id']


class ContributorSerializer(ModelSerializer):
    class Meta:

        model = Contributor
        fields = '__all__'
        read_field_only = ['id', 'project']


class ProjectSerializer(ModelSerializer):

    class Meta:

        model = Project
        fields = '__all__'
        read_field_only = ['id', 'author']


class IssueSerializer(ModelSerializer):
    class Meta:

        model = Issue
        fields = '__all__'
        read_field_only = ['id', 'project', 'author', 'created_time']


class CommentSerializer(ModelSerializer):
    class Meta:

        model = Comment
        fields = '__all__'
        read_field_only = ['id', 'author', 'issue', 'created_time']
