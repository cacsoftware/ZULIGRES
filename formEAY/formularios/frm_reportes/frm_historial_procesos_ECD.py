# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.adv


from pyeay.rows import ManipularRows
from pyeay.grillas import ManipularGrillas
from pyeay.dbcac.conexiondb import Ejecutar_SQL
from formEAY.dbaseCAC.dbVarios import DbGetVarios
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

from formEAY.constantesCAC.constantesCAC import AreasProduccion

from formEAY.constantesCAC.coloresCAC import ColorsFondoCellGrilla, Colors_botones

COLOR_RESALTE1 = wx.Colour(255, 236, 234)
COLOR_RESALTE2 = wx.Colour(229, 212, 210)



###########################################################################
## Class HistorialProcesos_ECD
###########################################################################

class HistorialProcesos_ECD(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                          title=u"Historial de Procesos [Extrusión, Cargue y Descargue de Vagonetas]",
                          pos=wx.DefaultPosition, size=wx.Size(1000, 650),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(750, 400), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        bSizer_principal = wx.BoxSizer(wx.VERTICAL)

        bSizer_panelCabecera = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_cabecera = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel_cabecera.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_cabecera = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_rango_fechas = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_rangoFechas = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Rango Fechas", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.lbl_etq_rangoFechas.Wrap(-1)
        self.lbl_etq_rangoFechas.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_rangoFechas.SetForegroundColour(wx.Colour(255, 128, 0))

        bSizer_rango_fechas.Add(self.lbl_etq_rangoFechas, 0, wx.ALL, 5)

        bSizer_fecha1 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fechaInicial = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Inicial:", wx.DefaultPosition,
                                                  wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_fechaInicial.Wrap(-1)
        bSizer_fecha1.Add(self.lbl_etq_fechaInicial, 0, wx.ALL, 5)

        self.datePicker_fecha1 = wx.adv.DatePickerCtrl(self.panel_cabecera, wx.ID_ANY, wx.DefaultDateTime,
                                                   wx.DefaultPosition, wx.DefaultSize, style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer_fecha1.Add(self.datePicker_fecha1, 1, wx.ALL, 5)

        bSizer_rango_fechas.Add(bSizer_fecha1, 0, wx.EXPAND, 5)

        bSizer_fecha2 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fechaFinal = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Final:", wx.DefaultPosition,
                                                wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_fechaFinal.Wrap(-1)
        bSizer_fecha2.Add(self.lbl_etq_fechaFinal, 0, wx.ALL, 5)

        self.datePicker_fecha2 = wx.adv.DatePickerCtrl(self.panel_cabecera, wx.ID_ANY, wx.DefaultDateTime,
                                                   wx.DefaultPosition, wx.DefaultSize, style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer_fecha2.Add(self.datePicker_fecha2, 1, wx.ALL, 5)

        bSizer_rango_fechas.Add(bSizer_fecha2, 1, wx.EXPAND, 5)

        bSizer_cabecera.Add(bSizer_rango_fechas, 1, wx.EXPAND, 5)

        bSizer_area = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_area = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Area", wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.lbl_etq_area.Wrap(-1)
        self.lbl_etq_area.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_area.SetForegroundColour(wx.Colour(255, 128, 0))

        bSizer_area.Add(self.lbl_etq_area, 0, wx.ALL, 5)

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        radioBox_areaChoices = [AreasProduccion.EXTRUSION, AreasProduccion.COCHADO , AreasProduccion.CARGUE_VAGONETAS, AreasProduccion.DESCARGUE_VAGONETAS]
        self.radioBox_area = wx.RadioBox(self.panel_cabecera, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, radioBox_areaChoices, 1, wx.RA_SPECIFY_COLS)
        self.radioBox_area.SetSelection(0)
        bSizer17.Add(self.radioBox_area, 0, wx.ALL, 5)

        bSizer_area.Add(bSizer17, 1, wx.EXPAND, 5)

        bSizer_cabecera.Add(bSizer_area, 0, wx.EXPAND, 5)

        bSizer_turno = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_turno = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Turno", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.lbl_etq_turno.Wrap(-1)
        self.lbl_etq_turno.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_turno.SetForegroundColour(wx.Colour(255, 128, 0))

        bSizer_turno.Add(self.lbl_etq_turno, 0, wx.ALL, 5)

        checkList_turnoChoices = [u"turno 1", u"turno 2"]
        self.checkList_turno = wx.CheckListBox(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                               checkList_turnoChoices, 0)
        bSizer_turno.Add(self.checkList_turno, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_cabecera.Add(bSizer_turno, 2, wx.EXPAND, 5)

        bSizer_estado = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_estado = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Estado", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.lbl_etq_estado.Wrap(-1)
        self.lbl_etq_estado.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_estado.SetForegroundColour(wx.Colour(255, 128, 0))

        bSizer_estado.Add(self.lbl_etq_estado, 0, wx.ALL, 5)

        checkList_estadoChoices = [u"Activo", u"Inactivo"]
        self.checkList_estado = wx.CheckListBox(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                checkList_estadoChoices, 0)
        bSizer_estado.Add(self.checkList_estado, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_cabecera.Add(bSizer_estado, 0, wx.EXPAND, 5)

        bSizer_botonesCabecera = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self.panel_cabecera, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer_botonesCabecera.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.btn_buscar = wx.Button(self.panel_cabecera, wx.ID_ANY, u"&Buscar", wx.DefaultPosition, wx.DefaultSize,
                                    wx.NO_BORDER)
        self.btn_buscar.SetBackgroundColour(wx.Colour(0, 255, 255))

        bSizer_botonesCabecera.Add(self.btn_buscar, 0, wx.ALL, 5)

        bSizer_cabecera.Add(bSizer_botonesCabecera, 0, wx.EXPAND, 5)

        self.panel_cabecera.SetSizer(bSizer_cabecera)
        self.panel_cabecera.Layout()
        bSizer_cabecera.Fit(self.panel_cabecera)
        bSizer_panelCabecera.Add(self.panel_cabecera, 1, wx.EXPAND | wx.ALL, 5)

        bSizer_principal.Add(bSizer_panelCabecera, 0, wx.EXPAND, 5)

        bSizer_panelResultados = wx.BoxSizer(wx.VERTICAL)

        self.m_panel_resultados = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_resultados.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer_resultados = wx.BoxSizer(wx.VERTICAL)

        bSizer_totalesConsulta = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_area_resultados = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"Area:", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.lbl_etq_area_resultados.Wrap(-1)
        bSizer_totalesConsulta.Add(self.lbl_etq_area_resultados, 0, wx.ALL, 5)

        self.lbl_area = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"DESCARGUE DE VAGONETAS", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.lbl_area.Wrap(-1)
        self.lbl_area.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_area.SetForegroundColour(wx.Colour(0, 0, 0))
        self.lbl_area.SetMinSize(wx.Size(170, -1))

        bSizer_totalesConsulta.Add(self.lbl_area, 0, wx.ALL, 5)

        self.lbl_etq_fechas = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"Fechas:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.lbl_etq_fechas.Wrap(-1)
        bSizer_totalesConsulta.Add(self.lbl_etq_fechas, 0, wx.ALL, 5)

        self.lbl_fechas = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_fechas.Wrap(-1)
        self.lbl_fechas.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_fechas.SetMinSize(wx.Size(150, -1))

        bSizer_totalesConsulta.Add(self.lbl_fechas, 0, wx.ALL, 5)

        self.lbl_etq_registrosEncontrados = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"Registros encontrados:",
                                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_registrosEncontrados.Wrap(-1)
        bSizer_totalesConsulta.Add(self.lbl_etq_registrosEncontrados, 0, wx.ALL, 5)

        self.lbl_registrosencontrados = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"", wx.DefaultPosition,
                                                      wx.DefaultSize, 0)
        self.lbl_registrosencontrados.Wrap(-1)
        self.lbl_registrosencontrados.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_registrosencontrados.SetMinSize(wx.Size(60, -1))

        bSizer_totalesConsulta.Add(self.lbl_registrosencontrados, 0, wx.ALL, 5)

        self.lbl_etq_totalCoches = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"Total Coches:", wx.DefaultPosition,
                                             wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
        self.lbl_etq_totalCoches.Wrap(-1)
        bSizer_totalesConsulta.Add(self.lbl_etq_totalCoches, 0, wx.ALL, 5)

        self.lbl_totalCoches = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.lbl_totalCoches.Wrap(-1)
        self.lbl_totalCoches.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_totalCoches.SetMinSize(wx.Size(60, -1))

        bSizer_totalesConsulta.Add(self.lbl_totalCoches, 0, wx.ALL, 5)

        self.lbl_totalUnidades = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"Total Unidades:",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_totalUnidades.Wrap(-1)
        bSizer_totalesConsulta.Add(self.lbl_totalUnidades, 0, wx.ALL, 5)

        self.lbl_total_unidades = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.lbl_total_unidades.Wrap(-1)
        self.lbl_total_unidades.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_total_unidades.SetMinSize(wx.Size(80, -1))

        bSizer_totalesConsulta.Add(self.lbl_total_unidades, 0, wx.ALL, 5)

        bSizer_resultados.Add(bSizer_totalesConsulta, 0, wx.EXPAND, 5)

        self.grid_resultado_busqueda = wx.grid.Grid(self.m_panel_resultados, wx.ID_ANY, wx.DefaultPosition,
                                                    wx.DefaultSize, 0)

        # Grid
        self.grid_resultado_busqueda.CreateGrid(5, 8)
        self.grid_resultado_busqueda.EnableEditing(True)
        self.grid_resultado_busqueda.EnableGridLines(True)
        self.grid_resultado_busqueda.EnableDragGridSize(False)
        self.grid_resultado_busqueda.SetMargins(0, 0)

        # Columns
        self.grid_resultado_busqueda.AutoSizeColumns()
        self.grid_resultado_busqueda.EnableDragColMove(False)
        self.grid_resultado_busqueda.EnableDragColSize(True)
        self.grid_resultado_busqueda.SetColLabelSize(30)
        self.grid_resultado_busqueda.SetColLabelValue(0, u"id")
        self.grid_resultado_busqueda.SetColLabelValue(1, u"uuid")
        self.grid_resultado_busqueda.SetColLabelValue(2, u"Fecha Inicio")
        self.grid_resultado_busqueda.SetColLabelValue(3, u"Hora Inicio")
        self.grid_resultado_busqueda.SetColLabelValue(4, u"Turno")
        self.grid_resultado_busqueda.SetColLabelValue(5, u"Cant. Coches")
        self.grid_resultado_busqueda.SetColLabelValue(6, u"Unidades")
        self.grid_resultado_busqueda.SetColLabelValue(7, u"Activo")
        self.grid_resultado_busqueda.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_resultado_busqueda.EnableDragRowSize(True)
        self.grid_resultado_busqueda.SetRowLabelSize(50)
        self.grid_resultado_busqueda.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_resultado_busqueda.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_resultado_busqueda.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer_resultados.Add(self.grid_resultado_busqueda, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel_resultados.SetSizer(bSizer_resultados)
        self.m_panel_resultados.Layout()
        bSizer_resultados.Fit(self.m_panel_resultados)
        bSizer_panelResultados.Add(self.m_panel_resultados, 1, wx.EXPAND | wx.ALL, 5)

        # self.lbl_nota1 = wx.StaticText(self, wx.ID_ANY,
        #                                u"// Para ver en detalle los registros --> DobleCliclik sobre la fila ",
        #                                wx.DefaultPosition, wx.DefaultSize, 0)
        # self.lbl_nota1.Wrap(-1)
        # self.lbl_nota1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        # self.lbl_nota1.SetForegroundColour(wx.Colour(0, 128, 0))

        # bSizer_panelResultados.Add(self.lbl_nota1, 0, wx.ALL, 5)

        bSizer_principal.Add(bSizer_panelResultados, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer_principal)
        self.Layout()

        self.Centre(wx.BOTH)

        ## OPERACIONES INICIALES EAY
        self.cargar_valores_de_inicializacion()

        # Connect Events
        self.radioBox_area.Bind(wx.EVT_RADIOBOX, self.radioBox_areaOnRadioBox)
        self.btn_buscar.Bind(wx.EVT_BUTTON, self.btn_buscarOnButtonClick)
        self.grid_resultado_busqueda.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,
                                          self.grid_resultado_busquedaOnGridCellLeftDClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def radioBox_areaOnRadioBox(self, event):
        area_produccion = self.radioBox_area.GetStringSelection()
        self.cargar_checkList_turno(area_produccion)
        event.Skip()

    def btn_buscarOnButtonClick(self, event):
        from formEAY.utilCAC.Utiles_proposito_general import ManejoFechasHoras

        area_produccion = self.radioBox_area.GetStringSelection()

        cad_turno = ''
        lista_turnos_sel = self.checkList_turno.GetCheckedStrings()

        if len(lista_turnos_sel) == 0 :
            wx.MessageBox(u'Debes seleccionar mínimo un Turno', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        for i in lista_turnos_sel:
            el_id = self.dic_turnos_todos[i][0]
            cad_turno += str(el_id) + ','
        cad_turno = cad_turno[:-1]

        if cad_turno != '':
            cad_turno = ' and id_turno in (' + cad_turno + ' )'

        cad_estado = ''
        lista_estados_sel = self.checkList_estado.GetCheckedStrings()

        if len(lista_estados_sel) == 0:
            wx.MessageBox(u'Debes seleccionar un Estado', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if len(lista_estados_sel) == 1:
            if lista_estados_sel[0] == 'Activo':
                cad_estado = ' AND activo = True '
            else:
                cad_estado = ' AND activo = False '

        fecha_inicio = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha1)
        fecha_fin = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha2)

        sSql = """
                    SELECT id_cabecera, uuid, fecha_inicio, hora_inicio, turno, total_coches, total_unidades, activo
                    FROM cabecera_proceso_ecd
                    WHERE fecha_inicio >= '{1}' and fecha_inicio <= '{2}' AND area_produccion = '{0}'                          
                """.format(area_produccion, fecha_inicio, fecha_fin)
        sSql = sSql + cad_turno + cad_estado + ' ORDER BY fecha_inicio DESC, turno   '

        cabeceras = ['id_cabecera', 'uuid', 'fecha_inicio', 'hora_inicio', 'turno', 'total_coches', 'total_unidades', 'activo']
        rows = Ejecutar_SQL.select_varios_registros(sSql, 'frm_historial_procesos_ECD/buscar()', 50, BasesDeDatos.DB_PRINCIPAL)

        if rows == None:
            self.m_panel_resultados.Hide()
        else:
            self.lbl_area.SetLabel(area_produccion)

            if area_produccion == 'EXTRUSION':
                self.lbl_etq_totalCoches.SetLabel('Total Coches:')
                self.grid_resultado_busqueda.SetColLabelValue(5, u"Cant. Coches")
            else:
                self.lbl_etq_totalCoches.SetLabel('Total Vagonetas:')
                self.grid_resultado_busqueda.SetColLabelValue(5, u"Cant. Vagonetas")

            cad_fecha = fecha_inicio + '  al  ' + fecha_fin
            self.lbl_fechas.SetLabel(cad_fecha)
            cant_registros = str(len(rows))
            self.lbl_registrosencontrados.SetLabel(cant_registros)

            sSql = """
                                SELECT sum(total_coches), sum(total_unidades)
                                FROM cabecera_proceso_ecd
                                WHERE fecha_inicio >= '{1}' and fecha_inicio <= '{2}' AND area_produccion = '{0}'                          
                            """.format(area_produccion, fecha_inicio, fecha_fin)
            sSql = sSql + cad_turno + cad_estado



            cabeceras = ['total_coches', 'total_unidades']
            row_totales = Ejecutar_SQL.select_un_registro(sSql, 'frm_historial_procesos_ECD/buscar()--> totales',
                                                                   BasesDeDatos.DB_PRINCIPAL)
            el_total_coches = str(row_totales[0])
            el_total_unidades = str(row_totales[1])
            self.lbl_totalCoches.SetLabel(el_total_coches)
            self.lbl_total_unidades.SetLabel(el_total_unidades)

            self.m_panel_resultados.Show()

        ManipularGrillas.llenarGrilla(self.grid_resultado_busqueda, rows)

        dic_color = {5: COLOR_RESALTE2, 6: COLOR_RESALTE1}
        ManipularGrillas.setColorFondoCeldaGrilla(self.grid_resultado_busqueda, dic_color)

        ManipularGrillas.setColorGrisFilasEstadoTrueFalse(self.grid_resultado_busqueda, 7)

        event.Skip()

    def grid_resultado_busquedaOnGridCellLeftDClick(self, event):
        event.Skip()


    ##  FUNCIONES EAY



    def cargar_checkList_turno(self, area_produccion):

        rows = DbGetVarios.listaTurnos(area_produccion, True)
        # id_turno, nom_turno, hora_inicio, hora_salida, activo

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.dic_turnos_todos = ManipularRows.crearDiccionarioTodosLosCampos(rows, 1)
            self.checkList_turno.Set(la_lista)

    def cargar_valores_de_inicializacion(self):
        self.set_configuaracion_grid_resultado_busqueda()
        self.puntero_fila_resultado_busqueda = ManipularGrillas.limpiarGrilla(self.grid_resultado_busqueda)
        self.cargar_checkList_turno('EXTRUSION')
        self.grid_resultado_busqueda.HideCol(1)  ##  ocultar    UUID


    def set_configuaracion_grid_resultado_busqueda(self):

        list_columnas = [0, 1, 2, 3, 4, 5, 6, 7]
        ManipularGrillas.setColumnasSoloLectura(self.grid_resultado_busqueda, list_columnas)

        # list_columnas = [7]
        # ManipularGrillas.setColumnasFormatoCHK(self.grid_resultado_busqueda, list_columnas)

        self.grid_resultado_busqueda.AutoSizeColumns()
