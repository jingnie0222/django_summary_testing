# Generated by Django 2.1.1 on 2019-08-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.CharField(default='', max_length=50)),
                ('start_time', models.CharField(default='', max_length=50)),
                ('end_time', models.CharField(default='', max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('step', models.IntegerField(default=-1)),
                ('testitem', models.IntegerField(default=0)),
                ('newdataip', models.CharField(default='', max_length=500)),
                ('newdatauser', models.CharField(default='', max_length=500)),
                ('newdatapassw', models.CharField(default='', max_length=500)),
                ('newdatapath', models.CharField(default='', max_length=500)),
                ('newconfip', models.CharField(default='', max_length=500)),
                ('newconfuser', models.CharField(default='', max_length=500)),
                ('newconfpassw', models.CharField(default='', max_length=500)),
                ('newconfpath', models.CharField(default='', max_length=500)),
                ('runningIP', models.CharField(default='', max_length=50)),
                ('testsvn', models.TextField(default='')),
                ('basesvn', models.TextField(default='')),
                ('errorlog', models.TextField(default='')),
                ('cost_test', models.TextField(default='')),
                ('cost_base', models.TextField(default='')),
                ('result_diff_precent', models.TextField(default='')),
                ('test_cpu_performance', models.TextField(default='')),
                ('base_cpu_performance', models.TextField(default='')),
                ('regression_test_result', models.TextField(default='')),
                ('cache_compatibility', models.TextField(default='')),
                ('probe_result', models.TextField(default='')),
                ('stress_test_cpu', models.TextField(default='')),
                ('stress_test_cost', models.TextField(default='')),
                ('stress_test_qps', models.TextField(default='')),
                ('stress_test_heap', models.TextField(default='')),
                ('stress_test_memory', models.TextField(default='')),
                ('exceptions', models.TextField(default='')),
                ('is_freeze', models.BooleanField(default=False)),
                ('if_startmem', models.BooleanField(default=True)),
                ('remarks', models.TextField(default='')),
                ('result_hcyzx', models.TextField(default='')),
                ('result_dmfgl', models.TextField(default='')),
                ('result_kpdiff', models.TextField(default='')),
                ('pvscheck_block_num', models.IntegerField(default=-1)),
                ('pvscheck_result_link', models.TextField(default='')),
            ],
        ),
    ]
