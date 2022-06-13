from django.shortcuts import render

from .models import Todolist
from .serializers import TodoSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin

# Create your views here.
class CreateView(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Todolist.objects.all()
    serializer_class = TodoSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class UpdatedeleteRetrive(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
    queryset = Todolist.objects.all()
    serializer_class = TodoSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)