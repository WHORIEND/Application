# Generated by Django 3.2.7 on 2021-11-17 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Detail_category',
            fields=[
                ('cid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('detail_name', models.CharField(max_length=30)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
