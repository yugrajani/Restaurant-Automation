# Generated by Django 2.2 on 2019-04-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbconnection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.IntegerField()),
                ('menu_item', models.CharField(max_length=100)),
                ('item_quantity', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'currentorder',
            },
        ),
    ]
