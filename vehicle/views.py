from rest_framework.viewsets import ModelViewSet

from vehicle.models import Car
from vehicle.serializers import CarSerializer


class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

