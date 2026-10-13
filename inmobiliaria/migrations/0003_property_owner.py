from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def require_empty_properties(apps, schema_editor):
    Property = apps.get_model("inmobiliaria", "inmobiliaria")
    if Property.objects.using(schema_editor.connection.alias).exists():
        raise RuntimeError(
            "Assign an owner to existing properties before applying this migration."
        )


class Migration(migrations.Migration):

    dependencies = [
        ("inmobiliaria", "0002_rename_models_and_add_property_fields"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="inmobiliaria",
            name="inmobiliaria_comuna",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="propiedades",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.RunPython(
            require_empty_properties,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="inmobiliaria",
            name="inmobiliaria_comuna",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="propiedades",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
