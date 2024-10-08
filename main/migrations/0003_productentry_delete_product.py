# Generated by Django 5.1.1 on 2024-09-16 23:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_delete_moodentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ProductName', models.CharField(max_length=255)),
                ('ProductDescription', models.TextField()),
                ('ProductPrice', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
