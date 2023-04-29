# Generated by Django 4.2 on 2023-04-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('theme_color', models.CharField(max_length=7)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_open', models.BooleanField()),
            ],
            options={
                'ordering': ['name', 'date'],
            },
        ),
    ]
