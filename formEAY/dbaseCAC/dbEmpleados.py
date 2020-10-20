# -*- coding: utf-8 -*-


from pyeay.dbcac.conexiondb import Ejecutar_SQL
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

base_nom_funcion = 'dbEmpleados/'


class Get_empleados():

    @staticmethod
    def lista_basica(area_trabajo, activo=True):
        """
        Obtiene una lista de los empleados, con solo los datos basicos

        :param area_trabajo:  string -->  Por ej del area de 'EXTRUSION'
        :param activo: Boolean
        :return: rows, cabeceras  -->  id_empleado, nom_completo , area_trabajo, activo
        """

        nom_funcion = base_nom_funcion + 'get_empleados_lista_basica'

        cabeceras = ['id_empleado', 'nom_completo', 'area_trabajo', 'activo']

        sSql = u"""SELECT id_empleado, nom || ' ' || ape1 ||  ' ' || ape2 as nom_completo , area_trabajo, activo
             FROM empleado
             WHERE  area_trabajo = '{0}' AND activo = {1}
             ORDER BY nom, ape1, ape2
          """.format(area_trabajo, activo
                     )
        cant_registros = 20

        rows = Ejecutar_SQL.select_varios_registros(sSql, nom_funcion, cant_registros, BasesDeDatos.DB_PRINCIPAL)

        return rows
