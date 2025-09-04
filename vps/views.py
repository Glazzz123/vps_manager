from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import VPS
from .serializers import VPSSerializer

class VPSViewSet(viewsets.ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['status', 'cpu', 'ram', 'hdd']
    ordering_fields = ['cpu', 'ram', 'hdd']

    @action(detail=True, methods=['patch'])
    def change_status(self, request, pk=None):
        vps = self.get_object()
        status = request.data.get('status')
        if status in dict(VPS.STATUS_CHOICES):
            vps.status = status
            vps.save()
            return Response({'status': 'Status updated successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
