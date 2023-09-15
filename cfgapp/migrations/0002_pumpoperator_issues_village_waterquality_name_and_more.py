# Generated by Django 4.1.5 on 2023-07-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfgapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PumpOperator',
            fields=[
                ('phone', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='issues',
            name='village',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='waterquality',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='waterquality',
            name='village',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]