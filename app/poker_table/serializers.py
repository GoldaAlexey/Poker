from rest_framework import serializers

from .models import Table

class TablesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = ["TableId", "TableName"]

class TableSerializer(serializers.ModelSerializer):
    TableName = serializers.CharField(max_length=500)
    PlayerIn = serializers.IntegerField()
    class Meta:
        model = Table
        fields = ["TableId", "TableName", "PlayerIn"]