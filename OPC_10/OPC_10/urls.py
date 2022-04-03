"""OPC_10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from SoftDesk.views import ContributorViewSet, IssueViewSet, ProjectViewSet, UserViewSet, CommentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register('user', UserViewSet, 'user')
router.register('projects', ProjectViewSet, 'projects')


project_router = routers.NestedSimpleRouter(
    router, 'projects', lookup='project')
project_router.register('contributors', ContributorViewSet, 'contributors')
project_router.register('issues', IssueViewSet, 'issues')


issues_router = routers.NestedSimpleRouter(
    project_router, 'issues', lookup='issue')
issues_router.register('comments', CommentViewSet, 'comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issues_router.urls)),
]
