# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

import pandas as pd

import wx.xrc
import wx.grid
import wx.adv

from pyeay.dbcac.conexiondb import Ejecutar_SQL
from pyeay.rows import ManipularRows
from pyeay.grillas import ManipularGrillas
from formEAY.dbaseCAC.dbVarios import DbGetVarios

from formEAY.constantesCAC.constantesCAC import BasesDeDatos
from formEAY.constantesCAC.constantesCAC import AreasProduccion
from formEAY.constantesCAC.coloresCAC import ColorsFondoCellGrilla, Colors_botones

# COLOR_RESALTE_PRIMERA = ColorsFondoCellGrilla.RESALTE_2
# COLOR_RESALTE_SEGUNDA = ColorsFondoCellGrilla.RESALTE_5
#
# COLOR_RESALTE_ROTURA = ColorsFondoCellGrilla.RESALTE_ROSA
# COLOR_RESALTE_ROTURA_CLARO = ColorsFondoCellGrilla.RESALTE_ROSA2
#
# COLOR_RESALTE_TOTAL = ColorsFondoCellGrilla.RESALTE_AGUAMARINA
#
# AREA_EXTRUSION = AreasProduccion.EXTRUSION
# AREA_CARGUE_VAGONETAS = AreasProduccion.CARGUE_VAGONETAS
# AREA_DESCARGUE_VAGONETAS = AreasProduccion.DESCARGUE_VAGONETAS

COLOR_RESALTE_PRIMERA = wx.Colour(255, 236, 234)
COLOR_RESALTE_SEGUNDA = wx.Colour(229, 212, 210)

COLOR_RESALTE_ROTURA = wx.Colour(233, 192, 192)  ## ROTURA
COLOR_RESALTE_ROTURA_CLARO = ColorsFondoCellGrilla.RESALTE_ROSA2

COLOR_RESALTE_TOTAL = wx.Colour(255, 213, 177)

AREA_EXTRUSION = AreasProduccion.EXTRUSION
AREA_CARGUE_VAGONETAS = AreasProduccion.CARGUE_VAGONETAS
AREA_DESCARGUE_VAGONETAS = AreasProduccion.DESCARGUE_VAGONETAS

###########################################################################
## Class HistorialProcesos_ECD
###########################################################################

class HistorialDetalleProcesos_ECD(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                          title=u"Historial Detalle Procesos [Extrusión, Cargue y Descargue de Vagonetas]",
                          pos=wx.DefaultPosition, size=wx.Size(1000, 650),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(750, 400), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))
        
        self.orden_ascendente=True
        self.df = None

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

        radioBox_areaChoices = [AreasProduccion.EXTRUSION, AreasProduccion.CARGUE_VAGONETAS, AreasProduccion.DESCARGUE_VAGONETAS, 'DESPACHOS']
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

        # bSizer_estado = wx.BoxSizer(wx.VERTICAL)
        #
        # self.lbl_etq_estado = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Estado", wx.DefaultPosition,
        #                                     wx.DefaultSize, 0)
        # self.lbl_etq_estado.Wrap(-1)
        # self.lbl_etq_estado.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        # self.lbl_etq_estado.SetForegroundColour(wx.Colour(112, 112, 112))
        #
        # bSizer_estado.Add(self.lbl_etq_estado, 0, wx.ALL, 5)
        #
        # checkList_estadoChoices = [u"Activo", u"Inactivo"]
        # self.checkList_estado = wx.CheckListBox(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
        #                                         checkList_estadoChoices, 0)
        # bSizer_estado.Add(self.checkList_estado, 1, wx.ALL | wx.EXPAND, 5)
        #
        # bSizer_cabecera.Add(bSizer_estado, 0, wx.EXPAND, 5)

        bSizer_botonesCabecera = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self.panel_cabecera, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer_botonesCabecera.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.btn_buscar = wx.Button(self.panel_cabecera, wx.ID_ANY, u"&Buscar", wx.DefaultPosition, wx.DefaultSize,
                                    wx.NO_BORDER)
        self.btn_buscar.SetBackgroundColour(wx.Colour(0, 255, 255))

        bSizer_botonesCabecera.Add(self.btn_buscar, 0, wx.ALL, 5)

        self.btn_graficar = wx.Button(self.panel_cabecera, wx.ID_ANY, u"&Graficar", wx.DefaultPosition, wx.DefaultSize,
                                    wx.NO_BORDER)
        self.btn_graficar.SetBackgroundColour(wx.Colour(255, 128, 0))
        self.btn_graficar.SetForegroundColour(wx.WHITE)

        bSizer_botonesCabecera.Add(self.btn_graficar, 0, wx.ALL, 5)


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

        self.lbl_area = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"", wx.DefaultPosition,
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

        self.lbl_registrosencontrados = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"0", wx.DefaultPosition,
                                                      wx.DefaultSize, 0)
        self.lbl_registrosencontrados.Wrap(-1)
        self.lbl_registrosencontrados.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_registrosencontrados.SetMinSize(wx.Size(60, -1))
        bSizer_totalesConsulta.Add(self.lbl_registrosencontrados, 0, wx.ALL, 5)

        ###
        self.lbl_etq_turnos = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"Turnos"
                                                                                u":",
                                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_turnos.Wrap(-1)
        bSizer_totalesConsulta.Add(self.lbl_etq_turnos, 0, wx.ALL, 5)

        self.lbl_turnos = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"", wx.DefaultPosition,
                                                      wx.DefaultSize, 0)
        self.lbl_turnos.Wrap(-1)
        self.lbl_turnos.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_turnos.SetMinSize(wx.Size(60, -1))
        bSizer_totalesConsulta.Add(self.lbl_turnos, 0, wx.ALL, 5)

        ###




        bSizer_resultados.Add(bSizer_totalesConsulta, 0, wx.EXPAND, 5)

        self.grid_totales = wx.grid.Grid(self.m_panel_resultados, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_totales.CreateGrid(1, 2)
        self.grid_totales.EnableEditing(True)
        self.grid_totales.EnableGridLines(True)
        self.grid_totales.EnableDragGridSize(False)
        self.grid_totales.SetMargins(0, 0)

        # Columns
        self.grid_totales.AutoSizeColumns()
        self.grid_totales.EnableDragColMove(False)
        self.grid_totales.EnableDragColSize(True)
        self.grid_totales.SetColLabelSize(30)
        self.grid_totales.SetColLabelValue(0, u"Total Unidades")
        self.grid_totales.SetColLabelValue(1, u"Total Toneladas")
        self.grid_totales.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_totales.EnableDragRowSize(True)
        self.grid_totales.SetRowLabelSize(50)
        self.grid_totales.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_totales.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_totales.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer_resultados.Add(self.grid_totales, 0, wx.ALL | wx.EXPAND, 5)

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

        self.lbl_nota1 = wx.StaticText(self, wx.ID_ANY,
                                       u"DobleClick sobre el encabezado de la tabla para ordenar",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_nota1.Wrap(-1)
        self.lbl_nota1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.lbl_nota1.SetForegroundColour(wx.Colour(0, 128, 0))

        bSizer_panelResultados.Add(self.lbl_nota1, 0, wx.ALL, 5)

        bSizer_principal.Add(bSizer_panelResultados, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer_principal)
        self.Layout()

        self.Centre(wx.BOTH)

        ## OPERACIONES INICIALES EAY
        self.cargar_valores_de_inicializacion()

        # Connect Events
        self.radioBox_area.Bind(wx.EVT_RADIOBOX, self.radioBox_areaOnRadioBox)
        self.btn_buscar.Bind(wx.EVT_BUTTON, self.btn_buscarOnButtonClick)
        self.btn_graficar.Bind(wx.EVT_BUTTON, self.btn_graficarOnButtonClick)
        self.grid_resultado_busqueda.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,
                                          self.grid_resultado_busquedaOnGridCellLeftDClick)
        self.grid_resultado_busqueda.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK,
                                          self.grid_resultado_busquedaOnGridLabelLeftDClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def radioBox_areaOnRadioBox(self, event):
        area_produccion = self.radioBox_area.GetStringSelection()
        self.cargar_checkList_turno(area_produccion)
        event.Skip()

    def btn_graficarOnButtonClick(self, event):

        cant_filas = self.grid_resultado_busqueda.GetNumberRows()

        if cant_filas == 0:
            wx.MessageBox(u'No hay datos para graficar, intentalo presionando el Boton Buscar', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        area = self.lbl_area.GetLabel()
        fechas = self.lbl_fechas.GetLabel()
        turnos = self.lbl_turnos.GetLabel()

        dic_valores_resumen={}
        dic_valores_detalle={}

        dic_cabecera = {'area':area, 'fechas': fechas, 'turnos': turnos}
        dic_valores ={}

        if area == 'EXTRUSION':

            list_unidades = []

            dic_valores_detalle = {}

            list_productos = []
            list_unidades = []

            for i in range(cant_filas):
                list_productos.append(self.grid_resultado_busqueda.GetCellValue(i, 1))
                list_unidades.append(int(self.grid_resultado_busqueda.GetCellValue(i, 3)))

                dic_valores_detalle = {'list_productos':list_productos, 'list_unidades':list_unidades}

        if area == 'CARGUE DE VAGONETAS':

            list_unid_resumen = []
            list_ton_resumen = []

            list_unid_resumen.append(int(self.grid_totales.GetCellValue(0, 0)))
            list_unid_resumen.append(int(self.grid_totales.GetCellValue(0, 1)))
            list_ton_resumen.append(float(self.grid_totales.GetCellValue(0, 2)))
            list_ton_resumen.append(float(self.grid_totales.GetCellValue(0, 3)))

            dic_valores_resumen = {'list_unid_resumen': list_unid_resumen, 'list_ton_resumen':list_ton_resumen}

            list_productos = []
            list_prod_ok = []
            list_prod_rotos = []
            for i in range(cant_filas):
                list_productos.append(self.grid_resultado_busqueda.GetCellValue(i, 1))
                list_prod_ok.append(int(self.grid_resultado_busqueda.GetCellValue(i, 3)))
                list_prod_rotos.append(int(self.grid_resultado_busqueda.GetCellValue(i, 4)))

                dic_valores_detalle = {'list_productos':list_productos, 'list_prod_ok':list_prod_ok, 'list_prod_rotos':list_prod_rotos}

        if area == 'DESCARGUE DE VAGONETAS':

            list_unid_resumen = []
            list_ton_resumen = []

            list_unid_resumen.append(int(self.grid_totales.GetCellValue(0, 1)))
            list_unid_resumen.append(int(self.grid_totales.GetCellValue(0, 2)))
            list_unid_resumen.append(int(self.grid_totales.GetCellValue(0, 3)))

            list_ton_resumen.append(float(self.grid_totales.GetCellValue(0, 8)))
            list_ton_resumen.append(float(self.grid_totales.GetCellValue(0, 9)))
            list_ton_resumen.append(float(self.grid_totales.GetCellValue(0, 10)))

            dic_valores_resumen = {'list_unid_resumen': list_unid_resumen, 'list_ton_resumen':list_ton_resumen}

            list_productos = []
            list_prod_primera = []
            list_prod_segunda = []
            list_prod_rotos = []
            for i in range(cant_filas):
                list_productos.append(self.grid_resultado_busqueda.GetCellValue(i, 1))
                list_prod_primera.append(int(self.grid_resultado_busqueda.GetCellValue(i, 4)))
                list_prod_segunda.append(int(self.grid_resultado_busqueda.GetCellValue(i, 5)))
                list_prod_rotos.append(int(self.grid_resultado_busqueda.GetCellValue(i, 6)))

                dic_valores_detalle = {'list_productos':list_productos, 'list_prod_primera':list_prod_primera,
                                       'list_prod_segunda':list_prod_segunda,
                                       'list_prod_rotos': list_prod_rotos
                                       }

        if area == 'DESPACHOS':

            list_unid_resumen = []
            list_ton_resumen = []

            list_unid_resumen.append(int(self.grid_totales.GetCellValue(0, 1)))
            list_unid_resumen.append(int(self.grid_totales.GetCellValue(0, 2)))

            list_ton_resumen.append(float(self.grid_totales.GetCellValue(0, 6)))
            list_ton_resumen.append(float(self.grid_totales.GetCellValue(0, 7)))

            dic_valores_resumen = {'list_unid_resumen': list_unid_resumen, 'list_ton_resumen':list_ton_resumen}

            list_productos = self.df['Producto']
            list_prod_primera = self.df['Primera']
            list_prod_segunda = self.df['Segunda']

            dic_valores_detalle = {'list_productos':list_productos, 'list_prod_primera':list_prod_primera,
                                   'list_prod_segunda':list_prod_segunda
                                   }

        import formEAY.formularios.frm_graficas.frm_GraficosHistorialDetalleProcesos as frm_GraficosHistorialDetalleProcesos
        frame_GraficosHistorialDetalleProcesos = frm_GraficosHistorialDetalleProcesos.GraficosHistorialDetalleProcesos(self, dic_cabecera,
                                                                                                                       dic_valores_resumen, dic_valores_detalle)
        frame_GraficosHistorialDetalleProcesos.Center()
        frame_GraficosHistorialDetalleProcesos.Show()

        event.Skip()

    def btn_buscarOnButtonClick(self, event):
        from formEAY.utilCAC.Utiles_proposito_general import ManejoFechasHoras

        turnos = []
        for i in self.checkList_turno.GetCheckedStrings():
            turnos.append(i)

        self.lbl_turnos.SetLabel(str(turnos))

        area_produccion = self.radioBox_area.GetStringSelection()

        cad_turno = ''
        lista_turnos_sel = self.checkList_turno.GetCheckedStrings()

        fecha_inicio = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha1)
        fecha_fin = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha2)

        if area_produccion != 'DESPACHOS':
            if len(lista_turnos_sel) == 0 :
                wx.MessageBox(u'Debes seleccionar mínimo un Turno', u'Atención', wx.OK | wx.ICON_INFORMATION)
                return 0

            for i in lista_turnos_sel:
                el_id = self.dic_turnos_todos[i][0]
                cad_turno += str(el_id) + ','
            cad_turno = cad_turno[:-1]

            if cad_turno != '':
                cad_turno = ' and id_turno in (' + cad_turno + ' )'



            rows, cabeceras = self.buscar( area_produccion, fecha_inicio, fecha_fin, cad_turno)

            if rows == None:
                self.m_panel_resultados.Hide()
            else:
                self.lbl_area.SetLabel(area_produccion)

                cad_fecha = fecha_inicio + '  al  ' + fecha_fin
                self.lbl_fechas.SetLabel(cad_fecha)
                cant_registros = str(len(rows))
                self.lbl_registrosencontrados.SetLabel(cant_registros)

                row_totales, cabeceras = self.buscarTotales(area_produccion, fecha_inicio, fecha_fin, cad_turno)

                ManipularGrillas.llenarGrilla(self.grid_totales, row_totales)
                ManipularGrillas.reemplazarValorCeldaGrilla(self.grid_totales, 'None', '0')

                self.m_panel_resultados.Show()

        if area_produccion == 'DESPACHOS':
            cad_sql ="""
                        SELECT dd.id_producto, dd.producto, p.peso,  
                                (sum(dd.cant_primera) + sum(dd.cant_segunda)) as total_unids,
                                sum(dd.cant_primera) as primera, sum(dd.cant_segunda) as segunda,
                                
                                trunc((sum(dd.cant_primera)*100.0) / ((sum(dd.cant_primera) + sum(dd.cant_segunda)) ), 2) as porct_primera, 
                                trunc((sum(dd.cant_segunda)*100.0) / ((sum(dd.cant_primera) + sum(dd.cant_segunda)) ), 2) as porct_segunda,                                 
                                
                                trunc((sum(dd.cant_primera * p.peso) + sum(dd.cant_segunda * p.peso)) / 1000000.0, 2) as Total_ton, 
                                trunc(sum(dd.cant_primera * p.peso) / 1000000.0, 2) as ton_primera, 
                                trunc(sum(dd.cant_segunda * p.peso) / 1000000.0, 2) as ton_segunda
                        FROM detalle_despacho as dd, producto as p
                        WHERE dd.activo = True and  dd.id_producto = p.id_producto AND dd.uuid in (
                            SELECT uuid
                            FROM despacho_mercancia
                            WHERE  fecha >= '{0}' and fecha <= '{1}'
                            )
                        GROUP BY dd.id_producto, dd.producto, p.peso
                        ORDER BY dd.producto
            """.format(fecha_inicio, fecha_fin)
            cabeceras = []
            rows = Ejecutar_SQL.select_varios_registros(cad_sql, 'frm_historial_detalle_procesos_ECD/btn_buscarOnButtonClick',
                                                        1000, BasesDeDatos.DB_PRINCIPAL)

            if rows == None:
                self.m_panel_resultados.Hide()
            else:
                self.lbl_area.SetLabel('DESPACHOS')

                cad_fecha = fecha_inicio + '  al  ' + fecha_fin
                self.lbl_fechas.SetLabel(cad_fecha)
                cant_registros = str(len(rows))
                self.lbl_registrosencontrados.SetLabel(cant_registros)

                ManipularGrillas.setCantidadColumnasGrilla(self.grid_resultado_busqueda , 11)
                list_cabeceras = ['id', 'Producto', 'Peso gr', 'Total Unidas', 'Unids Primera', 'Unids Segunda',
                                  '% Primera', '% Segunda',
                                  'Total ton', 'Ton Primera', 'Ton Segunda']
                ManipularGrillas.setCabecerasGrilla(self.grid_resultado_busqueda, list_cabeceras)

                ManipularGrillas.setCantidadColumnasGrilla(self.grid_totales, 8)
                list_cabeceras = ['Total Unids', 'Primera', 'Segunda', '% Primera', '% Segunda', 'Total Ton', 'Ton 1ra', 'Ton 2da']
                ManipularGrillas.setCabecerasGrilla(self.grid_totales, list_cabeceras)

                self.df = pd.DataFrame(rows, columns = ['id', 'Producto', 'Peso gr', 'Total Unids',  'Primera', 'Segunda',
                                                   '% Primera', '% Segunda',
                                                   'Total Ton', 'Ton Primera', 'Ton Segunda'])


                df_totales = self.df[['Total Unids', 'Primera', 'Segunda','% Primera', '% Segunda', 'Total Ton', 'Ton Primera', 'Ton Segunda']].sum()


                rows_resumen = []
                rows_resumen.append(df_totales.tolist())

                ManipularGrillas.llenarGrilla(self.grid_totales, rows_resumen)

                total_unids = float(self.grid_totales.GetCellValue(0,0))
                primera_unids = float(self.grid_totales.GetCellValue(0,1))
                segunda_unids = float(self.grid_totales.GetCellValue(0,2))

                porct_primera = round((primera_unids / total_unids) * 100.0, 2)
                porct_segunda = round((segunda_unids / total_unids) * 100.0, 2)

                self.grid_totales.SetCellValue(0, 3, str(porct_primera))
                self.grid_totales.SetCellValue(0, 4, str(porct_segunda))



                self.m_panel_resultados.Show()


        ManipularGrillas.llenarGrilla(self.grid_resultado_busqueda, rows)
        ManipularGrillas.reemplazarValorCeldaGrilla(self.grid_resultado_busqueda, 'None', '0')

        self.colorearGrilla()


        event.Skip()

    def grid_resultado_busquedaOnGridCellLeftDClick(self, event):
        event.Skip()

    def grid_resultado_busquedaOnGridLabelLeftDClick(self, event):

        columna = event.GetCol()
        lista_tipoColumna = []
        area = self.lbl_area.GetLabel()

        if self.orden_ascendente == True:
            self.orden_ascendente = False
        else:
            self.orden_ascendente = True

        if area == 'EXTRUSION':
            lista_tipoColumna = ['int', 'str', 'int', 'int', 'float']
        if area == 'CARGUE DE VAGONETAS':
            lista_tipoColumna = ['int', 'str', 'int', 'int', 'int', 'float', 'float', 'float']
        if area == 'DESCARGUE DE VAGONETAS':
            lista_tipoColumna = ['int', 'str', 'int', 'int', 'int', 'int',  'int', 'float', 'float', 'float', 'float', 'float', 'float']
        if area == 'DESPACHOS':
            lista_tipoColumna = ['int', 'str', 'int', 'int', 'int', 'int',  'float', 'float', 'float', 'float', 'float']


        ManipularGrillas.ordenarGrillaPorColumna(self.grid_resultado_busqueda, columna, lista_tipoColumna,
                                                 self.orden_ascendente)
        self.colorearGrilla()
        event.Skip()


    ##  FUNCIONES EAY

    def colorearGrilla(self):
        area_produccion = self.lbl_area.GetLabel()

        if area_produccion == AREA_EXTRUSION:
            dic_color = {3: COLOR_RESALTE_PRIMERA, 4: COLOR_RESALTE_SEGUNDA}
            ManipularGrillas.setColorFondoCeldaGrilla(self.grid_resultado_busqueda, dic_color)

            dic_color = {0: COLOR_RESALTE_PRIMERA, 1: COLOR_RESALTE_SEGUNDA}
            ManipularGrillas.setColorFondoCeldaGrilla(self.grid_totales, dic_color)

        if area_produccion == AREA_CARGUE_VAGONETAS:
            dic_color = {3: COLOR_RESALTE_TOTAL, 4: COLOR_RESALTE_ROTURA_CLARO,
                         5: COLOR_RESALTE_TOTAL, 6: COLOR_RESALTE_ROTURA_CLARO,
                         7: COLOR_RESALTE_ROTURA
                         }
            ManipularGrillas.setColorFondoCeldaGrilla(self.grid_resultado_busqueda, dic_color)

            dic_color = {0: COLOR_RESALTE_TOTAL, 1: COLOR_RESALTE_ROTURA_CLARO,
                         2: COLOR_RESALTE_TOTAL, 3: COLOR_RESALTE_ROTURA_CLARO,
                         4: COLOR_RESALTE_ROTURA
                         }
            ManipularGrillas.setColorFondoCeldaGrilla(self.grid_totales, dic_color)

        if area_produccion == AREA_DESCARGUE_VAGONETAS:
            dic_color = {3: COLOR_RESALTE_TOTAL,
                         4: COLOR_RESALTE_PRIMERA, 5: COLOR_RESALTE_SEGUNDA, 6: COLOR_RESALTE_ROTURA,
                         7: COLOR_RESALTE_PRIMERA, 8: COLOR_RESALTE_SEGUNDA, 9: COLOR_RESALTE_ROTURA,
                         10: COLOR_RESALTE_PRIMERA, 11: COLOR_RESALTE_SEGUNDA, 12: COLOR_RESALTE_ROTURA,
                         }
            ManipularGrillas.setColorFondoCeldaGrilla(self.grid_resultado_busqueda, dic_color)

            dic_color = {0: COLOR_RESALTE_TOTAL,
                         1: COLOR_RESALTE_PRIMERA, 2: COLOR_RESALTE_SEGUNDA, 3: COLOR_RESALTE_ROTURA,
                         4: COLOR_RESALTE_PRIMERA, 5: COLOR_RESALTE_SEGUNDA, 6: COLOR_RESALTE_ROTURA,
                         7: COLOR_RESALTE_TOTAL,
                         8: COLOR_RESALTE_PRIMERA, 9: COLOR_RESALTE_SEGUNDA, 10: COLOR_RESALTE_ROTURA,
                         }
            ManipularGrillas.setColorFondoCeldaGrilla(self.grid_totales, dic_color)

        if area_produccion == 'DESPACHOS':
            dic_color = {3: COLOR_RESALTE_TOTAL, 4: COLOR_RESALTE_PRIMERA, 5: COLOR_RESALTE_SEGUNDA,
                         8: COLOR_RESALTE_TOTAL, 9: COLOR_RESALTE_PRIMERA, 10: COLOR_RESALTE_SEGUNDA
                         }
            ManipularGrillas.setColorFondoCeldaGrilla(self.grid_resultado_busqueda, dic_color)

            dic_color = {0: COLOR_RESALTE_TOTAL, 1: COLOR_RESALTE_PRIMERA, 2: COLOR_RESALTE_SEGUNDA,
                         5: COLOR_RESALTE_TOTAL, 6: COLOR_RESALTE_PRIMERA, 7: COLOR_RESALTE_SEGUNDA
                         }
            ManipularGrillas.setColorFondoCeldaGrilla(self.grid_totales, dic_color)

        self.Layout()

    def buscarTotales(self, area_produccion, fecha_inicio, fecha_fin, cad_turno):
        rows = []
        sSql = ''
        cabeceras = []
        if area_produccion == AREA_CARGUE_VAGONETAS:
            sSql = """
                SELECT  SUM(t1.total_unidades), 
                        SUM(t2.cant_rotos), 
                        trunc(SUM(t1.ton_cargados), 2), 
                        trunc(SUM(t2.ton_rotos),2),
                        trunc(SUM((100.0 * t2.ton_rotos)) / SUM((t2.ton_rotos + t1.ton_cargados )), 2)                     
                    FROM 
                    (   SELECT  dcv.id_producto as el_id, dcv.producto as producto, sum(dcv.unidades_producto) as total_unidades,
                                p.peso as peso, p.peso * sum(dcv.unidades_producto) / 1000000.0  as ton_cargados   
                        FROM  detalle_cargue_vagonetas as dcv, producto as p
                        WHERE   p.id_producto = dcv.id_producto   and  dcv.uuid in 
                                (                
                                SELECT uuid
                                FROM cabecera_proceso_ecd
                                WHERE fecha_inicio >= '{0}' and fecha_inicio <= '{1}' AND area_produccion = 'CARGUE DE VAGONETAS'
                                        {2}  and activo = True 
                                )
                        GROUP BY  dcv.id_producto, dcv.producto, p.peso                                   
                    ) AS t1
                FULL OUTER  JOIN
                    (   SELECT rcv.id_producto as el_id, rcv.producto, sum(rcv.cant_rotos) as cant_rotos,
                                p.peso * sum(rcv.cant_rotos) / 1000000.0  as ton_rotos                             
                        FROM   rotura_cargue_vagonetas as rcv, producto as p
                        WHERE  p.id_producto = rcv.id_producto   and  rcv.uuid in 
                                (
                                SELECT uuid
                                FROM cabecera_proceso_ecd
                                WHERE fecha_inicio >= '{0}' and fecha_inicio <= '{1}' AND area_produccion = 'CARGUE DE VAGONETAS'
                                        {2}  and activo = True 
                                )
                        GROUP BY rcv.id_producto, rcv.producto, p.peso 
                    ) AS t2                
                 ON ( t1.el_id = t2.el_id)       
            
            """.format(fecha_inicio, fecha_fin, cad_turno)

            cabeceras = ['Total Unid Primera', 'Total Unids Rotura', 'Total Toneladas', 'Toneladas Rotura', '% Rotura']

        if area_produccion == AREA_DESCARGUE_VAGONETAS:
            sSql = """
                    SELECT 	sum(de_primera) + sum(de_segunda) + sum(rotos) as total_unidades, 
                            sum(de_primera) as primera, 
                            sum(de_segunda) as segunda, 
                            sum(rotos) as rotos,
                            trunc((sum(de_primera)*100.0) / (sum(de_primera) + sum(de_segunda) + sum(rotos)), 2) as porcentaje_primera,
                            trunc((sum(de_segunda)*100.0) / (sum(de_primera) + sum(de_segunda) + sum(rotos)), 2) as porcentaje_segunda,
                            trunc((sum(rotos)*100.0) / (sum(de_primera) + sum(de_segunda) + sum(rotos)), 2) as porcentaje_rotura,
                            trunc((sum(p.peso * de_primera) + sum(p.peso * de_segunda) + sum(p.peso * rotos)) / 1000000.0, 2) as Total_Toneladas,
                            trunc(sum(p.peso * de_primera) /1000000.0, 2) as ton_primera,
                            trunc(sum(p.peso * de_segunda) /1000000.0, 2) as ton_segunda,
                            trunc(sum(p.peso * rotos) /1000000.0, 2) as ton_rotos
                    FROM producto as p, detalle_descargue_vagonetas as ddv
                    WHERE p.id_producto = ddv.id_producto and uuid in (
                        SELECT uuid
                        FROM cabecera_proceso_ecd
                        WHERE fecha_inicio >= '{0}' and fecha_inicio <= '{1}' AND area_produccion = 'DESCARGUE DE VAGONETAS'
                            {2} and activo = True 
                                            )                  
                    """.format(fecha_inicio, fecha_fin, cad_turno)

            cabeceras = ['Total Unidades', 'Primera', 'Segunda',  'Rotura',
                         '% primera', '% segunda', '% Rotura','Total Toneladas', 'Ton 1ra', 'Ton 2da', 'Ton Rotura']

        if area_produccion == AREA_EXTRUSION :
                sSql = """
                            SELECT sum(unidades_producto)  as total_unidades,
                                   trunc( sum( p.peso * unidades_producto / 1000000.0), 2) as ton_producto
                            FROM producto as p, detalle_extrusion as de
                            WHERE  p.id_producto = de.id_producto and  uuid in (
                                SELECT uuid
                                FROM cabecera_proceso_ecd
                                WHERE fecha_inicio >= '{0}' and fecha_inicio <= '{1}' AND area_produccion = 'EXTRUSION'
                                    {2} and activo = True 
                                                    )                  
                            """.format(fecha_inicio, fecha_fin, cad_turno)

                cabeceras = ['Total Unidades', 'Total Toneladas']


        ManipularGrillas.setCantidadColumnasGrilla(self.grid_totales, len(cabeceras))
        ManipularGrillas.setCabecerasGrilla(self.grid_totales, cabeceras)
        rows = Ejecutar_SQL.select_varios_registros(sSql, 'frm_historial_procesos_ECD/buscarTotales()',  1, BasesDeDatos.DB_PRINCIPAL)

        return rows, cabeceras

    def buscar(self, area_produccion, fecha_inicio, fecha_fin, cad_turno):
        rows = []
        sSql = ''
        cabeceras = []

        if area_produccion == AREA_CARGUE_VAGONETAS:
            sSql = """
                    SELECT t1.el_id, t1.producto, t1.peso, t1.total_unidades, t2.cant_rotos, 
                            trunc(t1.ton_cargados, 2), 
                            trunc(t2.ton_rotos, 2),
                            trunc((100.0 * t2.ton_rotos) / (t2.ton_rotos + t1.ton_cargados), 2)
                      
                    FROM
                    (   SELECT  dcv.id_producto as el_id, dcv.producto as producto, sum(dcv.unidades_producto) as total_unidades,
                                p.peso as peso, p.peso * sum(dcv.unidades_producto) / 1000000.0  as ton_cargados   
                        FROM  detalle_cargue_vagonetas as dcv, producto as p
                        WHERE   p.id_producto = dcv.id_producto   and  dcv.uuid in 
                                (                
                                SELECT uuid
                                FROM cabecera_proceso_ecd
                                WHERE fecha_inicio >= '{0}' and fecha_inicio <= '{1}' AND area_produccion = 'CARGUE DE VAGONETAS'
                                        {2}  and activo = True 
                                )
                        GROUP BY  dcv.id_producto, dcv.producto, p.peso                                   
                    ) AS t1
                FULL OUTER  JOIN
                    (   SELECT rcv.id_producto as el_id, rcv.producto, sum(rcv.cant_rotos) as cant_rotos,
                                p.peso * sum(rcv.cant_rotos) / 1000000.0  as ton_rotos                             
                        FROM   rotura_cargue_vagonetas as rcv, producto as p
                        WHERE  p.id_producto = rcv.id_producto   and  rcv.uuid in 
                                (
                                SELECT uuid
                                FROM cabecera_proceso_ecd
                                WHERE fecha_inicio >= '{0}' and fecha_inicio <= '{1}' AND area_produccion = 'CARGUE DE VAGONETAS'
                                        {2}  and activo = True 
                                )
                        GROUP BY rcv.id_producto, rcv.producto, p.peso 
                    ) AS t2                
                 ON ( t1.el_id = t2.el_id)                   
                            """.format(fecha_inicio, fecha_fin, cad_turno)

            cabeceras = ['id Producto', 'Producto', 'Peso gramos', 'Total Unid. Primera', 'Unid. Rotura', 'Toneladas',
                         'Toneladas Rotura', '% Rotura']

        if area_produccion == AREA_DESCARGUE_VAGONETAS:
            sSql = """
                    SELECT p.id_producto, producto, p.peso, (sum(de_primera) + sum(de_segunda) + sum(rotos)) as total_unidades, sum(de_primera) as primera, 
                            sum(de_segunda) as segunda, sum(rotos) as rotos,
                            trunc((sum(de_primera)*100.0) / (sum(de_primera) + sum(de_segunda) + sum(rotos)), 2) as porcentaje_primera,
                            trunc((sum(de_segunda)*100.0) / (sum(de_primera) + sum(de_segunda) + sum(rotos)), 2) as porcentaje_segunda,
                            trunc((sum(rotos)*100.0) / (sum(de_primera) + sum(de_segunda) + sum(rotos)), 2) as porcentaje_rotura,
                            trunc((p.peso * sum(de_primera) /1000000.0), 2) as ton_primera,
                            trunc((p.peso * sum(de_segunda) /1000000.0), 2) as ton_segunda,
                            trunc((p.peso * sum(rotos) /1000000.0), 2) as ton_rotos
                    FROM producto as p, detalle_descargue_vagonetas as ddv
                    WHERE p.id_producto = ddv.id_producto and uuid in (
                        SELECT uuid
                        FROM cabecera_proceso_ecd
                        WHERE fecha_inicio >= '{0}' and fecha_inicio <= '{1}' AND area_produccion = 'DESCARGUE DE VAGONETAS'
                            {2} and activo = True 
                                            )
                        GROUP BY p.id_producto, producto                    
                    """.format(fecha_inicio, fecha_fin, cad_turno)

            cabeceras = ['id Producto', 'Producto', 'Peso gramos',  'Total Unidades', 'Primera', 'Segunda', 'Rotura',
                         '% primera', '% segunda', '% Rotura', 'Ton 1ra', 'Ton 2da', 'Ton Rotura']

        if area_produccion == AREA_EXTRUSION :
                sSql = """
                            SELECT p.id_producto, producto, p.peso,  sum(unidades_producto)  as total_unidades,
                                    trunc(p.peso * sum(unidades_producto) / 1000000.0, 2) as ton_producto
                            FROM producto as p, detalle_extrusion as de
                            WHERE  p.id_producto = de.id_producto and  uuid in (
                                SELECT uuid
                                FROM cabecera_proceso_ecd
                                WHERE fecha_inicio >= '{0}' and fecha_inicio <= '{1}' AND area_produccion = 'EXTRUSION'
                                    {2} and activo = True 
                                                    )
                                GROUP BY p.id_producto, producto                    
                            """.format(fecha_inicio, fecha_fin, cad_turno)

                cabeceras = ['id Producto', 'Producto', 'Peso gramos','Total Unidades', 'Toneladas']

        ManipularGrillas.setCantidadColumnasGrilla(self.grid_resultado_busqueda, len(cabeceras))
        ManipularGrillas.setCabecerasGrilla(self.grid_resultado_busqueda, cabeceras)
        rows = Ejecutar_SQL.select_varios_registros(sSql, 'frm_historial_procesos_ECD/buscar()',  500, BasesDeDatos.DB_PRINCIPAL)

        return rows, cabeceras

    def cargar_checkList_turno(self, area_produccion):

        if area_produccion == 'DESPACHOS':
            self.checkList_turno.Clear()
        else:
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
        self.grid_totales.AutoSizeColumns()

    def set_configuaracion_grid_resultado_busqueda(self):

        # list_columnas = [0, 1, 2, 3, 4, 5, 6]
        # ManipularGrillas.setColumnasSoloLectura(self.grid_resultado_busqueda, list_columnas)

        self.grid_resultado_busqueda.EnableEditing(False)

        self.grid_resultado_busqueda.AutoSizeColumns()
