# Generated by Django 4.2.7 on 2023-12-13 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0001_initial'),
        ('points', '0003_remove_point_samples_delete_pointsample'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='points.point')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.sample')),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='samples',
            field=models.ManyToManyField(through='points.PointSample', to='samples.sample'),
        ),
    ]
