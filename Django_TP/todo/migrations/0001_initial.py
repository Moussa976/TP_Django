# Generated by Django 3.0.3 on 2020-12-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('is_done', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]