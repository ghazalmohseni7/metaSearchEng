from django.shortcuts import render
from metasearchengine import engine
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
class searchAPIView(APIView):
    def post(self,request,format=None):
        try:
            print("tru")
            search_key_word=request.POST['word']
            print(search_key_word)
            search_result=engine.returnie(search_key_word)
            print(search_result)
            data=[]
            return Response({'data':search_result},status=status.HTTP_200_OK)
        except:
            return Response({'status':'INTERNAL_SERVER_ERROR'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
