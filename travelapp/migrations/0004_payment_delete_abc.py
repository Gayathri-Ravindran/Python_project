# Generated by Django 4.2.3 on 2023-08-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_abc_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pic')),
                ('dec', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='abc',
        ),
    ]
