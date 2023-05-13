# Generated by Django 4.0.10 on 2023-05-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0044_appointment_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_information',
            name='department',
            field=models.CharField(blank=True, choices=[('Cardiologists', 'Cardiologists'), ('Neurologists', 'Neurologists'), ('Pediatricians', 'Pediatricians'), ('Physiatrists', 'Psychiatrists'), ('Dermatologists', 'Dermatologists')], max_length=200, null=True),
        ),
    ]
