# Generated by Django 4.1.4 on 2022-12-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tablea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col_1', models.CharField(blank=True, db_column='COL 1', max_length=9, null=True)),
                ('col_2', models.CharField(blank=True, db_column='COL 2', max_length=9, null=True)),
                ('col_3', models.CharField(blank=True, db_column='COL 3', max_length=11, null=True)),
                ('col_4', models.CharField(blank=True, db_column='COL 4', max_length=12, null=True)),
                ('col_5', models.CharField(blank=True, db_column='COL 5', max_length=14, null=True)),
                ('col_6', models.CharField(blank=True, db_column='COL 6', max_length=9, null=True)),
                ('col_7', models.CharField(blank=True, db_column='COL 7', max_length=15, null=True)),
                ('col_8', models.CharField(blank=True, db_column='COL 8', max_length=16, null=True)),
                ('col_9', models.CharField(blank=True, db_column='COL 9', max_length=14, null=True)),
                ('col_10', models.CharField(blank=True, db_column='COL 10', max_length=19, null=True)),
                ('col_11', models.CharField(blank=True, db_column='COL 11', max_length=13, null=True)),
                ('col_12', models.CharField(blank=True, db_column='COL 12', max_length=22, null=True)),
                ('col_13', models.CharField(blank=True, db_column='COL 13', max_length=9, null=True)),
                ('col_14', models.CharField(blank=True, db_column='COL 14', max_length=10, null=True)),
                ('col_15', models.CharField(blank=True, db_column='COL 15', max_length=12, null=True)),
                ('col_16', models.CharField(blank=True, db_column='COL 16', max_length=7, null=True)),
                ('col_17', models.CharField(blank=True, db_column='COL 17', max_length=13, null=True)),
                ('col_18', models.CharField(blank=True, db_column='COL 18', max_length=14, null=True)),
                ('col_19', models.CharField(blank=True, db_column='COL 19', max_length=12, null=True)),
                ('col_20', models.CharField(blank=True, db_column='COL 20', max_length=17, null=True)),
                ('col_21', models.CharField(blank=True, db_column='COL 21', max_length=11, null=True)),
                ('col_22', models.CharField(blank=True, db_column='COL 22', max_length=20, null=True)),
                ('col_23', models.CharField(blank=True, db_column='COL 23', max_length=12, null=True)),
                ('col_24', models.CharField(blank=True, db_column='COL 24', max_length=13, null=True)),
                ('col_25', models.CharField(blank=True, db_column='COL 25', max_length=15, null=True)),
                ('col_26', models.CharField(blank=True, db_column='COL 26', max_length=10, null=True)),
                ('col_27', models.CharField(blank=True, db_column='COL 27', max_length=16, null=True)),
                ('col_28', models.CharField(blank=True, db_column='COL 28', max_length=17, null=True)),
                ('col_29', models.CharField(blank=True, db_column='COL 29', max_length=15, null=True)),
                ('col_30', models.CharField(blank=True, db_column='COL 30', max_length=20, null=True)),
                ('col_31', models.CharField(blank=True, db_column='COL 31', max_length=14, null=True)),
                ('col_32', models.CharField(blank=True, db_column='COL 32', max_length=23, null=True)),
            ],
            options={
                'db_table': 'TABLEA',
                'managed': False,
            },
        ),
    ]
