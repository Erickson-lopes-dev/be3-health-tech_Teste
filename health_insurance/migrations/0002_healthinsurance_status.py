# Generated by Django 3.2.3 on 2021-06-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_insurance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthinsurance',
            name='status',
            field=models.CharField(default='Ativo', max_length=100),
        ),
    ]
