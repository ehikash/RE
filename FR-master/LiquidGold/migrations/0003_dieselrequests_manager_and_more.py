# Generated by Django 4.0 on 2022-02-01 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LiquidGold', '0002_alter_dieselrequests_cto_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dieselrequests',
            name='manager',
            field=models.ForeignKey(default=1, limit_choices_to={'type': 'MANAGER'}, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='LiquidGold.engineer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dieselrequests',
            name='cto_status',
            field=models.CharField(choices=[('approved', 'approved'), ('rejected', 'rejected'), ('pending', 'pending'), ('confirmed', 'confirmed')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='dieselrequests',
            name='noc_status',
            field=models.CharField(choices=[('approved', 'approved'), ('rejected', 'rejected'), ('pending', 'pending'), ('confirmed', 'confirmed')], default='pending', max_length=10),
        ),
    ]