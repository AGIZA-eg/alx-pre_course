# Generated by Django 4.2.5 on 2023-09-25 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src_users', '0002_user_created_user_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]