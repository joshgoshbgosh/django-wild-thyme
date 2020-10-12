from rest_framework import serializers


from menu.models import Menu_Item




class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_Item
        fields = ('name', 'price',)
