# Generated by Django 3.1.7 on 2022-02-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20220202_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order_id',
            field=models.CharField(default='0', max_length=128),
        ),
    ]
