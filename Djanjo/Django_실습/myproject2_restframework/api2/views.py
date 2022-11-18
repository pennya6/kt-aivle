from rest_framework import viewsets
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.views import APIView
from django.contrib.auth.models import User
from api2.serializers import *
from blog.models import *

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

class PostListView(ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostListSerializer

class PostRetrieveView(RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostRetrieveSerializer
    
class CommentView(CreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    
# class PostLikeAPIView(UpdateAPIView):
#     queryset=Post.objects.all()
#     serializer_class=PostLikeSerializer
    
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         data={'like':instance.like+1}
#         serializer = self.get_serializer(instance, data=data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         if getattr(instance, '_prefetched_objects_cache', None):
#             # If 'prefetch_related' has been applied to a queryset, we need to
#             # forcibly invalidate the prefetch cache on the instance.
#             instance._prefetched_objects_cache = {}

#         return Response(data['like'])

# get방식으로 처리
class PostLikeAPIView(GenericAPIView):
    queryset=Post.objects.all()
    def get(self,request,*args,**kwargs):
        instance=self.get_object()
        instance.like +=1
        instance.save()
        return Response(instance.like)
        
    