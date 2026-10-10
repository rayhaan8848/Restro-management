from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView

router = DefaultRouter()
router.register("register", RegisterView, basename="register")
router.register("login", LoginView, basename="login")

urlpatterns = [
    path("",include(router.urls))
]

