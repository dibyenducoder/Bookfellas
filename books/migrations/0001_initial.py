# Generated by Django 2.2 on 2019-05-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField(max_length=200)),
                ('ratings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('desc', models.TextField(max_length=200)),
                ('ratings', models.DecimalField(decimal_places=2, max_digits=3)),
                ('pages', models.IntegerField()),
                ('publish_date', models.DateField()),
                ('author', models.ManyToManyField(to='books.Author')),
                ('genre', models.ManyToManyField(to='books.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='genre',
            field=models.ManyToManyField(to='books.Genre'),
        ),
    ]
