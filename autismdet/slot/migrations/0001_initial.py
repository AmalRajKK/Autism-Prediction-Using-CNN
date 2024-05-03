# Generated by Django 3.2.23 on 2024-01-09 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('slot_number', models.CharField(max_length=45)),
                ('from_field', models.CharField(db_column='from', max_length=45)),
                ('to', models.CharField(max_length=45)),
                ('date', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'slot',
                'managed': False,
            },
        ),
    ]