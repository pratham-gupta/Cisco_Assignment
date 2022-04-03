# Generated by Django 4.0.3 on 2022-04-02 19:10

from django.db import migrations, models
import router_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('router_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sapid', models.CharField(max_length=18)),
                ('hostname', models.CharField(max_length=14)),
                ('loopback', models.GenericIPAddressField(unique=True)),
                ('macaddress', models.CharField(max_length=17, validators=[router_api.models.validate_mac_address])),
            ],
        ),
    ]
