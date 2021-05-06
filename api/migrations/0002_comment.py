# Generated by Django 3.2 on 2021-05-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('nickname', models.CharField(blank=True, max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]