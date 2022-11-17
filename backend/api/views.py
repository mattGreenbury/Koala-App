import json
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from koalas.models import KoalaDB
from koalas.serializers import KoalaDBSerializer

@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    # DRF API View
    instance = KoalaDB.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(instance)
        data = KoalaDBSerializer(instance).data
    return Response(data)