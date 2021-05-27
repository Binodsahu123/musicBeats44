# Generated by Django 2.2.5 on 2021-01-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0003_likedsong'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('singer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/Singer')),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(choices=[('Album', 'Album'), ('Bollywood', 'Bollywood'), ('Hollywood', 'Hollywood'), ('Rajasthani', 'Rajasthani'), ('Haryanvi', 'Haryanvi'), ('Punjabi', 'Punjabi')], default='Album', max_length=20),
        ),
        migrations.AddField(
            model_name='song',
            name='year',
            field=models.CharField(choices=[('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2015', '2015'), ('2010', '2010'), ('2005', '2005'), ('2000', '2000'), ('1995', '1995'), ('1990', '1990'), ('1985', '1985'), ('2000', '2000')], default='2021', max_length=20),
        ),
    ]