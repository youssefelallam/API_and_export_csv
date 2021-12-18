from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Prod
from .serializers import prodSerializer
from rest_framework import generics, serializers
from django.http import HttpResponse
import csv

class listProd(generics.ListCreateAPIView):
    queryset = Prod.objects.all()
    serializer_class = prodSerializer

class listProdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prod.objects.all()
    serializer_class = prodSerializer


def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Title','Date','Start Time','End Time','Task Stats'])

    for task in Prod.objects.all().values_list('title','date','startTime','endTime','complit'):
        writer.writerow(task)
    response['Content-Disposition'] = 'attachment; filename="Data.csv"'

    return response