from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.generics import CreateAPIView

from app.models import Group
from app.serializers import GroupSerializer, RawGroupItemsSerializer


class GroupViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    """
    Allows Read/List/Delete the group
    """
    queryset = Group.objects.prefetch_related('items').all()
    serializer_class = GroupSerializer


class GroupCreateAPIView(CreateAPIView):
    """
    Performs export from the raw list of strings
    """
    serializer_class = RawGroupItemsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('groups-list')
        return Response(serializer.errors)
