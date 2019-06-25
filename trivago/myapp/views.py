from django.shortcuts import render
import csv,os,re
from rest_framework import viewsets,generics
from .models import Solution, Clicks
from .serializers import SolutionSerializer, ClicksSerializer, AmenitySerializer
from rest_framework.views import APIView, Response

'''
Get all Solution entries
'''
class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

'''
Get all Clicks entries
'''
class ClicksViewSet(viewsets.ModelViewSet):
    queryset = Clicks.objects.all()
    serializer_class = ClicksSerializer

'''
To retrieve top amenity for a user
'''
class amenityList(generics.ListAPIView):
    serializer_class = AmenitySerializer

    def get_queryset(self):
        queryset = Solution.objects.all()
        # username = self.request.query_params.get('username')
        username = self.kwargs['username']
        username = re.sub(r'.*=','',username)
        print(username)
        if username is not None:
            queryset = Solution.objects.filter(user_id=username)
        return queryset

'''
To retrieve top clicks for a user
'''
class ClicksList(generics.ListAPIView):
    serializer_class = ClicksSerializer

    def get_queryset(self):
        queryset = Clicks.objects.all()
        username = self.kwargs['username']
        username = re.sub(r'.*=', '', username)
        print(username)
        if username is not None:
            queryset = Clicks.objects.filter(user_id=username)
        return queryset

'''
Load the data 
'''
class CustomView(APIView):
    def get(self, request, format=None):

        path = "C:\\backup\Lynda\projects\pro"
        os.chdir(path)

        # os.chdir(path)
        # C:\backup\Lynda\projects\pro
        print("Uploading selections")
        with open("C:\\backup\Lynda\projects\pro\selections.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p =list(row.values())
                q = Solution.objects.create(timestamp = p[0],user_id = p[1], amenity_id = p[2])
                q.save()
            print("uploaded selections.csv")

        print("Uploading clicks")
        with open("C:\\backup\Lynda\projects\pro\clicks.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p =list(row.values())
                q = Clicks.objects.create(timestamp = p[0],user_id = p[1], hotel_id = p[2], hotel_region=p[3])
                q.save()
            print("uploaded clicks.csv")
        return Response("Successfully Loaded Solution & clicks DB's")

    def post(self, request, format=None):
        return Response("Some Post Response")
