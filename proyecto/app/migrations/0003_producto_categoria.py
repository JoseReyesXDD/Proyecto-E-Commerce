# Generated by Django 5.1.7 on 2025-03-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_producto_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Electronica', 'Electrónica'), ('Ropa', 'Ropa'), ('Hogar', 'Hogar'), ('Belleza', 'Belleza'), ('Libros', 'Libros')], default='Electronica', max_length=50),
        ),
    ]
