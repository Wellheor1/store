# Generated by Django 4.0.3 on 2022-04-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_orders_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Выполнен', 'Выполнен'), ('Отменён', 'Отменён'), ('Оплачен', 'Оплачен'), ('Новый', 'Новый')], default='Новый', max_length=50),
        ),
    ]
