# Generated by Django 5.1.3 on 2025-01-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(default='')),
                ('data', models.JSONField(blank=True, default=dict)),
                ('html', models.TextField(blank=True, default='')),
                ('css', models.TextField(blank=True, default='')),
            ],
        ),
    ]
