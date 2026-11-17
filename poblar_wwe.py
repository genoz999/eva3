import os
import sys
from pathlib import Path
from datetime import date
import pymysql

pymysql.install_as_MySQLdb()
import django

# Detecta automáticamente la carpeta donde está settings.py
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

settings_file = next(BASE_DIR.rglob("settings.py"), None)
if not settings_file:
    raise FileNotFoundError("No se encontró settings.py en el proyecto.")

modulo_settings = f"{settings_file.parent.name}.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", modulo_settings)
django.setup()

from luchadores.models import Marca, Luchador

# 1. Asegurar que existan las marcas
raw, _ = Marca.objects.get_or_create(nombre="Raw")
smackdown, _ = Marca.objects.get_or_create(nombre="SmackDown")
nxt, _ = Marca.objects.get_or_create(nombre="NXT")
hof, _ = Marca.objects.get_or_create(nombre="Hall Of Fame")

# 2. Lista de luchadores a agregar
roster = [
    {"nombre_ring": "Cody Rhodes", "marca": smackdown, "peso_kg": 100, "fecha_debut": date(2006, 5, 13), "es_campeon": True},
    {"nombre_ring": "Roman Reigns", "marca": smackdown, "peso_kg": 120, "fecha_debut": date(2010, 9, 9), "es_campeon": False},
    {"nombre_ring": "Seth Rollins", "marca": raw, "peso_kg": 98, "fecha_debut": date(2005, 1, 1), "es_campeon": False},
    {"nombre_ring": "Gunther", "marca": raw, "peso_kg": 135, "fecha_debut": date(2005, 8, 16), "es_campeon": True},
    {"nombre_ring": "CM Punk", "marca": raw, "peso_kg": 99, "fecha_debut": date(1999, 1, 1), "es_campeon": False},
    {"nombre_ring": "Rhea Ripley", "marca": raw, "peso_kg": 62, "fecha_debut": date(2013, 1, 1), "es_campeon": False},
    {"nombre_ring": "Trick Williams", "marca": nxt, "peso_kg": 109, "fecha_debut": date(2021, 2, 24), "es_campeon": True},
    {"nombre_ring": "Oba Femi", "marca": nxt, "peso_kg": 141, "fecha_debut": date(2022, 11, 18), "es_campeon": False},
    {"nombre_ring": "The Undertaker", "marca": hof, "peso_kg": 140, "fecha_debut": date(1987, 6, 26), "es_campeon": False},
    {"nombre_ring": "Stone Cold Steve Austin", "marca": hof, "peso_kg": 114, "fecha_debut": date(1989, 9, 30), "es_campeon": False},
]

# 3. Insertar sin duplicar
creados = 0
for datos in roster:
    _, creado = Luchador.objects.get_or_create(
        nombre_ring=datos["nombre_ring"],
        defaults=datos
    )
    if creado:
        creados += 1

print(f"¡Listo! Usando '{modulo_settings}', se agregaron {creados} luchadores nuevos.")