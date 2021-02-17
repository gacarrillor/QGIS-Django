# Generated by Django 2.2.13 on 2021-02-10 19:06

from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    Geopackage = apps.get_model('geopackages', 'Geopackage')
    for row in Geopackage.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('geopackages', '0006_add_uuid_field'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop)
    ]
