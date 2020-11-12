# -*- coding: utf-8 -*-

from pyeay.dbcac.conexiondb import Ejecutar_SQL, GenerarSql
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

base_nom_funcion = 'dbVarios/'


class DbGetVarios():

    @staticmethod
    def listaTurnos(area_trabajo, activo=True):
        """
        Obtiene el listado de los turnos

        :param area_trabajo:
        :param activo:
        :return: rows, cabeceras  -->  id_turno, nom_turno, hora_inicio, hora_salida, activo
        """

        nom_funcion = base_nom_funcion + 'get_productos'

        cabeceras = ['id_turno', 'nom_turno', ' hora_inicio', 'hora_salida', 'activo', 'dias_operacion']

        sSql = u"""SELECT id_turno, nom_turno, hora_inicio, hora_salida, activo, dias_operacion
             FROM turno
             WHERE activo = {0} and area_trabajo = '{1}'
             ORDER BY nom_turno
          """.format(activo, area_trabajo
                     )
        cant_registros = 20

        rows = Ejecutar_SQL.select_varios_registros(sSql, nom_funcion, cant_registros, BasesDeDatos.DB_PRINCIPAL)

        return rows

    @staticmethod
    def listaCoches(activo=True):
        """

        :param activo:
        :return: rows, cabeceras  -->    id_coche, nom_coche
        """

        nom_funcion = base_nom_funcion + 'get_coches'

        cabeceras = ['id_coche', 'nom_coche']

        sSql = u"""SELECT id_coche, nom_coche
             FROM coche
             WHERE activo = {0} 
             ORDER BY nom_coche
          """.format(activo
                     )
        cant_registros = 20

        rows = Ejecutar_SQL.select_varios_registros(sSql, nom_funcion, cant_registros, BasesDeDatos.DB_PRINCIPAL)

        return rows

    @staticmethod
    def listaVagonetas(activo=True):
        """

        :param activo:
        :return: rows, cabeceras  -->    id_vagoneta, nom_vagoneta
        """

        nom_funcion = base_nom_funcion + 'get_vagonetas'

        cabeceras = ['id_vagoneta', 'nom_vagoneta']

        sSql = u"""SELECT id_vagoneta, nom_vagoneta
             FROM vagoneta
             WHERE activo = {0} and estado = 'FUNCIONANDO'
             ORDER BY nom_vagoneta
          """.format(activo
                     )
        cant_registros = 120

        rows = Ejecutar_SQL.select_varios_registros(sSql, nom_funcion, cant_registros, BasesDeDatos.DB_PRINCIPAL)

        return rows

    @staticmethod
    def listaBoquillas(activo=True):
        """

        :param activo:
        :return: rows, cabeceras   -->  id_boquilla, nom_boquilla
        """

        nom_funcion = base_nom_funcion + 'get_boquillas'

        cabeceras = ['id_boquilla', 'nom_boquilla']

        sSql = u"""SELECT id_boquilla, nom_boquilla
             FROM boquilla
             WHERE activo = {0} 
             ORDER BY nom_boquilla
          """.format(activo
                     )
        cant_registros = 20

        rows = Ejecutar_SQL.select_varios_registros(sSql, nom_funcion, cant_registros, BasesDeDatos.DB_PRINCIPAL)

        return rows

    @staticmethod
    def listaRelevanciaNota(activo=True):
        """

        :param activo:
        :return: rows, cabeceras  -->  d_relevancia_nota, nom_relevancia
        """

        nom_funcion = base_nom_funcion + 'get_relevancia_nota'

        cabeceras = ['id_relevancia_nota', 'nom_relevancia']

        sSql = u"""SELECT id_relevancia_nota, nom_relevancia
             FROM relevancia_nota
             WHERE activo = {0} 
             ORDER BY nom_relevancia
          """.format(activo
                     )
        cant_registros = 30

        rows = Ejecutar_SQL.select_varios_registros(sSql, nom_funcion, cant_registros, BasesDeDatos.DB_PRINCIPAL)

        return rows

    @staticmethod
    def listaContextoNota(activo=True):
        """

        :param activo:
        :return:  rows, cabeceras   -->  id_contexto_nota, nom_contexto
        """

        nom_funcion = base_nom_funcion + 'get_contexto_nota'

        cabeceras = ['id_contexto_nota', 'nom_contexto']

        sSql = u"""SELECT id_contexto_nota, nom_contexto
             FROM contexto_nota
             WHERE activo = {0} 
             ORDER BY nom_contexto
          """.format(activo
                     )
        cant_registros = 30

        rows = Ejecutar_SQL.select_varios_registros(sSql, nom_funcion, cant_registros, BasesDeDatos.DB_PRINCIPAL)

        return rows

    @staticmethod
    def listaRecesoProgramado(activo=True):
        """

        :param activo:
        :return: rows, cabeceras  -->   id_receso, nom_receso, minutos_descanso
        """

        nom_funcion = base_nom_funcion + 'get_receso_programado'

        cabeceras = ['id_receso', 'nom_receso', 'minutos_descanso']

        sSql = u"""SELECT id_receso, nom_receso, minutos_descanso
             FROM receso
             WHERE activo = {0} 
             ORDER BY nom_receso
          """.format(activo
                     )
        cant_registros = 30

        rows = Ejecutar_SQL.select_varios_registros(sSql, nom_funcion, cant_registros, BasesDeDatos.DB_PRINCIPAL)

        return rows


class DbInsertVarios():

    @staticmethod
    def cabeceraProcesoECD(uuid, usuario, mac, fecha_transacccion, hora_transacion, id_turno, turno,
                           total_coches, total_unidades, fecha_inicio, hora_inicio, fecha_fin,
                           hora_fin, activo, area_produccion, minutos_jornada, minutos_recesos, minutos_novedades):

        nom_funcion = base_nom_funcion + 'cabeceraProcesoECD'

        sSql = u"""INSERT INTO cabecera_proceso_ecd (uuid, usuario, mac, fecha_transacccion, hora_transacion, id_turno, 
                                    turno, total_coches, total_unidades, fecha_inicio, hora_inicio, fecha_fin, hora_fin,
                                    activo, area_produccion,
                                    minutos_jornada, minutos_recesos, minutos_novedades)
                            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', {5}, '{6}', {7},
                                    {8}, '{9}', '{10}', '{11}', '{12}', '{13}', '{14}',
                                    {15}, {16}, {17})
                          """.format(uuid, usuario, mac, fecha_transacccion, hora_transacion, id_turno, turno,
                                     total_coches, total_unidades, fecha_inicio, hora_inicio, fecha_fin,
                                     hora_fin, activo, area_produccion, minutos_jornada, minutos_recesos, minutos_novedades)

        try:

            Ejecutar_SQL.insert_filas(sSql, nom_funcion, BasesDeDatos.DB_PRINCIPAL)
            valor_retorno = 1
        except:
            valor_retorno = 0

        return valor_retorno

    @staticmethod
    def notas(self):
        nom_funcion = base_nom_funcion + 'Notas'

        nom_tabla = 'notas_por_proceso'
        dic_campos = {
            'fecha': 'str',
            'relevancia': 'str',
            'contexto': 'str',
            'nota': 'str',
            'activo': 'str',
            'uuid': 'str',
            'area_produccion': 'str',
            'estado': 'str',
            'contranota': 'str'
        }

        cant_filas = self.grid_notas.GetNumberRows()
        cant_columnas = (self.grid_notas.GetNumberCols()) - 1  ## -1 Para no tener en cuenta la columna CHK
        list_valores = []

        if cant_filas < 1:
            return 0

        for i in range(cant_filas):
            list_fila = []
            for j in range(cant_columnas):
                dato = self.grid_notas.GetCellValue(i, j)
                list_fila.append(dato.upper())
            list_fila.append(True)  # es para el campo Activo de la base de datos
            list_fila.append(self.uuid_eay)
            list_fila.append(self.AREA_PRODUCCION)
            list_fila.append('INDEFINIDO')  #ESTADO
            list_fila.append('')            #CONTRANOTA

            list_valores.append(list_fila)

        sSql_insert_notas = GenerarSql.crearMultiInsertSql(nom_tabla, dic_campos, list_valores)

        rta_insert_notas = Ejecutar_SQL.insert_filas(sSql_insert_notas, nom_funcion, BasesDeDatos.DB_PRINCIPAL)

        return rta_insert_notas

    @staticmethod
    def novedades(self):
        nom_funcion = base_nom_funcion + 'Novedades'

        nom_tabla = 'novedades_por_proceso'
        dic_campos = {
            'fecha': 'str',
            'hora': 'str',
            'parada_minutos': 'int',
            'novedad': 'str',
            'activo': 'str',
            'uuid': 'str',
            'area_produccion': 'str'
        }

        cant_filas = self.grid_novedades.GetNumberRows()
        cant_columnas = (self.grid_novedades.GetNumberCols()) - 1  ## -1 Para no tener en cuenta la columna CHK
        list_valores = []

        if cant_filas < 1:
            return 0

        for i in range(cant_filas):
            list_fila = []
            for j in range(cant_columnas):
                dato = self.grid_novedades.GetCellValue(i, j)
                list_fila.append(dato.upper())
            list_fila.append(True)  # es para el campo Activo de la base de datos
            list_fila.append(self.uuid_eay)
            list_fila.append(self.AREA_PRODUCCION)

            list_valores.append(list_fila)

        sSql_insert_novedades = GenerarSql.crearMultiInsertSql(nom_tabla, dic_campos, list_valores)

        rta_insert_novedades = Ejecutar_SQL.insert_filas(sSql_insert_novedades, nom_funcion, BasesDeDatos.DB_PRINCIPAL)

        return rta_insert_novedades

    @staticmethod
    def recesosProgramados(self):
        nom_funcion = base_nom_funcion + 'guardarRecesosProgramados'

        nom_tabla = 'receso_por_proceso'
        dic_campos = {
            'id_receso': 'int',
            'receso': 'str',
            'minutos_descanso': 'int',
            'activo': 'str',
            'uuid': 'str',
            'area_produccion': 'str',
        }

        cant_filas = self.grid_recesos.GetNumberRows()
        cant_columnas = (self.grid_recesos.GetNumberCols())
        list_valores = []

        if cant_filas < 1:
            return 0

        for i in range(cant_filas):
            list_fila = []
            for j in range(cant_columnas):
                dato = self.grid_recesos.GetCellValue(i, j)
                list_fila.append(dato)
            list_fila.append(True)  # es para el campo Activo de la base de datos
            list_fila.append(self.uuid_eay)
            list_fila.append(self.AREA_PRODUCCION)

            list_valores.append(list_fila)

        sSql_insert_recesosProgramados = GenerarSql.crearMultiInsertSql(nom_tabla, dic_campos, list_valores)

        rta_insert_recesosProgramados = Ejecutar_SQL.insert_filas(sSql_insert_recesosProgramados, nom_funcion, BasesDeDatos.DB_PRINCIPAL)

        return rta_insert_recesosProgramados

    @staticmethod
    def detalleExtrusion(self):
        nom_funcion = base_nom_funcion + 'guardarDetalleExtrusion'

        nom_tabla = 'detalle_extrusion'
        dic_campos = {
            'id_producto': 'int',
            'producto': 'str',
            'coche': 'str',
            'cant_coches': 'int',
            'unidades_producto': 'int',
            'unid_parrilla_vacia': 'int',
            'total': 'int',
            'contador': 'int',
            'activo': 'str',
            'uuid': 'str'
        }

        cant_filas = self.grid_extrusion.GetNumberRows()
        cant_columnas = (self.grid_extrusion.GetNumberCols()) - 1
        list_valores = []

        if cant_filas < 1:
            return 0

        for i in range(cant_filas):
            list_fila = []
            for j in range(cant_columnas):
                dato = self.grid_extrusion.GetCellValue(i, j)
                list_fila.append(dato)
            list_fila.append(True)  # es para el campo Activo de la base de datos
            list_fila.append(self.uuid_eay)

            list_valores.append(list_fila)

        sSql_insert_DetalleExtrusion = GenerarSql.crearMultiInsertSql(nom_tabla, dic_campos, list_valores)

        rta_insert_DetalleExtrusion = Ejecutar_SQL.insert_filas(sSql_insert_DetalleExtrusion, nom_funcion, BasesDeDatos.DB_PRINCIPAL)

        return rta_insert_DetalleExtrusion

    @staticmethod
    def detalleCocheros(self, secadero):
        nom_funcion = base_nom_funcion + 'guardarDetalleExtrusion'

        nom_tabla = 'detalle_cocheros'
        dic_campos = {
            'secadero': 'str',
            'id_producto': 'int',
            'producto': 'str',
            'cant_coches': 'int',
            'unid_x_coche': 'int',
            'unid_parrilla_vacia': 'int',
            'total': 'int',
            'rotura': 'int',
            'activo': 'str',
            'uuid': 'str',

        }

        cant_filas = self.grid_extrusion.GetNumberRows()
        cant_columnas = (self.grid_extrusion.GetNumberCols()) - 1
        list_valores = []

        if cant_filas < 1:
            return 0

        for i in range(cant_filas):
            list_fila = []
            for j in range(cant_columnas):
                dato = self.grid_extrusion.GetCellValue(i, j)
                list_fila.append(dato)
            list_fila.append(True)  # es para el campo Activo de la base de datos
            list_fila.append(self.uuid_eay)
            #list_fila.append(secadero)

            list_valores.append(list_fila)

        sSql_insert_DetalleCocheros = GenerarSql.crearMultiInsertSql(nom_tabla, dic_campos, list_valores)

        rta_insert_DetalleCocheros = Ejecutar_SQL.insert_filas(sSql_insert_DetalleCocheros, nom_funcion,
                                                                BasesDeDatos.DB_PRINCIPAL)

        return rta_insert_DetalleCocheros

    @staticmethod
    def detalleCargueVagonetas(self):
        nom_funcion = base_nom_funcion + 'detalleCargueVagonetas'

        nom_tabla = 'detalle_cargue_vagonetas'
        dic_campos = {
            'id_producto': 'int',
            'producto': 'str',
            'vagoneta': 'str',
            'unidades_producto': 'int',
            'activo': 'str',
            'uuid': 'str'
        }

        cant_filas = self.grid_cargueVagonetas.GetNumberRows()
        cant_columnas = self.grid_cargueVagonetas .GetNumberCols()
        list_valores = []

        if cant_filas < 1:
            return 0

        for i in range(cant_filas):

            for j in range(2, cant_columnas):
                list_fila = []
                producto = self.grid_cargueVagonetas.GetColLabelValue(j)
                id_producto = self.dic_productos_id[producto][0]
                list_fila.append(id_producto)
                list_fila.append(producto)
                vagoneta = self.grid_cargueVagonetas.GetCellValue(i, 0)
                list_fila.append(vagoneta)
                unidades_producto = self.grid_cargueVagonetas.GetCellValue(i, j)
                if unidades_producto == '':
                    unidades_producto = 0
                list_fila.append(unidades_producto)

                list_fila.append(True)  # es para el campo Activo de la base de datos
                list_fila.append(self.uuid_eay)

                list_valores.append(list_fila)


        sSql_insert_DetalleCargueVagonetas = GenerarSql.crearMultiInsertSql(nom_tabla, dic_campos, list_valores)

        print(sSql_insert_DetalleCargueVagonetas)



        rta_insert_DetalleCargueVagonetas = Ejecutar_SQL.insert_filas(sSql_insert_DetalleCargueVagonetas, nom_funcion, BasesDeDatos.DB_PRINCIPAL)

        return rta_insert_DetalleCargueVagonetas, list_valores

    @staticmethod
    def detalleDescargueVagonetas(self):
        nom_funcion = base_nom_funcion + 'detalleDescargueVagonetas'

        nom_tabla = 'detalle_descargue_vagonetas'
        dic_campos = {
            'id_producto': 'int',
            'producto': 'str',
            'empleado': 'str',
            'vagoneta': 'str',
            'de_primera': 'int',
            'de_segunda': 'int',
            'rotos': 'int',
            'activo': 'str',
            'uuid': 'str'

        }

        cant_filas = self.grid_descargue_vagonetas.GetNumberRows()
        cant_columnas = self.grid_descargue_vagonetas.GetNumberCols()
        list_valores = []

        if cant_filas < 1:
            return 0

        #print('linea 490 dbvarios ',self.dic_productos_id)

        for j in range(3, cant_columnas):
            list_fila = []
            for i in range(0, cant_filas, 3):
                list_fila = []
                producto = self.grid_descargue_vagonetas.GetColLabelValue(j)
                id_producto = self.dic_productos_id[producto]
                list_fila.append(id_producto)
                list_fila.append(producto)
                empleado = self.grid_descargue_vagonetas.GetCellValue(i, 0)
                vagoneta = self.grid_descargue_vagonetas.GetCellValue(i, 1)
                list_fila.append(empleado)
                list_fila.append(vagoneta)

                primera = self.grid_descargue_vagonetas.GetCellValue(i, j)
                if primera == '':
                    primera = 0
                list_fila.append(primera)

                segunda = self.grid_descargue_vagonetas.GetCellValue(i+1, j)
                if segunda == '':
                    segunda = 0
                list_fila.append(segunda)

                rotos = self.grid_descargue_vagonetas.GetCellValue(i+2, j)
                if rotos == '':
                    rotos = 0
                list_fila.append(rotos)


                list_fila.append(True)  # es para el campo Activo de la base de datos
                list_fila.append(self.uuid_eay)

                list_valores.append(list_fila)

        sSql_insert_DetalleDescargueVagonetas = GenerarSql.crearMultiInsertSql(nom_tabla, dic_campos, list_valores)

        rta_insert_DetalleDescargueVagonetas = Ejecutar_SQL.insert_filas(sSql_insert_DetalleDescargueVagonetas, nom_funcion, BasesDeDatos.DB_PRINCIPAL)

        return rta_insert_DetalleDescargueVagonetas

    @staticmethod
    def personal(self):
        nom_funcion = base_nom_funcion + 'guardarPersonal'

        nom_tabla = 'empleados_por_proceso'
        dic_campos = {
            'area_produccion': 'str',
            'uuid': 'str',
            'id_empleado': 'int',
            'activo': 'str'
        }

        list_valores = []

        for nom_empleado in self.checkList_personal.GetCheckedStrings():
            list_empleado = []
            list_empleado.append(self.AREA_PRODUCCION)
            list_empleado.append(self.uuid_eay)
            id_empleado = self.diccionario_personal[nom_empleado]
            list_empleado.append(id_empleado)
            activo = True
            list_empleado.append(activo)
            list_valores.append(list_empleado)

        sSql_insert_empleados = GenerarSql.crearMultiInsertSql(nom_tabla, dic_campos, list_valores)

        rta_insert_empleados = Ejecutar_SQL.insert_filas(sSql_insert_empleados, nom_funcion, BasesDeDatos.DB_PRINCIPAL)

        return rta_insert_empleados