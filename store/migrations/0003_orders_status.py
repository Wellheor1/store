# Generated by Django 4.0.3 on 2022-04-07 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_nomenclature_count_nomenclature_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED'), ('PAID', 'PAID'), ('NEW', 'NEW')], default='NEW', max_length=50),
        ),
    ]
