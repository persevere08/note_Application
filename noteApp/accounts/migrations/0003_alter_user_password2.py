# Generated by Django 4.2.17 on 2024-12-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_password2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password2',
            field=models.CharField(default='', max_length=255),
        ),
    ]
