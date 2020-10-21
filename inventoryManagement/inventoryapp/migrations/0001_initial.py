# Generated by Django 3.1.2 on 2020-10-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('party_name', models.CharField(default='no', max_length=50)),
                ('bill_no', models.IntegerField()),
                ('bill_date', models.CharField(max_length=10)),
                ('bill_amount', models.FloatField(max_length=15)),
                ('lot_no', models.IntegerField()),
                ('quality', models.CharField(max_length=100)),
                ('than', models.IntegerField()),
                ('mtrs', models.FloatField(max_length=15)),
                ('bale', models.IntegerField()),
                ('rate', models.FloatField(max_length=15)),
                ('lr_no', models.IntegerField()),
                ('order_no', models.IntegerField()),
                ('state', models.CharField(default='Transit', max_length=10)),
            ],
        ),
    ]
