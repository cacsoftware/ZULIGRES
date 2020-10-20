# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import matplotlib.pyplot as plt
import numpy as np

###########################################################################
## Class GraficosProduccionPorPeriodo
###########################################################################

class GraficosProduccionPorPeriodo(wx.Frame):

    def __init__(self, parent, dic_cabecera, dic_valores, maximo_unidades, maximo_toneladas, n):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Graficos.  Historial Detalle Procesos",
                          pos=wx.DefaultPosition, size=wx.Size(800, 700),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(700, 600), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.dic_cabecera = dic_cabecera
        self.dic_valores = dic_valores
        self.maximo_unidades = maximo_unidades
        self.maximo_toneladas = maximo_toneladas
        self.n = n

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_area = wx.StaticText(self, wx.ID_ANY, u"Area:", wx.DefaultPosition, wx.Size(50, -1),
                                          wx.ALIGN_RIGHT)
        self.lbl_etq_area.Wrap(-1)
        self.lbl_etq_area.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_area.SetForegroundColour(wx.Colour(255, 128, 0))

        bSizer2.Add(self.lbl_etq_area, 0, wx.ALL, 5)

        self.lbl_area = wx.StaticText(self, wx.ID_ANY, u"EXTRUSION", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_area.Wrap(-1)
        self.lbl_area.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))

        bSizer2.Add(self.lbl_area, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        bSizer21 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fechas = wx.StaticText(self, wx.ID_ANY, u"Fechas:", wx.DefaultPosition, wx.Size(50, -1),
                                            wx.ALIGN_RIGHT)
        self.lbl_etq_fechas.Wrap(-1)
        self.lbl_etq_fechas.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_fechas.SetForegroundColour(wx.Colour(255, 128, 0))

        bSizer21.Add(self.lbl_etq_fechas, 0, wx.ALL, 5)

        self.lbl_fechas = wx.StaticText(self, wx.ID_ANY, u"[25-JUN-2020 ...  16-JUL-2020]", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.lbl_fechas.Wrap(-1)
        bSizer21.Add(self.lbl_fechas, 0, wx.ALL, 5)

        bSizer1.Add(bSizer21, 0, wx.EXPAND, 5)

        bSizer22 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_turnos = wx.StaticText(self, wx.ID_ANY, u"Turnos:", wx.DefaultPosition, wx.Size(50, -1),
                                            wx.ALIGN_RIGHT)
        self.lbl_etq_turnos.Wrap(-1)
        self.lbl_etq_turnos.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_turnos.SetForegroundColour(wx.Colour(255, 128, 0))

        bSizer22.Add(self.lbl_etq_turnos, 0, wx.ALL, 5)

        self.lbl_turnos = wx.StaticText(self, wx.ID_ANY, u"AM", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_turnos.Wrap(-1)
        bSizer22.Add(self.lbl_turnos, 0, wx.ALL, 5)

        bSizer1.Add(bSizer22, 0, wx.EXPAND, 5)

        bSizer221 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_turnos1 = wx.StaticText(self, wx.ID_ANY, u"Periodo:", wx.DefaultPosition, wx.Size(50, -1),
                                             wx.ALIGN_RIGHT)
        self.lbl_etq_turnos1.Wrap(-1)
        self.lbl_etq_turnos1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_turnos1.SetForegroundColour(wx.Colour(255, 128, 0))

        bSizer221.Add(self.lbl_etq_turnos1, 0, wx.ALL, 5)

        self.lbl_perido = wx.StaticText(self, wx.ID_ANY, u"SEMANA", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_perido.Wrap(-1)
        bSizer221.Add(self.lbl_perido, 0, wx.ALL, 5)

        bSizer1.Add(bSizer221, 0, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.notebook_graficos = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panel_resumen = wx.Panel(self.notebook_graficos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
        bSizer_detalle1 = wx.BoxSizer(wx.VERTICAL)

        self.bitmap_produccion_unidades = wx.StaticBitmap(self.panel_resumen, wx.ID_ANY, wx.NullBitmap,
                                                          wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_detalle1.Add(self.bitmap_produccion_unidades, 1, wx.ALL | wx.EXPAND, 5)

        self.panel_resumen.SetSizer(bSizer_detalle1)
        self.panel_resumen.Layout()
        bSizer_detalle1.Fit(self.panel_resumen)
        self.notebook_graficos.AddPage(self.panel_resumen, u"Unidades", True)
        self.m_panel2 = wx.Panel(self.notebook_graficos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                 wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.bitmap_produccion_toneladas = wx.StaticBitmap(self.m_panel2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                                           wx.DefaultSize, 0)
        bSizer9.Add(self.bitmap_produccion_toneladas, 0, wx.ALL, 5)

        self.m_panel2.SetSizer(bSizer9)
        self.m_panel2.Layout()
        bSizer9.Fit(self.m_panel2)
        self.notebook_graficos.AddPage(self.m_panel2, u"Toneladas", False)

        bSizer10.Add(self.notebook_graficos, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer23 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_nota = wx.StaticText(self, wx.ID_ANY,
                                      u" // Con DobleClick puedes abrir la imagen en el visor de imagenes",
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_nota.Wrap(-1)
        self.lbl_nota.SetForegroundColour(wx.Colour(0, 128, 0))

        bSizer23.Add(self.lbl_nota, 0, wx.ALL, 5)

        bSizer1.Add(bSizer23, 0, wx.EXPAND, 5)

        ## VALORES INICIALES EAY
        self.func_valoresIniciales()

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


    ##  FUNCIONES EAY

    def func_valoresIniciales(self):
        self.lbl_area.SetLabel(self.dic_cabecera['area'])
        self.lbl_fechas.SetLabel(self.dic_cabecera['fechas'])
        self.lbl_turnos.SetLabel(str(self.dic_cabecera['turnos']))
        self.lbl_perido.SetLabel(self.dic_cabecera['periodo'])

        self.graficarUnidades()
        self.graficarToneladas()


    def graficarUnidades(self):
        plt.rc('axes', titlesize=14)
        # plt.rc('xtick', labelsize=10)
        plt.rc('ytick', labelsize=8)

        fig, ax = plt.subplots(1,1)
        fig.set_size_inches(7, 5)


        if self.dic_cabecera['area'] == 'EXTRUSION':
            x = self.dic_valores['x']
            y = self.dic_valores['y_u']

            plt.ylim(0, self.maximo_unidades)

            plt.plot(x, y, marker=".", color="sandybrown")

            plt.legend(['Primera', 'Rotura'], loc=(0.8, 1.01), fontsize=9)

            plt.xticks(rotation=30, fontsize=6)

            ax.grid(color='lightgray')

            nom_archivo = 'GRAFICOS/' + 'ProduccionPorPeriodo' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_produccion_unidades.SetBitmap(wx.Bitmap(img1))

        if self.dic_cabecera['area'] == 'CARGUE DE VAGONETAS':

            x = self.dic_valores['x']
            y1_u = self.dic_valores['y1_u']
            y2_u = self.dic_valores['y2_u']

            plt.ylim(0, self.maximo_unidades)

            plt.plot(x, y1_u, marker=".", color="sandybrown")
            plt.plot(x, y2_u, marker=".", color="brown",  linestyle="--")

            plt.legend(['Primera', 'Rotura'], loc=(0.8, 1.01), fontsize=9)

            plt.xticks(rotation=30, fontsize=6)

            ax.grid(color='lightgray')


            nom_archivo = 'GRAFICOS/' + 'ProduccionPorPeriodo' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_produccion_unidades.SetBitmap(wx.Bitmap(img1))

        if self.dic_cabecera['area'] == 'DESCARGUE DE VAGONETAS':
            x = self.dic_valores['x']
            y1_u = self.dic_valores['y1_u']
            y2_u = self.dic_valores['y2_u']
            y3_u = self.dic_valores['y3_u']

            plt.ylim(0, self.maximo_unidades)

            plt.plot(x, y1_u, marker=".", color="sandybrown")
            plt.plot(x, y2_u, marker=".", color="skyblue")
            plt.plot(x, y3_u, marker=".", color="brown", linestyle="--")

            plt.legend(['Primera', 'Segunda', 'Rotura'],  fontsize=9)

            plt.xticks(rotation=30, fontsize=6)

            ax.grid(color='lightgray')

            nom_archivo = 'GRAFICOS/' + 'ProduccionPorPeriodo' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_produccion_unidades.SetBitmap(wx.Bitmap(img1))

    def graficarToneladas(self):
        plt.rc('axes', titlesize=14)
        # plt.rc('xtick', labelsize=10)
        plt.rc('ytick', labelsize=8)

        fig, ax = plt.subplots(1, 1)
        fig.set_size_inches(8, 4)


        if self.dic_cabecera['area'] == 'CARGUE DE VAGONETAS':

            x = self.dic_valores['x']

            y1_t = self.dic_valores['y1_t']
            y2_t = self.dic_valores['y2_t']

            plt.ylim(0, self.maximo_toneladas)

            plt.plot(x, y1_t, marker=".", color="sandybrown")
            plt.plot(x, y2_t, marker=".", color="brown", linestyle="--")

            plt.legend(['Primera', 'Rotura'], loc=(0.8, 1.01), fontsize=9)

            plt.xticks(rotation=30, fontsize=6)

            ax.grid(color='lightgray')

            nom_archivo = 'GRAFICOS/' + 'ProduccionPorPeriodo_toneladas' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_produccion_toneladas.SetBitmap(wx.Bitmap(img1))

        if self.dic_cabecera['area'] == 'EXTRUSION':
            x = self.dic_valores['x']
            y = self.dic_valores['y_t']

            plt.ylim(0, self.maximo_toneladas)

            plt.plot(x, y, marker=".", color="sandybrown")

            plt.legend(['Toneladas Extruidas'], loc=(0.8, 1.01), fontsize=9)

            plt.xticks(rotation=30, fontsize=6)

            ax.grid(color='lightgray')

            nom_archivo = 'GRAFICOS/' + 'ProduccionPorPeriodo_toneladas' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_produccion_toneladas.SetBitmap(wx.Bitmap(img1))


        if self.dic_cabecera['area'] == 'DESCARGUE DE VAGONETAS':
            x = self.dic_valores['x']
            y1_t = self.dic_valores['y1_t']
            y2_t = self.dic_valores['y2_t']
            y3_t = self.dic_valores['y3_t']

            plt.ylim(0, self.maximo_toneladas)

            plt.plot(x, y1_t, marker=".", color="sandybrown")
            plt.plot(x, y2_t, marker=".", color="skyblue")
            plt.plot(x, y3_t, marker=".", color="brown", linestyle="--")

            plt.legend(['Primera', 'Segunda', 'Rotura'],  fontsize=9)

            plt.xticks(rotation=30, fontsize=6)

            ax.grid(color='lightgray')

            nom_archivo = 'GRAFICOS/' + 'ProduccionPorPeriodo_toneladas' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_produccion_toneladas.SetBitmap(wx.Bitmap(img1))




