from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomSerializer


class CustomRegisterView(RegisterView):
    serializer_class = CustomSerializer