# Generated by Django 2.2.2 on 2019-06-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20190627_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burgers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numb', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('photo', models.ImageField(upload_to='photos/burgers/')),
                ('is_pub', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numb', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('photo', models.ImageField(upload_to='photos/drinks/')),
                ('is_pub', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numb', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('photo', models.ImageField(upload_to='photos/pasta/')),
                ('is_pub', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numb', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('photo', models.ImageField(upload_to='photos/pizza/')),
                ('is_pub', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]
