from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Table as Tables
from .serializers import TableSerializer, TablesListSerializer


class TableListView(APIView):
    def get(self, request):
        tables = Tables.objects.all()
        serializer = TablesListSerializer(tables, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TableView(APIView):
    def get(self, request, pk):
        table = Tables.objects.get(TableId=pk)
        serializer = TableSerializer(table)
        return Response(serializer.data)
    def put(self, request, pk):
        try:
            table = Tables.objects.get(pk=pk)
        except Tables.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TableSerializer(table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            table = Tables.objects.get(pk=pk)
        except Tables.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    