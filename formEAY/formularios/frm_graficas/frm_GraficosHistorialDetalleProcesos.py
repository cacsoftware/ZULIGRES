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
## Class GraficosHistorialDetalleProcesos
###########################################################################

class GraficosHistorialDetalleProcesos(wx.Frame):

    def __init__(self, parent, dic_cabecera, dic_valores_resumen, dic_valores_detalle):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Graficos.  Historial Detalle Procesos",
                          pos=wx.DefaultPosition, size=wx.Size(1100, 700),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(700, 600), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.dic_cabecera =dic_cabecera
        self.dic_valores_resumen = dic_valores_resumen
        self.dic_valores_detalle = dic_valores_detalle

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_area = wx.StaticText(self, wx.ID_ANY, u"Area:", wx.DefaultPosition, wx.Size(45, -1),
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

        self.lbl_etq_fechas = wx.StaticText(self, wx.ID_ANY, u"Fechas:", wx.DefaultPosition, wx.Size(45, -1),
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

        self.lbl_etq_turnos = wx.StaticText(self, wx.ID_ANY, u"Turnos:", wx.DefaultPosition, wx.Size(45, -1),
                                            wx.ALIGN_RIGHT)
        self.lbl_etq_turnos.Wrap(-1)
        self.lbl_etq_turnos.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_turnos.SetForegroundColour(wx.Colour(255, 128, 0))

        bSizer22.Add(self.lbl_etq_turnos, 0, wx.ALL, 5)

        self.lbl_turnos = wx.StaticText(self, wx.ID_ANY, u"AM", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_turnos.Wrap(-1)
        bSizer22.Add(self.lbl_turnos, 0, wx.ALL, 5)

        bSizer1.Add(bSizer22, 0, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.notebook_graficos = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.panel_resumen = wx.Panel(self.notebook_graficos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
        bSizer_detalle1 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer131 = wx.BoxSizer(wx.VERTICAL)

        # self.lbl_etq_unidades1 = wx.StaticText(self.panel_resumen, wx.ID_ANY, u"Unidades", wx.DefaultPosition,
        #                                        wx.DefaultSize, wx.ALIGN_CENTRE)
        # self.lbl_etq_unidades1.Wrap(-1)
        # self.lbl_etq_unidades1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        # self.lbl_etq_unidades1.SetForegroundColour(wx.Colour(0, 128, 255))
        #
        # bSizer131.Add(self.lbl_etq_unidades1, 0, wx.ALL | wx.EXPAND, 5)

        self.bitmap_resumen_unidades = wx.StaticBitmap(self.panel_resumen, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                                       wx.DefaultSize, 0)
        bSizer131.Add(self.bitmap_resumen_unidades, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_detalle1.Add(bSizer131, 1, wx.EXPAND, 5)

        bSizer141 = wx.BoxSizer(wx.VERTICAL)

        # self.lbl_etq_toneladas1 = wx.StaticText(self.panel_resumen, wx.ID_ANY, u"Toneladas", wx.DefaultPosition,
        #                                         wx.DefaultSize, wx.ALIGN_CENTRE)
        # self.lbl_etq_toneladas1.Wrap(-1)
        # self.lbl_etq_toneladas1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        # self.lbl_etq_toneladas1.SetForegroundColour(wx.Colour(0, 128, 255))
        #
        # bSizer141.Add(self.lbl_etq_toneladas1, 0, wx.ALL | wx.EXPAND, 5)

        # self.bitmap_resumen_toneladas = wx.StaticBitmap(self.panel_resumen, wx.ID_ANY, wx.NullBitmap,
        #                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        # bSizer141.Add(self.bitmap_resumen_toneladas, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_detalle1.Add(bSizer141, 1, wx.EXPAND, 5)

        self.panel_resumen.SetSizer(bSizer_detalle1)
        self.panel_resumen.Layout()
        bSizer_detalle1.Fit(self.panel_resumen)
        self.notebook_graficos.AddPage(self.panel_resumen, u"Resumen", True)
        self.panel_detalle = wx.Panel(self.notebook_graficos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
        bSizer_detalle = wx.BoxSizer(wx.HORIZONTAL)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        # self.lbl_etq_unidades = wx.StaticText(self.panel_detalle, wx.ID_ANY, u"Unidades", wx.DefaultPosition,
        #                                       wx.DefaultSize, wx.ALIGN_CENTRE)
        # self.lbl_etq_unidades.Wrap(-1)
        # self.lbl_etq_unidades.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        # self.lbl_etq_unidades.SetForegroundColour(wx.Colour(0, 128, 255))
        #
        # bSizer13.Add(self.lbl_etq_unidades, 0, wx.ALL | wx.EXPAND, 5)

        self.bitmap_detalle_unidades = wx.StaticBitmap(self.panel_detalle, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                                       wx.DefaultSize, 0)
        bSizer13.Add(self.bitmap_detalle_unidades, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_detalle.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        # self.lbl_etq_toneladas = wx.StaticText(self.panel_detalle, wx.ID_ANY, u"Toneladas", wx.DefaultPosition,
        #                                        wx.DefaultSize, wx.ALIGN_CENTRE)
        # self.lbl_etq_toneladas.Wrap(-1)
        # self.lbl_etq_toneladas.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        # self.lbl_etq_toneladas.SetForegroundColour(wx.Colour(0, 128, 255))
        #
        # bSizer14.Add(self.lbl_etq_toneladas, 0, wx.ALL | wx.EXPAND, 5)

        self.bitmap_detalle_toneladas = wx.StaticBitmap(self.panel_detalle, wx.ID_ANY, wx.NullBitmap,
                                                        wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer14.Add(self.bitmap_detalle_toneladas, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_detalle.Add(bSizer14, 1, wx.EXPAND, 5)

        self.panel_detalle.SetSizer(bSizer_detalle)
        self.panel_detalle.Layout()
        bSizer_detalle.Fit(self.panel_detalle)
        self.notebook_graficos.AddPage(self.panel_detalle, u"Detalle", False)

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

        self.graficarResumenUnidades()
        self.graficarDetalleProductos()


    def graficarResumenUnidades(self):
        plt.rc('axes', titlesize=14)
        # plt.rc('xtick', labelsize=10)
        plt.rc('ytick', labelsize=8)

        fig, ax = plt.subplots(1,2)
        fig.set_size_inches(6, 4)

        if self.dic_cabecera['area'] == 'EXTRUSION':
            self.notebook_graficos.SetSelection(1)

        if self.dic_cabecera['area'] == 'CARGUE DE VAGONETAS':
            x = ['Prod Primera', 'Prod Rotura']

            #dic_valores_resumen = {'list_unid_resumen': list_unid_resumen, 'list_ton_resumen': list_ton_resumen}

            y1 = self.dic_valores_resumen['list_unid_resumen']
            y2 = self.dic_valores_resumen['list_ton_resumen']

            ax[0].bar(x, y1, color='sandybrown', width=0.4)
            ax[0].legend(['Unidades'], fontsize =8)

            ax[1].bar(x, y2, color='deepskyblue', width=0.4)
            ax[1].legend(['Toneladas'], fontsize =8)

            plt.suptitle('Cargue de Vagonetas', color='blue')

            nom_archivo = 'GRAFICOS/' + 'Resumen' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_resumen_unidades.SetBitmap(wx.Bitmap(img1))

        if self.dic_cabecera['area'] == 'DESCARGUE DE VAGONETAS':
            x = ['Primera',  'Segunda', 'Rotura']

            #dic_valores_resumen = {'list_unid_resumen': list_unid_resumen, 'list_ton_resumen': list_ton_resumen}

            y1 = self.dic_valores_resumen['list_unid_resumen']
            y2 = self.dic_valores_resumen['list_ton_resumen']

            ax[0].bar(x, y1, color='sandybrown', width=0.4)
            ax[0].legend(['Unidades'], fontsize =8)

            ax[1].bar(x, y2, color='deepskyblue', width=0.4)
            ax[1].legend(['Toneladas'], fontsize =8)

            plt.suptitle('Descargue de Vagonetas', color='blue')

            nom_archivo = 'GRAFICOS/' + 'Resumen' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_resumen_unidades.SetBitmap(wx.Bitmap(img1))

        if self.dic_cabecera['area'] == 'DESPACHOS':
            x = ['Primera',  'Segunda']

            #dic_valores_resumen = {'list_unid_resumen': list_unid_resumen, 'list_ton_resumen': list_ton_resumen}

            y1 = self.dic_valores_resumen['list_unid_resumen']
            y2 = self.dic_valores_resumen['list_ton_resumen']

            ax[0].bar(x, y1, color='sandybrown', width=0.4)
            ax[0].legend(['Unidades'], fontsize =8)

            ax[1].bar(x, y2, color='deepskyblue', width=0.4)
            ax[1].legend(['Toneladas'], fontsize =8)

            plt.suptitle('Descargue de Vagonetas', color='blue')

            nom_archivo = 'GRAFICOS/' + 'Resumen' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_resumen_unidades.SetBitmap(wx.Bitmap(img1))



    def graficarDetalleProductos(self):

        plt.rc('axes', titlesize=14)
        # plt.rc('xtick', labelsize=10)
        plt.rc('ytick', labelsize=8)

        fig, ax = plt.subplots()
        fig.set_size_inches(11, 5)

        if self.dic_cabecera['area'] == 'EXTRUSION':
            # dic_valores_detalle = {'list_productos':list_productos, 'list_unidades':list_unidades}

            y= np.array(self.dic_valores_detalle['list_productos'])
            x1 = np.array(self.dic_valores_detalle['list_unidades'])

            ax.barh(y, x1, color='sandybrown', label="Unidades")
            ax.legend(loc=(0.8, 1.03), fontsize=8)


            plt.suptitle(u'Extrusión', color='blue')

            nom_archivo = 'GRAFICOS/' + 'Detalle' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_detalle_unidades.SetBitmap(wx.Bitmap(img1))

        if self.dic_cabecera['area'] == 'CARGUE DE VAGONETAS':
            # dic_valores_detalle = {'list_productos':list_productos, 'list_prod_ok':list_prod_ok, 'list_prod_rotos':list_prod_rotos}


            y= np.array(self.dic_valores_detalle['list_productos'])
            x1 = np.array(self.dic_valores_detalle['list_prod_ok'])
            x2 = np.array(self.dic_valores_detalle['list_prod_rotos'])

            ax.barh(y, x1, color='sandybrown', label = "Unids Primera")
            #ax.legend(['Unids OK'], fontsize=8)
            ax.barh(y, x2, left = x1,  color='brown', label = "Unids Rotura")
            ax.legend(loc=(0.8, 1.03), fontsize=8)

            # ax[1].barh(x, y2, color='blue')
            # ax[1].legend(['Toneladas'], fontsize=8)

            plt.suptitle('Cargue de Vagonetas', color='blue')

            nom_archivo = 'GRAFICOS/' + 'Detalle' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_detalle_unidades.SetBitmap(wx.Bitmap(img1))

        if self.dic_cabecera['area'] == 'DESCARGUE DE VAGONETAS':
            # dic_valores_detalle = {'list_productos':list_productos, 'list_prod_primera':list_prod_primera,
            #                                        'list_prod_segunda':list_prod_segunda,
            #                                        'list_prod_rotos': list_prod_rotos
            #                                        }


            y= np.array(self.dic_valores_detalle['list_productos'])
            x1 = np.array(self.dic_valores_detalle['list_prod_primera'])
            x2 = np.array(self.dic_valores_detalle['list_prod_segunda'])
            x3 = np.array(self.dic_valores_detalle['list_prod_rotos'])

            ax.barh(y, x1, color='sandybrown', label = "De Primera")
            #ax.legend(['Unids OK'], fontsize=8)
            ax.barh(y, x2, left = x1,  color='palevioletred', label = "De segunda")  #darkseagreen  rosybrown
            ax.barh(y, x3, left=x1 + x2, color='brown', label="Rotura")

            ax.legend(loc=(0.8, 1.03), fontsize=8)

            # ax[1].barh(x, y2, color='blue')
            # ax[1].legend(['Toneladas'], fontsize=8)

            plt.suptitle('Descargue de Vagonetas', color='blue')

            nom_archivo = 'GRAFICOS/' + 'Detalle' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_detalle_unidades.SetBitmap(wx.Bitmap(img1))


        if self.dic_cabecera['area'] == 'DESPACHOS':
            # dic_valores_detalle = {'list_productos':list_productos, 'list_prod_primera':list_prod_primera,
            #                                        'list_prod_segunda':list_prod_segunda,
            #                                        }


            y= np.array(self.dic_valores_detalle['list_productos'])
            x1 = np.array(self.dic_valores_detalle['list_prod_primera'])
            x2 = np.array(self.dic_valores_detalle['list_prod_segunda'])

            ax.barh(y, x1, color='sandybrown', label = "De Primera")
            #ax.legend(['Unids OK'], fontsize=8)
            ax.barh(y, x2, left = x1,  color='palevioletred', label = "De segunda")  #darkseagreen  rosybrown

            ax.legend(loc=(0.8, 1.03), fontsize=8)

            # ax[1].barh(x, y2, color='blue')
            # ax[1].legend(['Toneladas'], fontsize=8)

            plt.suptitle('Despachos', color='blue')

            nom_archivo = 'GRAFICOS/' + 'Detalle' + '.png'
            plt.savefig(nom_archivo)

            img1 = wx.Image(nom_archivo, wx.BITMAP_TYPE_ANY)
            self.bitmap_detalle_unidades.SetBitmap(wx.Bitmap(img1))


        self.Layout()



        #plt.show()




