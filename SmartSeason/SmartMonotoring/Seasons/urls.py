from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Seasons import views
from .views import UserViewSet, FieldViewSet, UpdateViewSet
from .views import login_view, signup_view, dashboard


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'fields', FieldViewSet)
router.register(r'updates', UpdateViewSet)

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', include(router.urls)),
]
