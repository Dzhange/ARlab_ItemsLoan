# Generated by Django 2.0.7 on 2018-09-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0012_auto_20180922_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='spec',
            field=models.CharField(choices=[('SC', 'Boot C in 302'), ('FR', '301'), ('SD', 'Boot D in 302'), ('SB', 'Boot B in 302'), ('ST', 'All Boots(ABCD) in 302'), ('SA', 'Boot A in 302')], max_length=2),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='spec',
            field=models.CharField(choices=[('EP', 'EarPhone'), ('DT', 'Ddesktop'), ('MC', 'iMac'), ('SP', 'Speaker'), ('PT', 'Printer')], max_length=20),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='status',
            field=models.CharField(choices=[('TB', 'Toltally Broken'), ('PF', 'Perfect'), ('SB', 'Slightly Broken')], max_length=2),
        ),
    ]
