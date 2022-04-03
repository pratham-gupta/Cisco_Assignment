from rest_framework import serializers
from router_api.models import Router
from router_api.models import validate_mac_address


class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = ('router_id','sapid',"hostname",'loopback','macaddress')


class CreateRouterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Router
        fields = ("sapid","hostname",'loopback','macaddress')

class UpdateRouterSerializer(serializers.Serializer):
    sapid = serializers.CharField(max_length=18)
    hostname = serializers.CharField(max_length=14)
    loopback = serializers.IPAddressField()
    macaddress = serializers.CharField(max_length=17,validators = [validate_mac_address])
    
    # class Meta:
    #     model = Router
    #     fields = ('sapid','hostname','macaddress','loopback')