# Generated by Django 4.1.3 on 2023-01-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ho', models.CharField(max_length=255)),
                ('ten', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mat_khau', models.CharField(max_length=50)),
                ('dien_thoai', models.CharField(max_length=20)),
                ('dia_chi', models.TextField()),
            ],
        ),
    ]
