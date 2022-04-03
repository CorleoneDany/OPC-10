from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Project, Contributor

owner_methods = ("PUT", "DELETE")
contrib_methods = ("POST", "GET")

# has permission = route sans params donc get et list


class HasContributorPermission(BasePermission):
    # si request.user = autheur du projet donner tous les droits sur les contributeurs
    def has_permission(self, request, view):
        project = Project.objects.get(pk=view.kwargs['project_pk'])
        if request.user == project.author:
            return True


class HasProjectPermission(BasePermission):
    def has_permission(self, request, view):
        # si le contributor a accès aux projets (cls)
        if 'pk' in view.kwargs:
            return bool(
                Contributor.objects.filter(user=request.user)
                .filter(project=view.kwargs['pk'])
                .exists()
            )
        return True

    def has_object_permission(self, request, view, obj):
        # si le contributor a accès au projet (obj)
        if request.method in owner_methods:
            return obj.author == request.user
        elif request.method in contrib_methods:
            return bool(
                Contributor.objects.filter(user=request.user)
                .filter(project=view.kwargs['pk'])
                .exists()
            )
        return False


class HasIssuePermission(BasePermission):
    def has_permission(self, request, view):
        return bool(
            Contributor.objects.filter(user=request.user)
            .filter(project=view.kwargs['project_pk'])
            .exists()
        )

    def has_object_permission(self, request, view, obj):
        if request.method in owner_methods:
            return request.user == obj.author
        if obj.author == request.user:
            return True


class HasCommentPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(
            Contributor.objects.filter(user=request.user)
            .filter(project=view.kwargs['project_pk'])
            .exists()
        )

    def has_object_permission(self, request, view, obj):
        if request.method in owner_methods:
            return request.user == obj.author
