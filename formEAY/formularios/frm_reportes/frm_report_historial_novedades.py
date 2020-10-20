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


from pyeay.grillas import ManipularGrillas
from pyeay.dbcac.conexiondb import Ejecutar_SQL

from formEAY.constantesCAC.constantesCAC import BasesDeDatos
from formEAY.constantesCAC.coloresCAC import ColorsFondoCellGrilla, Colors_botones

COLOR_RESALTE1 = ColorsFondoCellGrilla.RESALTE_2
COLOR_RESALTE2 = ColorsFondoCellGrilla.RESALTE_5


###########################################################################
## Class HistorialDeNovedades
###########################################################################

class HistorialDeNovedades(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Historial de Novedades", pos=wx.DefaultPosition,
                          size=wx.Size(890, 650), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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
        self.lbl_etq_rangoFechas.SetForegroundColour(wx.Colour(255, 128, 64))

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

        bSizer_cabecera.Add(bSizer_rango_fechas, 2, wx.EXPAND, 5)

        bSizer1611 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticline311 = wx.StaticLine(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_VERTICAL)
        bSizer1611.Add(self.m_staticline311, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_cabecera.Add(bSizer1611, 0, wx.EXPAND, 5)

        bSizer_area = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_area = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Area", wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.lbl_etq_area.Wrap(-1)
        self.lbl_etq_area.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_area.SetForegroundColour(wx.Colour(255, 128, 64))

        bSizer_area.Add(self.lbl_etq_area, 0, wx.ALL, 5)

        checkList_areaChoices = [u"EXTRUSION", u"CARGUE DE VAGONETAS", u"DESCARGUE DE VAGONETAS"]
        self.checkList_area = wx.CheckListBox(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              checkList_areaChoices, 0 | wx.NO_BORDER)
        bSizer_area.Add(self.checkList_area, 0, wx.ALL, 5)

        bSizer_cabecera.Add(bSizer_area, 2, wx.EXPAND, 5)

        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticline3 = wx.StaticLine(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_VERTICAL)
        bSizer16.Add(self.m_staticline3, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_cabecera.Add(bSizer16, 0, wx.EXPAND, 5)

        bSizer_estado = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_estado = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Estado", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.lbl_etq_estado.Wrap(-1)
        self.lbl_etq_estado.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_estado.SetForegroundColour(wx.Colour(255, 128, 0))

        bSizer_estado.Add(self.lbl_etq_estado, 0, wx.ALL, 5)

        checkList_estadoChoices = [u"Activo", u"Inactivo"]
        self.checkList_estado = wx.CheckListBox(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                checkList_estadoChoices, 0 | wx.NO_BORDER)
        bSizer_estado.Add(self.checkList_estado, 0, wx.ALL | wx.EXPAND, 5)

        bSizer_cabecera.Add(bSizer_estado, 1, wx.EXPAND, 5)

        bSizer161 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticline31 = wx.StaticLine(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_VERTICAL)
        bSizer161.Add(self.m_staticline31, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_cabecera.Add(bSizer161, 0, wx.EXPAND, 5)

        bSizer_turno = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_turno = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Tiempo de parada", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.lbl_etq_turno.Wrap(-1)
        self.lbl_etq_turno.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_turno.SetForegroundColour(wx.Colour(255, 128, 64))

        bSizer_turno.Add(self.lbl_etq_turno, 0, wx.ALL, 5)

        self.checkBox_todos = wx.CheckBox(self.panel_cabecera, wx.ID_ANY, u"Todos", wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.checkBox_todos.SetValue(True)
        bSizer_turno.Add(self.checkBox_todos, 0, wx.ALL, 5)

        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_de = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"De", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_de.Wrap(-1)
        bSizer15.Add(self.lbl_etq_de, 0, wx.ALL, 5)

        self.txt_tiempo1 = wx.TextCtrl(self.panel_cabecera, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer15.Add(self.txt_tiempo1, 0, wx.ALL, 5)

        self.lbl_etq_a = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"a", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_a.Wrap(-1)
        bSizer15.Add(self.lbl_etq_a, 0, wx.ALL, 5)

        self.txt_tiempo2 = wx.TextCtrl(self.panel_cabecera, wx.ID_ANY, u"20", wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer15.Add(self.txt_tiempo2, 0, wx.ALL, 5)

        self.lbl_etq_minutos = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"minutos", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.lbl_etq_minutos.Wrap(-1)
        bSizer15.Add(self.lbl_etq_minutos, 0, wx.ALL, 5)

        bSizer_turno.Add(bSizer15, 1, wx.EXPAND, 5)

        bSizer_cabecera.Add(bSizer_turno, 2, wx.EXPAND, 5)

        bSizer1612 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticline312 = wx.StaticLine(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_VERTICAL)
        bSizer1612.Add(self.m_staticline312, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_cabecera.Add(bSizer1612, 0, wx.EXPAND, 5)

        bSizer_botonesCabecera = wx.BoxSizer(wx.VERTICAL)

        self.btn_buscar = wx.Button(self.panel_cabecera, wx.ID_ANY, u"&Buscar", wx.DefaultPosition, wx.DefaultSize,
                                    wx.NO_BORDER)
        self.btn_buscar.SetBackgroundColour(wx.Colour(0, 255, 255))

        bSizer_botonesCabecera.Add(self.btn_buscar, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self.panel_cabecera, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer_botonesCabecera.Add(self.m_staticText6, 1, wx.ALL, 5)

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

        bSizer_totales = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_registros_encontrados = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"Registros Encontrados:",
                                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_registros_encontrados.Wrap(-1)
        bSizer_totales.Add(self.lbl_etq_registros_encontrados, 0, wx.ALL, 5)

        self.lbl_cant_registros = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"0", wx.DefaultPosition,
                                                wx.Size(30, -1), 0)
        self.lbl_cant_registros.Wrap(-1)
        bSizer_totales.Add(self.lbl_cant_registros, 0, wx.ALL, 5)

        self.lbl_etq_total_minutos_en_parada = wx.StaticText(self.m_panel_resultados, wx.ID_ANY,
                                                             u"Total minutos en parada:", wx.DefaultPosition,
                                                             wx.DefaultSize, 0)
        self.lbl_etq_total_minutos_en_parada.Wrap(-1)
        bSizer_totales.Add(self.lbl_etq_total_minutos_en_parada, 0, wx.ALL, 5)

        self.lbl_total_parada = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"0", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_total_parada.Wrap(-1)
        bSizer_totales.Add(self.lbl_total_parada, 0, wx.ALL, 5)

        bSizer_resultados.Add(bSizer_totales, 0, wx.EXPAND, 5)

        self.grid_resultado_busqueda = wx.grid.Grid(self.m_panel_resultados, wx.ID_ANY, wx.DefaultPosition,
                                                    wx.DefaultSize, 0)

        # Grid
        self.grid_resultado_busqueda.CreateGrid(0, 8)
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
        self.grid_resultado_busqueda.SetColLabelValue(1, u"Fecha")
        self.grid_resultado_busqueda.SetColLabelValue(2, u"Hora")
        self.grid_resultado_busqueda.SetColLabelValue(3, u"Area Producción")
        self.grid_resultado_busqueda.SetColLabelValue(4, u"Novedad")
        self.grid_resultado_busqueda.SetColLabelValue(5, u"Parada")
        self.grid_resultado_busqueda.SetColLabelValue(6, u"Uuid")
        self.grid_resultado_busqueda.SetColLabelValue(7, u"Activo")
        self.grid_resultado_busqueda.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_resultado_busqueda.EnableDragRowSize(True)
        self.grid_resultado_busqueda.SetRowLabelSize(1)
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

        self.lbl_nota1 = wx.StaticText(self, wx.ID_ANY,
                                       u"// Para ver en detalle los registros --> DobleCliclik sobre la fila ",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_nota1.Wrap(-1)
        self.lbl_nota1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.lbl_nota1.SetForegroundColour(wx.Colour(0, 128, 0))

        bSizer_panelResultados.Add(self.lbl_nota1, 0, wx.ALL, 5)

        bSizer_principal.Add(bSizer_panelResultados, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer_principal)
        self.Layout()

        self.Centre(wx.BOTH)

        ## VALORES INICIALES
        self.func_inicializacion()

        # Connect Events
        self.btn_buscar.Bind(wx.EVT_BUTTON, self.btn_buscarOnButtonClick)
        self.grid_resultado_busqueda.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,
                                          self.grid_resultado_busquedaOnGridCellLeftDClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btn_buscarOnButtonClick(self, event):
        from formEAY.utilCAC.Utiles_proposito_general import ManejoFechasHoras

        cad_estado = ''
        lista_estados_sel = self.checkList_estado.GetCheckedStrings()

        if len(lista_estados_sel) == 0:
            wx.MessageBox(u'Debes seleccionar un Estado', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        t1 = self.txt_tiempo1.GetValue()
        t2 = self.txt_tiempo2.GetValue()
        if t1 == '' or t1 == '0':
            wx.MessageBox(u'Debes ingresar un tiempo1  valido', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if t2 == '' or t2 == '0':
            wx.MessageBox(u'Debes ingresar un tiempo2  valido', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        cad_estado = ''
        for estado in lista_estados_sel:
            if estado == 'Activo':
                estado = 'True'
            else:
                estado = 'False'

            cad_estado += estado + ","
        cad_estado = cad_estado[:-1]
        if cad_estado != '':
            cad_estado = ' and activo in (' + cad_estado + ')'

        lista_areas_sel = self.checkList_area.GetCheckedStrings()

        if len(lista_areas_sel) == 0:
            wx.MessageBox(u'Debes seleccionar mínimo un Area de trabajo', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        cad_area = ''
        for area in lista_areas_sel:
            cad_area += "'" + area + "',"

        cad_area = cad_area[:-1]

        if cad_area != '':
            cad_area = ' and area_produccion in (' + cad_area + ' )'

        cad_paradas = ''
        if self.checkBox_todos.GetValue() == 0:
            cad_paradas = ' AND    parada_minutos >=  {0} AND parada_minutos <= {1} '.format(t1, t2)

        fecha_inicio = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha1)
        fecha_fin = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha2)

        cad_order_by = ' ORDER BY fecha, hora, area_produccion '

        sSql = """  SELECT id, fecha, hora, area_produccion, novedad, parada_minutos, uuid, activo
                    FROM novedades_por_proceso
                    WHERE fecha >= '{0}'  and fecha <= '{1}'   {2}  {3}   {4}   {5}               
                        """.format(fecha_inicio, fecha_fin, cad_area, cad_estado, cad_paradas, cad_order_by)

        cabeceras = ['ID', 'fecha', 'hora', 'area_produccion', 'novedad', 'parada_minutos', 'uuid', 'activo']

        rows = Ejecutar_SQL.select_varios_registros(sSql, 'frm_report_historial_novedades/buscar()', 150, BasesDeDatos.DB_PRINCIPAL)

        if rows == None:
            self.m_panel_resultados.Hide()
        else:
            ManipularGrillas.llenarGrilla(self.grid_resultado_busqueda, rows)

            sSql = """  SELECT sum(parada_minutos), count(id)
                                FROM novedades_por_proceso
                                WHERE fecha >= '{0}'  and fecha <= '{1}'   {2}  {3}   {4}               
                                    """.format(fecha_inicio, fecha_fin, cad_area, cad_estado, cad_paradas)

            cabeceras = ['total_paradas']
            row_totales = Ejecutar_SQL.select_un_registro(sSql, 'frm_historial_novedades/buscar()--> totales', BasesDeDatos.DB_PRINCIPAL)

            self.lbl_total_parada.SetLabel(str(row_totales[0]))
            self.lbl_cant_registros.SetLabel(str(row_totales[1]))

        # dic_color = {4: COLOR_RESALTE1, 5: COLOR_RESALTE2}
        # ManipularGrillas.setColorFondoCeldaGrilla(self.grid_resultado_busqueda, dic_color)

        ManipularGrillas.setColorGrisFilasEstadoTrueFalse(self.grid_resultado_busqueda, 7)

        event.Skip()

    def grid_resultado_busquedaOnGridCellLeftDClick(self, event):
        event.Skip()


    ##  FUNCIONES EAY
    def func_inicializacion(self):
        self.grid_resultado_busqueda.AutoSizeColumns()
        self.grid_resultado_busqueda.HideCol(6)


