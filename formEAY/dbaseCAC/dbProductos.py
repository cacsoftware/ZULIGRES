# -*- coding: utf-8 -*-

from formEAY.constantesCAC.constantesCAC import BasesDeDatos
from pyeay.dbcac.conexiondb import Ejecutar_SQL

base_nom_funcion = 'dbProductos/'


class DbInsertProductos():

    @staticmethod
    def producto(nom_producto):
        nom_funcion = base_nom_funcion + 'insertar_producto'


        sSql = u"""INSERT INTO producto (nom_producto)
                    VALUES ('{0}')
                  """.format(nom_producto
                             )

        Ejecutar_SQL.insert_filas(sSql, nom_funcion, BasesDeDatos.DB_PRINCIPAL)


class Get_productos():

    @staticmethod
    def listaBasica(cant_registros = 50, activo = True):
        """
        Obtine la lista de los productos,  Con solo datos básicos

        :param activo:
        :return: rows, cabeceras  -->  id_producto, nom_producto, activo
        """

        nom_funcion = base_nom_funcion + 'get_productos'

        #cabeceras =['id_producto', 'nom_producto',  'activo']

        sSql = u"""SELECT id_producto, nom_producto, activo, unid_x_coche, unid_x_estiba, unid_x_vagoneta
             FROM producto
             WHERE activo = {0}
             ORDER BY nom_producto
          """.format(activo
                     )

        rows = Ejecutar_SQL.select_varios_registros(sSql, nom_funcion, cant_registros, BasesDeDatos.DB_PRINCIPAL)

        return rows




