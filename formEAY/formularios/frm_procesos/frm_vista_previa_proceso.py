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

import pandas as pd

from pyeay.grillas import ManipularGrillas
from pyeay.dbcac.conexiondb import Ejecutar_SQL, GenerarSql
from formEAY.constantesCAC.constantesCAC import BasesDeDatos


###########################################################################
## Class VistaPreviaProceso
###########################################################################

class VistaPreviaProceso(wx.Frame):

    def __init__(self, parent, usuario, dir_mac, img_proceso, tipoProceso, uuid=-1, estado='True'):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Vista previa proceso", pos=wx.DefaultPosition,
                          size=wx.Size(828, 680), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(650, 600), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.usuario = usuario
        self.dir_mac = dir_mac
        self.tipoProceso = tipoProceso
        self.uuid = uuid
        self.estado=estado

        self.orden_ascendente = True
        self.columna = 0

        bSizer_extrusion = wx.BoxSizer(wx.VERTICAL)


        bSizer_panel_principal = wx.BoxSizer(wx.VERTICAL)

        bSizer_panel_cabecera = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_cabecera = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel_cabecera.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.bitmap_logo_proceso = wx.StaticBitmap(self.panel_cabecera, wx.ID_ANY,
                                                   wx.Bitmap(img_proceso,
                                                             wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.bitmap_logo_proceso, 0, wx.ALL, 5)

        bSizer9.Add(bSizer7, 0, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_turno = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Turno:", wx.DefaultPosition,
                                           wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_turno.Wrap(-1)
        bSizer14.Add(self.lbl_etq_turno, 0, wx.ALL, 5)

        self.lbl_turno = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"el_turno", wx.DefaultPosition, wx.DefaultSize,
                                       0)
        self.lbl_turno.Wrap(-1)
        self.lbl_turno.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer14.Add(self.lbl_turno, 1, wx.ALL, 5)

        self.lbl_etq_total_coches = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Total coches:", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.lbl_etq_total_coches.Wrap(-1)
        bSizer14.Add(self.lbl_etq_total_coches, 0, wx.ALL, 5)

        self.lbl_total_coches = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"100", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_total_coches.Wrap(-1)
        self.lbl_total_coches.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer14.Add(self.lbl_total_coches, 0, wx.ALL, 5)

        self.lbl_etq_total_unidades = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Total Unidades:",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_total_unidades.Wrap(-1)
        bSizer14.Add(self.lbl_etq_total_unidades, 0, wx.ALL, 5)

        self.lbl_total_unides = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"893", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_total_unides.Wrap(-1)
        self.lbl_total_unides.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer14.Add(self.lbl_total_unides, 0, wx.ALL, 5)

        bSizer6.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer81 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fecha_inicio = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Inicio:", wx.DefaultPosition,
                                                  wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_fecha_inicio.Wrap(-1)
        bSizer81.Add(self.lbl_etq_fecha_inicio, 0, wx.ALL, 5)

        self.lbl_fecha_inicio = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"25 oct 2021", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_fecha_inicio.Wrap(-1)
        self.lbl_fecha_inicio.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer81.Add(self.lbl_fecha_inicio, 0, wx.ALL, 5)

        bSizer13.Add(bSizer81, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fecha_fin = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Fin:", wx.DefaultPosition,
                                               wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lbl_etq_fecha_fin.Wrap(-1)
        bSizer8.Add(self.lbl_etq_fecha_fin, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        self.lbl_fecha_fin = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"21 de diciembre 2021", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.lbl_fecha_fin.Wrap(-1)
        self.lbl_fecha_fin.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer8.Add(self.lbl_fecha_fin, 0, wx.ALL, 5)

        bSizer13.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer6.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer9.Add(bSizer6, 1, wx.EXPAND, 5)

        self.panel_cabecera.SetSizer(bSizer9)
        self.panel_cabecera.Layout()
        bSizer9.Fit(self.panel_cabecera)
        bSizer_panel_cabecera.Add(self.panel_cabecera, 1, wx.EXPAND | wx.ALL, 5)

        bSizer_panel_principal.Add(bSizer_panel_cabecera, 0, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_panel_empleado = wx.BoxSizer(wx.VERTICAL)

        bSizer4.Add(bSizer_panel_empleado, 0, wx.EXPAND, 5)

        bSizer_panel_extrusion1 = wx.BoxSizer(wx.VERTICAL)

        self.panel1_extrusion = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel1_extrusion.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_panel_extrusion = wx.BoxSizer(wx.VERTICAL)

        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

        self.grid_productos = wx.grid.Grid(self.panel1_extrusion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_productos.CreateGrid(5, 10)
        self.grid_productos.EnableEditing(False)
        self.grid_productos.EnableGridLines(True)
        self.grid_productos.EnableDragGridSize(False)
        self.grid_productos.SetMargins(0, 0)

        # Columns
        self.grid_productos.AutoSizeColumns()
        self.grid_productos.EnableDragColMove(False)
        self.grid_productos.EnableDragColSize(True)
        self.grid_productos.SetColLabelSize(30)
        self.grid_productos.SetColLabelValue(0, u"Producto")
        self.grid_productos.SetColLabelValue(1, u"Coche")
        self.grid_productos.SetColLabelValue(2, u"Cant Coches")
        self.grid_productos.SetColLabelValue(3, u"Unid Producto")
        self.grid_productos.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_productos.EnableDragRowSize(True)
        self.grid_productos.SetRowLabelSize(40)
        self.grid_productos.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_productos.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_productos.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer16.Add(self.grid_productos, 5, wx.ALL | wx.EXPAND, 5)

        self.grid_rotura = wx.grid.Grid(self.panel1_extrusion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_rotura.CreateGrid(5, 3)
        self.grid_rotura.EnableEditing(False)
        self.grid_rotura.EnableGridLines(True)
        self.grid_rotura.EnableDragGridSize(False)
        self.grid_rotura.SetMargins(0, 0)

        # Columns
        self.grid_rotura.AutoSizeColumns()
        self.grid_rotura.EnableDragColMove(False)
        self.grid_rotura.EnableDragColSize(True)
        self.grid_rotura.SetColLabelSize(30)
        self.grid_rotura.SetColLabelValue(0, u"id")
        self.grid_rotura.SetColLabelValue(1, u"Producto")
        self.grid_rotura.SetColLabelValue(2, u"Cant Rotos")
        self.grid_rotura.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_rotura.EnableDragRowSize(True)
        self.grid_rotura.SetRowLabelSize(40)
        self.grid_rotura.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_rotura.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_rotura.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer16.Add(self.grid_rotura, 3, wx.ALL, 5)

        bSizer_panel_extrusion.Add(bSizer16, 1, wx.EXPAND, 5)

        self.panel1_extrusion.SetSizer(bSizer_panel_extrusion)
        self.panel1_extrusion.Layout()
        bSizer_panel_extrusion.Fit(self.panel1_extrusion)
        bSizer_panel_extrusion1.Add(self.panel1_extrusion, 1, wx.EXPAND | wx.ALL, 5)

        bSizer4.Add(bSizer_panel_extrusion1, 2, wx.EXPAND, 5)

        bSizer_panel_principal.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer_notebook = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.NB_NOPAGETHEME | wx.FULL_REPAINT_ON_RESIZE)
        self.panel_empleado = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TAB_TRAVERSAL)
        self.panel_empleado.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer47 = wx.BoxSizer(wx.VERTICAL)

        self.grid_empleados = wx.grid.Grid(self.panel_empleado, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_empleados.CreateGrid(5, 3)
        self.grid_empleados.EnableEditing(True)
        self.grid_empleados.EnableGridLines(True)
        self.grid_empleados.EnableDragGridSize(False)
        self.grid_empleados.SetMargins(0, 0)

        # Columns
        self.grid_empleados.AutoSizeColumns()
        self.grid_empleados.EnableDragColMove(False)
        self.grid_empleados.EnableDragColSize(True)
        self.grid_empleados.SetColLabelSize(30)
        self.grid_empleados.SetColLabelValue(0, u"id")
        self.grid_empleados.SetColLabelValue(1, u"Nombre")
        self.grid_empleados.SetColLabelValue(2, u"Apellidos")
        self.grid_empleados.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_empleados.EnableDragRowSize(True)
        self.grid_empleados.SetRowLabelSize(40)
        self.grid_empleados.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_empleados.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_empleados.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer47.Add(self.grid_empleados, 0, wx.ALL, 5)

        self.panel_empleado.SetSizer(bSizer47)
        self.panel_empleado.Layout()
        bSizer47.Fit(self.panel_empleado)
        self.m_notebook1.AddPage(self.panel_empleado, u"Empleados", True)
        self.panel_notebook_recesos = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                               wx.TAB_TRAVERSAL)
        self.panel_notebook_recesos.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_panel_notebook_recesos = wx.BoxSizer(wx.VERTICAL)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        bSizer_panel_notebook_recesos.Add(bSizer36, 0, wx.EXPAND, 5)

        bSizer341 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer48 = wx.BoxSizer(wx.VERTICAL)

        self.grid_recesos = wx.grid.Grid(self.panel_notebook_recesos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_recesos.CreateGrid(5, 3)
        self.grid_recesos.EnableEditing(True)
        self.grid_recesos.EnableGridLines(True)
        self.grid_recesos.EnableDragGridSize(False)
        self.grid_recesos.SetMargins(0, 0)

        # Columns
        self.grid_recesos.AutoSizeColumns()
        self.grid_recesos.EnableDragColMove(False)
        self.grid_recesos.EnableDragColSize(True)
        self.grid_recesos.SetColLabelSize(30)
        self.grid_recesos.SetColLabelValue(0, u"id")
        self.grid_recesos.SetColLabelValue(1, u"Receso")
        self.grid_recesos.SetColLabelValue(2, u"Minutos")
        self.grid_recesos.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_recesos.EnableDragRowSize(True)
        self.grid_recesos.SetRowLabelSize(40)
        self.grid_recesos.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_recesos.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_recesos.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer48.Add(self.grid_recesos, 1, wx.ALL | wx.EXPAND, 5)

        bSizer341.Add(bSizer48, 1, wx.EXPAND, 5)

        bSizer_panel_notebook_recesos.Add(bSizer341, 1, wx.EXPAND, 5)

        self.panel_notebook_recesos.SetSizer(bSizer_panel_notebook_recesos)
        self.panel_notebook_recesos.Layout()
        bSizer_panel_notebook_recesos.Fit(self.panel_notebook_recesos)
        self.m_notebook1.AddPage(self.panel_notebook_recesos, u"Recesos Programados", False)
        self.panel_notebook_novedades1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                  wx.TAB_TRAVERSAL)
        self.panel_notebook_novedades1.SetBackgroundColour(wx.Colour(255, 255, 255))

        panel_notebook_novedades = wx.BoxSizer(wx.VERTICAL)

        bSizer342 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer521 = wx.BoxSizer(wx.VERTICAL)

        self.grid_novedades = wx.grid.Grid(self.panel_notebook_novedades1, wx.ID_ANY, wx.DefaultPosition,
                                           wx.DefaultSize, 0)

        # Grid
        self.grid_novedades.CreateGrid(5, 5)
        self.grid_novedades.EnableEditing(True)
        self.grid_novedades.EnableGridLines(True)
        self.grid_novedades.EnableDragGridSize(False)
        self.grid_novedades.SetMargins(0, 0)

        # Columns
        self.grid_novedades.AutoSizeColumns()
        self.grid_novedades.EnableDragColMove(False)
        self.grid_novedades.EnableDragColSize(True)
        self.grid_novedades.SetColLabelSize(30)
        self.grid_novedades.SetColLabelValue(0, u"id")
        self.grid_novedades.SetColLabelValue(1, u"Fecha")
        self.grid_novedades.SetColLabelValue(2, u"Hora")
        self.grid_novedades.SetColLabelValue(3, u"parada (min)")
        self.grid_novedades.SetColLabelValue(4, u"Novedad")
        self.grid_novedades.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_novedades.SetRowSize(0, 19)
        self.grid_novedades.SetRowSize(1, 18)
        self.grid_novedades.SetRowSize(2, 19)
        self.grid_novedades.SetRowSize(3, 19)
        self.grid_novedades.SetRowSize(4, 19)
        self.grid_novedades.EnableDragRowSize(True)
        self.grid_novedades.SetRowLabelSize(40)
        self.grid_novedades.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_novedades.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_novedades.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer521.Add(self.grid_novedades, 1, wx.ALL | wx.EXPAND, 5)

        bSizer342.Add(bSizer521, 1, wx.EXPAND, 5)

        panel_notebook_novedades.Add(bSizer342, 1, wx.EXPAND, 5)

        self.panel_notebook_novedades1.SetSizer(panel_notebook_novedades)
        self.panel_notebook_novedades1.Layout()
        panel_notebook_novedades.Fit(self.panel_notebook_novedades1)
        self.m_notebook1.AddPage(self.panel_notebook_novedades1, u"Novedades", False)
        self.panel_notebook_notas1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.TAB_TRAVERSAL)
        self.panel_notebook_notas1.SetBackgroundColour(wx.Colour(255, 255, 255))

        panel_notebook_notas = wx.BoxSizer(wx.VERTICAL)

        bSizer3421 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5211 = wx.BoxSizer(wx.VERTICAL)

        self.grid_notas = wx.grid.Grid(self.panel_notebook_notas1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_notas.CreateGrid(5, 6)
        self.grid_notas.EnableEditing(True)
        self.grid_notas.EnableGridLines(True)
        self.grid_notas.EnableDragGridSize(False)
        self.grid_notas.SetMargins(0, 0)

        # Columns
        self.grid_notas.AutoSizeColumns()
        self.grid_notas.EnableDragColMove(False)
        self.grid_notas.EnableDragColSize(True)
        self.grid_notas.SetColLabelSize(30)
        self.grid_notas.SetColLabelValue(0, u"id")
        self.grid_notas.SetColLabelValue(1, u"Fecha")
        self.grid_notas.SetColLabelValue(2, u"Relevancia")
        self.grid_notas.SetColLabelValue(3, u"Contexto")
        self.grid_notas.SetColLabelValue(4, u"Nota")
        self.grid_notas.SetColLabelValue(5, u"Contranota")
        self.grid_notas.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_notas.SetRowSize(0, 19)
        self.grid_notas.SetRowSize(1, 18)
        self.grid_notas.SetRowSize(2, 19)
        self.grid_notas.SetRowSize(3, 19)
        self.grid_notas.SetRowSize(4, 19)
        self.grid_notas.EnableDragRowSize(True)
        self.grid_notas.SetRowLabelSize(40)
        self.grid_notas.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_notas.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_notas.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer5211.Add(self.grid_notas, 1, wx.ALL | wx.EXPAND, 5)

        bSizer3421.Add(bSizer5211, 1, wx.EXPAND, 5)

        panel_notebook_notas.Add(bSizer3421, 1, wx.EXPAND, 5)

        self.panel_notebook_notas1.SetSizer(panel_notebook_notas)
        self.panel_notebook_notas1.Layout()
        panel_notebook_notas.Fit(self.panel_notebook_notas1)
        self.m_notebook1.AddPage(self.panel_notebook_notas1, u"Notas", False)

        bSizer_notebook.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        bSizer_panel_principal.Add(bSizer_notebook, 1, wx.EXPAND, 5)

        bSizer_pie_de_formulario = wx.BoxSizer(wx.HORIZONTAL)

        bSizer56 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_ver_formato = wx.Button(self, wx.ID_ANY, u"Ver formato", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer56.Add(self.btn_ver_formato, 0, wx.ALL, 5)

        self.btn_ver_procedimiento = wx.Button(self, wx.ID_ANY, u"Ver Procedimiento", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        bSizer56.Add(self.btn_ver_procedimiento, 0, wx.ALL, 5)

        self.lbl_etq_estado = wx.StaticText(self, wx.ID_ANY, u"Estado:", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_RIGHT)
        self.lbl_etq_estado.Wrap(-1)
        bSizer56.Add(self.lbl_etq_estado, 1, wx.ALL, 5)

        self.lbl_estado = wx.StaticText(self, wx.ID_ANY, u"ACTIVO", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT)
        self.lbl_estado.Wrap(-1)
        self.lbl_estado.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer56.Add(self.lbl_estado, 1, wx.ALL, 5)



        bSizer_pie_de_formulario.Add(bSizer56, 1, wx.EXPAND, 5)

        bSizer55 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_anular = wx.Button(self, wx.ID_ANY, u"&Anular", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.btn_anular.SetForegroundColour(wx.Colour(255, 255, 255))
        self.btn_anular.SetBackgroundColour(wx.Colour(255, 0, 0))

        bSizer55.Add(self.btn_anular, 0, wx.ALL, 5)

        bSizer_pie_de_formulario.Add(bSizer55, 0, wx.EXPAND, 5)

        bSizer_panel_principal.Add(bSizer_pie_de_formulario, 0, wx.EXPAND, 5)

        bSizer_extrusion.Add(bSizer_panel_principal, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer_extrusion)

        ## VALORES INICIALES EAY

        self.func_inicializarValores()


        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.grid_productos.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.grid_productosOnGridLabelLeftDClick)
        self.m_notebook1.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.m_notebook1OnNotebookPageChanged)
        self.grid_novedades.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_novedadesOnGridCellLeftClick)
        self.grid_notas.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_notasOnGridCellLeftClick)
        self.btn_ver_formato.Bind(wx.EVT_BUTTON, self.btn_ver_formatoOnButtonClick)
        self.btn_ver_procedimiento.Bind(wx.EVT_BUTTON, self.btn_ver_procedimientoOnButtonClick)
        self.btn_anular.Bind(wx.EVT_BUTTON, self.btn_anularOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def grid_productosOnGridLabelLeftDClick(self, event):
        columna = event.GetCol()

        if self.orden_ascendente == True:
            self.orden_ascendente = False
        else:
            self.orden_ascendente = True


        self.columna = columna

        lista_tipoColumna = ['int', 'str', 'str', 'int', 'int', 'int', 'int',
                             'float', 'float', 'float']

        ManipularGrillas.ordenarGrillaPorColumna(self.grid_productos, self.columna, lista_tipoColumna,
                                                 self.orden_ascendente)


        event.Skip()

    def m_notebook1OnNotebookPageChanged(self, event):
        event.Skip()

    def grid_novedadesOnGridCellLeftClick(self, event):
        event.Skip()

    def grid_notasOnGridCellLeftClick(self, event):
        event.Skip()

    def btn_ver_formatoOnButtonClick(self, event):
        event.Skip()

    def btn_ver_procedimientoOnButtonClick(self, event):
        event.Skip()

    def btn_anularOnButtonClick(self, event):

        if self.uuid == -1:

            cad_sql = """
                                SELECT turno, total_coches, total_unidades, fecha_inicio, fecha_fin, uuid
                                FROM cabecera_proceso_ecd 
                                WHERE area_produccion = '{0}' and id_cabecera in
                                    (     
                                        SELECT MAX(id_cabecera) 
                                                FROM cabecera_proceso_ecd 
                                                WHERE area_produccion = '{0}' and activo ='true'
                                    )
                            """.format(self.tipoProceso)

            row = Ejecutar_SQL.select_un_registro(cad_sql, 'func_buscar_id_ultimoProceso', BasesDeDatos.DB_PRINCIPAL)
            self.uuid = str(row['uuid'])

        cad_sql = """ UPDATE cabecera_proceso_ecd SET activo='false'
                WHERE uuid = '{0}'
        """.format(self.uuid)

        rta = Ejecutar_SQL.update_filas(cad_sql, 'btn_anularOnButtonClick', BasesDeDatos.DB_PRINCIPAL)

        if rta == 1:
            ## AJUSTAMOS LOS STOCKS DE ACUERDO AL PROCESO
            if self.tipoProceso == 'EXTRUSION':
                self.func_actualizar_stock_productos_extrusion()
            if self.tipoProceso == 'COCHADO':
                self.func_actualizar_stock_productos_cochado()
            if self.tipoProceso == 'CARGUE DE VAGONETAS':
                self.func_actualizar_stock_productos_cargueVagonetas()
            if self.tipoProceso == 'DESCARGUE DE VAGONETAS':
                self.func_actualizar_stock_productos_descargueVagonetas()


            mensaje= u'El Proceso de ' + self.tipoProceso + '  fue realizado correctamente'
            wx.MessageBox(mensaje, u'Atención', wx.OK | wx.ICON_INFORMATION)
            self.Destroy()
        else:
            wx.MessageBox(u'Se han presentado problemas, no fue posible eliminar el proceso', u'Atención', wx.OK | wx.ICON_INFORMATION)


        event.Skip()


    ##FUNCIONES EAY

    def func_actualizar_stock_productos_extrusion(self):

        rows = self.func_crear_dataframe_producto_extrusion()

        nom_tabla = 'producto'
        cols_busqueda = [0]
        cols_a_modificar = [1]

        dic_operaciones = {'stock_extrusion':'stock_extrusion - '}

        nom_campos = ['id_producto', 'stock_extrusion']
        tipo_campos = ['int', 'int']

        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows, cols_busqueda, cols_a_modificar, nom_campos,
                                                          tipo_campos, dic_operaciones)

        rta = Ejecutar_SQL.insert_filas(sSql, 'frm_vista_previa_proceso/func_actualizar_stock_productos_extrusion', BasesDeDatos.DB_PRINCIPAL)

        return rta

    def func_actualizar_stock_productos_cochado(self):

        rows_primera, rows_total = self.func_crear_dataframe_producto_cochado()

        nom_tabla = 'producto'
        cols_busqueda = [0]
        cols_a_modificar = [1]

        dic_operaciones = {'stock_cochado':'stock_cochado - '}
        nom_campos = ['id_producto', 'stock_cochado']
        tipo_campos = ['int', 'int']
        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows_primera, cols_busqueda, cols_a_modificar, nom_campos,
                                                          tipo_campos, dic_operaciones)
        rta = Ejecutar_SQL.insert_filas(sSql, 'frm_vista_previa_proceso/func_actualizar_stock_productos_cochado', BasesDeDatos.DB_PRINCIPAL)


        dic_operaciones = {'stock_extrusion': 'stock_extrusion + '}
        nom_campos = ['id_producto', 'stock_extrusion']
        tipo_campos = ['int', 'int']
        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows_total, cols_busqueda, cols_a_modificar,
                                                          nom_campos,
                                                          tipo_campos, dic_operaciones)
        rta = Ejecutar_SQL.insert_filas(sSql, 'frm_vista_previa_proceso/func_actualizar_stock_productos_cochado',
                                        BasesDeDatos.DB_PRINCIPAL)

        return rta

    def func_actualizar_stock_productos_cargueVagonetas(self):

        rows_primera, rows_rotura = self.func_crear_dataframe_producto_cargueVagonetas()

        nom_tabla = 'producto'
        cols_busqueda = [0]
        cols_a_modificar = [1]

        dic_operaciones = {'stock_cargue':'stock_cargue - '}
        nom_campos = ['id_producto', 'stock_cargue']
        tipo_campos = ['int', 'int']
        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows_primera, cols_busqueda, cols_a_modificar, nom_campos,
                                                          tipo_campos, dic_operaciones)
        rta = Ejecutar_SQL.insert_filas(sSql, 'frm_vista_previa_proceso/func_actualizar_stock_productos_cargueVagonetas', BasesDeDatos.DB_PRINCIPAL)


        dic_operaciones = {'stock_cochado': 'stock_cochado + '}
        nom_campos = ['id_producto', 'stock_cochado']
        tipo_campos = ['int', 'int']
        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows_primera, cols_busqueda, cols_a_modificar,
                                                          nom_campos,
                                                          tipo_campos, dic_operaciones)
        rta = Ejecutar_SQL.insert_filas(sSql, 'frm_vista_previa_proceso/func_actualizar_stock_productos_cargueVagonetas',
                                        BasesDeDatos.DB_PRINCIPAL)

        dic_operaciones = {'stock_cochado': 'stock_cochado + '}
        nom_campos = ['id_producto', 'stock_cochado']
        tipo_campos = ['int', 'int']
        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows_rotura, cols_busqueda, cols_a_modificar,
                                                          nom_campos,
                                                          tipo_campos, dic_operaciones)
        rta = Ejecutar_SQL.insert_filas(sSql,
                                        'frm_vista_previa_proceso/func_actualizar_stock_productos_cargueVagonetas',
                                        BasesDeDatos.DB_PRINCIPAL)

        return rta

    def func_actualizar_stock_productos_descargueVagonetas(self):

        rows_primera, rows_segunda,  rows_total = self.func_crear_dataframe_producto_descargueVagonetas()

        print('primera')
        print(rows_primera)
        print('segunda')
        print(rows_segunda)
        print('total')
        print(rows_total)

        nom_tabla = 'producto'
        cols_busqueda = [0]
        cols_a_modificar = [1]

        dic_operaciones = {'stock_primera':'stock_primera - '}
        nom_campos = ['id_producto', 'stock_primera']
        tipo_campos = ['int', 'int']
        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows_primera, cols_busqueda, cols_a_modificar, nom_campos,
                                                          tipo_campos, dic_operaciones)
        rta = Ejecutar_SQL.insert_filas(sSql, 'frm_vista_previa_proceso/func_actualizar_stock_productos_descargueVagonetas', BasesDeDatos.DB_PRINCIPAL)


        dic_operaciones = {'stock_segunda': 'stock_segunda - '}
        nom_campos = ['id_producto', 'stock_segunda']
        tipo_campos = ['int', 'int']
        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows_segunda, cols_busqueda, cols_a_modificar,
                                                          nom_campos,
                                                          tipo_campos, dic_operaciones)
        rta = Ejecutar_SQL.insert_filas(sSql, 'frm_vista_previa_proceso/func_actualizar_stock_productos_descargueVagonetas',
                                        BasesDeDatos.DB_PRINCIPAL)

        dic_operaciones = {'stock_cargue': 'stock_cargue + '}
        nom_campos = ['id_producto', 'stock_cargue']
        tipo_campos = ['int', 'int']
        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows_total, cols_busqueda, cols_a_modificar,
                                                          nom_campos,
                                                          tipo_campos, dic_operaciones)
        rta = Ejecutar_SQL.insert_filas(sSql,
                                        'frm_vista_previa_proceso/func_actualizar_stock_productos_descargueVagonetas',
                                        BasesDeDatos.DB_PRINCIPAL)

        return rta

    def func_crear_dataframe_producto_extrusion(self):
        cant_filas = self.grid_productos.GetNumberRows()
        datos = []
        fila = []
        list_columnas = [0, 6]
        nom_columnas = ['id', 'cant']

        for i in range(cant_filas):
            for j in list_columnas:  ## numero de columna
                fila.append(int(self.grid_productos.GetCellValue(i, j)))
            datos.append(fila)
            fila = []

        df = pd.DataFrame(datos,
                          columns=nom_columnas
                          )
        df= df.groupby(['id']).sum()
        #df = df.sort_values(['producto', 'calidad'])

        rows = df.to_records().tolist()
        return rows


    def func_crear_dataframe_producto_cochado(self):
        cant_filas = self.grid_productos.GetNumberRows()

        datos_primera = []
        datos_total = []

        for i in range(cant_filas):
            id = int(self.grid_productos.GetCellValue(i, 0))
            de_primera = int(self.grid_productos.GetCellValue(i, 6))
            rotos = int(self.grid_productos.GetCellValue(i, 7))
            total = de_primera + rotos

            datos_primera.append([id, de_primera])
            datos_total.append([id, total])

        df_primera = pd.DataFrame(datos_primera,
                          columns=['id', 'cant']
                          )
        df_primera= df_primera.groupby(['id']).sum()
        rows_primera = df_primera.to_records().tolist()

        df_total = pd.DataFrame(datos_total,
                                  columns=['id', 'cant']
                                  )
        df_total = df_total.groupby(['id']).sum()
        rows_total = df_total.to_records().tolist()

        return rows_primera, rows_total

    def func_crear_dataframe_producto_descargueVagonetas(self):
        cant_filas = self.grid_productos.GetNumberRows()

        datos_primera = []
        datos_segunda = []
        datos_total = []

        for i in range(cant_filas):
            id = int(self.grid_productos.GetCellValue(i, 0))
            de_primera = int(self.grid_productos.GetCellValue(i, 3))
            de_segunda = int(self.grid_productos.GetCellValue(i, 4))
            rotura = int(self.grid_productos.GetCellValue(i, 5))
            total = de_primera + de_segunda + rotura

            datos_primera.append([id, de_primera])
            datos_segunda.append([id, de_segunda])
            datos_total.append([id, total])

        df_primera = pd.DataFrame(datos_primera,
                          columns=['id', 'cant']
                          )
        df_primera= df_primera.groupby(['id']).sum()
        rows_primera = df_primera.to_records().tolist()

        df_segunda = pd.DataFrame(datos_segunda,
                                  columns=['id', 'cant']
                                  )
        df_segunda = df_segunda.groupby(['id']).sum()
        rows_segunda = df_segunda.to_records().tolist()

        df_total = pd.DataFrame(datos_total,
                                  columns=['id', 'cant']
                                  )
        df_total = df_total.groupby(['id']).sum()
        rows_total = df_total.to_records().tolist()

        return rows_primera, rows_segunda, rows_total


    def func_crear_dataframe_producto_cargueVagonetas(self):
        cant_filas_productos = self.grid_productos.GetNumberRows()
        cant_filas_rotura = self.grid_rotura.GetNumberRows()
        datos_primera = []
        datos_rotura = []
        fila = []

        for i in range(cant_filas_productos):
            for j in [0, 3]:  ## numero de columna
                fila.append(int(self.grid_productos.GetCellValue(i, j)))
            datos_primera.append(fila)
            fila = []

        df_primera = pd.DataFrame(datos_primera,
                          columns=['id', 'cant']
                          )
        df_primera= df_primera.groupby(['id']).sum()

        #print('df_primera:', df_primera)

        rows_primera = df_primera.to_records().tolist()

        ## _________________________________________________
        fila = []
        for i in range(cant_filas_rotura):
            for j in [0, 2]:  ## numero de columna
                fila.append(int(self.grid_rotura.GetCellValue(i, j)))
            datos_rotura.append(fila)
            fila = []

        df_rotura = pd.DataFrame(datos_rotura,
                          columns=['id', 'cant']
                          )
        df_rotura= df_rotura.groupby(['id']).sum()

        #print('df_rotura:',  df_rotura)

        rows_rotura = df_rotura.to_records().tolist()

        return rows_primera, rows_rotura


    def func_inicializarValores(self):
        self.grid_rotura.AutoSizeColumns()
        self.grid_notas.AutoSizeColumns()
        self.grid_productos.AutoSizeColumns()
        self.grid_empleados.AutoSizeColumns()
        self.grid_novedades.AutoSizeColumns()
        self.grid_recesos.AutoSizeColumns()

        self.lbl_estado.SetLabel(self.estado)
        if self.estado != 'True':
            self.btn_anular.Hide()
            self.lbl_estado.SetLabel('ANULADO')
        else:
            self.lbl_estado.SetLabel('ACTIVO')

        if self.tipoProceso not in ('CARGUE DE VAGONETAS'):
            self.grid_rotura.Hide()

        if self.uuid == -1:
            el_uuid = self.func_buscar_id_ultimoProceso()
            self.func_cargar_Proceso(el_uuid)
        else:
            self.func_cargarCabeceraProceso(self.uuid)
            self.func_cargar_Proceso(self.uuid)


    def func_buscar_id_ultimoProceso(self):
        cad_sql = """
                    SELECT turno, total_coches, total_unidades, fecha_inicio, fecha_fin, uuid
                    FROM cabecera_proceso_ecd 
                    WHERE area_produccion = '{0}' and id_cabecera in
                        (     
                            SELECT MAX(id_cabecera) 
                                    FROM cabecera_proceso_ecd 
                                    WHERE area_produccion = '{0}' and activo ='true'
                        )
                """.format(self.tipoProceso)

        row = Ejecutar_SQL.select_un_registro(cad_sql, 'func_buscar_id_ultimoProceso', BasesDeDatos.DB_PRINCIPAL)
        if row != None:

            self.lbl_turno.SetLabel(row['turno'])
            self.lbl_total_coches.SetLabel(str(row['total_coches']))
            self.lbl_total_unides.SetLabel(str(row['total_unidades']))
            self.lbl_fecha_inicio.SetLabel(str(row['fecha_inicio']))
            self.lbl_fecha_fin.SetLabel(str(row['fecha_fin']))
            uuid = str(row['uuid'])
            return uuid
        else:
            wx.MessageBox(u'No hay datos para mostrar', u'Atención', wx.OK | wx.ICON_INFORMATION)
            self.Destroy()


    def func_cargarCabeceraProceso(self, uuid):
        cad_sql = """
                            SELECT turno, total_coches, total_unidades, fecha_inicio, fecha_fin, uuid
                            FROM cabecera_proceso_ecd 
                            WHERE uuid = '{0}' 
                        """.format(uuid)

        row = Ejecutar_SQL.select_un_registro(cad_sql, 'func_cargarCabeceraProceso', BasesDeDatos.DB_PRINCIPAL)

        self.lbl_turno.SetLabel(row['turno'])
        self.lbl_total_coches.SetLabel(str(row['total_coches']))
        self.lbl_total_unides.SetLabel(str(row['total_unidades']))
        self.lbl_fecha_inicio.SetLabel(str(row['fecha_inicio']))
        self.lbl_fecha_fin.SetLabel(str(row['fecha_fin']))


    def func_cargar_Proceso(self, uuid):

        if self.tipoProceso == 'EXTRUSION':
            cad_sql = """
                        SELECT  id_producto, producto, coche, cant_coches, unidades_producto, unid_parrilla_vacia, total, contador
                        FROM detalle_extrusion
                        WHERE uuid = '{0}'
            """.format(uuid)




            rows_productos = Ejecutar_SQL.select_varios_registros(cad_sql, '', 100, BasesDeDatos.DB_PRINCIPAL)

            ManipularGrillas.setCantidadColumnasGrilla(self.grid_productos, 8)
            ManipularGrillas.llenarGrilla(self.grid_productos, rows_productos)
            list_cabeceras = ['id', 'Producto', 'Coche/Est', 'cant Coches/Est', 'U x Coche/Est', 'U Parrillas Vacias', 'Total', 'Contador']
            ManipularGrillas.setCabecerasGrilla(self.grid_productos, list_cabeceras)

        if self.tipoProceso == 'COCHADO':
            cad_sql = """
                                    SELECT  id_producto, producto, secadero, cant_coches, unid_x_coche, unid_parrilla_vacia, total, rotura
                                    FROM detalle_cocheros
                                    WHERE uuid = '{0}'
                        """.format(uuid)

            rows_productos = Ejecutar_SQL.select_varios_registros(cad_sql, '', 100, BasesDeDatos.DB_PRINCIPAL)

            ManipularGrillas.setCantidadColumnasGrilla(self.grid_productos, 8)
            ManipularGrillas.llenarGrilla(self.grid_productos, rows_productos)
            list_cabeceras = ['id', 'Producto', 'Secadero', 'Cant Coches', 'Unid x Coche', 'U Parrillas Vacias',
                              'Total', 'Rotura']
            ManipularGrillas.setCabecerasGrilla(self.grid_productos, list_cabeceras)

        if self.tipoProceso == 'CARGUE DE VAGONETAS':
            cad_sql = """
                        SELECT  id_producto, producto, vagoneta, unidades_producto
                        FROM detalle_cargue_vagonetas
                        WHERE uuid = '{0}'
                                    """.format(uuid)

            rows_productos = Ejecutar_SQL.select_varios_registros(cad_sql, '', 200, BasesDeDatos.DB_PRINCIPAL)

            ManipularGrillas.setCantidadColumnasGrilla(self.grid_productos, 4)
            ManipularGrillas.llenarGrilla(self.grid_productos, rows_productos)
            list_cabeceras = ['id', 'Producto', 'Vagoneta', 'Unidades Producto']
            ManipularGrillas.setCabecerasGrilla(self.grid_productos, list_cabeceras)

            cad_sql2 = """
                        SELECT  id_producto, producto, cant_rotos
                        FROM rotura_cargue_vagonetas
                        WHERE uuid = '{0}'
                                                """.format(uuid)

            rows_productos_rotura = Ejecutar_SQL.select_varios_registros(cad_sql2, '', 200, BasesDeDatos.DB_PRINCIPAL)
            ManipularGrillas.llenarGrilla(self.grid_rotura, rows_productos_rotura)

        if self.tipoProceso == 'DESCARGUE DE VAGONETAS':
            cad_sql = """
                        SELECT  id_producto, producto, vagoneta, de_primera, de_segunda, rotos, empleado
                        FROM detalle_descargue_vagonetas
                        WHERE uuid = '{0}'
                                    """.format(uuid)

            rows_productos = Ejecutar_SQL.select_varios_registros(cad_sql, '', 100, BasesDeDatos.DB_PRINCIPAL)

            ManipularGrillas.setCantidadColumnasGrilla(self.grid_productos, 7)
            ManipularGrillas.llenarGrilla(self.grid_productos, rows_productos)
            list_cabeceras = ['id', 'Producto', 'Vagoneta', 'Primera', 'Segunda', 'Rotura', 'Empleado']
            ManipularGrillas.setCabecerasGrilla(self.grid_productos, list_cabeceras)

        ##LLENAMOS LA GRILLA DE EMPLEADOS
        cad_sql = """
                    SELECT e.id_empleado, e.nom, concat(e.ape1, ' ', e.ape2)
                    FROM empleado as e, empleados_por_proceso as epp
                    WHERE epp.uuid = '{0}' and e.id_empleado=epp.id_empleado
        """.format(uuid)

        rows_empleados = Ejecutar_SQL.select_varios_registros(cad_sql, '', 100, BasesDeDatos.DB_PRINCIPAL)
        ManipularGrillas.llenarGrilla(self.grid_empleados, rows_empleados)

        ## LLENAMOS LOS RECESOS PROGRAMADOS
        cad_sql = """
                            SELECT id_receso, receso, minutos_descanso
                            FROM receso_por_proceso
                            WHERE uuid = '{0}'
                """.format(uuid)

        rows_recesos = Ejecutar_SQL.select_varios_registros(cad_sql, '', 100, BasesDeDatos.DB_PRINCIPAL)
        ManipularGrillas.llenarGrilla(self.grid_recesos, rows_recesos)

        ## LLENAMOS LAS NOVEDADES
        cad_sql = """
                                            SELECT id, fecha, hora, parada_minutos, novedad
                                            FROM novedades_por_proceso
                                            WHERE uuid = '{0}'
                                """.format(uuid)

        rows_noverdades = Ejecutar_SQL.select_varios_registros(cad_sql, '', 100, BasesDeDatos.DB_PRINCIPAL)
        ManipularGrillas.llenarGrilla(self.grid_novedades, rows_noverdades)

        ## LLENAMOS LAS NOTAS
        cad_sql = """
                                    SELECT id, fecha, relevancia, contexto, nota, contranota
                                    FROM notas_por_proceso
                                    WHERE uuid = '{0}'
                        """.format(uuid)

        rows_notas = Ejecutar_SQL.select_varios_registros(cad_sql, '', 100, BasesDeDatos.DB_PRINCIPAL)
        ManipularGrillas.llenarGrilla(self.grid_notas, rows_notas)



