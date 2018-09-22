# Generated by Django 2.0.7 on 2018-09-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0010_auto_20180922_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='spec',
            field=models.CharField(choices=[('SD', 'Boot D in 302'), ('FR', '301'), ('SC', 'Boot C in 302'), ('SB', 'Boot B in 302'), ('SA', 'Boot A in 302'), ('ST', 'All Boots(ABCD) in 302')], max_length=2),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='spec',
            field=models.CharField(choices=[('SP', 'Speaker'), ('PT', 'Printer'), ('EP', 'EarPhone'), ('MC', 'iMac'), ('DT', 'Ddesktop')], max_length=20),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='status',
            field=models.CharField(choices=[('SB', 'Slightly Broken'), ('TB', 'Toltally Broken'), ('PF', 'Perfect')], max_length=2),
        ),
    ]