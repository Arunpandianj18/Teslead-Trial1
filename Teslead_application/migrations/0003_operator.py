# Generated by Django 5.0.6 on 2024-10-23 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teslead_application', '0002_cell_rename_first_name_firstname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cell_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teslead_application.cell')),
            ],
        ),
    ]
