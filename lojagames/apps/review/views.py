from django.shortcuts import render
from django.http import JsonResponse
#from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializer import ReviewSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def review_list(request):

        user = request.user
        if review_list.author != user:
             return Response({'response':'You dont have permission'})
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def review_create(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors) 



#class GamesViewSet(viewsets.ModelViewSet):
#  queryset = Games.objects.all()
#  serializer_class = GamesSerializer