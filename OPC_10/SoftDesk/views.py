from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import User, Contributor, Project, Issue, Comment
from .serializers import UserSerializer, ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer

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

    @api_view(['POST'])
    def create_user(request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
        return Response(user.data)

    @api_view(['POST'])
    def login_user(request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
        return Response(user.data)

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

    @api_view(['GET'])
    def get_project(request):
        project = Project.objects.all()
        project_serializer = ProjectSerializer(project, many=True)
        return Response(project_serializer.data)

    @api_view(['GET'])
    def get_projects(request):
        projects = Project.objects.all()
        project_serializer = ProjectSerializer(projects, many=True)
        return Response(project_serializer.data)

    @api_view(['POST'])
    def create_project(request):
        project = ProjectSerializer(data=request.data)
        if project.is_valid():
            project.save()
        return Response(project.data)

    @api_view(['PUT'])
    def update_project(request, project_id):
        project = Project.objects.get(id=project_id)
        project_serializer = ProjectSerializer(project, data=request.data)
        if project_serializer.is_valid():
            project_serializer.save()
        return Response(project_serializer.data)

    @api_view(['DELETE'])
    def delete_project(request, project_id):
        project = Project.objects.get(id=project_id)
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

    @api_view(['GET'])
    def get_contributors(request, project_id):
        contributors = Contributor.objects.filter(project_id=project_id)
        contributors_serializer = ContributorSerializer(
            contributors, many=True)
        return Response(contributors_serializer.data)

    @api_view(['GET'])
    def get_contributors(request, project_id):
        contributors = Contributor.objects.filter(project_id=project_id)
        contributors_serializer = ContributorSerializer(
            contributors, many=True)
        return Response(contributors_serializer.data)

    @api_view(['POST'])
    def create_contributor(request):
        contributor = ContributorSerializer(data=request.data)
        if contributor.is_valid():
            contributor.save()
        return Response(contributor.data)

    @api_view(['PUT'])
    def update_contributor(request, contributor_id):
        contributor = Contributor.objects.get(id=contributor_id)
        contributor_serializer = ContributorSerializer(
            contributor, data=request.data)
        if contributor_serializer.is_valid():
            contributor_serializer.save()
        return Response(contributor_serializer.data)

    @api_view(['DELETE'])
    def delete_contributor(request, contributor_id):
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

    @api_view(['GET'])
    def get_issues(request, project_id):
        issues = Issue.objects.filter(project_id=project_id)
        issues_serializer = IssueSerializer(issues, many=True)
        return Response(issues_serializer.data)

    @api_view(['GET'])
    def get_issue(request, issue_id):
        issue = Issue.objects.get(id=issue_id)
        issue_serializer = IssueSerializer(issue)
        return Response(issue_serializer.data)

    @api_view(['POST'])
    def create_issue(request, project_id):
        issue = IssueSerializer(data=request.data)
        if issue.is_valid():
            issue.save()
        return Response(issue.data)

    @api_view(['PUT'])
    def update_issue(request, issue_id):
        issue = Issue.objects.get(id=issue_id)
        issue_serializer = IssueSerializer(issue, data=request.data)
        if issue_serializer.is_valid():
            issue_serializer.save()
        return Response(issue_serializer.data)

    @api_view(['DELETE'])
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

    @api_view(['GET'])
    def get_comments(request, issue_id):
        comments = Comment.objects.filter(issue_id=issue_id)
        comments_serializer = CommentSerializer(comments, many=True)
        return Response(comments_serializer.data)

    @api_view(['GET'])
    def get_comment(request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment_serializer = CommentSerializer(comment)
        return Response(comment_serializer.data)

    @api_view(['POST'])
    def create_comment(request, issue_id):
        comment = CommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(comment.data)

    @api_view(['PUT'])
    def update_comment(request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment_serializer = CommentSerializer(comment, data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
        return Response(comment_serializer.data)

    @api_view(['DELETE'])
    def delete_comment(request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return Response(status=204)
