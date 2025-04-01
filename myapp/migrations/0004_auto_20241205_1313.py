# Generated by Django 3.1.12 on 2024-12-05 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20241205_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='myapp.customer'),
            preserve_default=False,
        ),
    ]
