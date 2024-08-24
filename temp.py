import os
import time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from m7_python.models import Inmuebles, Region

def get_list_inmuebles(name, descr):
    lista_inmuebles = Inmuebles.objects.filter(nombre_inmueble__contains=name).filter(descripcion__contains=descr)
    
    archivo1=open("datos.txt", "w")
    for l in lista_inmuebles.values():
        archivo1.write(str(l))
        archivo1.write("\n")
        
    archivo1.close()
    
    return lista_inmuebles

resultado = get_list_inmuebles("Providencia","Cocina")

def get_list_inmuebles_by_comuna(comuna):
    select = f"""
    SELECT A.id, A.nombre_inmueble, A.descripcion 
    FROM public.m7_python_inmuebles as A
    INNER JOIN public.m7_python_region as B ON A.id_region_id = B.id
    INNER JOIN public.m7_python_comuna as C ON A.id_comuna_id = C.id
    WHERE C.comuna LIKE '%%{str(comuna)}%%'
    """
    results = Inmuebles.objects.raw(select)
    
    archivo1=open("datos2.txt", "w")
    for com in results:
        archivo1.write(com.nombre_inmueble+', '+com.descripcion)
        archivo1.write("\n")
    archivo1.close()
    
get_list_inmuebles_by_comuna("Bernardo")


def get_list_inmuebles_region(id):
    region = str(Region.objects.filter(id=id).values()[0]["region"])
    
    lista_inmuebles = Inmuebles.objects.filter(id_region_id=id)
    
    archivo1=open("datos3.txt", "w")
    for l in lista_inmuebles.values():
        archivo1.write(str(l['nombre_inmueble']))
        archivo1.write(', ')
        archivo1.write(region)
        archivo1.write("\n")
    archivo1.close()
    
get_list_inmuebles_region(16)

def get_list_inmuebles_by_region(region):
    select = f"""
    select A.id,
    A.nombre_inmueble,
    A.descripcion
    FROM public.m7_python_inmuebles as A
    INNER JOIN public.m7_python_region as B
    ON A.id_region_id = B.id
    INNER JOIN public.m7_python_comuna as C
    ON A.id_comuna_id = C.id
    WHERE B."region" like '%%{str(region)}%%'
    """
    results = Inmuebles.objects.raw(select)
    
    archivo1=open("datos4.txt", "w")
    for p in results:
        archivo1.write(p.nombre_inmueble+', '+p.descripcion)
        archivo1.write("\n")
    archivo1.close()
    
get_list_inmuebles_by_region("Metrop")