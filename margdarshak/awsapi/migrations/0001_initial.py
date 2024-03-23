# Generated by Django 5.0.3 on 2024-03-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Area",
            fields=[
                (
                    "area_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("area_name", models.CharField(max_length=255)),
                ("l1n1", models.CharField(max_length=100)),
                ("l2n2", models.CharField(max_length=100)),
                ("zone_id", models.CharField(max_length=100)),
                ("city_id", models.CharField(max_length=100)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Cedative",
            fields=[
                (
                    "cedative_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("bl1n1", models.CharField(max_length=100)),
                ("bcedativeid", models.CharField(max_length=100)),
                ("wlsu_id", models.CharField(max_length=100)),
                ("cluster_id", models.CharField(max_length=100)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Cluster",
            fields=[
                (
                    "cluster_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("cluster_name", models.CharField(max_length=255)),
                ("l1n1", models.CharField(max_length=100)),
                ("l2n2", models.CharField(max_length=100)),
                ("area_id", models.CharField(max_length=100)),
                ("zone_id", models.CharField(max_length=100)),
                ("city_id", models.CharField(max_length=100)),
                ("cedetive_id", models.CharField(max_length=100)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="WLSU",
            fields=[
                (
                    "wlsu_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("wlsu_name", models.CharField(max_length=255)),
                ("l1n1", models.CharField(max_length=100)),
                ("cedetive_id", models.CharField(max_length=100)),
                ("wll", models.IntegerField()),
                ("sqi", models.IntegerField()),
                ("aqi", models.IntegerField()),
                ("vl", models.IntegerField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Zone",
            fields=[
                (
                    "zone_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("zone_name", models.CharField(max_length=255)),
                ("l1n1", models.CharField(max_length=100)),
                ("l2n2", models.CharField(max_length=100)),
                ("city_id", models.CharField(max_length=100)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(max_length=50)),
            ],
        ),
    ]
