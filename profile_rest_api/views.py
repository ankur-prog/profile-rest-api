from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """ Test API View"""

    def get(self, request, format=None):
        """ Return a list of API views """

        an_apiview = ['Test1','Test2','Test3']



        return Response({'message':"hello",'an_apiview':an_apiview})
