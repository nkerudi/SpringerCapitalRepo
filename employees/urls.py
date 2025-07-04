from django.urls import path, include
from .views import trigger_seed
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("run-seed/", trigger_seed)
]


