from django.contrib import admin
from django.urls import path
from main.views import CustomerRegistrationView, CustomerProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', CustomerRegistrationView.as_view(), name='customer-registration'),
    path('profile/<int:id>/', CustomerProfileView.as_view(), name='customer-profile'),
]
