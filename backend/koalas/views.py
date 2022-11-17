from rest_framework import generics

from .models import KoalaDB
from .serializers import KoalaDBSerializer

class KoalaDetailAPIView(generics.RetrieveAPIView):
    queryset = KoalaDB.objects.all()
    serializer_class = KoalaDBSerializer
    # lookup_field = 'pk' ??

koala_detail_view = KoalaDetailAPIView.as_view()

class KoalaCreateAPIView(generics.CreateAPIView):
    queryset = KoalaDB.objects.all()
    serializer_class = KoalaDBSerializer
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        serializer.save()

koala_create_view = KoalaCreateAPIView.as_view()

class KoalaListAPIView(generics.ListAPIView):
    queryset = KoalaDB.objects.all()
    serializer_class = KoalaDBSerializer

koala_list_view = KoalaListAPIView.as_view()