from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Testing an API view"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        'Uses HTTP Methods as function (put,post,patch,get,delete)',
        'Is similar to a traditional Django view',
        'Gives you the most control over the application logic',
        'Is manually mapped to URLs',
        ]

        return Response({'message':'Hello !','an_apiview':an_apiview})
