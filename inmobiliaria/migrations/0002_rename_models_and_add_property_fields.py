from decimal import Decimal

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inmobiliaria", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Inmobiliaria",
            new_name="Comuna",
        ),
        migrations.RenameModel(
            old_name="PacienteMascota",
            new_name="inmobiliaria",
        ),
        migrations.AddField(
            model_name="inmobiliaria",
            name="codigo_propiedad",
            field=models.CharField(default="MIGRADO", max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inmobiliaria",
            name="direccion",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inmobiliaria",
            name="tipo_propiedad",
            field=models.CharField(
                choices=[
                    ("DEPARTAMENTO", "Departamento"),
                    ("CASA", "Casa"),
                    ("OFICINA", "Oficina"),
                ],
                default="CASA",
                max_length=20,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inmobiliaria",
            name="precio_arriendo",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.00"),
                max_digits=10,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inmobiliaria",
            name="dormitorios",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inmobiliaria",
            name="baños",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inmobiliaria",
            name="disponible",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="inmobiliaria",
            name="fecha_publicacion",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name="inmobiliaria",
            name="comuna",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="propiedades",
                to="inmobiliaria.comuna",
            ),
            preserve_default=False,
        ),
    ]
