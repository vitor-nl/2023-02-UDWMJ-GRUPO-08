from django.shortcuts import render
from django.http import JsonResponse
#from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Review
from rest_framework import status
from .serializer import ReviewSerializer
from user.views import user_login
from user.models import User


# Create your views here.

@api_view(['GET'])
@permission_classes((TokenAuthentication,))
def review_list(request):

        user = request.user
        if review_list.author != user:
             return Response({'response':'You dont have permission'})
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def review_create(request):
    user = User.objects.get(all)
    token = request.auth
    if token == user:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT', 'DELETE'])
def review(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except:
        return Response({
            'error': 'Review does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return serializer.errors
    
    if request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#class GamesViewSet(viewsets.ModelViewSet):
#  queryset = Games.objects.all()
#  serializer_class = GamesSerializer