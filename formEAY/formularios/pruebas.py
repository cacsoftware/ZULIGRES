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
from uuid import uuid4
import pandas as pd
import os

from pyeay.validator import validador_solo_digitos
from pyeay.dbcac.conexiondb import Ejecutar_SQL, GenerarSql
from pyeay.formato import FormatearNumeros
from pyeay.rows import ManipularRows
from pyeay.grillas import ManipularGrillas

from formEAY.constantesCAC.constantesCAC import BasesDeDatos
from formEAY.dbaseCAC.dbVarios import DbGetVarios

from formEAY.constantesCAC.imgCAC import Img_grillas, Img_produccion
from formEAY.constantesCAC.coloresCAC import ColorsFondoCellGrilla
from formEAY.constantesCAC.constantesCAC import AreasProduccion

COLOR_RESALTE1 = ColorsFondoCellGrilla.RESALTE_2
COLOR_RESALTE2 = ColorsFondoCellGrilla.RESALTE_5

###########################################################################
## Class Extrusion
###########################################################################

class Extrusion(wx.Frame):

	def __init__(self, parent, usuario='usuario1', dir_mac='la dir mac del pc'):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PRUEBAS", pos=wx.DefaultPosition,
						  size=wx.Size(1140, 680), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.Size(1040, 680), wx.DefaultSize)
		self.SetBackgroundColour(wx.Colour(240, 240, 240))

		self.AREA_PRODUCCION = AreasProduccion.EXTRUSION
		self.uuid_eay = uuid4()
		self.usuario = usuario
		self.dir_mac = dir_mac

		icono_grillas = Img_grillas()
		img_produccion = Img_produccion()


		bSizer_extrusion = wx.BoxSizer(wx.VERTICAL)

		bSizer_panel_principal = wx.BoxSizer(wx.VERTICAL)

		bSizer_panel_cabecera = wx.BoxSizer(wx.HORIZONTAL)

		self.panel_cabecera = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.panel_cabecera.SetBackgroundColour(wx.Colour(255, 255, 255))

		bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer7 = wx.BoxSizer(wx.VERTICAL)

		self.bitmap_logo_proceso = wx.StaticBitmap(self.panel_cabecera, wx.ID_ANY,
												   wx.Bitmap(img_produccion.EXTRUSION,
															 wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer7.Add(self.bitmap_logo_proceso, 0, wx.ALL, 5)

		bSizer9.Add(bSizer7, 0, wx.EXPAND, 5)

		bSizer6 = wx.BoxSizer(wx.VERTICAL)

		bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl_etq_turno = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Turno:", wx.DefaultPosition,
										   wx.DefaultSize, 0)
		self.lbl_etq_turno.Wrap(-1)
		bSizer14.Add(self.lbl_etq_turno, 0, wx.ALL, 5)

		comboBox_turnoChoices = []
		self.comboBox_turno = wx.ComboBox(self.panel_cabecera, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
										  wx.Size(190, -1), comboBox_turnoChoices, wx.CB_READONLY | wx.CB_SORT)
		bSizer14.Add(self.comboBox_turno, 1, wx.ALL, 5)

		self.lbl_etq_total_coches = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Total coches:", wx.DefaultPosition,
												  wx.DefaultSize, 0)
		self.lbl_etq_total_coches.Wrap(-1)
		bSizer14.Add(self.lbl_etq_total_coches, 0, wx.ALL, 5)

		self.txt_total_coches = wx.TextCtrl(self.panel_cabecera, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
											wx.Size(55, -1), validator=validador_solo_digitos())
		bSizer14.Add(self.txt_total_coches, 0, wx.ALL, 5)

		self.lbl_etq_total_unidades = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Total Unidades:",
													wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl_etq_total_unidades.Wrap(-1)
		bSizer14.Add(self.lbl_etq_total_unidades, 0, wx.ALL, 5)

		self.txt_total_unidades = wx.TextCtrl(self.panel_cabecera, wx.ID_ANY, u"0",
											  wx.DefaultPosition, wx.Size(65, -1), validator=validador_solo_digitos())

		bSizer14.Add(self.txt_total_unidades, 0, wx.ALL, 5)

		bSizer6.Add(bSizer14, 1, wx.EXPAND, 5)

		bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer81 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl_etq_fecha_inicio = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Inicio:", wx.DefaultPosition,
												  wx.Size(70, -1), wx.ALIGN_RIGHT)
		self.lbl_etq_fecha_inicio.Wrap(-1)
		bSizer81.Add(self.lbl_etq_fecha_inicio, 0, wx.ALL, 5)

		self.datePicker_fecha_inicio_extrusion = wx.adv.DatePickerCtrl(self.panel_cabecera, wx.ID_ANY,
																	   wx.DefaultDateTime,
																	   wx.DefaultPosition, wx.DefaultSize,
																	   style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
		bSizer81.Add(self.datePicker_fecha_inicio_extrusion, 0, wx.ALL, 5)

		self.timePicker_hora_inicio_extrusion = wx.adv.TimePickerCtrl(self.panel_cabecera, id=wx.ID_ANY,
																	  dt=wx.DefaultDateTime,
																	  pos=wx.DefaultPosition, size=wx.Size(110, -1),
																	  style=wx.FNTP_DEFAULT_STYLE,
																	  validator=wx.DefaultValidator)

		bSizer81.Add(self.timePicker_hora_inicio_extrusion, 0, wx.ALL, 5)

		bSizer13.Add(bSizer81, 1, wx.EXPAND, 5)

		bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

		###__________________________________________

		self.lbl_etq_fecha_fin = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Fin:", wx.DefaultPosition,
											   wx.DefaultSize, wx.ALIGN_RIGHT)
		self.lbl_etq_fecha_fin.Wrap(-1)
		bSizer8.Add(self.lbl_etq_fecha_fin, 1, wx.ALIGN_LEFT | wx.ALL, 5)

		self.datePicker_fecha_fin = wx.adv.DatePickerCtrl(self.panel_cabecera, wx.ID_ANY, wx.DefaultDateTime,
														  wx.DefaultPosition, wx.DefaultSize,
														  style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
		bSizer8.Add(self.datePicker_fecha_fin, 0, wx.ALL, 5)

		self.timePicker_hora_fin_extrusion = wx.adv.TimePickerCtrl(self.panel_cabecera, id=wx.ID_ANY,
																   dt=wx.DefaultDateTime,
																   pos=wx.DefaultPosition, size=wx.Size(110, -1),
																   style=wx.FNTP_DEFAULT_STYLE,
																   validator=wx.DefaultValidator)

		bSizer8.Add(self.timePicker_hora_fin_extrusion, 0, wx.ALL, 5)

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

		bSizer141 = wx.BoxSizer(wx.HORIZONTAL)
		###__________________________________________

		self.lbl_etq_producto = wx.StaticText(self.panel1_extrusion, wx.ID_ANY, u"Producto:", wx.DefaultPosition,
											  wx.DefaultSize, 0)
		self.lbl_etq_producto.Wrap(-1)
		bSizer141.Add(self.lbl_etq_producto, 0, wx.ALL, 5)

		comboBox_productoChoices = []
		self.comboBox_producto = wx.ComboBox(self.panel1_extrusion, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
											 wx.DefaultSize, comboBox_productoChoices, wx.CB_READONLY)
		bSizer141.Add(self.comboBox_producto, 2, wx.ALL, 5)

		self.lbl_etq_coche = wx.StaticText(self.panel1_extrusion, wx.ID_ANY, u"Coche/Estiba:", wx.DefaultPosition,
										   wx.DefaultSize, 0)
		self.lbl_etq_coche.Wrap(-1)
		bSizer141.Add(self.lbl_etq_coche, 0, wx.ALL, 5)

		comboBox_cocheChoices = []
		self.comboBox_coche = wx.ComboBox(self.panel1_extrusion, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
										  wx.Size(110, -1), comboBox_cocheChoices, wx.CB_READONLY)
		bSizer141.Add(self.comboBox_coche, 0, wx.ALL, 5)

		# _________________________________________________________________________________________________________

		self.lbl_etq_cant_coches = wx.StaticText(self.panel1_extrusion, wx.ID_ANY, u"Cant Coches:", wx.DefaultPosition,
												 wx.DefaultSize, 0)
		self.lbl_etq_cant_coches.Wrap(-1)
		bSizer141.Add(self.lbl_etq_cant_coches, 0, wx.ALL, 5)

		self.txt_cant_coches = wx.TextCtrl(self.panel1_extrusion, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
										   wx.Size(40, -1), validator=validador_solo_digitos())
		bSizer141.Add(self.txt_cant_coches, 0, wx.ALL, 5)

		self.lbl_etq_x_coche = wx.StaticText(self.panel1_extrusion, wx.ID_ANY, u"Unid x Coche:", wx.DefaultPosition,
											 wx.DefaultSize, 0)
		self.lbl_etq_x_coche.Wrap(-1)
		bSizer141.Add(self.lbl_etq_x_coche, 0, wx.ALL, 5)

		self.txt_unidades_x_coche = wx.TextCtrl(self.panel1_extrusion, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
												wx.Size(40, -1), validator=validador_solo_digitos())
		bSizer141.Add(self.txt_unidades_x_coche, 0, wx.ALL, 5)

		self.lbl_etq_u_x_parrilla_vacia = wx.StaticText(self.panel1_extrusion, wx.ID_ANY, u"U x Parrilla Vacia:",
														wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl_etq_u_x_parrilla_vacia.Wrap(-1)
		bSizer141.Add(self.lbl_etq_u_x_parrilla_vacia, 0, wx.ALL, 5)

		self.txt_unidades_x_parrillaVacia = wx.TextCtrl(self.panel1_extrusion, wx.ID_ANY, wx.EmptyString,
														wx.DefaultPosition, wx.Size(40, -1),
														validator=validador_solo_digitos())
		bSizer141.Add(self.txt_unidades_x_parrillaVacia, 0, wx.ALL, 5)

		self.lbl_contador = wx.StaticText(self.panel1_extrusion, wx.ID_ANY, u"Contador:", wx.DefaultPosition,
										  wx.DefaultSize, 0)
		self.lbl_contador.Wrap(-1)
		bSizer141.Add(self.lbl_contador, 0, wx.ALL, 5)

		self.txt_contador = wx.TextCtrl(self.panel1_extrusion, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
										wx.Size(40, -1), validator=validador_solo_digitos())
		bSizer141.Add(self.txt_contador, 0, wx.ALL, 5)

		# _________________________________________________________________________________________________________

		self.btn_a_lista_extrusion = wx.Button(self.panel1_extrusion, wx.ID_ANY, u"--> Lista", wx.DefaultPosition,
											   wx.DefaultSize, 0)
		bSizer141.Add(self.btn_a_lista_extrusion, 0, wx.ALL, 5)

		bSizer_panel_extrusion.Add(bSizer141, 0, wx.EXPAND, 5)

		bSizer46 = wx.BoxSizer(wx.VERTICAL)

		self.m_staticline2 = wx.StaticLine(self.panel1_extrusion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
										   wx.LI_HORIZONTAL)
		bSizer46.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

		bSizer_panel_extrusion.Add(bSizer46, 0, wx.EXPAND, 5)

		bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

		self.grid_extrusion = wx.grid.Grid(self.panel1_extrusion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

		# Grid
		self.grid_extrusion.CreateGrid(5, 9)
		self.grid_extrusion.EnableEditing(True)
		self.grid_extrusion.EnableGridLines(True)
		self.grid_extrusion.EnableDragGridSize(False)
		self.grid_extrusion.SetMargins(0, 0)

		# Columns
		self.grid_extrusion.EnableDragColMove(False)
		self.grid_extrusion.EnableDragColSize(True)
		self.grid_extrusion.SetColLabelSize(30)
		self.grid_extrusion.SetColLabelValue(0, u"id")
		self.grid_extrusion.SetColLabelValue(1, u"Producto")
		self.grid_extrusion.SetColLabelValue(2, u"Coche/Vag")
		self.grid_extrusion.SetColLabelValue(3, u"Cant Coches/Vag")
		self.grid_extrusion.SetColLabelValue(4, u"U x Coche/Vag")
		self.grid_extrusion.SetColLabelValue(5, u"U Parrillas Vacias")
		self.grid_extrusion.SetColLabelValue(6, u"Total")
		self.grid_extrusion.SetColLabelValue(7, u"Contador")
		self.grid_extrusion.SetColLabelValue(8, u"Sel")
		self.grid_extrusion.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

		# Rows
		self.grid_extrusion.EnableDragRowSize(True)
		self.grid_extrusion.SetRowLabelSize(40)
		self.grid_extrusion.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

		# Label Appearance

		# Cell Defaults
		self.grid_extrusion.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
		self.grid_extrusion.AutoSizeColumns()
		bSizer16.Add(self.grid_extrusion, 1, wx.ALL | wx.EXPAND, 5)

		bSizer41 = wx.BoxSizer(wx.VERTICAL)

		self.bpButton_eliminar_item_seleccionado_grid_extrusion = wx.BitmapButton(self.panel1_extrusion, wx.ID_ANY,
																				  wx.Bitmap(
																					  icono_grillas.ELIMINAR_ITEM_SELECIONADO,
																					  wx.BITMAP_TYPE_ANY),
																				  wx.DefaultPosition, wx.DefaultSize,
																				  wx.BU_AUTODRAW | wx.NO_BORDER)

		self.bpButton_eliminar_item_seleccionado_grid_extrusion.SetBitmapCurrent(
			wx.Bitmap(icono_grillas.ELIMINAR_ITEM_SELECIONADO_SEL, wx.BITMAP_TYPE_ANY))
		bSizer41.Add(self.bpButton_eliminar_item_seleccionado_grid_extrusion, 0, wx.ALL, 5)

		self.bpButton_deseleccionar_todo_grid_extrusion = wx.BitmapButton(self.panel1_extrusion, wx.ID_ANY,
																		  wx.Bitmap(
																			  icono_grillas.DESELECCIONAR_TODO,
																			  wx.BITMAP_TYPE_ANY),
																		  wx.DefaultPosition, wx.DefaultSize,
																		  wx.BU_AUTODRAW | wx.NO_BORDER)

		self.bpButton_deseleccionar_todo_grid_extrusion.SetBitmapCurrent(
			wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
		bSizer41.Add(self.bpButton_deseleccionar_todo_grid_extrusion, 0, wx.ALL, 5)

		# self.m_staticline1 = wx.StaticLine(self.panel1_extrusion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
		#                                    wx.LI_HORIZONTAL)
		# bSizer41.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

		self.bpButton_limpiar_grid_extrusion = wx.BitmapButton(self.panel1_extrusion, wx.ID_ANY, wx.Bitmap(
			icono_grillas.LIMPIAR_GRILLA, wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
															   wx.BU_AUTODRAW | wx.NO_BORDER)

		self.bpButton_limpiar_grid_extrusion.SetBitmapCurrent(
			wx.Bitmap(icono_grillas.LIMPIAR_GRILLA_SEL, wx.BITMAP_TYPE_ANY))
		bSizer41.Add(self.bpButton_limpiar_grid_extrusion, 0, wx.ALL, 5)

		bSizer16.Add(bSizer41, 0, wx.EXPAND, 5)

		bSizer_panel_extrusion.Add(bSizer16, 1, wx.EXPAND, 5)

		self.panel1_extrusion.SetSizer(bSizer_panel_extrusion)
		self.panel1_extrusion.Layout()
		bSizer_panel_extrusion.Fit(self.panel1_extrusion)
		bSizer_panel_extrusion1.Add(self.panel1_extrusion, 1, wx.EXPAND | wx.ALL, 5)

		bSizer4.Add(bSizer_panel_extrusion1, 2, wx.EXPAND, 5)

		bSizer_panel_principal.Add(bSizer4, 1, wx.EXPAND, 5)

		bSizer_notebook = wx.BoxSizer(wx.VERTICAL)

		##________________________________________________________________________________________

		self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
									   wx.NB_NOPAGETHEME | wx.FULL_REPAINT_ON_RESIZE)
		self.panel_empleado = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
									   wx.TAB_TRAVERSAL)
		self.panel_empleado.SetBackgroundColour(wx.Colour(255, 255, 255))

		bSizer47 = wx.BoxSizer(wx.VERTICAL)

		self.lbl_etq_selecciona_personal = wx.StaticText(self.panel_empleado, wx.ID_ANY, u"Seleciona el Personal",
														 wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl_etq_selecciona_personal.Wrap(-1)
		bSizer47.Add(self.lbl_etq_selecciona_personal, 0, wx.ALL, 5)

		checkList_personalChoices = [u"A", u"B", u"C", u"D", u"E"]
		self.checkList_personal = wx.CheckListBox(self.panel_empleado, wx.ID_ANY, wx.DefaultPosition, wx.Size(200, 200),
												  checkList_personalChoices, wx.LB_MULTIPLE)
		bSizer47.Add(self.checkList_personal, 1, wx.ALL | wx.EXPAND, 5)

		self.panel_empleado.SetSizer(bSizer47)
		self.panel_empleado.Layout()
		bSizer47.Fit(self.panel_empleado)
		self.m_notebook1.AddPage(self.panel_empleado, u"Empleados", True)
		self.panel_notebook_recesos = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
											   wx.TAB_TRAVERSAL)
		self.panel_notebook_recesos.SetBackgroundColour(wx.Colour(255, 255, 255))

		bSizer_panel_notebook_recesos = wx.BoxSizer(wx.VERTICAL)

		## _____________________________________________________________________________

		bSizer36 = wx.BoxSizer(wx.VERTICAL)

		self.lbl_etq_informacion_recesos = wx.StaticText(self.panel_notebook_recesos, wx.ID_ANY,
														 u"//  La cantidad de minutos que tarda el  receso puede ser editada directamente en la grilla",
														 wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl_etq_informacion_recesos.Wrap(-1)
		self.lbl_etq_informacion_recesos.SetForegroundColour(wx.Colour(0, 128, 0))

		bSizer36.Add(self.lbl_etq_informacion_recesos, 0, wx.ALL, 5)

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

		# Cell Defaults
		self.grid_recesos.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)

		self.grid_recesos.AutoSizeColumns()

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

		bSizer321 = wx.BoxSizer(wx.VERTICAL)

		self.lbl_etq_informacion_novedades = wx.StaticText(self.panel_notebook_novedades1, wx.ID_ANY,
														   u"//  Se registran  acontecimientos ocurridos en el turno de trabajo, por ejemplo:  Averia banda transportadora",
														   wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl_etq_informacion_novedades.Wrap(-1)
		self.lbl_etq_informacion_novedades.SetForegroundColour(wx.Colour(0, 128, 0))

		bSizer321.Add(self.lbl_etq_informacion_novedades, 0, wx.ALL, 5)

		panel_notebook_novedades.Add(bSizer321, 0, wx.EXPAND, 5)

		bSizer331 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl_etq_novedad = wx.StaticText(self.panel_notebook_novedades1, wx.ID_ANY, u"Novedad:", wx.DefaultPosition,
											 wx.Size(75, -1), wx.ALIGN_RIGHT)
		self.lbl_etq_novedad.Wrap(-1)
		bSizer331.Add(self.lbl_etq_novedad, 0, wx.ALL, 5)

		self.txt_novedad = wx.TextCtrl(self.panel_notebook_novedades1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
									   wx.DefaultSize, 0)
		bSizer331.Add(self.txt_novedad, 1, wx.ALL, 5)

		panel_notebook_novedades.Add(bSizer331, 0, wx.EXPAND, 5)

		bSizer3311 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl_etq_fecha_hora_novedades = wx.StaticText(self.panel_notebook_novedades1, wx.ID_ANY, u"Fecha - Hora:",
														  wx.DefaultPosition, wx.Size(75, -1), wx.ALIGN_RIGHT)
		self.lbl_etq_fecha_hora_novedades.Wrap(-1)
		bSizer3311.Add(self.lbl_etq_fecha_hora_novedades, 0, wx.ALL, 5)

		self.datePicker_fecha_novedad = wx.adv.DatePickerCtrl(self.panel_notebook_novedades1, wx.ID_ANY,
															  wx.DefaultDateTime,
															  wx.DefaultPosition, wx.DefaultSize,
															  style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
		bSizer3311.Add(self.datePicker_fecha_novedad, 0, wx.ALL, 5)

		self.timePicker_hora_novedad = wx.adv.TimePickerCtrl(self.panel_notebook_novedades1, id=wx.ID_ANY,
															 dt=wx.DefaultDateTime,
															 pos=wx.DefaultPosition, size=wx.Size(110, -1),
															 style=wx.FNTP_DEFAULT_STYLE,
															 validator=wx.DefaultValidator)
		bSizer3311.Add(self.timePicker_hora_novedad, 0, wx.ALL, 5)

		self.lbl_etq_tiempor_parada_novedad = wx.StaticText(self.panel_notebook_novedades1, wx.ID_ANY,
															u"Tiempo Parada (minutos):", wx.DefaultPosition,
															wx.DefaultSize, 0)
		self.lbl_etq_tiempor_parada_novedad.Wrap(-1)
		bSizer3311.Add(self.lbl_etq_tiempor_parada_novedad, 0, wx.ALL, 5)

		self.txt_tiempo_parada_minutos = wx.TextCtrl(self.panel_notebook_novedades1, wx.ID_ANY, u"0",
													 wx.DefaultPosition, wx.Size(80, -1),
													 validator=validador_solo_digitos())

		bSizer3311.Add(self.txt_tiempo_parada_minutos, 0, wx.ALL, 5)

		self.btn_a_lista_novedades = wx.Button(self.panel_notebook_novedades1, wx.ID_ANY, u"--> Lista",
											   wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer3311.Add(self.btn_a_lista_novedades, 0, wx.ALL, 5)

		panel_notebook_novedades.Add(bSizer3311, 0, wx.EXPAND, 5)

		bSizer342 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer521 = wx.BoxSizer(wx.VERTICAL)

		self.grid_novedades = wx.grid.Grid(self.panel_notebook_novedades1, wx.ID_ANY, wx.DefaultPosition,
										   wx.DefaultSize, 0)

		# Grid
		self.grid_novedades.CreateGrid(5, 5)
		self.grid_novedades.EnableGridLines(True)
		self.grid_novedades.EnableDragGridSize(False)
		self.grid_novedades.SetMargins(0, 0)

		# Columns
		self.grid_novedades.EnableDragColMove(False)
		self.grid_novedades.EnableDragColSize(True)
		self.grid_novedades.SetColLabelSize(30)
		self.grid_novedades.SetColLabelValue(0, u"Fecha")
		self.grid_novedades.SetColLabelValue(1, u"Hora")
		self.grid_novedades.SetColLabelValue(2, u"parada (min)")
		self.grid_novedades.SetColLabelValue(3, u"Novedad")
		self.grid_novedades.SetColLabelValue(4, u"Sel")
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

		# Cell Defaults
		self.grid_novedades.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)

		self.grid_novedades.AutoSizeColumns()

		bSizer521.Add(self.grid_novedades, 1, wx.ALL | wx.EXPAND, 5)

		bSizer342.Add(bSizer521, 1, wx.EXPAND, 5)

		bSizer4121 = wx.BoxSizer(wx.VERTICAL)

		self.bpButton_eliminar_item_seleccionado_grid_novedades = wx.BitmapButton(self.panel_notebook_novedades1,
																				  wx.ID_ANY, wx.Bitmap(
				icono_grillas.ELIMINAR_ITEM_SELECIONADO, wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
																				  wx.DefaultSize,
																				  wx.BU_AUTODRAW | wx.NO_BORDER)

		self.bpButton_eliminar_item_seleccionado_grid_novedades.SetBitmapCurrent(
			wx.Bitmap(icono_grillas.ELIMINAR_ITEM_SELECIONADO_SEL, wx.BITMAP_TYPE_ANY))
		bSizer4121.Add(self.bpButton_eliminar_item_seleccionado_grid_novedades, 0, wx.ALL, 5)

		self.bpButton_deseleccionar_todo_grid_novedades = wx.BitmapButton(self.panel_notebook_novedades1, wx.ID_ANY,
																		  wx.Bitmap(
																			  icono_grillas.DESELECCIONAR_TODO,
																			  wx.BITMAP_TYPE_ANY),
																		  wx.DefaultPosition, wx.DefaultSize,
																		  wx.BU_AUTODRAW | wx.NO_BORDER)

		self.bpButton_deseleccionar_todo_grid_novedades.SetBitmapCurrent(
			wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
		bSizer4121.Add(self.bpButton_deseleccionar_todo_grid_novedades, 0, wx.ALL, 5)

		self.bpButton_limpiar_grid_novedades = wx.BitmapButton(self.panel_notebook_novedades1, wx.ID_ANY,
															   wx.Bitmap(
																   icono_grillas.LIMPIAR_GRILLA,
																   wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
															   wx.DefaultSize,
															   wx.BU_AUTODRAW | wx.NO_BORDER)

		self.bpButton_limpiar_grid_novedades.SetBitmapCurrent(
			wx.Bitmap(icono_grillas.LIMPIAR_GRILLA_SEL, wx.BITMAP_TYPE_ANY))
		bSizer4121.Add(self.bpButton_limpiar_grid_novedades, 0, wx.ALL, 5)

		bSizer342.Add(bSizer4121, 0, wx.EXPAND, 5)

		panel_notebook_novedades.Add(bSizer342, 1, wx.EXPAND, 5)

		self.panel_notebook_novedades1.SetSizer(panel_notebook_novedades)
		self.panel_notebook_novedades1.Layout()
		panel_notebook_novedades.Fit(self.panel_notebook_novedades1)
		self.m_notebook1.AddPage(self.panel_notebook_novedades1, u"Novedades", False)
		self.panel_notebook_notas1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
											  wx.TAB_TRAVERSAL)
		self.panel_notebook_notas1.SetBackgroundColour(wx.Colour(255, 255, 255))
		panel_notebook_notas = wx.BoxSizer(wx.VERTICAL)

		bSizer3211 = wx.BoxSizer(wx.VERTICAL)

		self.lbl_etq_informacion_notas = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY,
													   u"// Puedes registrar comentarios y asignarle una relevancia y un contexto",
													   wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl_etq_informacion_notas.Wrap(-1)
		self.lbl_etq_informacion_notas.SetForegroundColour(wx.Colour(0, 128, 0))

		bSizer3211.Add(self.lbl_etq_informacion_notas, 0, wx.ALL, 5)

		panel_notebook_notas.Add(bSizer3211, 0, wx.EXPAND, 5)

		bSizer3312 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl_etq_nota = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"Nota:", wx.DefaultPosition,
										  wx.Size(75, -1), wx.ALIGN_RIGHT)
		self.lbl_etq_nota.Wrap(-1)
		bSizer3312.Add(self.lbl_etq_nota, 0, wx.ALL, 5)

		self.txt_nota = wx.TextCtrl(self.panel_notebook_notas1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
									wx.DefaultSize, 0)
		bSizer3312.Add(self.txt_nota, 1, wx.ALL, 5)

		panel_notebook_notas.Add(bSizer3312, 0, wx.EXPAND, 5)

		bSizer33111 = wx.BoxSizer(wx.HORIZONTAL)

		# self.lbl_etq_fecha_evento = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"Fecha Evento:",
		#                                           wx.DefaultPosition, wx.Size(75, -1), wx.ALIGN_RIGHT)
		# self.lbl_etq_fecha_evento.Wrap(-1)
		# bSizer33111.Add(self.lbl_etq_fecha_evento, 0, wx.ALL, 5)
		#
		# self.datePicker_fecha_evento_nota = wx.adv.DatePickerCtrl(self.panel_notebook_notas1, wx.ID_ANY, wx.DefaultDateTime,
		#                                                       wx.DefaultPosition, wx.DefaultSize, style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
		# bSizer33111.Add(self.datePicker_fecha_evento_nota, 0, wx.ALL, 5)

		self.lbl_etq_area = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"Area:", wx.DefaultPosition,
										  wx.DefaultSize, 0)
		self.lbl_etq_area.Wrap(-1)
		bSizer33111.Add(self.lbl_etq_area, 0, wx.ALL, 5)

		self.lbl_extrusion = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"EXTRUSION", wx.DefaultPosition,
										   wx.DefaultSize, 0)
		self.lbl_extrusion.Wrap(-1)
		bSizer33111.Add(self.lbl_extrusion, 0, wx.ALL, 5)

		self.lbl_etq_relevancia = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"Relevancia:",
												wx.DefaultPosition, wx.DefaultSize, 0)
		self.lbl_etq_relevancia.Wrap(-1)
		bSizer33111.Add(self.lbl_etq_relevancia, 0, wx.ALL, 5)

		comboBox_relevancia_notaChoices = []
		self.comboBox_relevancia_nota = wx.ComboBox(self.panel_notebook_notas1, wx.ID_ANY, u"Combo!",
													wx.DefaultPosition, wx.DefaultSize, comboBox_relevancia_notaChoices,
													wx.CB_READONLY)
		bSizer33111.Add(self.comboBox_relevancia_nota, 1, wx.ALL, 5)

		self.lbl_etq_contexto = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"Contexto:", wx.DefaultPosition,
											  wx.DefaultSize, 0)
		self.lbl_etq_contexto.Wrap(-1)
		bSizer33111.Add(self.lbl_etq_contexto, 0, wx.ALL, 5)

		comboBox_contextoChoices = []
		self.comboBox_contexto = wx.ComboBox(self.panel_notebook_notas1, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
											 wx.DefaultSize, comboBox_contextoChoices, wx.CB_READONLY)
		bSizer33111.Add(self.comboBox_contexto, 1, wx.ALL, 5)

		self.btn_a_lista_notas = wx.Button(self.panel_notebook_notas1, wx.ID_ANY, u"--> Lista", wx.DefaultPosition,
										   wx.DefaultSize, 0)
		bSizer33111.Add(self.btn_a_lista_notas, 0, wx.ALL, 5)

		panel_notebook_notas.Add(bSizer33111, 0, wx.EXPAND, 5)

		bSizer3421 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer5211 = wx.BoxSizer(wx.VERTICAL)

		self.grid_notas = wx.grid.Grid(self.panel_notebook_notas1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

		# Grid
		self.grid_notas.CreateGrid(5, 5)
		self.grid_notas.EnableEditing(True)
		self.grid_notas.EnableGridLines(True)
		self.grid_notas.EnableDragGridSize(False)
		self.grid_notas.SetMargins(0, 0)

		# Columns
		self.grid_notas.EnableDragColMove(False)
		self.grid_notas.EnableDragColSize(True)
		self.grid_notas.SetColLabelSize(30)
		self.grid_notas.SetColLabelValue(0, u"Fecha")
		self.grid_notas.SetColLabelValue(1, u"Relevancia")
		self.grid_notas.SetColLabelValue(2, u"Contexto")
		self.grid_notas.SetColLabelValue(3, u"Nota")
		self.grid_notas.SetColLabelValue(4, u"Sel")
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

		# Cell Defaults
		self.grid_notas.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)

		self.grid_notas.AutoSizeColumns()

		bSizer5211.Add(self.grid_notas, 1, wx.ALL | wx.EXPAND, 5)

		bSizer3421.Add(bSizer5211, 1, wx.EXPAND, 5)

		bSizer41211 = wx.BoxSizer(wx.VERTICAL)

		self.bpButton_eliminar_item_seleccionado_grid_notas = wx.BitmapButton(self.panel_notebook_notas1, wx.ID_ANY,
																			  wx.Bitmap(
																				  icono_grillas.ELIMINAR_ITEM_SELECIONADO,
																				  wx.BITMAP_TYPE_ANY),
																			  wx.DefaultPosition, wx.DefaultSize,
																			  wx.BU_AUTODRAW | wx.NO_BORDER)

		self.bpButton_eliminar_item_seleccionado_grid_notas.SetBitmapCurrent(
			wx.Bitmap(icono_grillas.ELIMINAR_ITEM_SELECIONADO_SEL, wx.BITMAP_TYPE_ANY))
		bSizer41211.Add(self.bpButton_eliminar_item_seleccionado_grid_notas, 0, wx.ALL, 5)

		self.bpButton_deseleccionar_todo_grid_notas = wx.BitmapButton(self.panel_notebook_notas1, wx.ID_ANY,
																	  wx.Bitmap(
																		  icono_grillas.DESELECCIONAR_TODO,
																		  wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
																	  wx.DefaultSize, wx.BU_AUTODRAW | wx.NO_BORDER)

		self.bpButton_deseleccionar_todo_grid_notas.SetBitmapCurrent(
			wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
		bSizer41211.Add(self.bpButton_deseleccionar_todo_grid_notas, 0, wx.ALL, 5)

		self.bpButton_limpiar_grid_notas = wx.BitmapButton(self.panel_notebook_notas1, wx.ID_ANY,
														   wx.Bitmap(
															   icono_grillas.LIMPIAR_GRILLA,
															   wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
														   wx.DefaultSize, wx.BU_AUTODRAW | wx.NO_BORDER)

		self.bpButton_limpiar_grid_notas.SetBitmapCurrent(
			wx.Bitmap(icono_grillas.LIMPIAR_GRILLA_SEL, wx.BITMAP_TYPE_ANY))
		bSizer41211.Add(self.bpButton_limpiar_grid_notas, 0, wx.ALL, 5)

		bSizer3421.Add(bSizer41211, 0, wx.EXPAND, 5)

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

		bSizer_pie_de_formulario.Add(bSizer56, 0, wx.EXPAND, 5)

		bSizer55 = wx.BoxSizer(wx.HORIZONTAL)

		self.lbl_estado_guardar = wx.StaticText(self, wx.ID_ANY,
												u"1/7  Estamos guardando, el procesos puede tardar unos segundos...",
												wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
		self.lbl_estado_guardar.Wrap(-1)
		self.lbl_estado_guardar.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))
		self.lbl_estado_guardar.SetForegroundColour(wx.Colour(255, 0, 0))

		bSizer55.Add(self.lbl_estado_guardar, 1, wx.ALL, 5)

		self.btn_guardar = wx.Button(self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
		self.btn_guardar.SetBackgroundColour(wx.Colour(128, 255, 128))

		bSizer55.Add(self.btn_guardar, 0, wx.ALL, 5)

		## ----------------------

		bSizer_pie_de_formulario.Add(bSizer55, 1, wx.EXPAND, 5)

		bSizer_panel_principal.Add(bSizer_pie_de_formulario, 0, wx.EXPAND, 5)

		bSizer_extrusion.Add(bSizer_panel_principal, 1, wx.EXPAND, 5)

		self.SetSizer(bSizer_extrusion)
		self.Layout()

		self.Centre(wx.BOTH)

		## OPERACIONES INICIALES EAY
		#self.cargar_valores_de_inicializacion()

		# Connect Events

		self.m_notebook1.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.m_notebook1OnNotebookPageChanged)

		# self.comboBox_boquillas.Bind(wx.EVT_LEFT_DOWN, self.comboBox_boquillasOnLeftDown)
		self.comboBox_turno.Bind(wx.EVT_LEFT_DOWN, self.comboBox_turnoOnLeftDown)
		self.comboBox_producto.Bind(wx.EVT_LEFT_DOWN, self.comboBox_productoOnLeftDown)
		self.comboBox_coche.Bind(wx.EVT_LEFT_DOWN, self.comboBox_cocheOnLeftDown)
		self.comboBox_coche.Bind(wx.EVT_COMBOBOX, self.comboBox_cocheOnCombobox)
		self.comboBox_relevancia_nota.Bind(wx.EVT_LEFT_DOWN, self.comboBox_relevancia_notaOnLeftDown)
		self.comboBox_contexto.Bind(wx.EVT_LEFT_DOWN, self.comboBox_contextoOnLeftDown)
		self.comboBox_turno.Bind(wx.EVT_COMBOBOX, self.comboBox_turnoOnCombobox)

		self.btn_a_lista_extrusion.Bind(wx.EVT_BUTTON, self.btn_a_lista_extrusionOnButtonClick)

		self.bpButton_eliminar_item_seleccionado_grid_extrusion.Bind(wx.EVT_BUTTON,
																	 self.bpButton_eliminar_item_seleccionado_grid_extrusionOnButtonClick)
		# self.bpButton_eliminar_item_seleccionado_grid_boquilla.Bind(wx.EVT_BUTTON, self.bpButton_eliminar_item_seleccionado_grid_boquillaOnButtonClick)
		self.bpButton_eliminar_item_seleccionado_grid_novedades.Bind(wx.EVT_BUTTON,
																	 self.bpButton_eliminar_item_seleccionado_grid_novedadesOnButtonClick)
		self.bpButton_eliminar_item_seleccionado_grid_notas.Bind(wx.EVT_BUTTON,
																 self.bpButton_eliminar_item_seleccionado_grid_notasOnButtonClick)

		self.bpButton_deseleccionar_todo_grid_extrusion.Bind(wx.EVT_BUTTON,
															 self.bpButton_deseleccionar_todo_grid_extrusionOnButtonClick)
		self.bpButton_deseleccionar_todo_grid_novedades.Bind(wx.EVT_BUTTON,
															 self.bpButton_deseleccionar_todo_grid_novedadesOnButtonClick)
		self.bpButton_deseleccionar_todo_grid_notas.Bind(wx.EVT_BUTTON,
														 self.bpButton_deseleccionar_todo_grid_notasOnButtonClick)
		# self.bpButton_deseleccionar_todo_grid_boquilla.Bind(wx.EVT_BUTTON, self.bpButton_deseleccionar_todo_grid_boquillaOnButtonClick)

		self.bpButton_limpiar_grid_notas.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_notasOnButtonClick)
		self.bpButton_limpiar_grid_novedades.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_novedadesOnButtonClick)
		# self.bpButton_limpiar_grid_boquilla.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_boquillaOnButtonClick)
		self.bpButton_limpiar_grid_extrusion.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_extrusionOnButtonClick)

		# self.btn_a_lista_boquilla.Bind(wx.EVT_BUTTON, self.btn_a_lista_boquillaOnButtonClick)
		# self.grid_boquilla.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_boquillaOnGridCellLeftClick)

		self.btn_a_lista_novedades.Bind(wx.EVT_BUTTON, self.btn_a_lista_novedadesOnButtonClick)
		self.grid_novedades.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_novedadesOnGridCellLeftClick)

		self.btn_a_lista_notas.Bind(wx.EVT_BUTTON, self.btn_a_lista_notasOnButtonClick)
		self.grid_notas.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_notasOnGridCellLeftClick)

		self.btn_ver_formato.Bind(wx.EVT_BUTTON, self.btn_ver_formatoOnButtonClick)
		self.btn_ver_procedimiento.Bind(wx.EVT_BUTTON, self.btn_ver_procedimientoOnButtonClick)
		self.btn_guardar.Bind(wx.EVT_BUTTON, self.btn_guardarOnButtonClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class

	def m_notebook1OnNotebookPageChanged(self, event):
		event.Skip()

	def comboBox_cocheOnCombobox(self, event):
		event.Skip()

	def comboBox_cocheOnLeftDown(self, event):
		event.Skip()

	def comboBox_productoOnLeftDown(self, event):
		event.Skip()

	def comboBox_relevancia_notaOnLeftDown(self, event):
		event.Skip()

	def comboBox_contextoOnLeftDown(self, event):
		event.Skip()

	def comboBox_turnoOnLeftDown(self, event):
		event.Skip()

	def comboBox_turnoOnCombobox(self, event):
		event.Skip()

	def btn_a_lista_notasOnButtonClick(self, event):
		event.Skip()

	def btn_a_lista_novedadesOnButtonClick(self, event):
		event.Skip()

	def btn_a_lista_extrusionOnButtonClick(self, event):
		event.Skip()

	def bpButton_eliminar_item_seleccionado_grid_extrusionOnButtonClick(self, event):
		event.Skip()

	def bpButton_eliminar_item_seleccionado_grid_novedadesOnButtonClick(self, event):
		event.Skip()

	def bpButton_eliminar_item_seleccionado_grid_notasOnButtonClick(self, event):
		event.Skip()

	def bpButton_eliminar_item_seleccionado_grid_boquillaOnButtonClick(self, event):
		event.Skip()

	def bpButton_deseleccionar_todo_grid_extrusionOnButtonClick(self, event):
		event.Skip()

	def bpButton_deseleccionar_todo_grid_novedadesOnButtonClick(self, event):
		event.Skip()

	def bpButton_deseleccionar_todo_grid_notasOnButtonClick(self, event):
		event.Skip()

	def bpButton_deseleccionar_todo_grid_boquillaOnButtonClick(self, event):
		event.Skip()

	def bpButton_limpiar_grid_extrusionOnButtonClick(self, event):
		event.Skip()

	def bpButton_limpiar_grid_notasOnButtonClick(self, event):
		event.Skip()

	def bpButton_limpiar_grid_novedadesOnButtonClick(self, event):
		event.Skip()

	def bpButton_limpiar_grid_boquillaOnButtonClick(self, event):
		event.Skip()

	def grid_boquillaOnGridCellLeftClick(self, event):
		event.Skip()

	def grid_novedadesOnGridCellLeftClick(self, event):
		event.Skip()

	def grid_notasOnGridCellLeftClick(self, event):
		event.Skip()

	def btn_ver_formatoOnButtonClick(self, event):
		fecha1 = self.datePicker_fecha_inicio_extrusion.GetValue()

		event.Skip()

	def btn_ver_procedimientoOnButtonClick(self, event):
		self.calcular_tiempos()
		event.Skip()

	def btn_guardarOnButtonClick(self, event):
		from pyeay.fechasHoras import ManejoFechasHoras
		cant_seg = ManejoFechasHoras.cantidadSegundosEntre2Fechas(self.datePicker_fecha_inicio_extrusion, self.datePicker_fecha_fin,
																  self.timePicker_hora_inicio_extrusion, self.timePicker_hora_fin_extrusion)

		print('can seg: ', cant_seg)
		event.Skip()

	##  FUNCIONES EAY
	def calcular_tiempos(self):
		from datetime import datetime, date, time, timedelta

		formato1 = "%d/%m/%Y %H:%M:%S"
		fecha2 = datetime(1995, 11, 5, 0, 0, 0)

		fecha_inicio = self.datePicker_fecha_inicio_extrusion.GetValue()
		hora_inicio = self.timePicker_hora_inicio_extrusion.GetValue()
		anyo_1 = fecha_inicio.year
		mes_1 = fecha_inicio.month
		dia_1 = fecha_inicio.day
		hora_1 = hora_inicio.hour
		minuto_1 = hora_inicio.minute
		segundo_1 = hora_inicio.second
		fecha1 = datetime(anyo_1, mes_1+1, dia_1, hora_1, minuto_1, segundo_1)

		fecha_fin = self.datePicker_fecha_fin.GetValue()
		hora_fin = self.timePicker_hora_fin_extrusion.GetValue()
		anyo_2 = fecha_fin.year
		mes_2 = fecha_fin.month
		dia_2 = fecha_fin.day
		hora_2 = hora_fin.hour
		minuto_2 = hora_fin.minute
		segundo_2 = hora_fin.second
		fecha2 = datetime(anyo_2, mes_2 + 1, dia_2, hora_2, minuto_2, segundo_2)

		print('fecha 1:', fecha1, 'fechas 2:', fecha2)

		diferencia = fecha2 - fecha1

		cant_minutos =   (diferencia.days * 24 * 60) +  (diferencia.seconds / 60)



		print('diferencia en minutos', cant_minutos)

if __name__ == '__main__':
	# window = MainWindow()
	app = wx.App()

	# db_modificacionesBaseDatos.tabla_39__insumo()

	frame_principal = Extrusion(None)
	frame_principal.Center()
	frame_principal.Show()

	app.MainLoop()