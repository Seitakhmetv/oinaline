from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import Http404
from api.models import Platform, Publisher, Genre, Type, Screenshot, Game
from api.serializers import PlatformSerializer, PublisherSerializer, GenreSerializer, TypeSerializer, ScreenshotSerializer, GameSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
# Create your views here.

@api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
def platform_list(request):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    if request.method == 'GET':
        array = Platform.objects.all()
        serializer = PlatformSerializer(array, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
def get_platform(request, id):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    try:
        platform = Platform.objects.get(id=id)
    except Platform.DoesNotExist as e:
        return Response({'message': str(e)}, status=404)

    if request.method == 'GET':
        serializer = PlatformSerializer(platform)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PlatformSerializer(instance=platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        platform.delete()
        return Response({'message': 'deleted'}, status=204)

class PublisherListAPIVIEW(APIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        array = Publisher.objects.all()
        serializer = PublisherSerializer(array, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class GetPublisherAPIVIEW(APIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Publisher.objects.get(id=pk)
        except Publisher.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        publisher = self.get_object(pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)

    def put(self, request, pk=None):
        publisher = self.get_object(pk)
        serializer = PublisherSerializer(instance=publisher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        publisher = self.get_object(pk)
        publisher.delete()
        return Response({'message': 'deleted'}, status=204)

#Generics-----------------------------------------------
########################################################
class GenreList(ListCreateAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def get_queryset(self):
        return super().get_queryset()

class GetGenreAPIVIEW(RetrieveUpdateDestroyAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    lookup_field = "id"
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def get_queryset(self):
        return super().get_queryset()

########################################################

class TypeList(ListCreateAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def get_queryset(self):
        return super().get_queryset()

class GetTypeAPIVIEW(RetrieveUpdateDestroyAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    lookup_field = "id"
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def get_queryset(self):
        return super().get_queryset()

########################################################

class ScreenshotList(ListCreateAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    serializer_class = ScreenshotSerializer
    queryset = Screenshot.objects.all()
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def get_queryset(self):
        return super().get_queryset()

class GetScreenshotAPIVIEW(RetrieveUpdateDestroyAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    serializer_class = ScreenshotSerializer
    queryset = Screenshot.objects.all()
    lookup_field = "id"
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def get_queryset(self):
        return super().get_queryset()

########################################################

class GameList(ListCreateAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def get_queryset(self):
        return super().get_queryset()

class GetGameAPIVIEW(RetrieveUpdateDestroyAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    lookup_field = "id"
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def get_queryset(self):
        return super().get_queryset()

########################################################