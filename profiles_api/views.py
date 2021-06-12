from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

#this is an APIView
class HelloApiView(APIView):
    """Testing an API view"""

    #This statement configures our APIView to have and apply the serializer class that we have created
    serializer_class = serializers.HelloSerializer


    def get(self,request,format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        'Uses HTTP Methods as function (put,post,patch,get,delete)',
        'Is similar to a traditional Django view',
        'Gives you the most control over the application logic',
        'Is manually mapped to URLs',
        ]

        return Response({'message':'Hello !','an_apiview':an_apiview})

    def post(self,request):
        """Return a hello message with the dummy name in the post call"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})


#this is a ViewSet
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self,request):
        """Create a new hello message"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by it's id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',) #adding serach filtering to email and name fields

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
