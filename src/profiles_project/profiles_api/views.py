# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 


class HelloApiView (APIView):
    def get(self,request,format=None):
      an_api_view=[
        'Uses Http Method sdklsdfk lsdf sf ',
        'sadsada sdsad ad asd sad ',
        'sfskldfj kdsjfmskdjf ksdf sdjf ',
        'sdfsd fdfk ldfkdlfk fkdlf kdf '
      ]
      return Response({'message':'hello Spi ','an_api_view':an_api_view})