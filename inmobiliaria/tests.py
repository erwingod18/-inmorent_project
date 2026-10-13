from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Comuna, inmobiliaria


class PropiedadAdminTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="test-password",
        )
        self.comuna = Comuna.objects.create(
            nombre="Santiago",
            region="Metropolitana",
            codigo_clasificacion="RM-001",
        )
        self.client.force_login(self.user)

    def test_admin_add_form_saves_property(self):
        response = self.client.post(
            reverse("admin:inmobiliaria_inmobiliaria_add"),
            {
                "codigo_propiedad": "DEP-001",
                "direccion": "Av. Central 123",
                "tipo_propiedad": "DEPARTAMENTO",
                "precio_arriendo": "450000.00",
                "dormitorios": "2",
                "baños": "1",
                "disponible": "on",
                "comuna": str(self.comuna.pk),
                "inmobiliaria_comuna": str(self.user.pk),
                "_save": "Guardar",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        propiedad = inmobiliaria.objects.get(codigo_propiedad="DEP-001")
        self.assertEqual(propiedad.direccion, "Av. Central 123")
        self.assertEqual(propiedad.comuna, self.comuna)
