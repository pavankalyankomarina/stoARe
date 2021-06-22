# Generated by Django 3.2.4 on 2021-06-22 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210622_0531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='image',
        ),
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='shop.image'),
        ),
    ]
