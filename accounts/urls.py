from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CustomerRegisterView,AdminRegisterView,StaffRegisterView, LoginView

router = DefaultRouter()
router.register("register/customer", CustomerRegisterView, basename="customer_register"),
router.register("register/admin", AdminRegisterView, basename="admin_register"),
router.register("register/staff", StaffRegisterView, basename="staff_regiter"),
router.register("login", LoginView, basename="login")

urlpatterns = [
    path("",include(router.urls))
]

