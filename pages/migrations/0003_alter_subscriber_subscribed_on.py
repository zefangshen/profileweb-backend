# Generated by Django 5.0.7 on 2024-07-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_project_summary_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='subscribed_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]