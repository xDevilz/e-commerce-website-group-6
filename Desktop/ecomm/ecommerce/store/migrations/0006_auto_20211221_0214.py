# Generated by Django 3.2.9 on 2021-12-20 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211221_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='UnitPrice',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='FullName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Mail',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Phone',
        ),
    ]