from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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
