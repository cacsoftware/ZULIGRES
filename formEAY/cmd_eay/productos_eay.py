# -*- coding: utf-8 -*-

import formEAY.dbaseCAC.dbProductos as dbProductos
import pprint


def insertar_productos(cant):
    from formEAY.dbaseCAC.dbProductos import DbInsertProductos
    obj_sql = DbInsertProductos()

    for i in range(cant):
        nom_producto = 'Producto - ' + str(i)
        print(nom_producto)
        obj_sql.producto(nom_producto)


def mostrar_productos():

    rows, cabeceras = dbProductos.get_productos()

    if rows != None:
        graficar_tabla ( rows, cabeceras, 12)

    input('final')


def graficar_tabla(rows, cabeceras, ancho_col=10, cad_sep ='  |  '):
    str_cabecera  = ''
    for i in cabeceras:
        i = i.center(ancho_col)
        i = i[: ancho_col] + cad_sep
        str_cabecera += i
    str_cabecera = cad_sep + str_cabecera

    str_todas_filas = ''
    for fila in rows:

        str_fila = ''
        for i in fila:
            i = str(i)
            i = i.center(ancho_col)
            i = i[: ancho_col] + cad_sep
            str_fila += i

        str_fila = cad_sep + str_fila
        str_todas_filas += str_fila + '\n'

    str_separador = ' ' * int(len(cad_sep)/2) + '-' * (len(str_cabecera)- len(cad_sep))

    print(str_separador)
    print(str_cabecera)
    print(str_separador)
    print(str_todas_filas)
    print(str_separador)


if __name__ == '__main__':
    #mostrar_productos()

    insertar_productos()

    input('final')