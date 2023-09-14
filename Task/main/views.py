from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Customer
from .serializers import CustomerRegistrationSerializer
from django.views.generic import DetailView

class CustomerRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = CustomerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Create a new customer
            customer = Customer.objects.create(
                name=name,
                email=email,
                password=password
            )

            # Generate JWT tokens
            refresh = RefreshToken.for_user(customer)
            access_token = str(refresh.access_token)

            # Create a link for the user's profile (you can customize this)
            profile_link = f"https://127.0.0.1/profile/{customer.id}/"

            return Response(
                {
                    'access_token': access_token,
                    'refresh_token': str(refresh),
                    'profile_link': profile_link
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerProfileView(DetailView):
    model = Customer
    template_name = 'profile.html'
    context_object_name = 'customer'
    pk_url_kwarg = 'id'
