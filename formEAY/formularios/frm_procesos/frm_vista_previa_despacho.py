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


###########################################################################
## Class frm_vistaPreviaDespacho
###########################################################################

class frm_vistaPreviaDespacho(wx.Frame):

    def __init__(self, parent, usuario, dir_mac, uuid=-1, estado='True'):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Vista Previa Despacho", pos=wx.DefaultPosition,
                          size=wx.Size(721, 692), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(700, 400), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.usuario = usuario
        self.dir_mac = dir_mac
        self.uuid = uuid
        self.estado = estado

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel1.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_titulo = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Mercancia Despachada", wx.DefaultPosition,
                                            wx.DefaultSize, wx.ALIGN_CENTRE)
        self.lbl_etq_titulo.Wrap(-1)
        self.lbl_etq_titulo.SetFont(wx.Font(11, 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_titulo.SetForegroundColour(wx.Colour(255, 128, 64))

        bSizer4.Add(self.lbl_etq_titulo, 1, wx.ALL, 5)

        bSizer2.Add(bSizer4, 0, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fecha = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Fecha:", wx.DefaultPosition, wx.Size(60, -1),
                                           wx.ALIGN_RIGHT)
        self.lbl_etq_fecha.Wrap(-1)
        bSizer3.Add(self.lbl_etq_fecha, 0, wx.ALL, 5)

        self.lbl_fecha = wx.StaticText(self.m_panel1, wx.ID_ANY, u"25 jun 2021", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_fecha.Wrap(-1)
        bSizer3.Add(self.lbl_fecha, 0, wx.ALL, 5)

        self.lbl_etq_ordenDeServicio = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Orden de Servicio:",
                                                     wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lbl_etq_ordenDeServicio.Wrap(-1)
        bSizer3.Add(self.lbl_etq_ordenDeServicio, 1, wx.ALL, 5)

        self.lbl_numOrdenservicio = wx.StaticText(self.m_panel1, wx.ID_ANY, u"025", wx.DefaultPosition,
                                                  wx.Size(130, -1), 0)
        self.lbl_numOrdenservicio.Wrap(-1)
        self.lbl_numOrdenservicio.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))
        self.lbl_numOrdenservicio.SetForegroundColour(wx.Colour(255, 0, 0))

        bSizer3.Add(self.lbl_numOrdenservicio, 0, wx.ALL, 5)

        bSizer2.Add(bSizer3, 0, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_cliente = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Cliente:", wx.DefaultPosition, wx.Size(60, -1),
                                             wx.ALIGN_RIGHT)
        self.lbl_etq_cliente.Wrap(-1)
        bSizer5.Add(self.lbl_etq_cliente, 0, wx.ALL, 5)

        self.lbl_cliente = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Joaquin Lobo", wx.DefaultPosition, wx.DefaultSize,
                                         0)
        self.lbl_cliente.Wrap(-1)
        self.lbl_cliente.SetFont(wx.Font(10, 70, 90, 92, False, wx.EmptyString))

        bSizer5.Add(self.lbl_cliente, 1, wx.ALL, 5)

        self.lbl_etq_nit = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Nit:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_nit.Wrap(-1)
        bSizer5.Add(self.lbl_etq_nit, 0, wx.ALL, 5)

        self.lbl_nit = wx.StaticText(self.m_panel1, wx.ID_ANY, u"88.256.145", wx.DefaultPosition, wx.Size(130, -1), 0)
        self.lbl_nit.Wrap(-1)
        self.lbl_nit.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer5.Add(self.lbl_nit, 0, wx.ALL, 5)

        bSizer2.Add(bSizer5, 0, wx.EXPAND, 5)

        bSizer51 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_direccion = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Dirección:", wx.DefaultPosition,
                                               wx.Size(60, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_direccion.Wrap(-1)
        bSizer51.Add(self.lbl_etq_direccion, 0, wx.ALL, 5)

        self.lbl_direccion = wx.StaticText(self.m_panel1, wx.ID_ANY, u"calle 25 n 36-11", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.lbl_direccion.Wrap(-1)
        bSizer51.Add(self.lbl_direccion, 1, wx.ALL, 5)

        self.lbl_etq_celular = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Celular:", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.lbl_etq_celular.Wrap(-1)
        bSizer51.Add(self.lbl_etq_celular, 0, wx.ALL, 5)

        self.lbl_celular = wx.StaticText(self.m_panel1, wx.ID_ANY, u"311.256.32.10", wx.DefaultPosition,
                                         wx.Size(130, -1), 0)
        self.lbl_celular.Wrap(-1)
        self.lbl_celular.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer51.Add(self.lbl_celular, 0, wx.ALL, 5)

        bSizer2.Add(bSizer51, 0, wx.EXPAND, 5)

        bSizer511 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_transporte = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Transporte:", wx.DefaultPosition,
                                                wx.Size(60, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_transporte.Wrap(-1)
        bSizer511.Add(self.lbl_etq_transporte, 0, wx.ALL, 5)

        self.lbl_transporto = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Camilo Volqueta Azul Placa:256-HYU",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_transporto.Wrap(-1)
        bSizer511.Add(self.lbl_transporto, 1, wx.ALL, 5)

        bSizer2.Add(bSizer511, 0, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.grid_productos = wx.grid.Grid(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_productos.CreateGrid(5, 5)
        self.grid_productos.EnableEditing(True)
        self.grid_productos.EnableGridLines(True)
        self.grid_productos.EnableDragGridSize(False)
        self.grid_productos.SetMargins(0, 0)

        # Columns
        self.grid_productos.EnableDragColMove(False)
        self.grid_productos.EnableDragColSize(True)
        self.grid_productos.SetColLabelSize(30)
        self.grid_productos.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_productos.EnableDragRowSize(True)
        self.grid_productos.SetRowLabelSize(80)
        self.grid_productos.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_productos.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer14.Add(self.grid_productos, 1, wx.ALL | wx.EXPAND, 5)

        bSizer2.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_estado = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Estado:", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_RIGHT)
        self.lbl_etq_estado.Wrap(-1)
        bSizer9.Add(self.lbl_etq_estado, 1, wx.ALL, 5)

        self.lbl_estado = wx.StaticText(self.m_panel1, wx.ID_ANY, u"ACTIVO", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.lbl_estado.Wrap(-1)
        self.lbl_estado.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer9.Add(self.lbl_estado, 0, wx.ALL, 5)

        self.btn_anular = wx.Button(self.m_panel1, wx.ID_ANY, u"&Anular", wx.DefaultPosition, wx.DefaultSize,
                                    wx.NO_BORDER)
        self.btn_anular.SetForegroundColour(wx.Colour(255, 255, 255))
        self.btn_anular.SetBackgroundColour(wx.Colour(255, 0, 0))

        bSizer9.Add(self.btn_anular, 0, wx.ALL, 5)

        bSizer2.Add(bSizer9, 0, wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_anular.Bind(wx.EVT_BUTTON, self.btn_anularOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btn_anularOnButtonClick(self, event):
        event.Skip()


