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

class CargueVagonetas(wx.Frame):

    def __init__(self, parent, usuario='usuario1', dir_mac = 'la dir mac del pc'):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Registrar Cargue Vagonetas", pos=wx.DefaultPosition,
                          size=wx.Size(1040, 680), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(1040, 680), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.dic_productos_id = 0

        self.AREA_PRODUCCION = AreasProduccion.CARGUE_VAGONETAS
        self.uuid_eay = uuid4()
        self.usuario = usuario
        self.dir_mac = dir_mac

        icono_grillas = Img_grillas()
        self.img_produccion = Img_produccion()

        bSizer_extrusion = wx.BoxSizer(wx.VERTICAL)

        bSizer_panel_principal = wx.BoxSizer(wx.VERTICAL)

        bSizer_panel_cabecera = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_cabecera = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel_cabecera.SetBackgroundColour(wx.WHITE)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.bitmap_logo_proceso = wx.StaticBitmap(self.panel_cabecera, wx.ID_ANY,
                                                   wx.Bitmap(self.img_produccion.CARGUE_VAGONETAS,
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

        self.lbl_etq_total_vagonetas = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Total Vagonetas:", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.lbl_etq_total_vagonetas.Wrap(-1)
        bSizer14.Add(self.lbl_etq_total_vagonetas, 0, wx.ALL, 5)

        self.txt_total_vagonetas = wx.TextCtrl(self.panel_cabecera, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(55, -1), validator=validador_solo_digitos())
        bSizer14.Add(self.txt_total_vagonetas, 0, wx.ALL, 5)

        self.lbl_etq_total_unidades = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Total Unidades:",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_total_unidades.Wrap(-1)
        bSizer14.Add(self.lbl_etq_total_unidades, 0, wx.ALL, 5)

        self.txt_total_unidades = wx.TextCtrl(self.panel_cabecera, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.Size(65, -1), validator=validador_solo_digitos())

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

        self.lbl_etq_fecha_fin = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Fin:", wx.DefaultPosition,
                                               wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lbl_etq_fecha_fin.Wrap(-1)
        bSizer8.Add(self.lbl_etq_fecha_fin, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        self.datePicker_fecha_fin = wx.adv.DatePickerCtrl(self.panel_cabecera, wx.ID_ANY, wx.DefaultDateTime,
                                                          wx.DefaultPosition, wx.Size(90, -1),
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

        self.panel_empleado = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel_empleado.SetBackgroundColour(wx.WHITE)

        bSizer47 = wx.BoxSizer(wx.VERTICAL)

        ## --------------

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
        bSizer_panel_empleado.Add(self.panel_empleado, 1, wx.EXPAND | wx.ALL, 5)

        bSizer4.Add(bSizer_panel_empleado, 0, wx.EXPAND, 5)

        bSizer_panel_cargueVagonetas = wx.BoxSizer(wx.VERTICAL)

        self.panel1_cargueVagonetas = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel1_cargueVagonetas.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_panel_extrusion = wx.BoxSizer(wx.VERTICAL)

        bSizer141 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_llenar_tabla = wx.Button(self.panel1_cargueVagonetas, wx.ID_ANY, u"--> Llenar Tabla",
                                               wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.btn_llenar_tabla.SetBackgroundColour(wx.Colour(254, 232, 73))

        bSizer141.Add(self.btn_llenar_tabla, 0, wx.ALL, 5)

        bSizer_panel_extrusion.Add(bSizer141, 0, wx.EXPAND, 5)

        bSizer46 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline2 = wx.StaticLine(self.panel1_cargueVagonetas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer46.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_panel_extrusion.Add(bSizer46, 0, wx.EXPAND, 5)

        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

        self.grid_cargueVagonetas = wx.grid.Grid(self.panel1_cargueVagonetas, wx.ID_ANY, wx.DefaultPosition,
                                                 wx.DefaultSize, 0)

        # Grid
        self.grid_cargueVagonetas.CreateGrid(0, 1)
        self.grid_cargueVagonetas.EnableEditing(True)
        self.grid_cargueVagonetas.EnableGridLines(True)
        self.grid_cargueVagonetas.EnableDragGridSize(False)
        self.grid_cargueVagonetas.SetMargins(0, 0)

        # Columns
        self.grid_cargueVagonetas.AutoSizeColumns()
        self.grid_cargueVagonetas.EnableDragColMove(False)
        self.grid_cargueVagonetas.EnableDragColSize(True)
        self.grid_cargueVagonetas.SetColLabelSize(30)
        self.grid_cargueVagonetas.SetColLabelValue(0, u"Vagoneta")
        self.grid_cargueVagonetas.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_cargueVagonetas.EnableDragRowSize(True)
        self.grid_cargueVagonetas.SetRowLabelSize(40)
        self.grid_cargueVagonetas.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_cargueVagonetas.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer16.Add(self.grid_cargueVagonetas, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_panel_extrusion.Add(bSizer16, 1, wx.EXPAND, 5)

        self.panel1_cargueVagonetas.SetSizer(bSizer_panel_extrusion)
        self.panel1_cargueVagonetas.Layout()
        bSizer_panel_extrusion.Fit(self.panel1_cargueVagonetas)
        bSizer_panel_cargueVagonetas.Add(self.panel1_cargueVagonetas, 1, wx.EXPAND | wx.ALL, 5)

        bSizer4.Add(bSizer_panel_cargueVagonetas, 2, wx.EXPAND, 5)

        bSizer_panel_principal.Add(bSizer4, 2, wx.EXPAND, 5)

        bSizer_notebook = wx.BoxSizer(wx.VERTICAL)

        ## -------------------

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.NB_NOPAGETHEME | wx.FULL_REPAINT_ON_RESIZE)
        self.panel_notebook_rotura = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                 wx.TAB_TRAVERSAL)
        self.panel_notebook_rotura.SetBackgroundColour(wx.WHITE)
        bSizer_panel_notebook_rotura = wx.BoxSizer(wx.VERTICAL)

        bSizer32 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_informacion_boquillas = wx.StaticText(self.panel_notebook_rotura, wx.ID_ANY,
                                                           u"//  Se registra la cantidad de productos que han sufrido rotura",
                                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_informacion_boquillas.Wrap(-1)
        self.lbl_etq_informacion_boquillas.SetForegroundColour(wx.Colour(0, 128, 0))

        bSizer32.Add(self.lbl_etq_informacion_boquillas, 0, wx.ALL, 5)

        bSizer_panel_notebook_rotura.Add(bSizer32, 0, wx.EXPAND, 5)

        bSizer33 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_producto_roto = wx.StaticText(self.panel_notebook_rotura, wx.ID_ANY, u"Producto:",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_producto_roto.Wrap(-1)
        bSizer33.Add(self.lbl_etq_producto_roto, 0, wx.ALL, 5)

        comboBox_producto_rotoChoices = []
        self.comboBox_producto_roto = wx.ComboBox(self.panel_notebook_rotura, wx.ID_ANY, u"Combo!",
                                                  wx.DefaultPosition,  wx.Size(300, -1), comboBox_producto_rotoChoices,
                                                  wx.CB_READONLY)
        bSizer33.Add(self.comboBox_producto_roto, 0, wx.ALL, 5)

        self.lbl_etq_unidades_rotas = wx.StaticText(self.panel_notebook_rotura, wx.ID_ANY, u"Unidades Rotas:",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_unidades_rotas.Wrap(-1)
        bSizer33.Add(self.lbl_etq_unidades_rotas, 0, wx.ALL, 5)

        self.txt_unidades_rotas = wx.TextCtrl(self.panel_notebook_rotura, wx.ID_ANY, wx.EmptyString,
                                              wx.DefaultPosition, wx.Size(110, -1), validator=validador_solo_digitos())
        self.txt_unidades_rotas.SetMaxLength(5)
        bSizer33.Add(self.txt_unidades_rotas, 0, wx.ALL, 5)

        self.btn_a_lista_unidadesRotas = wx.Button(self.panel_notebook_rotura, wx.ID_ANY, u"--> Lista",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer33.Add(self.btn_a_lista_unidadesRotas, 0, wx.ALL, 5)

        bSizer_panel_notebook_rotura.Add(bSizer33, 0, wx.EXPAND, 5)

        bSizer34 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer52 = wx.BoxSizer(wx.VERTICAL)

        self.grid_rotura = wx.grid.Grid(self.panel_notebook_rotura, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          0)

        # Grid
        self.grid_rotura.CreateGrid(3, 4)
        self.grid_rotura.EnableEditing(True)
        self.grid_rotura.EnableGridLines(True)
        self.grid_rotura.EnableDragGridSize(False)
        self.grid_rotura.SetMargins(0, 0)

        # Columns
        self.grid_rotura.EnableDragColMove(False)
        self.grid_rotura.EnableDragColSize(True)
        self.grid_rotura.SetColLabelSize(30)
        self.grid_rotura.SetColLabelValue(0, u"id ")
        self.grid_rotura.SetColLabelValue(1, u"Producto")
        self.grid_rotura.SetColLabelValue(2, u"Cant. Rotos")
        self.grid_rotura.SetColLabelValue(3, u"Sel")
        self.grid_rotura.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_rotura.SetRowSize(0, 19)
        self.grid_rotura.SetRowSize(1, 18)
        self.grid_rotura.SetRowSize(2, 19)
        self.grid_rotura.EnableDragRowSize(True)
        self.grid_rotura.SetRowLabelSize(40)
        self.grid_rotura.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_rotura.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.grid_rotura.AutoSizeColumns()

        bSizer52.Add(self.grid_rotura, 1, wx.ALL | wx.EXPAND, 5)

        bSizer34.Add(bSizer52, 1, wx.EXPAND, 5)

        bSizer412 = wx.BoxSizer(wx.VERTICAL)

        self.bpButton_eliminar_item_seleccionado_grid_rotura = wx.BitmapButton(self.panel_notebook_rotura,
                                                                                 wx.ID_ANY, wx.Bitmap(
                icono_grillas.ELIMINAR_ITEM_SELECIONADO, wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                                                 wx.DefaultSize,
                                                                                 wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_eliminar_item_seleccionado_grid_rotura.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.ELIMINAR_ITEM_SELECIONADO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer412.Add(self.bpButton_eliminar_item_seleccionado_grid_rotura, 0, wx.ALL, 5)

        self.bpButton_deseleccionar_todo_grid_rotura = wx.BitmapButton(self.panel_notebook_rotura, wx.ID_ANY,
                                                                         wx.Bitmap(
                                                                             icono_grillas.DESELECCIONAR_TODO,
                                                                             wx.BITMAP_TYPE_ANY),
                                                                         wx.DefaultPosition, wx.DefaultSize,
                                                                         wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_deseleccionar_todo_grid_rotura.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer412.Add(self.bpButton_deseleccionar_todo_grid_rotura, 0, wx.ALL, 5)

        # self.m_staticline12 = wx.StaticLine(self.panel_notebook_rotura, wx.ID_ANY, wx.DefaultPosition,
        #                                     wx.DefaultSize, wx.LI_HORIZONTAL)
        # bSizer412.Add(self.m_staticline12, 0, wx.EXPAND | wx.ALL, 5)

        self.bpButton_limpiar_grid_rotura = wx.BitmapButton(self.panel_notebook_rotura, wx.ID_ANY,
                                                              wx.Bitmap(
                                                                  icono_grillas.LIMPIAR_GRILLA,
                                                                  wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                              wx.DefaultSize, wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_limpiar_grid_rotura.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.LIMPIAR_GRILLA_SEL, wx.BITMAP_TYPE_ANY))
        bSizer412.Add(self.bpButton_limpiar_grid_rotura, 0, wx.ALL, 5)

        bSizer34.Add(bSizer412, 0, wx.EXPAND, 5)

        bSizer_panel_notebook_rotura.Add(bSizer34, 1, wx.EXPAND, 5)

        self.panel_notebook_rotura.SetSizer(bSizer_panel_notebook_rotura)
        self.panel_notebook_rotura.Layout()
        bSizer_panel_notebook_rotura.Fit(self.panel_notebook_rotura)
        self.m_notebook1.AddPage(self.panel_notebook_rotura, u"Rotura", True)
        self.panel_notebook_recesos = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                               wx.TAB_TRAVERSAL)
        self.panel_notebook_recesos.SetBackgroundColour(wx.WHITE)
        bSizer_panel_notebook_recesos = wx.BoxSizer(wx.VERTICAL)

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
        self.grid_recesos.CreateGrid(3, 3)
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
        self.panel_notebook_novedades1.SetBackgroundColour(wx.WHITE)
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
        self.grid_novedades.CreateGrid(3, 5)
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

        # self.m_staticline121 = wx.StaticLine(self.panel_notebook_novedades1, wx.ID_ANY, wx.DefaultPosition,
        #                                      wx.DefaultSize, wx.LI_HORIZONTAL)
        # bSizer4121.Add(self.m_staticline121, 0, wx.EXPAND | wx.ALL, 5)

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
        self.panel_notebook_notas1.SetBackgroundColour(wx.WHITE)
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
        # self.datePicker_fecha_evento_nota = wx.adv.DatePickerCtrl(self.panel_notebook_notas1, wx.ID_ANY,
        #                                                           wx.DefaultDateTime,
        #                                                           wx.DefaultPosition, wx.DefaultSize,
        #                                                           style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
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

        # self.m_staticline1211 = wx.StaticLine(self.panel_notebook_notas1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
        #                                       wx.LI_HORIZONTAL)
        # bSizer41211.Add(self.m_staticline1211, 0, wx.EXPAND | wx.ALL, 5)

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

        ##
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
                                                u"1/7  Estamos guardando, el procesos puede tardar unos segundos...",
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
        ##

        bSizer_panel_principal.Add(bSizer_pie_de_formulario, 0, wx.EXPAND, 5)

        bSizer_extrusion.Add(bSizer_panel_principal, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer_extrusion)
        self.Layout()

        self.Centre(wx.BOTH)

        ## OPERACIONES INICIALES EAY
        self.cargar_valores_de_inicializacion()

        # Connect Events
        self.btn_ver_ultimoProceso.Bind(wx.EVT_BUTTON, self.btn_ver_ultimoProcesoOnButtonClick)

        self.m_notebook1.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.m_notebook1OnNotebookPageChanged)


        self.comboBox_turno.Bind(wx.EVT_LEFT_DOWN, self.comboBox_turnoOnLeftDown)
        # self.comboBox_producto.Bind(wx.EVT_LEFT_DOWN, self.comboBox_productoOnLeftDown)
        # self.comboBox_vagoneta.Bind(wx.EVT_LEFT_DOWN, self.comboBox_vagonetaOnLeftDown)
        self.comboBox_relevancia_nota.Bind(wx.EVT_LEFT_DOWN, self.comboBox_relevancia_notaOnLeftDown)
        self.comboBox_contexto.Bind(wx.EVT_LEFT_DOWN, self.comboBox_contextoOnLeftDown)
        self.comboBox_turno.Bind(wx.EVT_COMBOBOX, self.comboBox_turnoOnCombobox)
        self.comboBox_producto_roto.Bind(wx.EVT_LEFT_DOWN, self.comboBox_producto_rotoOnLeftDown)

        self.btn_llenar_tabla.Bind(wx.EVT_BUTTON, self.btn_llenar_tablaOnButtonClick)

        # self.bpButton_eliminar_item_seleccionado_grid_cargueVagonetas.Bind(wx.EVT_BUTTON,
        #                                                              self.bpButton_eliminar_item_seleccionado_grid_cargueVagonetasOnButtonClick)
        self.bpButton_eliminar_item_seleccionado_grid_rotura.Bind(wx.EVT_BUTTON,
                                                                    self.bpButton_eliminar_item_seleccionado_grid_roturaOnButtonClick)
        self.bpButton_eliminar_item_seleccionado_grid_novedades.Bind(wx.EVT_BUTTON,
                                                                     self.bpButton_eliminar_item_seleccionado_grid_novedadesOnButtonClick)
        self.bpButton_eliminar_item_seleccionado_grid_notas.Bind(wx.EVT_BUTTON,
                                                                 self.bpButton_eliminar_item_seleccionado_grid_notasOnButtonClick)

        # self.bpButton_deseleccionar_todo_grid_cargueVagonetas.Bind(wx.EVT_BUTTON,
        #                                                      self.bpButton_deseleccionar_todo_grid_cargueVagonetasOnButtonClick)
        self.bpButton_deseleccionar_todo_grid_novedades.Bind(wx.EVT_BUTTON,
                                                             self.bpButton_deseleccionar_todo_grid_novedadesOnButtonClick)
        self.bpButton_deseleccionar_todo_grid_notas.Bind(wx.EVT_BUTTON,
                                                         self.bpButton_deseleccionar_todo_grid_notasOnButtonClick)
        self.bpButton_deseleccionar_todo_grid_rotura.Bind(wx.EVT_BUTTON,
                                                            self.bpButton_deseleccionar_todo_grid_roturaOnButtonClick)

        self.bpButton_limpiar_grid_notas.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_notasOnButtonClick)
        self.bpButton_limpiar_grid_novedades.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_novedadesOnButtonClick)
        self.bpButton_limpiar_grid_rotura.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_roturaOnButtonClick)
        # self.bpButton_limpiar_grid_cargueVagonetas.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_cargueVagonetasOnButtonClick)

        self.btn_a_lista_unidadesRotas.Bind(wx.EVT_BUTTON, self.btn_a_lista_unidadesRotasOnButtonClick)


        self.grid_rotura.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_roturaOnGridCellLeftClick)
        self.grid_cargueVagonetas.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.grid_cargueVagonetasOnGridCellChange)



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
                                                                        self.img_produccion.CARGUE_VAGONETAS, 'CARGUE DE VAGONETAS')
        frame_vistaPrevia.Center()
        frame_vistaPrevia.Show()
        event.Skip()

    def btn_guardarOnButtonClick(self, event):

        from formEAY.dbaseCAC.dbVarios import DbInsertVarios
        from formEAY.dbaseCAC.dbVerificaciones import DbGetVerificaciones
        #from formEAY.utilCAC.Utiles_proposito_general import ManejoFechasHoras
        from pyeay.fechasHoras import ManejoFechasHoras

        fecha_inicio = self.datePicker_fecha_inicio_extrusion.GetValue()
        fecha_fin = self.datePicker_fecha_fin.GetValue()

        if fecha_fin < fecha_inicio:
            wx.MessageBox(u'Fechas inconsistentes, fecha fin debe ser mayor o igual a la fecha inicio', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        ##
        activo = 'True'

        fecha_inicio = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha_inicio_extrusion)
        fecha_fin = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha_fin)
        hora_inicio = ManejoFechasHoras.formatearHoraXSql(self.timePicker_hora_inicio_extrusion)
        hora_fin = ManejoFechasHoras.formatearHoraXSql(self.timePicker_hora_fin_extrusion)

        el_turno = self.comboBox_turno.GetValue()
        if el_turno == '':
            wx.MessageBox(u'Debes seleccionar un turno', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        dia_semana = ManejoFechasHoras.getDiaSemanaToNumero(self.datePicker_fecha_inicio_extrusion)
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

        ##

        cant_empleados = len(self.checkList_personal.GetCheckedStrings())
        if cant_empleados == 0:
            wx.MessageBox(u'Debes seleccionar el personal', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        total_vagonetas = self.txt_total_vagonetas.GetValue()


        # if total_vagonetas == '' or total_vagonetas == '0':
        #     wx.MessageBox(u'Debes ingresar un número valido del total vagonetas', u'Atención', wx.OK | wx.ICON_INFORMATION)
        #     return 0
        #
        # total_unidades = self.txt_total_unidades.GetValue()
        # if total_unidades == '' or total_unidades == '0':
        #     wx.MessageBox(u'Debes ingresar un número valido de total unidades', u'Atención',
        #                   wx.OK | wx.ICON_INFORMATION)
        #     return 0

        if self.grid_cargueVagonetas.GetNumberRows() == 0:
            wx.MessageBox(u'Grilla Cargue vagonetas esta vacia', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0
        else:
            total_vagonetas_grid, total_unidades_grid = self.calcular_totales_grilla_extrusion()

            # if total_vagonetas_grid != int(total_vagonetas):
            #     wx.MessageBox(u'Detectada una posible inconsistencia en la cantidad de vagonetas', u'Atención',
            #                   wx.OK | wx.ICON_INFORMATION)
            #     return 0
            # if total_unidades_grid != int(total_unidades):
            #     wx.MessageBox(u'Detectada una posible inconsistencia en la cantidad de unidades', u'Atención',
            #                   wx.OK | wx.ICON_INFORMATION)
            #     return 0

        fecha_transacccion, hora_transacion = ManejoFechasHoras.getFechaHoraActual()

        self.btn_guardar.Hide()

        ##
        fecha_transacccion, hora_transacion = ManejoFechasHoras.getFechaHoraActual()

        self.btn_guardar.Hide()

        cant_segundos = ManejoFechasHoras.cantidadSegundosEntre2Fechas(self.datePicker_fecha_inicio_extrusion,
                                                                       self.datePicker_fecha_fin,
                                                                       self.timePicker_hora_inicio_extrusion,
                                                                       self.timePicker_hora_fin_extrusion)

        minutos_jornada = cant_segundos / 60
        minutos_receso, minutos_novedades = self.func_calcular_tiempos()



        self.lbl_estado_guardar.SetLabel('1/9  Estamos guardando, el procesos puede tardar unos segundos...')
        rta_cabecera = DbInsertVarios.cabeceraProcesoECD(self.uuid_eay, self.usuario, self.dir_mac,
                                                           fecha_transacccion,
                                                           hora_transacion, id_turno, el_turno,
                                                           total_vagonetas_grid, total_unidades_grid, fecha_inicio, hora_inicio,
                                                           fecha_fin,
                                                           hora_fin, activo, self.AREA_PRODUCCION,
                                                         minutos_jornada, minutos_receso, minutos_novedades)

        self.lbl_estado_guardar.SetLabel('2/9  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_insert_DetalleCargueVagonetas = DbInsertVarios.detalleCargueVagonetas(self)

        # self.lbl_estado_guardar.SetLabel('3/9  Estamos guardando, el proceso puede tardar unos segundos...')
        # rta_insert_roturaCargueVagonetas = DbInsertVarios.roturaCargueVagonetas(self)

        self.lbl_estado_guardar.SetLabel('4/9  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_actualizar_stock = self.func_actualizar_stock_productos()

        self.lbl_estado_guardar.SetLabel('5/9  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_insert_empleados = DbInsertVarios.personal(self)


        self.lbl_estado_guardar.SetLabel('6/9  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_insert_recesosProgramados = DbInsertVarios.recesosProgramados(self)
        self.lbl_estado_guardar.SetLabel('7/9  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_insert_novedades = DbInsertVarios.novedades(self)
        self.lbl_estado_guardar.SetLabel('8/9  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_insert_notas = DbInsertVarios.notas(self)
        self.lbl_estado_guardar.SetLabel('9/9  Estamos guardando, el proceso puede tardar unos segundos...')
        rta_insert_rotura = self.guardar_listaRotura()

        self.lbl_estado_guardar.SetLabel('')

        wx.MessageBox(u'El formulario Cargue de Vagonetas fue guardado  correctamente', u'Atención', wx.OK | wx.ICON_INFORMATION)

        ## creamos un nuevo uuid
        self.uuid_eay = uuid4()
        ##
        self.Destroy()

        event.Skip()

    def m_notebook1OnNotebookPageChanged(self, event):
        if self.m_notebook1.GetSelection() == 1:  ## 1 es la pagina de recesos programados
            if self.grid_recesos.GetNumberRows() == 0:
                self.cargar_grid_receso_programado()
                self.panel_notebook_recesos.Layout()
        event.Skip()

    def comboBox_vagonetaOnLeftDown(self, event):
        if self.comboBox_vagoneta.GetItems() == []:
            self.cargar_combo_vagonetas()
        event.Skip()

    def comboBox_productoOnLeftDown(self, event):
        if self.comboBox_producto.GetItems() == []:
            self.cargar_combo_productos()
        event.Skip()

    def comboBox_producto_rotoOnLeftDown(self, event):
        if self.comboBox_producto_roto.GetItems() == []:
            self.cargar_combo_productos()
        event.Skip()

    def comboBox_relevancia_notaOnLeftDown(self, event):
        if self.comboBox_relevancia_nota.GetItems() == []:
            self.cargar_combo_relevancia_nota()
        event.Skip()

    def comboBox_contextoOnLeftDown(self, event):
        if self.comboBox_contexto.GetItems() == []:
            self.cargar_combo_contexto_nota()
        event.Skip()

    def comboBox_turnoOnLeftDown(self, event):
        if self.comboBox_turno.GetItems() == []:
            self.cargar_combo_turnos()
        event.Skip()

    def comboBox_turnoOnCombobox(self, event):

        str_turno = self.comboBox_turno.GetValue()
        lista_turnos = self.dic_turnos_todos[str_turno]

        h1 = lista_turnos[2]
        h2 = lista_turnos[3]

        self.timePicker_hora_inicio_extrusion.SetTime(h1.hour, h1.minute, h1.second)
        self.timePicker_hora_fin_extrusion.SetTime(h2.hour, h2.minute, h2.second)
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

        fecha = self.datePicker_fecha_inicio_extrusion.GetValue()
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

    def btn_llenar_tablaOnButtonClick(self, event):

        import formEAY.formularios.frm_procesos.frm_llenar_tabla_cargue_vagonetas as frm_llenar_tabla_cargue_vagonetas
        frame_llenar_tabla_cargueVagonetas = frm_llenar_tabla_cargue_vagonetas.LlenarTablaCargueVagonetas(self)
        frame_llenar_tabla_cargueVagonetas.Center()
        frame_llenar_tabla_cargueVagonetas.Show()

        return 0



        ### -----------------------------------------------

        manipular_grilla = ManipularGrillas()
        formato_numeros = FormatearNumeros()

        producto = self.comboBox_producto.GetValue()

        if producto == '':
            wx.MessageBox(u'Debes seleccionar un Producto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        try:
            id_producto = self.dic_cargueVagonetas[producto]
        except:
            return 0

        vagoneta = self.comboBox_vagoneta.GetValue()
        unidades_x_vagoneta = self.txt_unidades_x_vagoneta.GetValue()

        if producto == '':
            wx.MessageBox(u'Debes seleccionar un Producto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if vagoneta == '':
            wx.MessageBox(u'Debes seleccionar una vagoneta', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if unidades_x_vagoneta == '' or unidades_x_vagoneta == '0':
            wx.MessageBox(u'Debes ingresar un número valido de unidades por vagoneta', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        # unidades_x_vagoneta = formato_numeros.toNumMilesSigno(unidades_x_vagoneta, '')

        row = [id_producto, producto, vagoneta, unidades_x_vagoneta]

        self.puntero_fila_cargueVagoneta = manipular_grilla.nuevaFilaGrilla(self.grid_cargueVagonetas, row,
                                                                            self.puntero_fila_cargueVagoneta)

        dic_color = {3: COLOR_RESALTE1, 2: COLOR_RESALTE2}
        manipular_grilla.setColorFondoCeldaGrilla(self.grid_cargueVagonetas, dic_color)

        event.Skip()

    def btn_a_lista_unidadesRotasOnButtonClick(self, event):

        manipular_grilla = ManipularGrillas()
        formato_numeros = FormatearNumeros()

        producto_roto = self.comboBox_producto_roto.GetValue()

        if producto_roto == '':
            wx.MessageBox(u'Debes seleccionar un Producto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        cant_unit_rotas = self.txt_unidades_rotas.GetValue()
        if cant_unit_rotas == '' or cant_unit_rotas == '0':
            wx.MessageBox(u'Debes ingresar un número valido de unidades con rotura', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        try:
            id_producto_roto = self.dic_cargueVagonetas[producto_roto]
        except:
            return 0

        row = [id_producto_roto, producto_roto, cant_unit_rotas]

        self.puntero_fila_boquilla = manipular_grilla.nuevaFilaGrilla(self.grid_rotura, row,
                                                                      self.puntero_fila_boquilla)
        dic_color = {2: COLOR_RESALTE_ROSA}
        manipular_grilla.setColorFondoCeldaGrilla(self.grid_rotura, dic_color)

        event.Skip()

    def bpButton_eliminar_item_seleccionado_grid_cargueVagonetasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 4
        self.puntero_fila_cargueVagoneta = manipular_grilla.delFilasCHK(self.grid_cargueVagonetas, col_verificacion)

        dic_color = {3: COLOR_RESALTE1, 2: COLOR_RESALTE2}
        manipular_grilla.setColorFondoCeldaGrilla(self.grid_cargueVagonetas, dic_color)

        event.Skip()

    def bpButton_eliminar_item_seleccionado_grid_roturaOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 3
        self.puntero_fila_boquilla = manipular_grilla.delFilasCHK(self.grid_rotura, col_verificacion)

        dic_color = {2: COLOR_RESALTE_ROSA}
        manipular_grilla.setColorFondoCeldaGrilla(self.grid_rotura, dic_color)

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

    def bpButton_deseleccionar_todo_grid_cargueVagonetasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 4
        manipular_grilla.deseleccionarFilasCHK(self.grid_cargueVagonetas, col_verificacion)
        event.Skip()

    def bpButton_deseleccionar_todo_grid_roturaOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 3
        manipular_grilla.deseleccionarFilasCHK(self.grid_rotura, col_verificacion)
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

    def bpButton_limpiar_grid_roturaOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        self.puntero_fila_boquilla = manipular_grilla.limpiarGrilla(self.grid_rotura)
        event.Skip()

    def bpButton_limpiar_grid_cargueVagonetasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        self.puntero_fila_cargueVagoneta = manipular_grilla.limpiarGrilla(self.grid_cargueVagonetas)
        event.Skip()

    def bpButton_limpiar_grid_notasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        self.puntero_fila_notas = manipular_grilla.limpiarGrilla(self.grid_notas)
        event.Skip()

    def bpButton_limpiar_grid_novedadesOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        self.puntero_fila_novedades = manipular_grilla.limpiarGrilla(self.grid_novedades)
        event.Skip()

    def grid_roturaOnGridCellLeftClick(self, event):
        event.Skip()

    def grid_cargueVagonetasOnGridCellChange(self, event):
        self.recalcular_porcentaje_cubicacion_toda_tabla()
        event.Skip()

    def grid_novedadesOnGridCellLeftClick(self, event):
        event.Skip()

    def grid_notasOnGridCellLeftClick(self, event):
        event.Skip()

    def btn_ver_formatoOnButtonClick(self, event):
        from formEAY.constantesCAC.imgCAC import Img_formatos
        IMG_FORMATO_CARGUE_VAGONETAS = Img_formatos.CARGUE_VAGONETAS
        os.startfile(IMG_FORMATO_CARGUE_VAGONETAS)
        event.Skip()

    def btn_ver_procedimientoOnButtonClick(self, event):
        from formEAY.constantesCAC.imgCAC import Img_formatos
        IMG_CARGUE_VAGONETAS_PROCEDIMIENTO = Img_formatos.CARGUE_VAGONETAS_PROCEDIMIENTO
        os.startfile(IMG_CARGUE_VAGONETAS_PROCEDIMIENTO)
        event.Skip()



    ##  FUNCIONES EAY
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

    def recalcular_porcentaje_cubicacion_toda_tabla(self):
        cant_filas = self.grid_cargueVagonetas.GetNumberRows()
        cant_cols = self.grid_cargueVagonetas.GetNumberCols() - 2

        cubicacion = 0.0

        for i in range(cant_filas):
            cubicacion = 0.0
            for j in range(cant_cols):
                valor_celda = self.grid_cargueVagonetas.GetCellValue(i, j+2)
                if valor_celda == '':
                    valor_celda = 0.0
                else:
                    valor_celda = float(valor_celda)
                producto = self.grid_cargueVagonetas.GetColLabelValue(j + 2)
                unidades_x_vagoneta = float(self.dic_productos_id[producto][5])

                cubicacion += (valor_celda / unidades_x_vagoneta) * 1.0

            if cubicacion > 1.02:
                COLOR_ROSADO = wx.Colour(255, 206, 222)
                self.grid_cargueVagonetas.SetCellBackgroundColour(i, 1, COLOR_ROSADO)
            else:
                COLOR_GRIS = wx.Colour(240, 240, 240)
                self.grid_cargueVagonetas.SetCellBackgroundColour(i, 1, COLOR_GRIS)

            self.grid_cargueVagonetas.SetCellValue(i, 1, str(round(cubicacion, 3)))
            self.Layout()

    def func_actualizar_stock_productos(self):

        #-----------------------------------
        cant_filas = self.grid_cargueVagonetas.GetNumberRows()
        cant_columnas = self.grid_cargueVagonetas.GetNumberCols()
        list_valores = []

        for j in range(2, cant_columnas):
            list_fila = []
            producto = self.grid_cargueVagonetas.GetColLabelValue(j)
            id_producto = self.dic_productos_id[producto][0]
            list_fila.append(id_producto)

            total_unidades = 0
            for i in range(cant_filas):
                unidades_producto = self.grid_cargueVagonetas.GetCellValue(i, j)
                if unidades_producto == '':
                    unidades_producto = 0
                total_unidades += int(unidades_producto)

            list_fila.append(total_unidades)

            list_valores.append(list_fila)

        rows_sumar_a_stock_cargue = list_valores

        cant_filas = self.grid_rotura.GetNumberRows()
        list_fila = []
        for i in range(cant_filas):

            id_producto = int(self.grid_rotura.GetCellValue(i, 0))
            list_fila.append(id_producto)
            unidades_producto = int(self.grid_rotura.GetCellValue(i, 2))
            list_fila.append(unidades_producto)

            list_valores.append(list_fila)
            list_fila = []

        #-----------------------------------
        df = pd.DataFrame(list_valores,
                          columns=['id', 'cant']
                          )
        df = df.groupby(['id']).sum()
        # df = df.sort_values(['producto', 'calidad'])

        rows = df.to_records().tolist()

        nom_tabla = 'producto'
        cols_busqueda = [0]
        cols_a_modificar = [1]

        dic_operaciones = {'stock_cochado':'stock_cochado - '}

        nom_campos = ['id_producto', 'stock_cochado']
        tipo_campos = ['int', 'int']

        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows, cols_busqueda, cols_a_modificar, nom_campos,
                                                          tipo_campos, dic_operaciones)

        rta = Ejecutar_SQL.update_filas(sSql, 'frm_cargue_vagonetas/func_actualizar_stock_productos', BasesDeDatos.DB_PRINCIPAL)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        nom_tabla = 'producto'
        cols_busqueda = [0]
        cols_a_modificar = [1]

        dic_operaciones = {'stock_cargue': 'stock_cargue + '}

        nom_campos = ['id_producto', 'stock_cargue']
        tipo_campos = ['int', 'int']

        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows_sumar_a_stock_cargue, cols_busqueda, cols_a_modificar, nom_campos,
                                              tipo_campos, dic_operaciones)

        rta = Ejecutar_SQL.insert_filas(sSql, 'frm_cargue_vagonetas/func_actualizar_stock_productos', BasesDeDatos.DB_PRINCIPAL)

        return rta

    def cargar_grid_cargueVagonetas(self, rows, cant_cols, row_cabeceras, list_columnas_soloNumeros, dic_productos_id):

        ManipularGrillas.setCantidadColumnasGrilla(self.grid_cargueVagonetas, cant_cols)
        ManipularGrillas.setCabecerasGrilla(self.grid_cargueVagonetas, row_cabeceras)
        ManipularGrillas.llenarGrilla(self.grid_cargueVagonetas, rows)

        self.dic_productos_id = dic_productos_id

        ManipularGrillas.setColumnasSoloNumeros(self.grid_cargueVagonetas, list_columnas_soloNumeros)

        list_columnas = [0, 1]
        ManipularGrillas.setColumnasSoloLectura(self.grid_cargueVagonetas, list_columnas)

        COLOR_GRIS = wx.Colour(240, 240, 240)
        dic_color = {0: COLOR_GRIS, 1: COLOR_GRIS}
        ManipularGrillas.setColorFondoCeldaGrilla(self.grid_cargueVagonetas, dic_color)

        self.func_colorear_porcentaje_cubicaccion_mayor_102()


        self.grid_cargueVagonetas.AutoSizeColumns()

    def func_colorear_porcentaje_cubicaccion_mayor_102(self):
        filas = self.grid_cargueVagonetas.GetNumberRows()
        cubicacion = 0.0
        for i in range(filas):
            dato = self.grid_cargueVagonetas.GetCellValue(i, 1)
            if dato == '':
                dato = 0.0
            cubicacion = float()
            if cubicacion > 1.02:
                COLOR_ROSADO = wx.Colour(255, 206, 222)
                self.grid_cargueVagonetas.SetCellBackgroundColour(i, 1, COLOR_ROSADO)
            else:
                COLOR_GRIS = wx.Colour(240, 240, 240)
                self.grid_cargueVagonetas.SetCellBackgroundColour(i, 1, COLOR_GRIS)


    def guardar_listaRotura(self):

        nom_tabla = 'rotura_cargue_vagonetas'
        dic_campos = {
            'id_producto': 'int',
            'producto': 'str',
            'cant_rotos': 'int',
            'activo': 'str',
            'uuid': 'str'
        }

        cant_filas = self.grid_rotura.GetNumberRows()
        cant_columnas = (self.grid_rotura.GetNumberCols()) - 1  ## -1 Para no tener en cuenta la columna CHK
        list_valores = []

        if cant_filas < 1:
            return 0

        for i in range(cant_filas):
            list_fila = []
            for j in range(cant_columnas):
                dato = self.grid_rotura.GetCellValue(i, j)
                list_fila.append(dato.upper())
            list_fila.append(True)  # es para el campo Activo de la base de datos
            list_fila.append(self.uuid_eay)

            list_valores.append(list_fila)

        sSql_insert_rotura = GenerarSql.crearMultiInsertSql(nom_tabla, dic_campos, list_valores)

        rta_insert_rotura = Ejecutar_SQL.insert_filas(sSql_insert_rotura, 'frm_cargueVagonetas_funcion_guardar_listaRotura', BasesDeDatos.DB_PRINCIPAL)

        return rta_insert_rotura

    def cargar_valores_de_inicializacion(self):

        # self.txt_total_vagonetas.SetMaxLength(6)
        # self.txt_total_unidades.SetMaxLength(9)

        self.lbl_etq_total_unidades.Hide()
        self.lbl_etq_total_vagonetas.Hide()

        self.txt_total_vagonetas.Hide()
        self.txt_total_unidades.Hide()


        #self.txt_unidades_x_vagoneta.SetMaxLength(7)
        self.txt_tiempo_parada_minutos.SetMaxLength(4)

        self.puntero_fila_cargueVagoneta = 0
        self.puntero_fila_boquilla = 0
        self.puntero_fila_notas = 0
        self.puntero_fila_novedades = 0

        self.cargar_checkList_personal()

        self.limpiar_todas_las_grillas()

        self.set_configuracion_grillas()
        self.set_configuracion_botones()

        self.grid_cargueVagonetas.AutoSizeColumns()

    def set_configuracion_botones(self):
        from formEAY.constantesCAC.coloresCAC import Colors_botones
        colors_botones = Colors_botones()

        self.btn_guardar.SetBackgroundColour(colors_botones.ACEPTAR)
        # self.btn_guardar.SetForegroundColour(wx.WHITE)
        self.btn_guardar.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD))

        #self.btn_llenar_tabla.SetBackgroundColour(colors_botones.AGREGAR_A_LISTA)
        self.btn_a_lista_notas.SetBackgroundColour(colors_botones.AGREGAR_A_LISTA)
        self.btn_a_lista_novedades.SetBackgroundColour(colors_botones.AGREGAR_A_LISTA)
        self.btn_a_lista_unidadesRotas.SetBackgroundColour(colors_botones.AGREGAR_A_LISTA)

        self.btn_guardar.SetWindowStyleFlag(wx.NO_BORDER)
        #self.btn_llenar_tabla.SetWindowStyleFlag(wx.NO_BORDER)
        self.btn_a_lista_notas.SetWindowStyleFlag(wx.NO_BORDER)
        self.btn_a_lista_novedades.SetWindowStyleFlag(wx.NO_BORDER)
        self.btn_a_lista_unidadesRotas.SetWindowStyleFlag(wx.NO_BORDER)

        self.lbl_estado_guardar.SetLabel('')

    def set_configuracion_grillas(self):
        self.set_configuracion_grilla_cargueVagonetas()
        self.set_configuracion_grilla_rotura()
        self.set_configuracion_grilla_recesos()
        self.set_configuracion_grilla_novedades()
        self.set_configuracion_grilla_notas()
        self.set_configuracion_cabeceras_grillas()
        
    def set_configuracion_cabeceras_grillas(self):
        self.grid_cargueVagonetas.SetLabelBackgroundColour(wx.WHITE)
        self.grid_cargueVagonetas.SetLabelTextColour(wx.BLACK)

        self.grid_rotura.SetLabelBackgroundColour(wx.WHITE)
        self.grid_rotura.SetLabelTextColour(wx.BLACK)

        self.grid_recesos.SetLabelBackgroundColour(wx.WHITE)
        self.grid_recesos.SetLabelTextColour(wx.BLACK)

        self.grid_novedades.SetLabelBackgroundColour(wx.WHITE)
        self.grid_novedades.SetLabelTextColour(wx.BLACK)

        self.grid_notas.SetLabelBackgroundColour(wx.WHITE)
        self.grid_notas.SetLabelTextColour(wx.BLACK)

    def set_configuracion_grilla_notas(self):
        list_columnas = [0, 1, 2, 3]
        ManipularGrillas.setColumnasSoloLectura(self.grid_notas, list_columnas)

        list_columnas = [4]
        ManipularGrillas.setColumnasFormatoCHK(self.grid_notas, list_columnas)

    def set_configuracion_grilla_novedades(self):
        list_columnas = [0, 1, 2, 3]
        ManipularGrillas.setColumnasSoloLectura(self.grid_novedades, list_columnas)

        list_columnas = [4]
        ManipularGrillas.setColumnasFormatoCHK(self.grid_novedades, list_columnas)

    def set_configuracion_grilla_rotura(self):
        list_columnas = [0, 1, 2]
        ManipularGrillas.setColumnasSoloLectura(self.grid_rotura, list_columnas)

        list_columnas = [3]
        ManipularGrillas.setColumnasFormatoCHK(self.grid_rotura, list_columnas)

    def set_configuracion_grilla_cargueVagonetas(self):
        self.grid_cargueVagonetas.SetRowLabelSize(1)
        # list_columnas = [0, 1, 2]
        # ManipularGrillas.setColumnasSoloLectura(self.grid_cargueVagonetas, list_columnas)
        #
        # list_columnas = [4]
        # ManipularGrillas.setColumnasFormatoCHK(self.grid_cargueVagonetas, list_columnas)

        list_columnas = [3]
        ManipularGrillas.setColumnasSoloNumeros(self.grid_cargueVagonetas, list_columnas)

    def set_configuracion_grilla_recesos(self):
        list_columnas = [0, 1]
        ManipularGrillas.setColumnasSoloLectura(self.grid_recesos, list_columnas)
        list_columnas = [2]
        ManipularGrillas.setColumnasSoloNumeros(self.grid_recesos, list_columnas)

    def limpiar_todas_las_grillas(self):
        self.puntero_fila_cargueVagoneta = ManipularGrillas.limpiarGrilla(self.grid_cargueVagonetas)
        self.puntero_fila_rotura = ManipularGrillas.limpiarGrilla(self.grid_rotura)
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
        rows = DbGetVarios.listaContextoNota(True)
        # id_contexto_nota, nom_contexto

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.dic_contexto_nota = ManipularRows.crearDiccionario(rows, 1, 0)
            self.comboBox_contexto.Set(la_lista)

    def cargar_combo_productos(self):
        from formEAY.dbaseCAC.dbProductos import Get_productos

        cant_registros = 500
        rows = Get_productos.listaBasica(cant_registros, True)

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.dic_cargueVagonetas = ManipularRows.crearDiccionario(rows, 1, 0)
            #self.comboBox_producto.Set(la_lista)
            self.comboBox_producto_roto.Set(la_lista)

    def cargar_combo_turnos(self):
        obj_formato = ManipularRows()

        rows = DbGetVarios.listaTurnos(self.AREA_PRODUCCION, True)
        # id_turno, nom_turno, hora_inicio, hora_salida, activo

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.dic_turnos_todos = ManipularRows.crearDiccionarioTodosLosCampos(rows, 1)
            self.comboBox_turno.Set(la_lista)

    def cargar_combo_vagonetas(self):
        rows = DbGetVarios.listaVagonetas(True)
        # id_vagoneta, nom_vagoneta

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.dic_vagonetas = ManipularRows.crearDiccionario(rows, 1, 0)
            self.comboBox_vagoneta.Set(la_lista)

    def cargar_checkList_personal(self):
        from formEAY.dbaseCAC.dbEmpleados import Get_empleados

        rows = Get_empleados.lista_basica(self.AREA_PRODUCCION)

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.diccionario_personal = ManipularRows.crearDiccionario(rows, 1, 0)
            self.checkList_personal.Set(la_lista)

    def calcular_totales_grilla_extrusion(self):
        """

        :return:  total_vagonetas, total_unidades
        """
        cant_filas = self.grid_cargueVagonetas.GetNumberRows()
        cant_cols = self.grid_cargueVagonetas.GetNumberCols()

        total_unidades = 0
        for i in range(cant_filas):
            for j in range(2, cant_cols):
                dato = self.grid_cargueVagonetas.GetCellValue(i, j)
                if dato == '':
                    dato = 0
                else:
                    total_unidades += int(dato)

        total_vagonetas = cant_filas

        return total_vagonetas, total_unidades


