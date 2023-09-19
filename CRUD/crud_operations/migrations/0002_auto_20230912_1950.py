# Generated by Django 3.2.7 on 2023-09-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_operations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_desc', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('task_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]