from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
