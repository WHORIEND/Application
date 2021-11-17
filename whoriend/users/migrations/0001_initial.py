# Generated by Django 3.2.7 on 2021-11-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('country', models.CharField(default='한국', max_length=20)),
                ('pic', models.ImageField(blank=True, upload_to='pic')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('can_teach', models.ManyToManyField(to='category.Detail_category')),
                ('interest', models.ManyToManyField(to='category.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
