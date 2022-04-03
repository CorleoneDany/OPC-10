from rest_framework.response import Response
from rest_framework import viewsets
from .models import User, Contributor, Project, Issue, Comment
from .serializers import UserSerializer, ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import (HasProjectPermission,
                          HasContributorPermission,
                          HasIssuePermission,
                          HasCommentPermission)


# Create your views here.

###############################################################################
###############################################################################
###############################################################################
####                            User Model                                 ####
###############################################################################
###############################################################################
###############################################################################


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


###############################################################################
###############################################################################
###############################################################################
####                            Project Model                              ####
###############################################################################
###############################################################################
###############################################################################


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, HasProjectPermission]

    def create(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save(author=request.user)
            contributor = Contributor.objects.create(project=project,
                                                     user=request.user,
                                                     role='Author')
            contributor.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

###############################################################################
###############################################################################
###############################################################################
####                          Contributor Model                            ####
###############################################################################
###############################################################################
###############################################################################


class ContributorViewSet(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()
    permission_classes = [IsAuthenticated, HasContributorPermission]

###############################################################################
###############################################################################
###############################################################################
####                            Issue Model                                ####
###############################################################################
###############################################################################
###############################################################################


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class = IssueSerializer
    queryset = Issue.objects.all()
    permission_classes = [IsAuthenticated, HasIssuePermission]

    def create(self, request, project_pk):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            project = Project.objects.get(pk=project_pk)
            issue = serializer.save(author=request.user, project=project)
            return Response(serializer.data)


###############################################################################
###############################################################################
###############################################################################
####                            Comment Model                              ####
###############################################################################
###############################################################################
###############################################################################

class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, HasCommentPermission]

    def create(self, request, issue_pk, project_pk):
        serializer = CommentSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            issue = Issue.objects.get(pk=issue_pk)
            comment = serializer.save(author=request.user, issue=issue)
            return Response(serializer.data)
