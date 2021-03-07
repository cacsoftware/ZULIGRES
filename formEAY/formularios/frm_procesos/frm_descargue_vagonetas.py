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


COLOR_RESALTE_ROSA = ColorsFondoCellGrilla.RESALTE_ROSA

AREA_PRODUCCION = AreasProduccion.DESCARGUE_VAGONETAS
###########################################################################
## Class CargueVagonetas
###########################################################################

class DescargueVagonetas(wx.Frame):

    def __init__(self, parent, usuario='usuario1', dir_mac = 'la dir mac del pc'):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Registro descargue Vagonetas", pos=wx.DefaultPosition,
                          size=wx.Size(960, 680), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(828, 680), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.dic_productos_id = 0
        self.dic_vagonetas_fechas = {}

        self.AREA_PRODUCCION = AreasProduccion.DESCARGUE_VAGONETAS
        self.uuid_eay = uuid4()
        self.usuario = usuario
        self.dir_mac = dir_mac

        icono_grillas = Img_grillas()
        self.img_produccion = Img_produccion()

        bSizer_cargueVagonetas = wx.BoxSizer(wx.VERTICAL)

        bSizer_panel_principal = wx.BoxSizer(wx.VERTICAL)

        bSizer_panel_cabecera = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_cabecera = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel_cabecera.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.bitmap_logo_proceso = wx.StaticBitmap(self.panel_cabecera, wx.ID_ANY,
                                                   wx.Bitmap(self.img_produccion.DESCARGUE_VAGONETAS,
                                                             wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.bitmap_logo_proceso, 0, wx.ALL, 5)

        bSizer9.Add(bSizer7, 0, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_turno = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Turno:", wx.DefaultPosition,
                                           wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_turno.Wrap(-1)
        bSizer14.Add(self.lbl_etq_turno, 0, wx.ALL, 5)

        comboBox_turnoChoices = []
        self.comboBox_turno = wx.ComboBox(self.panel_cabecera, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                          wx.Size(190, -1), comboBox_turnoChoices, wx.CB_READONLY | wx.CB_SORT)
        bSizer14.Add(self.comboBox_turno, 1, wx.ALL, 5)

        self.lbl_etq_total_vagonetas = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Total vagonetas:",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_total_vagonetas.Wrap(-1)
        bSizer14.Add(self.lbl_etq_total_vagonetas, 0, wx.ALL, 5)

        self.txt_total_vagonetas = wx.TextCtrl(self.panel_cabecera, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.Size(50, -1), validator= validador_solo_digitos())
        self.txt_total_vagonetas.SetMaxLength(6)
        bSizer14.Add(self.txt_total_vagonetas, 0, wx.ALL, 5)

        self.lbl_etq_total_unidades = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Total Unidades:",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_total_unidades.Wrap(-1)
        bSizer14.Add(self.lbl_etq_total_unidades, 0, wx.ALL, 5)

        self.txt_total_unidades = wx.TextCtrl(self.panel_cabecera, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.Size(60, -1), validator= validador_solo_digitos())
        bSizer14.Add(self.txt_total_unidades, 0, wx.ALL, 5)

        bSizer6.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer81 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fecha_inicio = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Inicio:", wx.DefaultPosition,
                                                  wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_fecha_inicio.Wrap(-1)
        bSizer81.Add(self.lbl_etq_fecha_inicio, 0, wx.ALL, 5)

        self.datePicker_fecha_inicio_cargue = wx.adv.DatePickerCtrl(self.panel_cabecera, wx.ID_ANY, wx.DefaultDateTime,
                                                                wx.DefaultPosition, wx.DefaultSize, style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer81.Add(self.datePicker_fecha_inicio_cargue, 0, wx.ALL, 5)

        self.timePicker_hora_inicio_cargue = wx.adv.TimePickerCtrl(self.panel_cabecera, id=wx.ID_ANY, dt=wx.DefaultDateTime,
               pos=wx.DefaultPosition, size=wx.Size(110, -1), style= wx.FNTP_DEFAULT_STYLE,
               validator=wx.DefaultValidator)
        
        bSizer81.Add(self.timePicker_hora_inicio_cargue, 0, wx.ALL, 5)

        bSizer13.Add(bSizer81, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fecha_fin = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Fin:", wx.DefaultPosition,
                                               wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lbl_etq_fecha_fin.Wrap(-1)
        bSizer8.Add(self.lbl_etq_fecha_fin, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        self.datePicker_fecha_fin = wx.adv.DatePickerCtrl(self.panel_cabecera, wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.Size(90, -1), style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer8.Add(self.datePicker_fecha_fin, 0, wx.ALL, 5)

        self.timePicker_hora_fin_cargue = wx.adv.TimePickerCtrl(self.panel_cabecera, id=wx.ID_ANY, dt=wx.DefaultDateTime,
               pos=wx.DefaultPosition, size=wx.Size(110, -1), style= wx.FNTP_DEFAULT_STYLE,
               validator=wx.DefaultValidator)

        bSizer8.Add(self.timePicker_hora_fin_cargue, 0, wx.ALL, 5)

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

        self.panel_empleado = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel_empleado.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer47 = wx.BoxSizer(wx.VERTICAL)

        ########

        self.lbl_etq_selecciona_personal = wx.StaticText(self.panel_empleado, wx.ID_ANY, u"Seleciona el Personal",
                                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_selecciona_personal.Wrap(-1)
        bSizer47.Add(self.lbl_etq_selecciona_personal, 0, wx.ALL, 5)

        checkList_personalChoices = []
        self.checkList_personal = wx.CheckListBox(self.panel_empleado, wx.ID_ANY, wx.DefaultPosition, wx.Size(200, 200),
                                                  checkList_personalChoices, wx.LB_MULTIPLE)
        bSizer47.Add(self.checkList_personal, 1, wx.ALL | wx.EXPAND, 5)

        self.panel_empleado.SetSizer(bSizer47)
        self.panel_empleado.Layout()
        bSizer47.Fit(self.panel_empleado)
        bSizer_panel_empleado.Add(self.panel_empleado, 1, wx.EXPAND | wx.ALL, 5)

        bSizer4.Add(bSizer_panel_empleado, 0, wx.EXPAND, 5)

        bSizer_panel_extrusion1 = wx.BoxSizer(wx.VERTICAL)

        self.panel1_extrusion = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel1_extrusion.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_panel_extrusion = wx.BoxSizer(wx.VERTICAL)

        bSizer141 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_a_lista_cargue_vagonetas = wx.Button(self.panel1_extrusion, wx.ID_ANY, u"--> Llenar Tabla",
                                                      wx.DefaultPosition, wx.DefaultSize, 0 | wx.NO_BORDER)
        self.btn_a_lista_cargue_vagonetas.SetBackgroundColour(wx.Colour(254, 235, 126))

        bSizer141.Add(self.btn_a_lista_cargue_vagonetas, 0, wx.ALL, 5)

        bSizer_panel_extrusion.Add(bSizer141, 0, wx.EXPAND, 5)

        bSizer46 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline2 = wx.StaticLine(self.panel1_extrusion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer46.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_panel_extrusion.Add(bSizer46, 0, wx.EXPAND, 5)

        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

        self.grid_descargue_vagonetas = wx.grid.Grid(self.panel1_extrusion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                  0)

        # Grid
        self.grid_descargue_vagonetas.CreateGrid(0, 2)
        self.grid_descargue_vagonetas.EnableEditing(True)
        self.grid_descargue_vagonetas.EnableGridLines(True)
        self.grid_descargue_vagonetas.EnableDragGridSize(False)
        self.grid_descargue_vagonetas.SetMargins(0, 0)

        # Columns
        self.grid_descargue_vagonetas.AutoSizeColumns()
        self.grid_descargue_vagonetas.EnableDragColMove(False)
        self.grid_descargue_vagonetas.EnableDragColSize(True)
        self.grid_descargue_vagonetas.SetColLabelSize(30)
        self.grid_descargue_vagonetas.SetColLabelValue(0, u"Vagoneta")
        self.grid_descargue_vagonetas.SetColLabelValue(1, u"Calidad")
        self.grid_descargue_vagonetas.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_descargue_vagonetas.EnableDragRowSize(True)
        self.grid_descargue_vagonetas.SetRowLabelSize(1)
        self.grid_descargue_vagonetas.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_descargue_vagonetas.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer16.Add(self.grid_descargue_vagonetas, 1, wx.ALL | wx.EXPAND, 5)

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
        self.panel_notebook_novedades1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                  wx.TAB_TRAVERSAL)
        self.panel_notebook_novedades1.SetBackgroundColour(wx.Colour(255, 255, 255))

        panel_notebook_novedades = wx.BoxSizer(wx.VERTICAL)

        bSizer321 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_informacion_novedades = wx.StaticText(self.panel_notebook_novedades1, wx.ID_ANY,
                                                           u"//  Se registran  eventos ocurrido en el turno de trabajo, por ejemplo:  Averia vagoneta 14",
                                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_informacion_novedades.Wrap(-1)
        self.lbl_etq_informacion_novedades.SetForegroundColour(wx.Colour(0, 128, 0))

        bSizer321.Add(self.lbl_etq_informacion_novedades, 0, wx.ALL, 5)

        panel_notebook_novedades.Add(bSizer321, 0, wx.EXPAND, 5)

        bSizer331 = wx.BoxSizer(wx.HORIZONTAL)

        #########
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

        self.datePicker_fecha_novedad = wx.adv.DatePickerCtrl(self.panel_notebook_novedades1, wx.ID_ANY, wx.DefaultDateTime,
                                                          wx.DefaultPosition, wx.DefaultSize, style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer3311.Add(self.datePicker_fecha_novedad, 0, wx.ALL, 5)

        self.timePicker_hora_novedad = wx.adv.TimePickerCtrl(self.panel_notebook_novedades1, id=wx.ID_ANY, dt=wx.DefaultDateTime,
               pos=wx.DefaultPosition, size=wx.Size(110, -1), style= wx.FNTP_DEFAULT_STYLE,
               validator=wx.DefaultValidator)
        
        bSizer3311.Add(self.timePicker_hora_novedad, 0, wx.ALL, 5)

        self.lbl_etq_tiempor_parada_novedad = wx.StaticText(self.panel_notebook_novedades1, wx.ID_ANY,
                                                            u"Tiempo Parada (minutos):", wx.DefaultPosition,
                                                            wx.DefaultSize, 0)
        self.lbl_etq_tiempor_parada_novedad.Wrap(-1)
        bSizer3311.Add(self.lbl_etq_tiempor_parada_novedad, 0, wx.ALL, 5)

        self.txt_tiempo_parada_minutos = wx.TextCtrl(self.panel_notebook_novedades1, wx.ID_ANY, u"0",
                                                     wx.DefaultPosition, wx.Size(80, -1), validator= validador_solo_digitos())
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
        self.grid_novedades.EnableEditing(True)
        self.grid_novedades.EnableGridLines(True)
        self.grid_novedades.EnableDragGridSize(False)
        self.grid_novedades.SetMargins(0, 0)

        # Columns
        self.grid_novedades.AutoSizeColumns()
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
                                                                              wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                                          wx.DefaultSize, wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_deseleccionar_todo_grid_novedades.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer4121.Add(self.bpButton_deseleccionar_todo_grid_novedades, 0, wx.ALL, 5)

        # self.m_staticline121 = wx.StaticLine(self.panel_notebook_novedades1, wx.ID_ANY, wx.DefaultPosition,
        #                                      wx.DefaultSize, wx.LI_HORIZONTAL)
        # bSizer4121.Add(self.m_staticline121, 0, wx.EXPAND | wx.ALL, 5)

        self.bpButton_limpiar_grid_novedades = wx.BitmapButton(self.panel_notebook_novedades1, wx.ID_ANY, wx.Bitmap(
            icono_grillas.LIMPIAR_GRILLA, wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                                               wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_limpiar_grid_novedades.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.LIMPIAR_GRILLA_SEL, wx.BITMAP_TYPE_ANY))
        bSizer4121.Add(self.bpButton_limpiar_grid_novedades, 0, wx.ALL, 5)

        bSizer342.Add(bSizer4121, 0, wx.EXPAND, 5)

        panel_notebook_novedades.Add(bSizer342, 1, wx.EXPAND, 5)

        self.panel_notebook_novedades1.SetSizer(panel_notebook_novedades)
        self.panel_notebook_novedades1.Layout()
        panel_notebook_novedades.Fit(self.panel_notebook_novedades1)
        self.m_notebook1.AddPage(self.panel_notebook_novedades1, u"Novedades", True)
        self.panel_notebook_recesos = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                               wx.TAB_TRAVERSAL)
        self.panel_notebook_recesos.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_panel_notebook_recesos = wx.BoxSizer(wx.VERTICAL)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_informacion_recesos = wx.StaticText(self.panel_notebook_recesos, wx.ID_ANY,
                                                         u"//  La cantidad de minutos que tarda el  receso, puede ser editada directamente en la grilla",
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

        # Cell Defaults
        self.grid_recesos.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer48.Add(self.grid_recesos, 1, wx.ALL | wx.EXPAND, 5)

        bSizer341.Add(bSizer48, 1, wx.EXPAND, 5)

        bSizer_panel_notebook_recesos.Add(bSizer341, 1, wx.EXPAND, 5)

        self.panel_notebook_recesos.SetSizer(bSizer_panel_notebook_recesos)
        self.panel_notebook_recesos.Layout()
        bSizer_panel_notebook_recesos.Fit(self.panel_notebook_recesos)
        self.m_notebook1.AddPage(self.panel_notebook_recesos, u"Recesos Programados", False)
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

        self.lbl_extrusion = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"DESCARGUE DE VAGONETAS", wx.DefaultPosition,
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
        bSizer33111.Add(self.comboBox_relevancia_nota, 0, wx.ALL, 5)

        self.lbl_etq_contexto = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"Contexto:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_etq_contexto.Wrap(-1)
        bSizer33111.Add(self.lbl_etq_contexto, 0, wx.ALL, 5)

        comboBox_contextoChoices = []
        self.comboBox_contexto = wx.ComboBox(self.panel_notebook_notas1, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                             wx.DefaultSize, comboBox_contextoChoices, wx.CB_READONLY)
        bSizer33111.Add(self.comboBox_contexto, 0, wx.ALL, 5)

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
        self.grid_notas.AutoSizeColumns()
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

        self.bpButton_deseleccionar_todo_grid_notas = wx.BitmapButton(self.panel_notebook_notas1, wx.ID_ANY, wx.Bitmap(
            icono_grillas.DESELECCIONAR_TODO, wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                                      wx.DefaultSize, wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_deseleccionar_todo_grid_notas.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer41211.Add(self.bpButton_deseleccionar_todo_grid_notas, 0, wx.ALL, 5)

        # self.m_staticline1211 = wx.StaticLine(self.panel_notebook_notas1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
        #                                       wx.LI_HORIZONTAL)
        # bSizer41211.Add(self.m_staticline1211, 0, wx.EXPAND | wx.ALL, 5)

        self.bpButton_limpiar_grid_notas = wx.BitmapButton(self.panel_notebook_notas1, wx.ID_ANY,
                                                           wx.Bitmap(icono_grillas.LIMPIAR_GRILLA,
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

        bSizer_panel_principal.Add(bSizer_notebook, 0, wx.EXPAND, 5)

        bSizer_pie_de_formulario = wx.BoxSizer(wx.HORIZONTAL)

        bSizer56 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_ver_formato = wx.Button(self, wx.ID_ANY, u"Ver formato", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer56.Add(self.btn_ver_formato, 0, wx.ALL, 5)

        self.btn_ver_procedimiento = wx.Button(self, wx.ID_ANY, u"Ver Procedimiento", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        bSizer56.Add(self.btn_ver_procedimiento, 0, wx.ALL, 5)

        self.btn_ver_ultimoProceso = wx.Button(self, wx.ID_ANY, u"Ver Ultimo Proceso", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        bSizer56.Add(self.btn_ver_ultimoProceso, 0, wx.ALL, 5)


        bSizer_pie_de_formulario.Add(bSizer56, 0, wx.EXPAND, 5)

        bSizer55 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_estado_guardar = wx.StaticText(self, wx.ID_ANY,
                                                u"1/7  Estamos guardando, el proceso puede tardar unos segundos...",
                                                wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.lbl_estado_guardar.Wrap(-1)
        self.lbl_estado_guardar.SetFont(wx.Font(10, 70, 90, 90, False, wx.EmptyString))
        self.lbl_estado_guardar.SetForegroundColour(wx.Colour(255, 0, 0))

        bSizer55.Add(self.lbl_estado_guardar, 1, wx.ALL, 5)

        self.btn_guardar = wx.Button(self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.btn_guardar.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.btn_guardar.SetForegroundColour(wx.Colour(255, 255, 255))
        self.btn_guardar.SetBackgroundColour(wx.Colour(110, 180, 66))

        bSizer55.Add(self.btn_guardar, 0, wx.ALL, 5)

        bSizer_pie_de_formulario.Add(bSizer55, 1, wx.EXPAND, 5)

        bSizer_panel_principal.Add(bSizer_pie_de_formulario, 0, wx.EXPAND, 5)

        bSizer_cargueVagonetas.Add(bSizer_panel_principal, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer_cargueVagonetas)
        self.Layout()

        self.Centre(wx.BOTH)

        ## OPERACIONES INICIALES EAY
        self.cargar_valores_de_inicializacion()

        # Connect Events
        #self.grid_descargue_vagonetas

        self.btn_ver_ultimoProceso.Bind(wx.EVT_BUTTON, self.btn_ver_ultimoProcesoOnButtonClick)

        self.grid_descargue_vagonetas.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.grid_descargue_vagonetasOnGridCellLeftDClick)

        self.comboBox_turno.Bind(wx.EVT_LEFT_DOWN, self.comboBox_turnoOnLeftDown)
        # self.comboBox_producto.Bind(wx.EVT_LEFT_DOWN, self.comboBox_productoOnLeftDown)
        # self.comboBox_vagoneta.Bind(wx.EVT_LEFT_DOWN, self.comboBox_vagonetaOnLeftDown)
        self.comboBox_relevancia_nota.Bind(wx.EVT_LEFT_DOWN, self.comboBox_relevancia_notaOnLeftDown)
        self.comboBox_contexto.Bind(wx.EVT_LEFT_DOWN, self.comboBox_contextoOnLeftDown)
        self.comboBox_turno.Bind(wx.EVT_COMBOBOX, self.comboBox_turnoOnCombobox)

        self.btn_a_lista_cargue_vagonetas.Bind(wx.EVT_BUTTON, self.btn_a_lista_cargue_vagonetasOnButtonClick)


        # self.bpButton_eliminar_item_seleccionado_grid_descargue_vagonetas.Bind(wx.EVT_BUTTON, self.bpButton_eliminar_item_seleccionado_grid_descargue_vagonetasOnButtonClick)
        self.bpButton_eliminar_item_seleccionado_grid_novedades.Bind(wx.EVT_BUTTON, self.bpButton_eliminar_item_seleccionado_grid_novedadesOnButtonClick)
        self.bpButton_eliminar_item_seleccionado_grid_notas.Bind(wx.EVT_BUTTON, self.bpButton_eliminar_item_seleccionado_grid_notasOnButtonClick)


        # self.bpButton_deseleccionar_todo_grid_descargue_vagonetas.Bind(wx.EVT_BUTTON, self.bpButton_deseleccionar_todo_grid_descargue_vagonetasOnButtonClick)
        self.bpButton_deseleccionar_todo_grid_notas.Bind(wx.EVT_BUTTON, self.bpButton_deseleccionar_todo_grid_notasOnButtonClick)
        self.bpButton_deseleccionar_todo_grid_novedades.Bind(wx.EVT_BUTTON, self.bpButton_deseleccionar_todo_grid_novedadesOnButtonClick)


        # self.bpButton_limpiar_grid_descargue_vagonetas.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_descargue_vagonetasOnButtonClick)
        self.bpButton_limpiar_grid_novedades.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_novedadesOnButtonClick)
        self.bpButton_limpiar_grid_notas.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_notasOnButtonClick)


        self.m_notebook1.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.m_notebook1OnNotebookPageChanged)

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

    def btn_ver_ultimoProcesoOnButtonClick(self, event):
        import formEAY.formularios.frm_procesos.frm_vista_previa_proceso as frm_vista_previa_proceso
        frame_vistaPrevia = frm_vista_previa_proceso.VistaPreviaProceso(self, self.usuario, self.dir_mac,
                                                                        self.img_produccion.DESCARGUE_VAGONETAS,
                                                                        'DESCARGUE DE VAGONETAS')
        frame_vistaPrevia.Center()
        frame_vistaPrevia.Show()
        event.Skip()


    def grid_descargue_vagonetasOnGridCellLeftDClick(self, event):
        fila = event.GetRow()
        columna = event.GetCol()
        if columna == 1:
            vagoneta = self.grid_descargue_vagonetas.GetCellValue(fila, 1)

            try:
                fechaBusqueda = self.dic_vagonetas_fechas[vagoneta]
                cad_sql = """
                                    SELECT det.vagoneta, det.id_producto, det.producto, det.unidades_producto, cab.fecha_inicio,  cab.turno
                                    FROM detalle_cargue_vagonetas as det, cabecera_proceso_ecd as cab
                                    WHERE cab.uuid = det.uuid  and  det.vagoneta = '{0}'  and cab.fecha_inicio = '{1}'      
                        """.format(vagoneta, fechaBusqueda)
                rows = Ejecutar_SQL.select_varios_registros(cad_sql, 'grid_resultado_busquedaOnGridCellLeftDClick', 500,
                                                            BasesDeDatos.DB_PRINCIPAL)

                import \
                    formEAY.formularios.frm_procesos.frm_detalle_cargue_vagoneta_individual as frm_detalle_cargue_vagoneta_individual
                frame_detalle_cargue_vagoneta_individual = frm_detalle_cargue_vagoneta_individual.DetalleCargueVagoneta(
                    self, rows)
                frame_detalle_cargue_vagoneta_individual.Center()
                frame_detalle_cargue_vagoneta_individual.Show()
            except:
                mensaje = u'No temenos información relacionada con la vagoneta ' + vagoneta
                wx.MessageBox(mensaje, u'Atención',
                              wx.OK | wx.ICON_INFORMATION)
        event.Skip()





    def btn_guardarOnButtonClick(self, event):

        from formEAY.dbaseCAC.dbVarios import DbInsertVarios
        from formEAY.dbaseCAC.dbVerificaciones import DbGetVerificaciones
        # from formEAY.utilCAC.Utiles_proposito_general import ManejoFechasHoras
        from pyeay.fechasHoras import ManejoFechasHoras

        fecha_inicio = self.datePicker_fecha_inicio_cargue.GetValue()
        fecha_fin = self.datePicker_fecha_fin.GetValue()

        if fecha_fin < fecha_inicio:
            wx.MessageBox(u'Fechas inconsistentes, fecha fin debe ser mayor o igual a la fecha inicio', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        activo = 'True'

        fecha_inicio = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha_inicio_cargue)
        fecha_fin = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha_fin)
        hora_inicio = ManejoFechasHoras.formatearHoraXSql(self.timePicker_hora_inicio_cargue)
        hora_fin = ManejoFechasHoras.formatearHoraXSql(self.timePicker_hora_fin_cargue)

        el_turno = self.comboBox_turno.GetValue()
        if el_turno == '':
            wx.MessageBox(u'Debes seleccionar un turno', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        dia_semana = ManejoFechasHoras.getDiaSemanaToNumero(self.datePicker_fecha_inicio_cargue)
        str_dias_operacion = self.dic_turnos_todos[el_turno][5]
        # 1111100  lunes a viernes

        dia_permitido = str_dias_operacion[dia_semana - 1]

        if dia_permitido == '0':
            wx.MessageBox(u'Dia no permido, para el turno', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        id_turno = self.dic_turnos_todos[el_turno][0]

        exite_el_turno = DbGetVerificaciones.existeTurno(id_turno, fecha_inicio, True, self.AREA_PRODUCCION)

        if exite_el_turno == True:
            wx.MessageBox(u'No es posible Continuar, este turno ya existe en la Base de Datos', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        cant_empleados = len(self.checkList_personal.GetCheckedStrings())
        if cant_empleados == 0:
            wx.MessageBox(u'Debes seleccionar el personal', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        # total_vagonetas = self.txt_total_vagonetas.GetValue()
        # if total_vagonetas == '' or total_vagonetas == '0':
        #     wx.MessageBox(u'Debes ingresar un número valido de total Vagonetas', u'Atención', wx.OK | wx.ICON_INFORMATION)
        #     return 0

        # total_unidades = self.txt_total_unidades.GetValue()
        # if total_unidades == '' or total_unidades == '0':
        #     wx.MessageBox(u'Debes ingresar un número valido de total unidades', u'Atención',
        #                   wx.OK | wx.ICON_INFORMATION)
        #     return 0

        if self.grid_descargue_vagonetas.GetNumberRows() == 0:
            wx.MessageBox(u'Grilla descargue de vagonetas esta vacia', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0
        else:
            total_vagonetas_grid, total_unidades_grid = self.calcular_totales_grilla_descargue_vagonetas()

            # if total_vagonetas_grid != int(total_vagonetas):
            #     wx.MessageBox(u'Detectada una posible inconsistencia en la cantidad de vagonetas', u'Atención',
            #                   wx.OK | wx.ICON_INFORMATION)
            #     return 0
            # if total_unidades_grid != int(total_unidades):
            #     wx.MessageBox(u'Detectada una posible inconsistencia en la cantidad de unidades', u'Atención',
            #                   wx.OK | wx.ICON_INFORMATION)
            #     return 0

        ############
        fecha_transacccion, hora_transacion = ManejoFechasHoras.getFechaHoraActual()

        self.btn_guardar.Hide()

        cant_segundos = ManejoFechasHoras.cantidadSegundosEntre2Fechas(self.datePicker_fecha_inicio_cargue,
                                                                       self.datePicker_fecha_fin,
                                                                       self.timePicker_hora_inicio_cargue,
                                                                       self.timePicker_hora_fin_cargue)

        minutos_jornada = cant_segundos / 60
        minutos_receso, minutos_novedades = self.func_calcular_tiempos()

        self.lbl_estado_guardar.SetLabel('1/7  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_cabecera = DbInsertVarios.cabeceraProcesoECD(self.uuid_eay, self.usuario, self.dir_mac, fecha_transacccion,
                                                         hora_transacion, id_turno, el_turno,
                                                         total_vagonetas_grid, total_unidades_grid, fecha_inicio, hora_inicio,
                                                         fecha_fin,
                                                         hora_fin, activo, self.AREA_PRODUCCION,
                                                         minutos_jornada, minutos_receso, minutos_novedades)

        self.lbl_estado_guardar.SetLabel('2/7  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_insert_empleados = DbInsertVarios.personal(self)


        self.lbl_estado_guardar.SetLabel('3/7  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_insert_DetalleExtrusion = DbInsertVarios.detalleDescargueVagonetas(self)


        rta_actualizar_stock_productos = self.func_actualizar_stock_productos()



        self.lbl_estado_guardar.SetLabel('4/7  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_insert_recesosProgramados = DbInsertVarios.recesosProgramados(self)
        self.lbl_estado_guardar.SetLabel('5/7  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_insert_novedades = DbInsertVarios.novedades(self)
        self.lbl_estado_guardar.SetLabel('6/7  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_insert_notas = DbInsertVarios.notas(self)


        self.lbl_estado_guardar.SetLabel('')

        wx.MessageBox(u'El formulario Descargue de Vagonetas fue guardado  correctamente', u'Atención', wx.OK | wx.ICON_INFORMATION)

        ## creamos un nuevo uuid
        self.uuid_eay = uuid4()

        self.Destroy()


        event.Skip()




    def m_notebook1OnNotebookPageChanged(self, event):
        if self.m_notebook1.GetSelection() == 1:  ## 1 es la pagina de recesos programados
            if self.grid_recesos.GetNumberRows() == 0:
                self.cargar_grid_receso_programado()
                self.panel_notebook_recesos.Layout()
        event.Skip()


    def comboBox_turnoOnLeftDown(self, event):
        if self.comboBox_turno.GetItems() == []:
            self.cargar_combo_turnos()
        event.Skip()


    def comboBox_relevancia_notaOnLeftDown(self, event):
        if self.comboBox_relevancia_nota.GetItems() == []:
            self.cargar_combo_relevancia_nota()
        event.Skip()

    def comboBox_contextoOnLeftDown(self, event):
        if self.comboBox_contexto.GetItems() == []:
            self.cargar_combo_contexto_nota()
        event.Skip()

    def comboBox_turnoOnCombobox(self, event):

        str_turno = self.comboBox_turno.GetValue()
        lista_turnos = self.dic_turnos_todos[str_turno]

        h1 = lista_turnos[2]
        h2 = lista_turnos[3]

        self.timePicker_hora_inicio_cargue.SetTime(h1.hour, h1.minute, h1.second)
        self.timePicker_hora_fin_cargue.SetTime(h2.hour, h2.minute, h2.second)

        fecha_inicio = self.datePicker_fecha_inicio_cargue.GetValue()






        event.Skip()

    def btn_a_lista_notasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()

        nota = self.txt_nota.GetValue()
        area = U'EXTRUSION'
        relevancia = self.comboBox_relevancia_nota.GetValue()
        contexto = self.comboBox_contexto.GetValue()

        if nota == '':
            wx.MessageBox(u'Debes ingresar una Nota', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if relevancia == '':
            wx.MessageBox(u'Debes seleccionar una relevancia', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if contexto == '':
            wx.MessageBox(u'Debes seleccionar un contexto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        fecha = self.datePicker_fecha_inicio_cargue.GetValue()
        fecha = fecha.Format("%d/%m/%y")

        row = [fecha, relevancia, contexto, nota]
        self.puntero_fila_notas = manipular_grilla.nuevaFilaGrilla(self.grid_notas, row,
                                                                   self.puntero_fila_notas)
        event.Skip()

    def btn_a_lista_novedadesOnButtonClick(self, event):

        manipular_grilla = ManipularGrillas()
        formato_numeros = FormatearNumeros()

        novedad = self.txt_novedad.GetValue()
        tiempo_parada = self.txt_tiempo_parada_minutos.GetValue()

        if novedad == '':
            wx.MessageBox(u'Debes ingresar una Novedad', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if tiempo_parada == '':
            wx.MessageBox(u'Debes ingresar un número valido para el tiempo de parada', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        tiempo_parada = formato_numeros.toNumMilesSigno(tiempo_parada)

        la_fecha = self.datePicker_fecha_novedad.GetValue()
        la_hora = self.timePicker_hora_novedad.GetValue()
        fecha = la_fecha.Format("%d/%m/%y")
        hora = la_hora.Format("%H:%M:%S")

        id_novedad = 25

        row = [fecha, hora, tiempo_parada, novedad]
        self.puntero_fila_novedades = manipular_grilla.nuevaFilaGrilla(self.grid_novedades, row,
                                                                       self.puntero_fila_novedades)
        event.Skip()

    def btn_a_lista_cargue_vagonetasOnButtonClick(self, event):
        import formEAY.formularios.frm_procesos.frm_llenar_tabla_descargue_vagonetas as frm_llenar_tabla_descargue_vagonetas
        frame_llenar_tabla_descargueVagonetas = frm_llenar_tabla_descargue_vagonetas.LlenarTablaDescargueVagonetas(self,
                                                                                                                   self.lista_empleados,
                                                                                                                   self.dic_vagonetas_fechas)
        frame_llenar_tabla_descargueVagonetas.Center()
        frame_llenar_tabla_descargueVagonetas.Show()
        event.Skip()

    def bpButton_eliminar_item_seleccionado_grid_descargue_vagonetasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 6
        self.puntero_fila_cargue_vagonetas = manipular_grilla.delFilasCHK(self.grid_descargue_vagonetas, col_verificacion)
        dic_color = {3: COLOR_RESALTE1, 4: COLOR_RESALTE2, 5: COLOR_RESALTE_ROSA}
        manipular_grilla.setColorFondoCeldaGrilla(self.grid_descargue_vagonetas, dic_color)
        event.Skip()

    def bpButton_eliminar_item_seleccionado_grid_novedadesOnButtonClick(self, event):
            manipular_grilla = ManipularGrillas()
            col_verificacion = 4
            self.puntero_fila_novedades = manipular_grilla.delFilasCHK(self.grid_novedades, col_verificacion)
            event.Skip()

    def bpButton_eliminar_item_seleccionado_grid_notasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 4
        self.puntero_fila_notas = manipular_grilla.delFilasCHK(self.grid_notas, col_verificacion)
        event.Skip()


    def bpButton_deseleccionar_todo_grid_descargue_vagonetasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 6
        manipular_grilla.deseleccionarFilasCHK(self.grid_descargue_vagonetas, col_verificacion)
        event.Skip()

    def bpButton_deseleccionar_todo_grid_novedadesOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 4
        manipular_grilla.deseleccionarFilasCHK(self.grid_novedades, col_verificacion)
        event.Skip()

    def bpButton_deseleccionar_todo_grid_notasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 4
        manipular_grilla.deseleccionarFilasCHK(self.grid_notas, col_verificacion)
        event.Skip()


    def bpButton_limpiar_grid_descargue_vagonetasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        self.puntero_fila_cargue_vagonetas = manipular_grilla.limpiarGrilla(self.grid_descargue_vagonetas)
        event.Skip()

    def bpButton_limpiar_grid_notasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        self.puntero_fila_notas = manipular_grilla.limpiarGrilla(self.grid_notas)
        event.Skip()

    def bpButton_limpiar_grid_novedadesOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        self.puntero_fila_novedades = manipular_grilla.limpiarGrilla(self.grid_novedades)
        event.Skip()


    def grid_novedadesOnGridCellLeftClick(self, event):
        event.Skip()

    def grid_notasOnGridCellLeftClick(self, event):
        event.Skip()

    def btn_ver_formatoOnButtonClick(self, event):
        from formEAY.constantesCAC.imgCAC import Img_formatos
        IMG_FORMATO_DESCARGUE_VAGONETAS = Img_formatos.DESCARGUE_VAGONETAS
        os.startfile(IMG_FORMATO_DESCARGUE_VAGONETAS)
        event.Skip()

    def btn_ver_procedimientoOnButtonClick(self, event):
        from formEAY.constantesCAC.imgCAC import Img_formatos
        IMG_DESCARGUE_PROCEDIMIENTO = Img_formatos.DESCARGUE_VAGONETAS_PROCEDIMIENTO
        os.startfile(IMG_DESCARGUE_PROCEDIMIENTO)
        event.Skip()



    ##  FUNCIONES EAY
    def func_cargar_diccionario_vagonetas_ultima_fecha(self):
        cad_sql = """
                    SELECT det.vagoneta,    max(cab.fecha_inicio)
                    FROM detalle_cargue_vagonetas as det, cabecera_proceso_ecd as cab
                    WHERE cab.uuid = det.uuid and cab.activo='TRUE'
                    GROUP BY det.vagoneta
                    ORDER BY det.vagoneta
        """
        rows = Ejecutar_SQL.select_varios_registros(cad_sql, 'func_cargar_diccionario_vagonetas_ultima_fecha', 500, BasesDeDatos.DB_PRINCIPAL)

        self.dic_vagonetas_fechas = ManipularRows.crearDiccionario(rows, 0, 1)



    def func_calcular_tiempos(self):
        minutos_recesos = 0
        minutos_novedades = 0
        filas_recesos = self.grid_recesos.GetNumberRows()
        for i in range(filas_recesos):
            minutos_recesos += int(self.grid_recesos.GetCellValue(i, 2))

        filas_novedades = self.grid_novedades.GetNumberRows()
        for i in range(filas_novedades):
            minutos_novedades += int(self.grid_novedades.GetCellValue(i, 2))

        return(minutos_recesos, minutos_novedades)

    def cargar_valores_de_inicializacion(self):

        self.txt_total_vagonetas.Hide()
        self.txt_total_unidades.Hide()
        self.lbl_etq_total_unidades.Hide()
        self.lbl_etq_total_vagonetas.Hide()

        self.txt_tiempo_parada_minutos.SetMaxLength(4)

        self.puntero_fila_cargue_vagonetas = 0
        self.puntero_fila_notas = 0
        self.puntero_fila_novedades = 0

        self.cargar_checkList_personal()

        self.limpiar_todas_las_grillas()

        self.set_configuracion_grillas()
        self.set_configuracion_botones()

        self.func_cargar_diccionario_vagonetas_ultima_fecha()




    def func_actualizar_stock_productos(self):

        rows = self.func_crear_datafreme_producto()

       #print(rows)

        nom_tabla = 'producto'
        cols_busqueda = [1]
        cols_a_modificar = [3, 4]

        dic_operaciones = {'stock_primera': 'stock_primera + ', 'stock_segunda': 'stock_segunda + '}

        nom_campos = ['x', 'id_producto', 'nom_producto', 'stock_primera', 'stock_segunda', 'rotos', 'total_1_y_2', 'total']
        tipo_campos = ['int', 'int', 'str', 'int', 'int', 'int', 'int', 'int']

        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows, cols_busqueda, cols_a_modificar, nom_campos,
                                              tipo_campos, dic_operaciones)

        rta = Ejecutar_SQL.update_filas(sSql, 'frm_descargue_vagonetas/func_actualizar_stock_productos', BasesDeDatos.DB_PRINCIPAL)

        # -------------------------------------------------------------------------
        cols_a_modificar = [7]

        dic_operaciones = {'stock_cargue': 'stock_cargue -'}

        nom_campos = ['x', 'id_producto', 'nom_producto', 'stock_primera', 'stock_segunda', 'rotos', 'total_1_y_2', 'stock_cargue']
        tipo_campos = ['int', 'int', 'str', 'int', 'int', 'int', 'int', 'int']

        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows, cols_busqueda, cols_a_modificar, nom_campos,
                                              tipo_campos, dic_operaciones)

        rta = Ejecutar_SQL.update_filas(sSql, 'frm_descargue_vagonetas/func_actualizar_stock_productos',  BasesDeDatos.DB_PRINCIPAL)

        return rta

    def func_crear_datafreme_producto(self):
        cant_filas = self.grid_descargue_vagonetas.GetNumberRows()
        cant_cols = self.grid_descargue_vagonetas.GetNumberCols()
        rows = []
        fila = []
        cant_primera = 0
        cant_segunda = 0
        cant_rotos = 0

        rango_primera = range(0, cant_filas, 3)
        rango_segunda = range(1, cant_filas, 3)
        rango_rotos = range(2, cant_filas, 3)


        for j in range(3, cant_cols):
            nom_producto = self.grid_descargue_vagonetas.GetColLabelValue(j)
            id_producto = self.dic_productos_id[nom_producto]
            cant_primera = 0
            cant_segunda = 0
            cant_rotos = 0
            for i in range(cant_filas):
                if i in rango_primera:
                    cant_primera += int(self.grid_descargue_vagonetas.GetCellValue(i,j))
                if i in rango_segunda:
                    cant_segunda += int(self.grid_descargue_vagonetas.GetCellValue(i,j))
                if i in rango_rotos:
                    cant_rotos += int(self.grid_descargue_vagonetas.GetCellValue(i,j))
            rows.append([id_producto, nom_producto, cant_primera, cant_segunda, cant_rotos])

        df = pd.DataFrame(rows,
                          columns=['id', 'producto', 'primera', 'segunda', 'rotos']
                          )
        #df= df.groupby(['id', 'producto']).sum()
        df['total_1_y_2'] = df[['primera', 'segunda']].sum(axis=1)
        df['total'] = df[['primera', 'segunda', 'rotos']].sum(axis=1)

        #df = df.sort_values(['producto', 'calidad'])

        #print(df)

        rows = df.to_records().tolist()
        return rows

    def cargar_grid_descargueVagonetas(self, rows, cant_cols, row_cabeceras, list_columnas_soloNumeros, dic_productos_id):

        ManipularGrillas.setCantidadColumnasGrilla(self.grid_descargue_vagonetas, cant_cols)
        ManipularGrillas.setCabecerasGrilla(self.grid_descargue_vagonetas, row_cabeceras)
        ManipularGrillas.llenarGrilla(self.grid_descargue_vagonetas, rows)

        self.dic_productos_id = dic_productos_id

        ManipularGrillas.setColumnasSoloNumeros(self.grid_descargue_vagonetas, list_columnas_soloNumeros)

        list_columnas = [0, 1, 2]
        ManipularGrillas.setColumnasSoloLectura(self.grid_descargue_vagonetas, list_columnas)

        dic_color = {0: COLOR_RESALTE1}
        ManipularGrillas.setColorFondoCeldaGrilla(self.grid_descargue_vagonetas, dic_color)

        dic_color = {0: wx.Colour(240, 240, 240), 1: wx.Colour(240, 240, 240), 2: wx.Colour(240, 240, 240)}
        ManipularGrillas.setColorFondoCeldaGrilla(self.grid_descargue_vagonetas, dic_color)

        self.fusionar_celdas_columna_vagoneta()
        self.colorear_filas_intercaladas()

        list_columnas = [0, 1, 2]
        ManipularGrillas.setColumnasSoloLectura(self.grid_descargue_vagonetas, list_columnas)

        self.grid_descargue_vagonetas.AutoSizeColumns()

    def colorear_filas_intercaladas(self):
        can_filas = self.grid_descargue_vagonetas.GetNumberRows()
        cant_cols = self.grid_descargue_vagonetas.GetNumberCols()
        for i in range(3, can_filas, 6):
            for j in range(3, cant_cols):
                self.grid_descargue_vagonetas.SetCellBackgroundColour(i, j, COLOR_RESALTE2)
                self.grid_descargue_vagonetas.SetCellBackgroundColour(i+1, j, COLOR_RESALTE2)
                self.grid_descargue_vagonetas.SetCellBackgroundColour(i+2, j, COLOR_RESALTE2)

    def fusionar_celdas_columna_vagoneta(self):
        can_filas = self.grid_descargue_vagonetas.GetNumberRows()
        for i in range(0, can_filas, 3):
            self.grid_descargue_vagonetas.SetCellSize(i, 0, 3, 1)
            self.grid_descargue_vagonetas.SetCellSize(i, 1, 3, 1)


    def set_configuracion_botones(self):
        from formEAY.constantesCAC.coloresCAC import Colors_botones
        colors_botones = Colors_botones()

        self.btn_guardar.SetBackgroundColour(colors_botones.ACEPTAR)
        # self.btn_guardar.SetForegroundColour(wx.WHITE)
        self.btn_guardar.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD))

        self.btn_a_lista_cargue_vagonetas.SetBackgroundColour(colors_botones.AGREGAR_A_LISTA)
        self.btn_a_lista_notas.SetBackgroundColour(colors_botones.AGREGAR_A_LISTA)
        self.btn_a_lista_novedades.SetBackgroundColour(colors_botones.AGREGAR_A_LISTA)

        self.btn_guardar.SetWindowStyleFlag(wx.NO_BORDER)
        self.btn_a_lista_cargue_vagonetas.SetWindowStyleFlag(wx.NO_BORDER)
        self.btn_a_lista_notas.SetWindowStyleFlag(wx.NO_BORDER)
        self.btn_a_lista_novedades.SetWindowStyleFlag(wx.NO_BORDER)

        self.lbl_estado_guardar.SetLabel('')

    def set_configuracion_grillas(self):

        self.set_configuaracion_grilla_cargue_vagonetas()
        self.set_configuaracion_grilla_recesos()
        self.set_configuaracion_grilla_novedades()
        self.set_configuaracion_grilla_notas()
        self.set_configuracion_cabeceras_grillas()

    def set_configuracion_cabeceras_grillas(self):
        self.grid_descargue_vagonetas.SetLabelBackgroundColour(wx.WHITE)
        self.grid_descargue_vagonetas.SetLabelTextColour(wx.BLACK)

        # self.grid_rotura.SetLabelBackgroundColour(wx.WHITE)
        # self.grid_rotura.SetLabelTextColour(wx.BLACK)

        self.grid_recesos.SetLabelBackgroundColour(wx.WHITE)
        self.grid_recesos.SetLabelTextColour(wx.BLACK)

        self.grid_novedades.SetLabelBackgroundColour(wx.WHITE)
        self.grid_novedades.SetLabelTextColour(wx.BLACK)

        self.grid_notas.SetLabelBackgroundColour(wx.WHITE)
        self.grid_notas.SetLabelTextColour(wx.BLACK)

    def set_configuaracion_grilla_notas(self):
        list_columnas = [0, 1, 2, 3]
        ManipularGrillas.setColumnasSoloLectura(self.grid_notas, list_columnas)

        list_columnas = [4]
        ManipularGrillas.setColumnasFormatoCHK(self.grid_notas, list_columnas)
        self.grid_notas.AutoSizeColumns()

    def set_configuaracion_grilla_novedades(self):

        list_columnas = [0, 1, 2, 3]
        ManipularGrillas.setColumnasSoloLectura(self.grid_novedades, list_columnas)

        list_columnas = [4]
        ManipularGrillas.setColumnasFormatoCHK(self.grid_novedades, list_columnas)
        self.grid_novedades.AutoSizeColumns()

    def set_configuaracion_grilla_cargue_vagonetas(self):
        list_columnas = [0, 1, 2]
        ManipularGrillas.setColumnasSoloLectura(self.grid_descargue_vagonetas, list_columnas)

        list_columnas = [3, 4, 5]
        ManipularGrillas.setColumnasSoloNumeros(self.grid_recesos, list_columnas)

        list_columnas = [6]
        ManipularGrillas.setColumnasFormatoCHK(self.grid_descargue_vagonetas, list_columnas)
        self.grid_descargue_vagonetas.AutoSizeColumns()

    def set_configuaracion_grilla_recesos(self):
        list_columnas = [0, 1]
        ManipularGrillas.setColumnasSoloLectura(self.grid_recesos, list_columnas)
        list_columnas = [2]
        ManipularGrillas.setColumnasSoloNumeros(self.grid_recesos, list_columnas)
        self.grid_recesos.AutoSizeColumns()

    def limpiar_todas_las_grillas(self):
        self.puntero_fila_cargue_vagonetas = ManipularGrillas.limpiarGrilla(self.grid_descargue_vagonetas)
        self.puntero_fila_notas = ManipularGrillas.limpiarGrilla(self.grid_notas)
        self.puntero_fila_novedades = ManipularGrillas.limpiarGrilla(self.grid_novedades)
        self.puntero_fila_recesos_programados = ManipularGrillas.limpiarGrilla(self.grid_recesos)


    def cargar_grid_receso_programado(self):
        rows = DbGetVarios.listaRecesoProgramado(True)
        # id_receso, nom_receso, minutos_descanso

        ManipularGrillas.llenarGrilla(self.grid_recesos, rows)

        cabeceras_grilla = [u' id', u'Receso', u'Minutos Descanso']
        ManipularGrillas.setCabecerasGrilla(self.grid_recesos, cabeceras_grilla)

    def cargar_combo_relevancia_nota(self):
        rows = DbGetVarios.listaRelevanciaNota(True)
        # id_relevancia_nota, nom_relevancia

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.dic_relevancia_nota = ManipularRows.crearDiccionario(rows, 1, 0)
            self.comboBox_relevancia_nota.Set(la_lista)

    def cargar_combo_contexto_nota(self):
        obj_formato = ManipularRows()

        rows = DbGetVarios.listaContextoNota(True)
        # id_contexto_nota, nom_contexto

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.dic_contexto_nota = ManipularRows.crearDiccionario(rows, 1, 0)
            self.comboBox_contexto.Set(la_lista)

    def cargar_combo_turnos(self):
        rows = DbGetVarios.listaTurnos(self.AREA_PRODUCCION, True)
        # id_turno, nom_turno, hora_inicio, hora_salida, activo

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.dic_turnos_todos = ManipularRows.crearDiccionarioTodosLosCampos(rows, 1)
            self.comboBox_turno.Set(la_lista)

    def cargar_checkList_personal(self):
        from formEAY.dbaseCAC.dbEmpleados import Get_empleados

        rows = Get_empleados.lista_basica(AREA_PRODUCCION)

        if rows != None:
            self.lista_empleados = ManipularRows.crearListaValores(rows, 1)
            self.diccionario_personal = ManipularRows.crearDiccionario(rows, 1, 0)
            self.checkList_personal.Set(self.lista_empleados)

    def calcular_totales_grilla_descargue_vagonetas(self):
        """

        :return:  total_vagonetas, total_unidades
        """
        cant_filas = self.grid_descargue_vagonetas.GetNumberRows()
        cant_cols = self.grid_descargue_vagonetas.GetNumberCols()

        total_unidades = 0
        for i in range(cant_filas):
            for j in range(3, cant_cols):
                dato = self.grid_descargue_vagonetas.GetCellValue(i, j)
                if dato == '':
                    dato = 0
                else:
                    total_unidades += int(dato)

        list_vagonetas = []
        for i in range(cant_filas):
            dato = self.grid_descargue_vagonetas.GetCellValue(i, 0)
            list_vagonetas.append(dato)

        conjunto=set(list_vagonetas)

        total_vagonetas = len(conjunto)

        return total_vagonetas, total_unidades



