# Generated by Django 4.1.3 on 2023-03-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]