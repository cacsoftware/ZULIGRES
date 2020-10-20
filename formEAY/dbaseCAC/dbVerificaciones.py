# -*- coding: utf-8 -*-

from pyeay.dbcac.conexiondb import Ejecutar_SQL
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

base_nom_funcion = 'dbVerificaciones/'

class DbGetVerificaciones():

    @staticmethod
    def existeTurno(id_turno, fecha, activo, areaProduccion):
        """
        :param id_turno:
        :param fecha:
        :return:  true si el turno exite
        """

        nom_funcion = base_nom_funcion + 'get_existe_turno'

        cabeceras =['id_turno']

        sSql = u"""SELECT id_turno
             FROM cabecera_proceso_ecd
             WHERE  id_turno = {0} and fecha_inicio = '{1}'  and  activo = {2} and area_produccion = '{3}'
          """.format(id_turno, fecha, activo, areaProduccion
                     )

        rows = Ejecutar_SQL.select_un_registro(sSql, nom_funcion, BasesDeDatos.DB_PRINCIPAL)


        if rows != None:
            existe = True
        else:
            existe = False
        return existe