from django.utils.decorators import method_decorator
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView

from apps.users.decorators import login_required
from apps.users.models import User
from rest_framework.response import Response

from .serializers import ShopSerializer
from .models import Shop


class ShopsViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing user shops or retrieve shop by id.
    """
    @method_decorator(login_required())
    def list(self, request, token, *args, **kwargs):
        user = User.objects.get(token=token)
        queryset = Shop.objects.filter(owner=user)
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(login_required())
    def retrieve(self, request, token, *args, **kwargs):
        pk = kwargs['id']
        user = User.objects.get(token=token)
        queryset = Shop.objects.get(id=pk)
        serializer = ShopSerializer(queryset)
        return Response(serializer.data)

class CreateShop(CreateAPIView):
    """
    Create new shop.
    """
    @method_decorator(login_required())
    def post(self, request, token, *args, **kwargs):
        name = request.data.get('name')

        if not name:
            return JsonResponse({'message': 'Missing name parameter.'}, status=411)

        shop = Shop(
            name=name,
            owner=User.objects.get(token=token)
        )
        shop.save()

        return JsonResponse({'message': 'Shop has been created.'}, status=201)
