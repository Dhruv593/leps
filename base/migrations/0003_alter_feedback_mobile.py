# Generated by Django 5.0.4 on 2024-04-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_loan_data_loan_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
    ]
