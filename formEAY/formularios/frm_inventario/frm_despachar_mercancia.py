# -*- coding: utf-8 -*-

import wx
import wx.grid
import wx.xrc
import os
import time
import pandas as pd
from uuid import uuid4

from pyeay.validator import validador_solo_digitos
from pyeay.dbcac.conexiondb import Ejecutar_SQL, GenerarSql
from pyeay.rows import ManipularRows
from pyeay.grillas import ManipularGrillas
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

from formEAY.constantesCAC.imgCAC import Img_grillas, Img_formularios_general

MORADO = wx.Colour(212, 206, 241)  ##ColorsFondoCellGrilla.RESALTE_ROSA
OLIVA = wx.Colour(231, 231, 171)
LILA = wx.Colour(230, 206, 232)


###########################################################################
## Class DespacharMercancia
###########################################################################

class DespacharMercancia(wx.Frame):

    def __init__(self, parent, usuario='usuario1', dir_mac='la dir mac del pc'):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Despachar Mercancia", pos=wx.DefaultPosition,
                          size=wx.Size(927, 689), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(700, 600), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.usuario = usuario
        self.dir_mac = dir_mac
        self.rows = []

        self.id_cliente = -1
        self.uuid_eay = uuid4()

        icono_grillas = Img_grillas()
        icono_formularios = Img_formularios_general()

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer_panel_principal = wx.BoxSizer(wx.VERTICAL)

        bSizer21 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel4.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer23 = wx.BoxSizer(wx.VERTICAL)

        bSizer_cliente = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_buscar_nit = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_buscar_cliente = wx.BitmapButton(self.m_panel4, wx.ID_ANY,
                                                  wx.Bitmap(icono_formularios.BUSCAR_CLIENTE,
                                                            wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                                  wx.BU_AUTODRAW | wx.NO_BORDER)

        self.btn_buscar_cliente.SetBitmapCurrent(
            wx.Bitmap(icono_formularios.BUSCAR_CLIENTE_SEL, wx.BITMAP_TYPE_ANY))
        self.btn_buscar_cliente.SetToolTip(u"Buscar Cliente")

        bSizer_buscar_nit.Add(self.btn_buscar_cliente, 0, wx.ALL, 5)

        self.searchCtrl_nit_cliente = wx.SearchCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                    wx.DefaultSize, wx.TE_PROCESS_ENTER)
        self.searchCtrl_nit_cliente.ShowSearchButton(True)
        self.searchCtrl_nit_cliente.ShowCancelButton(True)
        bSizer_buscar_nit.Add(self.searchCtrl_nit_cliente, 0, wx.ALL, 5)

        bSizer_cliente.Add(bSizer_buscar_nit, 0, wx.EXPAND, 5)

        bSizer_datos_cliente = wx.BoxSizer(wx.VERTICAL)

        bSizer_razon_social = wx.BoxSizer(wx.VERTICAL)

        self.lbl_razon_social = wx.StaticText(self.m_panel4, wx.ID_ANY, u"", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_razon_social.Wrap(-1)
        self.lbl_razon_social.SetFont(wx.Font(11, 70, 90, 92, False, wx.EmptyString))
        self.lbl_razon_social.SetForegroundColour(wx.Colour(191, 0, 96))

        bSizer_razon_social.Add(self.lbl_razon_social, 0, wx.ALL, 5)

        bSizer_datos_cliente.Add(bSizer_razon_social, 1, wx.EXPAND, 5)

        bSizer_nom_cliente = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_nombre = wx.StaticText(self.m_panel4, wx.ID_ANY, u"", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.lbl_nombre.Wrap(-1)
        self.lbl_nombre.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer_nom_cliente.Add(self.lbl_nombre, 1, wx.ALL, 5)

        self.lbl_etq_nit = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Nit:", wx.DefaultPosition, wx.Size(50, -1),
                                         wx.ALIGN_RIGHT)
        self.lbl_etq_nit.Wrap(-1)
        bSizer_nom_cliente.Add(self.lbl_etq_nit, 0, wx.ALL, 5)

        self.lbl_nit = wx.StaticText(self.m_panel4, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size(110, -1), 0)
        self.lbl_nit.Wrap(-1)
        self.lbl_nit.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer_nom_cliente.Add(self.lbl_nit, 0, wx.ALL, 5)

        bSizer_datos_cliente.Add(bSizer_nom_cliente, 0, wx.EXPAND, 5)

        bSizer_dir = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_dir = wx.StaticText(self.m_panel4, wx.ID_ANY, u"", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.lbl_dir.Wrap(-1)
        bSizer_dir.Add(self.lbl_dir, 1, wx.ALL, 5)

        self.lbl_etq_celular_cliente = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Celular:", wx.DefaultPosition,
                                                     wx.Size(50, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_celular_cliente.Wrap(-1)
        bSizer_dir.Add(self.lbl_etq_celular_cliente, 0, wx.ALL, 5)

        self.lbl_celular_cliente = wx.StaticText(self.m_panel4, wx.ID_ANY, u"", wx.DefaultPosition,
                                                 wx.Size(110, -1), 0)
        self.lbl_celular_cliente.Wrap(-1)
        bSizer_dir.Add(self.lbl_celular_cliente, 0, wx.ALL, 5)

        bSizer_datos_cliente.Add(bSizer_dir, 1, wx.EXPAND, 5)

        bSizer_cliente.Add(bSizer_datos_cliente, 1, wx.EXPAND, 5)

        bSizer23.Add(bSizer_cliente, 0, wx.EXPAND, 5)

        bSizer_quien_recibe = wx.BoxSizer(wx.VERTICAL)

        bSizer_datos_quien_recibe = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_quien_recibe = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Quien Recibe:", wx.DefaultPosition,
                                                  wx.Size(105, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_quien_recibe.Wrap(-1)
        bSizer_datos_quien_recibe.Add(self.lbl_etq_quien_recibe, 0, wx.ALL, 5)

        self.txt_quien_recibe = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bSizer_datos_quien_recibe.Add(self.txt_quien_recibe, 1, wx.ALL, 5)

        self.lbl_etq_celular_recibe = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Celular:", wx.DefaultPosition,
                                                    wx.Size(50, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_celular_recibe.Wrap(-1)
        bSizer_datos_quien_recibe.Add(self.lbl_etq_celular_recibe, 0, wx.ALL, 5)

        self.txt_celular_recibe = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.Size(110, -1), 0)
        bSizer_datos_quien_recibe.Add(self.txt_celular_recibe, 0, wx.ALL, 5)

        bSizer_quien_recibe.Add(bSizer_datos_quien_recibe, 0, wx.EXPAND, 5)

        bSizer_tipo_carro = wx.BoxSizer(wx.VERTICAL)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_tipo_carro = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Tipo Carro:", wx.DefaultPosition,
                                                wx.Size(105, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_tipo_carro.Wrap(-1)
        bSizer14.Add(self.lbl_etq_tipo_carro, 0, wx.ALL, 5)

        comboBox_tipo_carroChoices = [u"CAMION", u"VOLQUETA", u"CAMIONETA", u"FURGON", u"TRACTOCAMION"]
        self.comboBox_tipo_carro = wx.ComboBox(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.Size(130, -1), comboBox_tipo_carroChoices,
                                               wx.CB_READONLY | wx.CB_SORT)
        bSizer14.Add(self.comboBox_tipo_carro, 0, wx.ALL, 5)

        self.lbl_etq_color = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Color:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_color.Wrap(-1)
        bSizer14.Add(self.lbl_etq_color, 0, wx.ALL, 5)

        self.txt_color = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer14.Add(self.txt_color, 1, wx.ALL, 5)

        self.lbl_etq_placa = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Placa:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_placa.Wrap(-1)
        bSizer14.Add(self.lbl_etq_placa, 0, wx.ALL, 5)

        self.txt_placa = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), 0)
        bSizer14.Add(self.txt_placa, 0, wx.ALL, 5)

        self.lbl_etq_nacionalidad = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Nacionalidad:", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.lbl_etq_nacionalidad.Wrap(-1)
        bSizer14.Add(self.lbl_etq_nacionalidad, 0, wx.ALL, 5)

        comboBox_nacionalidadChoices = [u"COLOMBIA", u"VENEZUELA"]
        self.comboBox_nacionalidad = wx.ComboBox(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                 wx.DefaultSize, comboBox_nacionalidadChoices, wx.CB_READONLY)
        bSizer14.Add(self.comboBox_nacionalidad, 0, wx.ALL, 5)

        self.lbl_ciudad = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Ciudad:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_ciudad.Wrap(-1)
        bSizer14.Add(self.lbl_ciudad, 0, wx.ALL, 5)

        self.txt_ciudad = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(140, -1), 0)
        bSizer14.Add(self.txt_ciudad, 1, wx.ALL, 5)

        bSizer_tipo_carro.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer_quien_recibe.Add(bSizer_tipo_carro, 1, wx.EXPAND, 5)

        bSizer23.Add(bSizer_quien_recibe, 0, wx.EXPAND, 5)

        self.m_panel4.SetSizer(bSizer23)
        self.m_panel4.Layout()
        bSizer23.Fit(self.m_panel4)
        bSizer21.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        bSizer_panel_principal.Add(bSizer21, 0, wx.EXPAND, 5)

        bSizer_venta = wx.BoxSizer(wx.VERTICAL)

        self.panel_grilla = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel_grilla.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer141 = wx.BoxSizer(wx.VERTICAL)

        bSizer_origen_venta = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_origen_venta = wx.StaticText(self.panel_grilla, wx.ID_ANY, u"Origen Venta:", wx.DefaultPosition,
                                                  wx.Size(100, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_origen_venta.Wrap(-1)
        bSizer_origen_venta.Add(self.lbl_etq_origen_venta, 0, wx.ALL, 5)

        comboBox_origen_ventaChoices = [u"FERRETERIA", u"TEJAR"]
        self.comboBox_origen_venta = wx.ComboBox(self.panel_grilla, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                                 wx.Size(130, -1), comboBox_origen_ventaChoices, wx.CB_READONLY)
        bSizer_origen_venta.Add(self.comboBox_origen_venta, 0, wx.ALL, 5)

        self.lbl_etq_documento_ralacionado = wx.StaticText(self.panel_grilla, wx.ID_ANY, u"Documento Relacionado:",
                                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_documento_ralacionado.Wrap(-1)
        bSizer_origen_venta.Add(self.lbl_etq_documento_ralacionado, 0, wx.ALL, 5)

        self.txt_doc_relacionado = wx.TextCtrl(self.panel_grilla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        bSizer_origen_venta.Add(self.txt_doc_relacionado, 0, wx.ALL, 5)

        bSizer141.Add(bSizer_origen_venta, 0, wx.EXPAND, 5)

        bSizer_seleccionar_producto = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_calidad_producto = wx.StaticText(self.panel_grilla, wx.ID_ANY, u"Calidad Producto:",
                                                      wx.DefaultPosition, wx.Size(100, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_calidad_producto.Wrap(-1)
        bSizer_seleccionar_producto.Add(self.lbl_etq_calidad_producto, 0, wx.ALL, 5)

        comboBox_calidad_productoChoices = [u"PRIMERA", u"SEGUNDA"]
        self.comboBox_calidad_producto = wx.ComboBox(self.panel_grilla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                     wx.Size(130, -1), comboBox_calidad_productoChoices, wx.CB_READONLY)
        bSizer_seleccionar_producto.Add(self.comboBox_calidad_producto, 0, wx.ALL, 5)

        self.lbl_etq_producto = wx.StaticText(self.panel_grilla, wx.ID_ANY, u"Producto:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_etq_producto.Wrap(-1)
        bSizer_seleccionar_producto.Add(self.lbl_etq_producto, 0, wx.ALL, 5)

        comboBox_productoChoices = []
        self.comboBox_producto = wx.ComboBox(self.panel_grilla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(300, -1), comboBox_productoChoices, wx.CB_READONLY)
        bSizer_seleccionar_producto.Add(self.comboBox_producto, 0, wx.ALL, 5)

        self.lbl_etq_cantidad = wx.StaticText(self.panel_grilla, wx.ID_ANY, u"Cantidad:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_etq_cantidad.Wrap(-1)
        bSizer_seleccionar_producto.Add(self.lbl_etq_cantidad, 0, wx.ALL, 5)

        self.txt_cantidad = wx.TextCtrl(self.panel_grilla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, validator=validador_solo_digitos())
        bSizer_seleccionar_producto.Add(self.txt_cantidad, 0, wx.ALL, 5)

        self.btn_a_lista = wx.BitmapButton(self.panel_grilla, wx.ID_ANY,
                                           wx.Bitmap(icono_formularios.A_LISTA,
                                                     wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW | wx.NO_BORDER)

        self.btn_a_lista.SetBitmapCurrent(
            wx.Bitmap(icono_formularios.A_LISTA_SEL, wx.BITMAP_TYPE_ANY))

        self.btn_a_lista.SetToolTip(u"Agregar producto a la Lista")

        bSizer_seleccionar_producto.Add(self.btn_a_lista, 0, wx.ALL, 5)

        bSizer141.Add(bSizer_seleccionar_producto, 0, wx.EXPAND, 5)

        bSizer_grilla = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_editar_grilla = wx.BoxSizer(wx.VERTICAL)

        self.btn_eliminar_item_seleccionado_grid = wx.BitmapButton(self.panel_grilla, wx.ID_ANY, wx.Bitmap(
            icono_grillas.ELIMINAR_ITEM_SELECIONADO, wx.BITMAP_TYPE_ANY),
                                                                   wx.DefaultPosition, wx.DefaultSize,
                                                                   wx.BU_AUTODRAW | wx.NO_BORDER)

        self.btn_eliminar_item_seleccionado_grid.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.ELIMINAR_ITEM_SELECIONADO_SEL, wx.BITMAP_TYPE_ANY))
        self.btn_eliminar_item_seleccionado_grid.SetToolTip(u"Elimina items Seleccionados")

        bSizer_editar_grilla.Add(self.btn_eliminar_item_seleccionado_grid, 0, wx.ALL, 5)

        self.btn_deseleccionar_todo_grid = wx.BitmapButton(self.panel_grilla, wx.ID_ANY, wx.Bitmap(
            icono_grillas.DESELECCIONAR_TODO, wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                           wx.DefaultSize, wx.BU_AUTODRAW | wx.NO_BORDER)

        self.btn_deseleccionar_todo_grid.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
        self.btn_deseleccionar_todo_grid.SetToolTip(u"Deselecciona los items seleccionados")

        bSizer_editar_grilla.Add(self.btn_deseleccionar_todo_grid, 0, wx.ALL, 5)

        self.btn_limpiar_grid = wx.BitmapButton(self.panel_grilla, wx.ID_ANY,
                                                wx.Bitmap(icono_grillas.LIMPIAR_GRILLA,
                                                          wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                                wx.BU_AUTODRAW | wx.NO_BORDER)

        self.btn_limpiar_grid.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.LIMPIAR_GRILLA_SEL, wx.BITMAP_TYPE_ANY))
        self.btn_limpiar_grid.SetToolTip(u"Limpiar Lista")

        bSizer_editar_grilla.Add(self.btn_limpiar_grid, 0, wx.ALL, 5)

        bSizer_grilla.Add(bSizer_editar_grilla, 0, wx.EXPAND, 5)

        self.grid_productos = wx.grid.Grid(self.panel_grilla, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_productos.CreateGrid(0, 9)
        self.grid_productos.EnableEditing(True)
        self.grid_productos.EnableGridLines(True)
        self.grid_productos.SetGridLineColour(wx.Colour(224, 224, 224))
        self.grid_productos.EnableDragGridSize(False)
        self.grid_productos.SetMargins(0, 0)

        # Columns
        self.grid_productos.AutoSizeColumns()
        self.grid_productos.EnableDragColMove(False)
        self.grid_productos.EnableDragColSize(True)
        self.grid_productos.SetColLabelSize(30)
        self.grid_productos.SetColLabelValue(0, u"id")
        self.grid_productos.SetColLabelValue(1, u"Producto")
        self.grid_productos.SetColLabelValue(2, u"Calidad")
        self.grid_productos.SetColLabelValue(3, u"Cant")
        self.grid_productos.SetColLabelValue(4, u"Peso Ton")
        self.grid_productos.SetColLabelValue(5, u"Volumen m3")

        self.grid_productos.SetColLabelValue(6, u"cant primera")
        self.grid_productos.SetColLabelValue(7, u"cant_segunda")
        self.grid_productos.SetColLabelValue(8, u"Sel")

        self.grid_productos.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_productos.EnableDragRowSize(True)
        self.grid_productos.SetRowLabelSize(50)
        self.grid_productos.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_productos.SetLabelBackgroundColour(wx.Colour(255, 255, 255))
        self.grid_productos.SetLabelTextColour(wx.Colour(0, 0, 0))  # (128, 0, 64)

        # Cell Defaults
        self.grid_productos.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer_grilla.Add(self.grid_productos, 1, wx.ALL | wx.EXPAND, 5)

        bSizer141.Add(bSizer_grilla, 1, wx.EXPAND, 5)

        bSizer_nota = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_nota = wx.StaticText(self.panel_grilla, wx.ID_ANY, u"Nota:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_nota.Wrap(-1)
        bSizer_nota.Add(self.lbl_etq_nota, 0, wx.ALL, 5)

        self.txt_nota = wx.TextCtrl(self.panel_grilla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_nota.Add(self.txt_nota, 1, wx.ALL, 5)

        bSizer141.Add(bSizer_nota, 0, wx.EXPAND, 5)

        self.panel_grilla.SetSizer(bSizer141)
        self.panel_grilla.Layout()
        bSizer141.Fit(self.panel_grilla)
        bSizer_venta.Add(self.panel_grilla, 1, wx.EXPAND | wx.ALL, 5)

        bSizer_panel_principal.Add(bSizer_venta, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer_panel_principal, 1, wx.EXPAND, 5)

        bSizer_pie_pagina = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_total_unidades = wx.StaticText(self, wx.ID_ANY, u"Total Unidades:", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.lbl_etq_total_unidades.Wrap(-1)
        bSizer_pie_pagina.Add(self.lbl_etq_total_unidades, 0, wx.ALL, 5)

        self.lbl_total_unidades = wx.StaticText(self, wx.ID_ANY, u"25698", wx.DefaultPosition, wx.Size(100, -1), 0)
        self.lbl_total_unidades.Wrap(-1)
        self.lbl_total_unidades.SetForegroundColour(wx.Colour(128, 0, 64))

        bSizer_pie_pagina.Add(self.lbl_total_unidades, 0, wx.ALL, 5)

        self.lbl_etq_toneladas = wx.StaticText(self, wx.ID_ANY, u"Toneladas:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_toneladas.Wrap(-1)
        bSizer_pie_pagina.Add(self.lbl_etq_toneladas, 0, wx.ALL, 5)

        self.lbl_toneladas = wx.StaticText(self, wx.ID_ANY, u"25698", wx.DefaultPosition, wx.Size(100, -1), 0)
        self.lbl_toneladas.Wrap(-1)
        self.lbl_toneladas.SetForegroundColour(wx.Colour(128, 0, 64))

        bSizer_pie_pagina.Add(self.lbl_toneladas, 0, wx.ALL, 5)

        self.lbl_etq_volumen = wx.StaticText(self, wx.ID_ANY, u"Volumen (m3):", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_volumen.Wrap(-1)
        bSizer_pie_pagina.Add(self.lbl_etq_volumen, 0, wx.ALL, 5)

        self.lbl_volumen = wx.StaticText(self, wx.ID_ANY, u"25698", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_volumen.Wrap(-1)
        self.lbl_volumen.SetForegroundColour(wx.Colour(128, 0, 64))

        bSizer_pie_pagina.Add(self.lbl_volumen, 1, wx.ALL, 5)

        ##____________________________________________________________
        self.lbl_estado_guardar = wx.StaticText(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_estado_guardar.Wrap(-1)
        self.lbl_estado_guardar.SetForegroundColour(wx.Colour(128, 0, 64))

        bSizer_pie_pagina.Add(self.lbl_estado_guardar, 1, wx.ALL, 5)



        self.btn_guardar = wx.Button(self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.btn_guardar.SetBackgroundColour(wx.Colour(119, 255, 187))

        bSizer_pie_pagina.Add(self.btn_guardar, 0, wx.ALL, 5)

        bSizer1.Add(bSizer_pie_pagina, 0, wx.EXPAND, 5)

        ## VALORES INICIALES EAY
        self.func_valores_iniciales()

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_buscar_cliente.Bind(wx.EVT_BUTTON, self.btn_buscar_clienteOnButtonClick)
        self.btn_a_lista.Bind(wx.EVT_BUTTON, self.btn_a_listaOnButtonClick)
        self.btn_guardar.Bind(wx.EVT_BUTTON, self.btn_guardarOnButtonClick)
        self.btn_eliminar_item_seleccionado_grid.Bind(wx.EVT_BUTTON,
                                                      self.btn_eliminar_item_seleccionado_gridOnButtonClick)
        self.btn_deseleccionar_todo_grid.Bind(wx.EVT_BUTTON,
                                              self.btn_deseleccionar_todo_gridOnButtonClick)
        self.btn_limpiar_grid.Bind(wx.EVT_BUTTON,
                                   self.btn_limpiar_gridOnButtonClick)

        self.searchCtrl_nit_cliente.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.searchCtrl_nit_clienteOnSearchButton)
        self.searchCtrl_nit_cliente.Bind(wx.EVT_TEXT_ENTER, self.searchCtrl_nit_clienteOnTextEnter)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def searchCtrl_nit_clienteOnSearchButton(self, event):
        nit = self.searchCtrl_nit_cliente.GetValue()
        self.buscar_cliente_por_nit_o_celular(nit)
        event.Skip()

    def searchCtrl_nit_clienteOnTextEnter(self, event):
        nit = self.searchCtrl_nit_cliente.GetValue()
        self.buscar_cliente_por_nit_o_celular(nit)
        event.Skip()

    def btn_buscar_clienteOnButtonClick(self, event):
        import formEAY.formularios.frm_generales.frm_buscarCliente as frm_buscarCliente
        frame_BuscarCliente = frm_buscarCliente.BuscarCliente(self)
        frame_BuscarCliente.Center()
        frame_BuscarCliente.Show()
        event.Skip()

    def btn_a_listaOnButtonClick(self, event):
        # formato_numeros = FormatearNumeros()

        calidad = self.comboBox_calidad_producto.GetValue()
        if calidad == '':
            wx.MessageBox(u'Debes seleccionar un Tipo de calidad', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        producto = self.comboBox_producto.GetValue()
        if producto == '':
            wx.MessageBox(u'Debes seleccionar un Producto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        cantidad = self.txt_cantidad.GetValue()
        if cantidad == '' or cantidad == '0':
            wx.MessageBox(u'Debes ingresar una cantidad valida', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if calidad == 'PRIMERA':
            cant_primera = int(cantidad)
            cant_segunda = 0
        if calidad == 'SEGUNDA':
            cant_segunda = int(cantidad)
            cant_primera = 0

        id_producto = self.dic_productos[producto][0]

        peso_unit_ton = round(self.dic_productos[producto][2] * int(cantidad), 2)
        volumen_unit_m3 = round(self.dic_productos[producto][3] * int(cantidad), 2)

        row = [id_producto, producto, calidad, cantidad, peso_unit_ton, volumen_unit_m3, cant_primera, cant_segunda]

        self.puntero_fila_producto = ManipularGrillas.nuevaFilaGrilla(self.grid_productos, row,
                                                                      self.puntero_fila_producto)

        dic_color = {3: MORADO, 4: OLIVA, 5: LILA}
        ManipularGrillas.setColorFondoCeldaGrilla(self.grid_productos, dic_color)

        self.calcular_totales()

        event.Skip()

    def btn_guardarOnButtonClick(self, event):

        rta = self.func_validar_entrada_datos()
        if rta == 0:
            return 0
        else:
            self.btn_guardar.Hide()

            self.lbl_estado_guardar.SetLabel('1/3  Estamos guardando, el proceso puede tardar unos segundos...')
            rta1 = self.func_guardar_cabecera_despacho()
            self.lbl_estado_guardar.SetLabel('2/3  Estamos guardando, el proceso puede tardar unos segundos...')
            rta2 = self.func_guardar_items_despacho()
            self.lbl_estado_guardar.SetLabel('3/3  Estamos guardando, el proceso puede tardar unos segundos...')
            rta3 = self.func_actualizar_stock_productos()

            self.func_imprimir_orden_servicio()

            if rta1 == 1 and rta2 == 1 and rta3 == 1:
                mensaje = u'El proceso se llevo a cabo correctamente, Desea Imprimir?'

                dlg = wx.MessageDialog(None, mensaje,
                                       u'Atención...',
                                       wx.YES_NO | wx.ICON_QUESTION)
                retCode = dlg.ShowModal()
                if (retCode == wx.ID_YES):  # PARA MANDAR A IMPRIMIR
                    os.startfile('despachoMercancia.pdf', 'print')
                    time.sleep(1)  # pause 0.5 seconds
                    os.remove("despachoMercancia.pdf")
                else:
                    os.startfile('despachoMercancia.pdf')

                self.Destroy()

                return 0

        event.Skip()

    def btn_limpiar_gridOnButtonClick(self, event):
        self.puntero_fila_producto = ManipularGrillas.limpiarGrilla(self.grid_productos)
        self.lbl_total_unidades.SetLabel(str(0))
        self.lbl_toneladas.SetLabel(str(0))
        self.lbl_volumen.SetLabel(str(0))
        event.Skip()

    def btn_eliminar_item_seleccionado_gridOnButtonClick(self, event):
        col_verificacion = 8
        self.puntero_fila_producto = ManipularGrillas.delFilasCHK(self.grid_productos, col_verificacion)

        dic_color = {3: MORADO, 4: OLIVA, 5: LILA}
        ManipularGrillas.setColorFondoCeldaGrilla(self.grid_productos, dic_color)

        self.calcular_totales()

        event.Skip()

    def btn_deseleccionar_todo_gridOnButtonClick(self, event):
        col_verificacion = 8
        ManipularGrillas.deseleccionarFilasCHK(self.grid_productos, col_verificacion)
        event.Skip()

    ## FUNCIONES EAY

    def func_padreEayBuscarCliente(self, el_id, lista_valores):
        #lista_valores = [nom, ape1, ape2, nit, razon_social, dir, ciudad, celular]
        nom_completo = lista_valores[0] + ' ' + lista_valores[1] + ' ' + lista_valores[2]
        dir_completa = lista_valores[5] + ' ' + lista_valores[6]

        self.id_cliente = el_id
        self.lbl_nombre.SetLabel(nom_completo)
        self.lbl_razon_social.SetLabel(lista_valores[4])
        self.lbl_nit.SetLabel(lista_valores[3])
        self.lbl_dir.SetLabel(dir_completa)
        self.lbl_celular_cliente.SetLabel(lista_valores[7])




    def func_get_num_orden_despacho(self):
        sSql = """
                    SELECT MAX(id_despacho)
                    FROM despacho_mercancia
                    WHERE activo = 'True'
        """
        cabeceras = []

        row = Ejecutar_SQL.select_un_registro(sSql, 'frm_despachar_mercancia/func_get_num_orden_despacho', BasesDeDatos.DB_PRINCIPAL)

        return row[0]

    def func_imprimir_orden_servicio(self):
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        num_orden_servicio = self.func_get_num_orden_despacho()

        IMG_CABECERA = Img_formularios_general.CABECERA_ORDEN_SERVICIO
        IMG_PIE_PAGINA = Img_formularios_general.PIE_DE_PAGINA_ORDEN_SERVICIO

        ## carta = (612.0, 792.0)

        ajuste_y = 396

        c = canvas.Canvas("despachoMercancia.pdf", pagesize=letter)

        w, h = letter

        MARGEN_IZQ = 70

        CANT_FILAS_POR_HOJA = 11
        cant_filas_rows = len(self.rows)


        cant_hojas = cant_filas_rows // CANT_FILAS_POR_HOJA

        if cant_filas_rows // CANT_FILAS_POR_HOJA > 0:

            if cant_filas_rows > (cant_hojas * CANT_FILAS_POR_HOJA):
                cant_hojas += 1
        else:
            if cant_filas_rows < CANT_FILAS_POR_HOJA:
                cant_hojas += 1

        list_rangos = []
        for i in range(CANT_FILAS_POR_HOJA, cant_filas_rows + 1, CANT_FILAS_POR_HOJA):
            list_rangos.append(i)

        if cant_filas_rows < CANT_FILAS_POR_HOJA:
            list_rangos.append(cant_filas_rows)
        else:
            if cant_filas_rows % CANT_FILAS_POR_HOJA > 0:
                list_rangos.append(cant_filas_rows)


        for hoja in range(cant_hojas):

            c.drawImage(IMG_CABECERA, MARGEN_IZQ, h - 78, width=502, height=63)   #, width=50, height=50)

            c.drawImage(IMG_PIE_PAGINA, MARGEN_IZQ, 30 + ajuste_y + 20, width=502, height=48)  # , width=50, height=50)

            #---------------------------------------------------------
            razon_social = self.lbl_razon_social.GetLabel()
            nit = self.lbl_nit.GetLabel()
            dir = self.lbl_dir.GetLabel()
            cel = self.lbl_celular_cliente.GetLabel()

            quien_recibe = self.txt_quien_recibe.GetValue()
            celular_recibe = self.txt_celular_recibe.GetValue()
            tipo_carro = self.comboBox_tipo_carro.GetValue()
            color = self.txt_color.GetValue()
            placa = self.txt_placa.GetValue()
            nacionalidad = self.comboBox_nacionalidad.GetValue()
            ciudad_carro = self.txt_ciudad.GetValue()

            #////////////////////
            text = c.beginText(365, h - 80)
            text.setFont("Courier-Bold", 10)
            cad_orden = 'Orden de servicio: '
            text.textLine(cad_orden)
            c.drawText(text)

            text = c.beginText(425 + MARGEN_IZQ, h - 80)
            text.setFont("Courier-Bold", 12)
            text.setFillColorRGB(1, 0, 0)
            cad_orden = str(num_orden_servicio)
            text.textLine(cad_orden)
            c.drawText(text)
            #////////////////////

            text = c.beginText(MARGEN_IZQ, h - 105)
            text.setFont("Courier-Bold", 10)
            text.setFillColorRGB(0, 0, 0)

            cad_nomCliente = ''.ljust(9) + razon_social.ljust(51) + ''.rjust(10) + nit.ljust(12)
            text.textLine(cad_nomCliente)
            cad_dir =  dir.ljust(60) + ''.rjust(10) + cel.ljust(12)
            text.textLine(cad_dir)
            c.drawText(text)

            text = c.beginText(MARGEN_IZQ, h - 105)
            text.setFont("Courier", 10)

            cad_nomCliente = 'Cliente:'.ljust(9) + ''.ljust(49) + 'Nit: '.rjust(10)
            text.textLine(cad_nomCliente)
            cad_dir = ''.ljust(58) + 'Celular: '.rjust(10)
            text.textLine(cad_dir)
            c.drawText(text)

            text.setFont("Courier", 8)

            cad_transporte = 'Transporte: ' + quien_recibe + ' - ' + tipo_carro + ': ' + color + '  Placa: ' + placa + ' ' + \
                             ciudad_carro + ' ' + nacionalidad
            cad_transporte = cad_transporte.upper()

            text.textLine(cad_transporte)
            c.drawText(text)

            # ---------------------------------------------------------

            text = c.beginText(MARGEN_IZQ, h - 147)
            text.setFont("Courier-Bold", 10)
            cad_cabecera = '%-12s     %-50s  %-30s' % ('Cant', 'Producto', 'Calidad')
            text.textLine(cad_cabecera)
            c.drawText(text)

            c.setStrokeColorRGB(0.678, 0.78, 0.811)
            c.line(MARGEN_IZQ, h - 155, 545, h - 155)

            text = c.beginText(MARGEN_IZQ, h - 170)
            text.setFont("Courier", 10)



            for i in range((hoja) * 12,  list_rangos[hoja], 1):
                fila = self.rows[i]

                cant = fila[3]
                if cant == '0':
                    cant = fila[4]
                producto = fila[1]
                calidad = fila[2]

                cad_fila = '%-12s     %-50s  %-30s' % (cant, producto, calidad)

                text.textLine(cad_fila)

            c.drawText(text)

            text = c.beginText((w/2)-10, ajuste_y + 48)
            text.setFont("Courier", 8)
            num_pagina = ' pagina ' + str((hoja+1)) + '/' + str(cant_hojas)
            text.textLine(num_pagina)
            c.drawText(text)

            c.showPage()
        #....................................................................

        c.save()



    def func_crear_datafreme_producto(self):
        cant_filas = self.grid_productos.GetNumberRows()
        datos = []
        fila = []

        for i in range(cant_filas):
            for j in [0, 6, 7]:  ## numero de columna
                if j in [6, 7]:
                    fila.append(int(self.grid_productos.GetCellValue(i, j)))
                if j in [0, ]:
                    fila.append(self.grid_productos.GetCellValue(i, j))
            datos.append(fila)
            fila = []

        df = pd.DataFrame(datos,
                          columns=['id', 'cant_1ra', 'cant_2da']
                          )
        df= df.groupby(['id']).sum()
        #df = df.sort_values(['producto', 'calidad'])

        rows = df.to_records().tolist()



        return rows

    def func_actualizar_stock_productos(self):

        rows = self.func_crear_datafreme_producto()

        nom_tabla = 'producto'
        cols_busqueda = [0]
        cols_a_modificar = [1, 2]

        dic_operaciones = {'stock_primera':'stock_primera - ', 'stock_segunda':'stock_segunda - '}

        nom_campos = ['id_producto', 'stock_primera', 'stock_segunda']
        tipo_campos = ['int', 'int', 'int']

        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows, cols_busqueda, cols_a_modificar, nom_campos,
                                                          tipo_campos, dic_operaciones)

        rta = Ejecutar_SQL.insert_filas(sSql, 'frm_despachar_mercancia/func_actualizar_stock_productos', BasesDeDatos.DB_PRINCIPAL)

        return rta


    def func_guardar_items_despacho(self):

        cant_filas = self.grid_productos.GetNumberRows()
        fila = []
        self.rows = []

        for i in range(cant_filas):
            fila = []
            for j in [0, 1, 2, 6, 7]:
                fila.append(self.grid_productos.GetCellValue(i, j))
            fila.append(str(self.uuid_eay))
            self.rows.append(fila)

        nom_tabla = 'detalle_despacho'
        dic_campos = {'id_producto': 'int', 'producto':'str', 'calidad':'str', 'cant_primera':'int', 'cant_segunda':'int',
                      'uuid':'str'}
        sSql = GenerarSql.crearMultiInsertSql(nom_tabla, dic_campos, self.rows)

        rta = Ejecutar_SQL.insert_filas(sSql.upper(), 'frm_despachar_mercancia/func_guardar_items_despacho', BasesDeDatos.DB_PRINCIPAL)
        return rta

    def func_guardar_cabecera_despacho(self):
        from formEAY.utilCAC.Utiles_proposito_general import ManejoFechasHoras

        fecha, hora = ManejoFechasHoras.getFechaHoraActual()
        # self.id_cliente
        quien_recibe = self.txt_quien_recibe.GetValue()
        celular_recibe = self.txt_celular_recibe.GetValue()
        tipo_carro = self.comboBox_tipo_carro.GetValue()
        color = self.txt_color.GetValue()
        placa = self.txt_placa.GetValue()
        nacionalidad_carro = self.comboBox_nacionalidad.GetValue()
        ciudad_carro = self.txt_ciudad.GetValue()
        origen_venta = self.comboBox_origen_venta.GetValue()
        doc_relacionado = self.txt_doc_relacionado.GetValue()
        activo = 'True'
        total_unidades = self.lbl_total_unidades.GetLabel()
        peso_ton = self.lbl_toneladas.GetLabel()
        volumen_m3 = self.lbl_volumen.GetLabel()
        nota = self.txt_nota.GetValue()
        #self.uuid_eay
        # self.usuario
        # self.dir_mac

        sSql = """
                        INSERT INTO despacho_mercancia (fecha, hora, id_cliente, quien_recibe, celular_recibe, tipo_carro,
                                                        color, placa, nacionalidad_carro, ciudad_carro, origen_venta,
                                                        doc_relacionado, activo, total_unidades, peso_ton, volumen_m3,
                                                        nota, usuario, mac, uuid
                                                        ) 
                                        VALUES (
                                        '{0}', '{1}', {2}, '{3}', '{4}', '{5}', 
                                        '{6}', '{7}', '{8}', '{9}', '{10}', 
                                        '{11}', '{12}', {13}, {14}, {15}, 
                                        '{16}', '{17}', '{18}', '{19}'                                
                                        )
                """.format(fecha, hora, self.id_cliente, quien_recibe, celular_recibe, tipo_carro,
                           color, placa, nacionalidad_carro, ciudad_carro, origen_venta,
                           doc_relacionado, activo, total_unidades, peso_ton, volumen_m3,
                           nota, self.usuario, self.dir_mac, self.uuid_eay
                           )

        rta = Ejecutar_SQL.insert_filas(sSql.upper(), 'frm_despachar_mercancia/func_guardar_cabecera_despacho', BasesDeDatos.DB_PRINCIPAL)
        return rta

    def func_valores_iniciales(self):
        self.puntero_fila_producto = 0
        self.grid_productos.AutoSizeColumns()
        self.set_configuaracion_grilla_productos()
        self.cargar_combo_productos()

        self.lbl_total_unidades.SetLabel(str(0))
        self.lbl_toneladas.SetLabel(str(0))
        self.lbl_volumen.SetLabel(str(0))

        self.Layout()

    def cargar_combo_productos(self):

        cant_registros = 500

        sSql = """
                    SELECT id_producto, nom_producto, (peso/1000000.0) as peso_ton, (largo * ancho * alto)/1000000.0 as volumen_m3
                    FROM producto
                    WHERE activo = 'True'
                    ORDER BY nom_producto        
        """

        cabeceras = ['id', 'Producto', 'Peso_ton', 'Volumen_m3']
        rows = Ejecutar_SQL.select_varios_registros(sSql, 'cargar_combo_productos', cant_registros, BasesDeDatos.DB_PRINCIPAL)

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.dic_productos = ManipularRows.crearDiccionarioTodosLosCampos(rows, 1)

            self.comboBox_producto.Set(la_lista)

    def set_configuaracion_grilla_productos(self):
        list_columnas = [0, 1, 2, 3, 4, 5, 6, 7]
        ManipularGrillas.setColumnasSoloLectura(self.grid_productos, list_columnas)

        list_columnas = [8]
        ManipularGrillas.setColumnasFormatoCHK(self.grid_productos, list_columnas)

    def calcular_totales(self):
        filas = self.grid_productos.GetNumberRows()
        cant = 0
        peso = 0
        volumen = 0

        for i in range(filas):
            cant += int(self.grid_productos.GetCellValue(i, 3))
            peso += float(self.grid_productos.GetCellValue(i, 4))
            volumen += float(self.grid_productos.GetCellValue(i, 5))

        self.lbl_total_unidades.SetLabel(str(cant))
        self.lbl_toneladas.SetLabel(str(round(peso, 2)))
        self.lbl_volumen.SetLabel(str(round(volumen, 2)))

    def buscar_cliente_por_nit_o_celular(self, nit):
        sSql = """
            SELECT id_cliente, nom || ' ' || ape1 || ' ' || ape2 as nombre, razon_social, nit, dir || '. ' || ciudad, celular
            FROM  cliente 
            WHERE activo = 'True' AND (nit = '{0}'   OR celular = '{0}' )   
        """.format(nit)

        cabeceras = ['id', 'nom', 'razon_social', 'nit', 'dir', 'celular']

        rows = Ejecutar_SQL.select_un_registro(sSql, 'frm_despachar_mercancia/buscar_cliente_por_nit_o_celular',
                                               BasesDeDatos.DB_PRINCIPAL)

        if rows == None:
            self.id_cliente = -1
            self.lbl_nombre.SetLabel('')
            self.lbl_razon_social.SetLabel('')
            self.lbl_nit.SetLabel('')
            self.lbl_dir.SetLabel('')
            self.lbl_celular_cliente.SetLabel('')

            wx.MessageBox(u'Cliente No Registrado', u'Atención', wx.OK | wx.ICON_INFORMATION)

            return 0

        self.id_cliente = rows[0]
        self.lbl_nombre.SetLabel(rows[1])
        self.lbl_razon_social.SetLabel(rows[2])
        self.lbl_nit.SetLabel(rows[3])
        self.lbl_dir.SetLabel(rows[4])
        self.lbl_celular_cliente.SetLabel(rows[5])

    def func_validar_entrada_datos(self):

        if self.id_cliente == -1:
            wx.MessageBox(u'Debes seleccionar un cliente', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        cant_filas = self.grid_productos.GetNumberRows()
        if cant_filas == 0:
            wx.MessageBox(u'Debes ingresar mínimo un Producto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        if self.txt_quien_recibe.GetValue() == '':
            wx.MessageBox(u'Debes ingresar el Nombre del conductor quien recibirá la mercancia', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        if self.comboBox_tipo_carro.GetValue() == '':
            wx.MessageBox(u'Debes seleccionar el tipo de carro en que se transportara la mercancia', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        if self.txt_color.GetValue() == '':
            wx.MessageBox(u'Debes ingresar el color del carro', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return

        if self.txt_placa.GetValue() == '':
            wx.MessageBox(u'Debes ingresar la placa del carro', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return

        if self.comboBox_nacionalidad.GetValue() == '':
            wx.MessageBox(u'Debes seleccionar el pais de procedencia de las placas del carro', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        if self.txt_ciudad.GetValue() == '':
            wx.MessageBox(u'Debes ingresar la ciudad donde se expidieron las placas del carro', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return

        if self.comboBox_origen_venta.GetValue() == '':
            wx.MessageBox(u'Debes seleccionar el origen de la venta, [donde fue pactada la venta]', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        if self.txt_doc_relacionado.GetValue() == '':
            wx.MessageBox(u'Debes ingresar el numero de factura relacionada con la venta', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return

        ## si esta todo bien
        return 1
