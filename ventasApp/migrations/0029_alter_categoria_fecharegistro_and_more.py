# Generated by Django 5.0.7 on 2024-07-13 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasApp', '0028_alter_categoria_fecharegistro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 817063)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 816063)),
        ),
        migrations.AlterField(
            model_name='detallenotaalmacen',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 819575)),
        ),
        migrations.AlterField(
            model_name='detalleordencompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 819575)),
        ),
        migrations.AlterField(
            model_name='detallepedidoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 817566)),
        ),
        migrations.AlterField(
            model_name='documentocompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 820575)),
        ),
        migrations.AlterField(
            model_name='documentoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 820575)),
        ),
        migrations.AlterField(
            model_name='formapago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 817063)),
        ),
        migrations.AlterField(
            model_name='notaalmacen',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 819575)),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 818571)),
        ),
        migrations.AlterField(
            model_name='pedidoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 817566)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 817566)),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 818571)),
        ),
        migrations.AlterField(
            model_name='tipocliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 805551)),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2024, 7, 13, 14, 15, 36, 804551)),
        ),
    ]
