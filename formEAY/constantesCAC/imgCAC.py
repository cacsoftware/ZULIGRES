

import os

#LARUTA='C:/Users/svrCAC/PycharmProjects/ferretubosPrueba/formEAY/img/'

LARUTA_IMAGEN = os.path.join(os.getcwd(), 'formEAY', 'img', 'imagenes')


LARUTA_ICONO = os.path.join(os.getcwd(), 'formEAY', 'img', 'iconos')

LARUTA_WALLPAPER = os.path.join(os.getcwd(), 'ICONO', )
LARUTA_FORMATOS = os.path.join(os.getcwd(), 'FORMATOS', )


# LARUTA_IMAGEN='formEAY/img/imagenes/'
# LARUTA_ICONO='formEAY/img/iconos/'

## Imagenes para los formularios

class Img_formatos():
    EXTRUSION = os.path.join(LARUTA_FORMATOS, 'EXTRUSION_FORMATO.PDF')
    EXTRUSION_PROCEDIMIENTO = os.path.join(LARUTA_FORMATOS, 'EXTRUSION_PROCEDIMIENTO.PDF')

    CARGUE_VAGONETAS = os.path.join(LARUTA_FORMATOS, 'CARGUE_VAGONETAS_FORMATO.PDF')
    CARGUE_VAGONETAS_PROCEDIMIENTO = os.path.join(LARUTA_FORMATOS, 'CARGUE_VAGONETAS_PROCEDIMIENTO.PDF')

    DESCARGUE_VAGONETAS = os.path.join(LARUTA_FORMATOS, 'DESCARGUE_VAGONETAS_FORMATO.PDF')
    DESCARGUE_VAGONETAS_PROCEDIMIENTO = os.path.join(LARUTA_FORMATOS, 'DESCARGUE_VAGONETAS_PROCEDIMIENTO.PDF')

class Img_produccion():
    RUTA_IMAGEN = os.path.join(os.getcwd(), 'formEAY', 'img', 'imagenes', 'PRODUCCION')
    #FONDO_PRODUCCION=os.path.join(LARUTA_IMAGEN,'00_PRODUCCION.PNG')
    EXTRUSION = os.path.join(RUTA_IMAGEN,'EXTRUSION.PNG')
    CARGUE_VAGONETAS = os.path.join(RUTA_IMAGEN,'CARGUE VAGONETAS.PNG')
    DESCARGUE_VAGONETAS = os.path.join(RUTA_IMAGEN, 'DESCARGUE DE VAGONETAS.PNG')
    COCHADO = os.path.join(RUTA_IMAGEN, 'COCHADO.PNG')

class Img_grillas():
    RUTA_ICONO = os.path.join(os.getcwd(), 'formEAY', 'img', 'iconos', 'GRILLAS')
    ELIMINAR_ITEM_SELECIONADO = os.path.join(RUTA_ICONO,'ELIMINAR_ITEM_SELECCIONADO.jpg')
    ELIMINAR_ITEM_SELECIONADO_SEL = os.path.join(RUTA_ICONO,'ELIMINAR_ITEM_SELECCIONADO_SEL.jpg')

    DESELECCIONAR_TODO = os.path.join(RUTA_ICONO,'DESELECCIONAR_ITEMS.jpg')
    DESELECCIONAR_TODO_SEL = os.path.join(RUTA_ICONO,'DESELECCIONAR_ITEMS_SEL.jpg')

    LIMPIAR_GRILLA = os.path.join(RUTA_ICONO,'LIMPIAR_GRILLA.jpg')
    LIMPIAR_GRILLA_SEL = os.path.join(RUTA_ICONO,'LIMPIAR_GRILLA_SEL.jpg')

class Img_formularios_general():
    RUTA_ICONO = os.path.join(os.getcwd(), 'formEAY', 'img', 'iconos', 'FORMULARIOS')

    RUTA_WALLPAPER = os.path.join(os.getcwd(), 'formEAY', 'img', 'WALLPAPERS')

    WALLPAPER_PRINCIPAL = os.path.join(RUTA_WALLPAPER, 'WALLPAPER.PNG')

    CABECERA_ORDEN_SERVICIO = os.path.join(RUTA_ICONO, 'ENCABEZADO_ORDEN_SERVICIO.PNG')
    PIE_DE_PAGINA_ORDEN_SERVICIO = os.path.join(RUTA_ICONO, 'PIE DE PAGINA ORDEN DE SEERVICIO  ZULIGRES.PNG')

    A_LISTA = os.path.join(RUTA_ICONO, 'A_LISTA.PNG')
    A_LISTA_SEL = os.path.join(RUTA_ICONO, 'A_LISTA_SEL.PNG')

    BUSCAR_CLIENTE = os.path.join(RUTA_ICONO, 'CLIENTE.PNG')
    BUSCAR_CLIENTE_SEL = os.path.join(RUTA_ICONO, 'CLIENTE_SEL.PNG')

    ACTUALIZAR_FORMULARIO = os.path.join(RUTA_ICONO, 'ACTUALIZAR_FORMULARIO.JPG')
    ACTUALIZAR_FORMULARIO_SEL  = os.path.join(RUTA_ICONO, 'ACTUALIZAR_FORMULARIO_SEL.JPG')

    LIMPIAR_CONTROLES = os.path.join(RUTA_ICONO, 'LIMPIAR.JPG')
    LIMPIAR_CONTROLES_SEL = os.path.join(RUTA_ICONO, 'LIMPIAR_SEL.JPG')

    EDITAR = os.path.join(RUTA_ICONO, 'EDITAR.JPG')
    EDITAR_SEL = os.path.join(RUTA_ICONO, 'EDITAR_SEL.JPG')

    NUEVO_CLIENTE = os.path.join(RUTA_ICONO, 'NUEVO_CLIENTE.JPG')
    NUEVO_CLIENTE_SEL = os.path.join(RUTA_ICONO, 'NUEVO_CLIENTE_SEL.JPG')

    GUARDAR = os.path.join(RUTA_ICONO, 'GUARDAR.JPG')
    GUARDAR_SEL = os.path.join(RUTA_ICONO, 'GUARDAR_SEL.JPG')





