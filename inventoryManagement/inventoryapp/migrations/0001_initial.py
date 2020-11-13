# Generated by Django 2.2.5 on 2020-11-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArrivalLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('quantity', models.FloatField(default=0.0, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ColorRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('supplier', models.CharField(max_length=50)),
                ('order_date', models.DateField(default=None)),
                ('order_no', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('rate', models.FloatField()),
                ('amount', models.FloatField(max_length=15)),
                ('state', models.CharField(max_length=50)),
                ('recieving_date', models.DateField(default=None, null=True)),
                ('total_quantity', models.IntegerField()),
                ('godown', models.CharField(default='-', max_length=50)),
                ('lease', models.CharField(default='-', max_length=50)),
                ('lease_date', models.DateField(default=None, null=True)),
                ('a_date', models.DateField(default=None, null=True)),
                ('b_date', models.DateField(default=None, null=True)),
                ('a', models.CharField(default='-', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ColorSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DailyConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_date', models.DateField(default=None, null=True)),
                ('color', models.CharField(default='-', max_length=50)),
                ('quantity', models.FloatField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessingPartyName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processing_party', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualities', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('party_name', models.CharField(default='no', max_length=50)),
                ('bill_no', models.IntegerField()),
                ('bill_date', models.CharField(max_length=30)),
                ('bill_amount', models.FloatField(max_length=15)),
                ('lot_no', models.IntegerField()),
                ('quality', models.CharField(max_length=100)),
                ('than', models.IntegerField()),
                ('mtrs', models.FloatField(max_length=15)),
                ('bale', models.IntegerField()),
                ('rate', models.FloatField(max_length=15)),
                ('lr_no', models.IntegerField()),
                ('order_no', models.IntegerField()),
                ('state', models.CharField(default='Transit', max_length=30)),
                ('bale_recieved', models.IntegerField(default=0)),
                ('recieving_date', models.DateField(default=None, null=True)),
                ('processing_party_name', models.CharField(default='-', max_length=50)),
                ('total_bale', models.IntegerField()),
                ('checking_date', models.DateField(default=None, null=True)),
                ('processing_type', models.CharField(default='-', max_length=50)),
                ('sent_to_processing_date', models.DateField(default=None, null=True)),
                ('arrival_location', models.CharField(default='-', max_length=50)),
                ('recieve_processed_date', models.DateField(default=None, null=True)),
                ('total_thans', models.IntegerField()),
                ('total_mtrs', models.FloatField()),
                ('tally', models.BooleanField(default=False)),
            ],
        ),
    ]
