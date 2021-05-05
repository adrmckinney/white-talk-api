"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from core import views
from core import views as api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('users', views.UserViewSet, basename='user')
# router.register('posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/users/', views.UserView.as_view()),
    path('api/users/me/', views.LoggedInUserView.as_view()),
    path('api/users/<int:pk>/', views.UpdateUserView.as_view()),
    path('api/session-register/', api_views.SessionRegisterView.as_view()),
    path('api/sessions/', api_views.Sessions.as_view()),
    path('api/create-session/', api_views.CreateSession.as_view()),
    path('api/delete-session/<int:pk>/', api_views.DeleteSession.as_view()),
    path('api/update-session/<int:pk>/', api_views.UpdateSession.as_view()),
    path('api/delete-registrant/<int:pk>/',
         api_views.DeleteSessionRegistrant.as_view()),
    path('api/update-registrant/<int:pk>/',
         api_views.UpdateSessionRegistrant.as_view()),
    path('password/reset/confirm/<int:uid>/<int:token>',
         api_views.UserView.as_view()),
]

urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
