# Generated by Django 5.1 on 2024-09-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_medication_price_prescriptionmedication'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
