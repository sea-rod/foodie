# Generated by Django 4.2.1 on 2023-06-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customeraddresss_landmark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddresss',
            name='landmark',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customeraddresss',
            name='taluka',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customeraddresss',
            name='village_city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customeraddresss',
            name='ward',
            field=models.CharField(max_length=255, null=True),
        ),
    ]