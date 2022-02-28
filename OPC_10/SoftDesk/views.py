from multiprocessing import context
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User, Contributor, Project, Issue, Comment
from .serializers import UserSerializer, ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny


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
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        project = Project.objects.get(id=pk)
        project_serializer = ProjectSerializer(project)
        return Response(project_serializer.data)

    def create(self, request):
        project = Project.objects.create(
            **request.data, author_user_id=request.user)
        if project.is_valid():
            project.save()
            contributor = Contributor.objects.create(project_id=project,
                                                     user_id=request.user.id,
                                                     role='Author')
            contributor.save()
        return Response(project.data)

    def destroy(self, request, pk):
        project = Project.objects.get(id=pk)
        project.delete()
        return Response(status=204)

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
    permission_classes = [IsAuthenticated]

    def retrieve(request, project_id):
        contributors = Contributor.objects.filter(project_id=project_id)
        contributors_serializer = ContributorSerializer(
            contributors, many=True)
        return Response(contributors_serializer.data)

    def create(request):
        contributor = ContributorSerializer(data=request.data)
        if contributor.is_valid():
            contributor.save()
        return Response(contributor.data)

    def update(request, contributor_id):
        contributor = Contributor.objects.get(id=contributor_id)
        contributor_serializer = ContributorSerializer(
            contributor, data=request.data)
        if contributor_serializer.is_valid():
            contributor_serializer.save()
        return Response(contributor_serializer.data)

    def destroy(request, contributor_id):
        contributor = Contributor.objects.get(id=contributor_id)
        contributor.delete()
        return Response(status=204)

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
    permission_classes = [IsAuthenticated]

    def get_issues(request, project_id):
        issues = Issue.objects.filter(project_id=project_id)
        issues_serializer = IssueSerializer(issues, many=True)
        return Response(issues_serializer.data)

    def get_issue(request, issue_id):
        issue = Issue.objects.get(id=issue_id)
        issue_serializer = IssueSerializer(issue)
        return Response(issue_serializer.data)

    def create_issue(request, project_id):
        issue = IssueSerializer(data=request.data)
        if issue.is_valid():
            issue.save()
        return Response(issue.data)

    def update_issue(request, issue_id):
        issue = Issue.objects.get(id=issue_id)
        issue_serializer = IssueSerializer(issue, data=request.data)
        if issue_serializer.is_valid():
            issue_serializer.save()
        return Response(issue_serializer.data)

    def delete_issue(request, issue_id):
        issue = Issue.objects.get(id=issue_id)
        issue.delete()
        return Response(status=204)


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
    permission_classes = [IsAuthenticated]

    def get_comments(request, issue_id):
        comments = Comment.objects.filter(issue_id=issue_id)
        comments_serializer = CommentSerializer(comments, many=True)
        return Response(comments_serializer.data)

    def get_comment(request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment_serializer = CommentSerializer(comment)
        return Response(comment_serializer.data)

    def create_comment(request, issue_id):
        comment = CommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(comment.data)

    def update_comment(request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment_serializer = CommentSerializer(comment, data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
        return Response(comment_serializer.data)

    def delete_comment(request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return Response(status=204)


def get_user_from_session(request):
    if 'user' not in request.session:
        return None
    user = User.objects.get(id=request.session['user'])
    user_serializer = UserSerializer(user)
    return user_serializer.data
