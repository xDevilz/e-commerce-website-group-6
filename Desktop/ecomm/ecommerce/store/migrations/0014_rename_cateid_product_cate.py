# Generated by Django 3.2.9 on 2021-12-20 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_cate_product_cateid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='CateID',
            new_name='Cate',
        ),
    ]
