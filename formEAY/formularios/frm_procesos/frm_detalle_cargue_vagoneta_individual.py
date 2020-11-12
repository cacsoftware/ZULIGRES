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

from pyeay.grillas import ManipularGrillas


###########################################################################
## Class DetalleCargueVagoneta
###########################################################################

class DetalleCargueVagoneta(wx.Frame):

	def __init__(self, parent, rows):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Detalle Cargue de Vagoneta", pos=wx.DefaultPosition,
						  size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.Size(350, 250), wx.DefaultSize)
		self.SetBackgroundColour(wx.Colour(255, 255, 255))

		self.rows = rows

		bSizer_principal = wx.BoxSizer(wx.HORIZONTAL)

		self.panel_principal = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.panel_principal.SetBackgroundColour(wx.Colour(255, 255, 255))

		bSizer_cabecera = wx.BoxSizer(wx.VERTICAL)

		bSizer_titulo = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl_etq_cargueVagonetas = wx.StaticText(self.panel_principal, wx.ID_ANY, u"Detalle Cargue de Vagoneta",
													 wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl_etq_cargueVagonetas.Wrap(-1)
		self.lbl_etq_cargueVagonetas.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
		self.lbl_etq_cargueVagonetas.SetForegroundColour(wx.Colour(0, 0, 0))

		bSizer_titulo.Add(self.lbl_etq_cargueVagonetas, 0, wx.ALL, 5)

		#___________________________________________________________
		self.lbl_numero_vagoneta = wx.StaticText(self.panel_principal, wx.ID_ANY, u"-",
													wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl_numero_vagoneta.Wrap(-1)
		self.lbl_numero_vagoneta.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
		self.lbl_numero_vagoneta.SetForegroundColour(wx.Colour(255, 0, 0))

		bSizer_titulo.Add(self.lbl_numero_vagoneta, 0, wx.ALL, 5)

		#____________________________________________________________

		bSizer_cabecera.Add(bSizer_titulo, 0, wx.EXPAND, 5)

		bSizer_llenado = wx.BoxSizer(wx.VERTICAL)

		bSizer7 = wx.BoxSizer(wx.VERTICAL)

		bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl_etq_fecha_cargue = wx.StaticText(self.panel_principal, wx.ID_ANY, u"Fecha Cargue:", wx.DefaultPosition,
												  wx.Size(75, -1), wx.ALIGN_RIGHT)
		self.lbl_etq_fecha_cargue.Wrap(-1)
		bSizer8.Add(self.lbl_etq_fecha_cargue, 0, wx.ALL, 5)

		self.lbl_fecha_cargue = wx.StaticText(self.panel_principal, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize,
											  0)
		self.lbl_fecha_cargue.Wrap(-1)
		bSizer8.Add(self.lbl_fecha_cargue, 0, wx.ALL, 5)

		bSizer7.Add(bSizer8, 0, wx.EXPAND, 5)

		bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl_etq_turno = wx.StaticText(self.panel_principal, wx.ID_ANY, u"Turno:", wx.DefaultPosition,
										   wx.Size(75, -1), wx.ALIGN_RIGHT)
		self.lbl_etq_turno.Wrap(-1)
		bSizer9.Add(self.lbl_etq_turno, 0, wx.ALL, 5)

		self.lbl_turno = wx.StaticText(self.panel_principal, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl_turno.Wrap(-1)
		bSizer9.Add(self.lbl_turno, 0, wx.ALL, 5)

		bSizer7.Add(bSizer9, 0, wx.EXPAND, 5)

		bSizer_llenado.Add(bSizer7, 0, wx.EXPAND, 5)

		bSizer_grilla = wx.BoxSizer(wx.VERTICAL)

		self.m_panel_tabla = wx.Panel(self.panel_principal, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
									  wx.TAB_TRAVERSAL)
		self.m_panel_tabla.SetBackgroundColour(wx.Colour(255, 255, 255))

		bSizer_tabla = wx.BoxSizer(wx.VERTICAL)

		self.grid_tabla = wx.grid.Grid(self.m_panel_tabla, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

		# Grid
		self.grid_tabla.CreateGrid(0, 6)
		self.grid_tabla.EnableEditing(True)
		self.grid_tabla.EnableGridLines(True)
		self.grid_tabla.EnableDragGridSize(False)
		self.grid_tabla.SetMargins(0, 0)

		# Columns
		self.grid_tabla.AutoSizeColumns()
		self.grid_tabla.EnableDragColMove(False)
		self.grid_tabla.EnableDragColSize(True)
		self.grid_tabla.SetColLabelSize(30)
		self.grid_tabla.SetColLabelValue(0, u"Vagoneta")
		self.grid_tabla.SetColLabelValue(1, u"id Prod")
		self.grid_tabla.SetColLabelValue(2, u"Producto")
		self.grid_tabla.SetColLabelValue(3, u"Unidades")
		self.grid_tabla.SetColLabelValue(4, u"fecha cargue")
		self.grid_tabla.SetColLabelValue(5, u"Turno")
		self.grid_tabla.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

		# Rows
		self.grid_tabla.EnableDragRowSize(True)
		self.grid_tabla.SetRowLabelSize(1)
		self.grid_tabla.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

		# Label Appearance
		self.grid_tabla.SetLabelBackgroundColour(wx.Colour(240, 240, 240))

		# Cell Defaults
		self.grid_tabla.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
		bSizer_tabla.Add(self.grid_tabla, 1, wx.ALL | wx.EXPAND, 5)

		self.m_panel_tabla.SetSizer(bSizer_tabla)
		self.m_panel_tabla.Layout()
		bSizer_tabla.Fit(self.m_panel_tabla)
		bSizer_grilla.Add(self.m_panel_tabla, 1, wx.EXPAND | wx.ALL, 5)

		bSizer_llenado.Add(bSizer_grilla, 2, wx.EXPAND, 5)

		bSizer_cabecera.Add(bSizer_llenado, 1, wx.EXPAND, 5)

		self.panel_principal.SetSizer(bSizer_cabecera)
		self.panel_principal.Layout()
		bSizer_cabecera.Fit(self.panel_principal)
		bSizer_principal.Add(self.panel_principal, 1, wx.EXPAND | wx.ALL, 5)

		## VALORES INICIALES EAY
		self.func_cargar_grilla()

		self.SetSizer(bSizer_principal)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.grid_tabla.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.grid_tablaOnGridCellChange)
		self.grid_tabla.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.grid_resultado_busquedaOnGridCellLeftDClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def grid_tablaOnGridCellChange(self, event):
		event.Skip()

	def grid_resultado_busquedaOnGridCellLeftDClick(self, event):
		event.Skip()

	## FUNCIONES EAY


	def func_cargar_grilla(self):
		num_vagoneta = self.rows[0][0]
		fecha_cargue = str(self.rows[0][4])
		turno = self.rows[0][5]

		self.lbl_numero_vagoneta.SetLabel(num_vagoneta)
		self.lbl_fecha_cargue.SetLabel(fecha_cargue)
		self.lbl_turno.SetLabel(turno)


		ManipularGrillas.llenarGrilla(self.grid_tabla, self.rows)
		ManipularGrillas.ocultarColumnasGrilla(self.grid_tabla, [0, 4, 5])


		self.grid_tabla.AutoSizeColumns()


