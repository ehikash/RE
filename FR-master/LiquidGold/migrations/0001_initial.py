# Generated by Django 4.0 on 2022-01-26 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeiselReport',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('del_flag', models.CharField(blank=True, max_length=255, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('version', models.IntegerField()),
                ('actual_remaining_litres', models.CharField(blank=True, max_length=255, null=True)),
                ('expected_remaining_litres', models.CharField(blank=True, max_length=255, null=True)),
                ('gen_run_hour', models.CharField(blank=True, max_length=255, null=True)),
                ('indicative_consumption', models.CharField(blank=True, max_length=255, null=True)),
                ('actual_consumption', models.CharField(blank=True, max_length=255, null=True)),
                ('reference_top_up_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'deisel_report',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('del_flag', models.CharField(blank=True, max_length=255, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('version', models.IntegerField()),
                ('change_password', models.TextField()),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('enabled', models.TextField()),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_logged_on', models.TextField()),
                ('last_login_date', models.DateTimeField(blank=True, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('no_of_wrong_login_count', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('user_name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('zendesk_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'engineer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FuelTopUp',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('del_flag', models.CharField(blank=True, max_length=255, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('version', models.IntegerField()),
                ('fuel_level_after_top_up', models.CharField(blank=True, max_length=255, null=True)),
                ('fuel_level_before_top_up', models.CharField(blank=True, max_length=255, null=True)),
                ('generator_run_hours', models.CharField(blank=True, max_length=255, null=True)),
                ('litres', models.CharField(blank=True, max_length=255, null=True)),
                ('percentage_loading', models.CharField(blank=True, max_length=255, null=True)),
                ('top_up_date', models.DateTimeField(blank=True, null=True)),
                ('vendors', models.CharField(blank=True, max_length=255, null=True)),
                ('gen_run_hour_pic_id', models.CharField(blank=True, max_length=255, null=True)),
                ('gen_run_hour_pic_url', models.CharField(blank=True, max_length=255, null=True)),
                ('job_completion_form1', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'fuel_top_up',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('del_flag', models.CharField(blank=True, max_length=255, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('version', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('zone', models.CharField(blank=True, max_length=255, null=True)),
                ('no_of_ac_installed', models.CharField(blank=True, max_length=255, null=True)),
                ('nof_panels', models.CharField(blank=True, max_length=255, null=True)),
                ('sudo_name', models.CharField(blank=True, max_length=255, null=True)),
                ('fuel_tank_size', models.CharField(blank=True, max_length=255, null=True)),
                ('generator_size', models.CharField(blank=True, max_length=255, null=True)),
                ('gen_run_hour_date', models.DateTimeField(blank=True, null=True)),
                ('last_ac_maintenance_date', models.DateTimeField(blank=True, null=True)),
                ('last_generator_service_hour', models.BigIntegerField(blank=True, null=True)),
                ('last_panel_maintenance_date', models.DateTimeField(blank=True, null=True)),
                ('last_preventive_maintenance', models.TextField(blank=True, null=True)),
                ('last_preventive_maintenance_date', models.DateTimeField(blank=True, null=True)),
                ('last_recorded_run_hour', models.BigIntegerField(blank=True, null=True)),
                ('next_ac_maintenance_date', models.DateTimeField(blank=True, null=True)),
                ('next_panel_maintenance_date', models.DateTimeField(blank=True, null=True)),
                ('victron_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('current_fuel_level', models.BigIntegerField(blank=True, null=True)),
                ('fuel_level_date', models.DateTimeField(blank=True, null=True)),
                ('communicating', models.CharField(blank=True, max_length=255, null=True)),
                ('phcn', models.CharField(blank=True, max_length=255, null=True)),
                ('average_daily_fuel_usage', models.CharField(blank=True, max_length=255, null=True)),
                ('average_gen_daily_run_hour', models.BigIntegerField(blank=True, null=True)),
                ('hours_to_service', models.BigIntegerField(blank=True, null=True)),
                ('next_service_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiteReport',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('del_flag', models.CharField(blank=True, max_length=255, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('version', models.IntegerField()),
                ('ac_status_report', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
                ('connected', models.CharField(blank=True, max_length=255, null=True)),
                ('current_fuel_level', models.CharField(blank=True, max_length=255, null=True)),
                ('engineer', models.TextField(blank=True, null=True)),
                ('generator_age', models.CharField(blank=True, max_length=255, null=True)),
                ('generator_brand', models.CharField(blank=True, max_length=255, null=True)),
                ('generator_size', models.CharField(blank=True, max_length=255, null=True)),
                ('generator_status_report', models.TextField(blank=True, null=True)),
                ('inverter_status', models.CharField(blank=True, max_length=255, null=True)),
                ('last_delivery_date', models.CharField(blank=True, max_length=255, null=True)),
                ('last_delivery_quantity', models.CharField(blank=True, max_length=255, null=True)),
                ('last_gen_service_hours', models.CharField(blank=True, max_length=255, null=True)),
                ('last_panel_cleaning', models.CharField(blank=True, max_length=255, null=True)),
                ('last_service_date', models.CharField(blank=True, max_length=255, null=True)),
                ('lighting_status_report', models.CharField(blank=True, max_length=255, null=True)),
                ('load_on_critical_inverter_total', models.CharField(blank=True, max_length=255, null=True)),
                ('load_onl1', models.CharField(blank=True, max_length=255, null=True)),
                ('load_onl2', models.CharField(blank=True, max_length=255, null=True)),
                ('load_onl3', models.CharField(blank=True, max_length=255, null=True)),
                ('next_delivery_due_date', models.CharField(blank=True, max_length=255, null=True)),
                ('next_panel_cleaning', models.CharField(blank=True, max_length=255, null=True)),
                ('next_service_date', models.CharField(blank=True, max_length=255, null=True)),
                ('next_service_due', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_panels', models.CharField(blank=True, max_length=255, null=True)),
                ('pv_harvest_status', models.CharField(blank=True, max_length=255, null=True)),
                ('run_hour', models.CharField(blank=True, max_length=255, null=True)),
                ('site', models.TextField(blank=True, null=True)),
                ('solar_strings', models.CharField(blank=True, max_length=255, null=True)),
                ('status_report', models.CharField(blank=True, max_length=255, null=True)),
                ('torque_level_check_date', models.CharField(blank=True, max_length=255, null=True)),
                ('time_sheet_end', models.CharField(blank=True, max_length=255, null=True)),
                ('time_sheet_start', models.CharField(blank=True, max_length=255, null=True)),
                ('battery_appearance_ok', models.CharField(blank=True, max_length=255, null=True)),
                ('battery_temperature_ok', models.CharField(blank=True, max_length=255, null=True)),
                ('battery_terminal_ok', models.CharField(blank=True, max_length=255, null=True)),
                ('site_communicating', models.CharField(blank=True, max_length=255, null=True)),
                ('date_ac_issue_report', models.CharField(blank=True, max_length=255, null=True)),
                ('no_of_fault_ac', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('extra_image1', models.CharField(blank=True, max_length=255, null=True)),
                ('extra_image2', models.CharField(blank=True, max_length=255, null=True)),
                ('extra_image3', models.CharField(blank=True, max_length=255, null=True)),
                ('extra_image4', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'site_report',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DieselRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestdate', models.DateField(auto_now_add=True)),
                ('request_time', models.TimeField(auto_now_add=True, null=True)),
                ('mgr_approved_date', models.DateTimeField(auto_now=True, null=True)),
                ('cto_approved_date', models.DateTimeField(auto_now=True, null=True)),
                ('phcn_comment', models.CharField(blank=True, max_length=2000, null=True)),
                ('quantity_required', models.IntegerField(blank=True, null=True)),
                ('justification', models.CharField(blank=True, max_length=3000, null=True)),
                ('noc_approve', models.BooleanField(blank=True, null=True)),
                ('cto_approve', models.BooleanField(blank=True, null=True)),
                ('noc_comment', models.CharField(blank=True, max_length=3000, null=True)),
                ('cto_comment', models.CharField(blank=True, max_length=3000, null=True)),
                ('noc_status', models.CharField(choices=[('Approved', 'approved'), ('Rejected', 'rejected'), ('Pending', 'pending')], default='Pending', max_length=10)),
                ('cto_status', models.CharField(choices=[('Approved', 'approved'), ('Rejected', 'rejected'), ('Pending', 'pending')], default='Pending', max_length=10)),
                ('engineer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='LiquidGold.engineer', verbose_name='Confirm Engineer')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='LiquidGold.site', verbose_name='Confirm Site')),
            ],
            options={
                'verbose_name_plural': 'Diesel Requests',
                'ordering': ['-requestdate'],
            },
        ),
    ]
