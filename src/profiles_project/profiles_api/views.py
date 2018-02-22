# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response 
from . import serializers


class HelloApiView (APIView):
  serializer_class=serializers.HelloSerializer
  def get(self,request,format=None):
    an_api_view=[
      'Uses Http Method sdklsdfk lsdf sf ',
      'sadsada sdsad ad asd sad ',
      'sfskldfj kdsjfmskdjf ksdf sdjf ',
      'sdfsd fdfk ldfkdlfk fkdlf kdf '
    ]
    return Response({'message':'hello Spi ','an_api_view':an_api_view})
  def post(self,request):
    """Create a ahello Post in rest framework  """
    serializer=serializers.HelloSerializer(data=request.data)
    if serializer.is_valid():
      name=serializer.data.get('name')
      message="Hello  {0}".format(name)
      return Response({'message':message,'serializers':'serializer'})
    else:
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
