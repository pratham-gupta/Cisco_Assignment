from enum import unique
from django.db import models
import re
from django.core.exceptions import ValidationError
# Create your models here.

def validate_mac_address(mac_value):

    """
    Args: mac_value: 17 digit mac address
    Returns: bool True if valid else False

    Customer validation for macaddress field in Router Model
    Checks if given mac address is valid or not.
    """

    MAC_RE = r'^([0-9a-fA-F]{2}([:-]?|$)){6}$'
    mac_re = re.compile(MAC_RE)

    if re.fullmatch(mac_re,mac_value):
        return mac_value
    else:
        raise ValidationError('Invalid mac address')


class Router(models.Model):
    """Router Model to save router details
    Sapid,Hostname, IPAddress (ipv4) and Mac Address"""
    
    router_id = models.IntegerField(primary_key=True)
    sapid = models.CharField(max_length=18,null=False)
    hostname = models.CharField(max_length=14)
    loopback = models.GenericIPAddressField(unique=True,null=False)
    macaddress = models.CharField(max_length=17,validators=[validate_mac_address])

    # class meta:
    #     table_name = "Router_Details"