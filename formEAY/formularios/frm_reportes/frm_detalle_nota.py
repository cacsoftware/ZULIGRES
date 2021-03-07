# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from pyeay.dbcac.conexiondb import Ejecutar_SQL
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

###########################################################################
## Class DetalleNota
###########################################################################

class DetalleNota(wx.Frame):

    def __init__(self, parent, dic_nota,  lista_relevancias):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Detalle de Nota", pos=wx.DefaultPosition,
                          size=wx.Size(450, 450), style=wx.DEFAULT_FRAME_STYLE | wx.NO_BORDER | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(450, 400), wx.Size(450, -1))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.padre = parent

        self.dic_nota = dic_nota
        self.lista_relevancias = lista_relevancias


        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_area = wx.StaticText(self, wx.ID_ANY, u"Area:", wx.DefaultPosition, wx.Size(60, -1),
                                          wx.ALIGN_RIGHT)
        self.lbl_etq_area.Wrap(-1)
        self.lbl_etq_area.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))

        bSizer2.Add(self.lbl_etq_area, 0, wx.ALL | wx.EXPAND, 5)

        self.lbl_area = wx.StaticText(self, wx.ID_ANY, u"EXTRUSIÓN", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_area.Wrap(-1)
        self.lbl_area.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))

        bSizer2.Add(self.lbl_area, 1, wx.ALL | wx.EXPAND, 5)

        self.checkBox_estado = wx.CheckBox(self, wx.ID_ANY, u"Activo", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.checkBox_estado, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_contexto = wx.StaticText(self, wx.ID_ANY, u"Contexto:", wx.DefaultPosition, wx.Size(60, -1),
                                              wx.ALIGN_RIGHT)
        self.lbl_etq_contexto.Wrap(-1)
        bSizer4.Add(self.lbl_etq_contexto, 0, wx.ALL, 5)

        self.lbl_contexto = wx.StaticText(self, wx.ID_ANY, u"SOLICITUD", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_contexto.Wrap(-1)
        bSizer4.Add(self.lbl_contexto, 1, wx.ALL, 5)

        self.lbl_etq_fecha = wx.StaticText(self, wx.ID_ANY, u"Fecha:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_fecha.Wrap(-1)
        bSizer4.Add(self.lbl_etq_fecha, 0, wx.ALL, 5)

        self.lbl_fecha = wx.StaticText(self, wx.ID_ANY, u"25/01/2020", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_fecha.Wrap(-1)
        bSizer4.Add(self.lbl_fecha, 0, wx.ALL, 5)

        bSizer6.Add(bSizer4, 0, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_relevancia = wx.StaticText(self, wx.ID_ANY, u"Relevancia:", wx.DefaultPosition, wx.Size(60, -1),
                                                wx.ALIGN_RIGHT)
        self.lbl_etq_relevancia.Wrap(-1)
        bSizer5.Add(self.lbl_etq_relevancia, 0, wx.ALL, 5)

        comboBox_relevanciaChoices = []
        self.comboBox_relevancia = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                               comboBox_relevanciaChoices, wx.CB_READONLY)
        bSizer5.Add(self.comboBox_relevancia, 1, wx.ALL, 5)

        self.lbl_etq_estado = wx.StaticText(self, wx.ID_ANY, u"Estado:", wx.DefaultPosition, wx.Size(60, -1),
                                            wx.ALIGN_RIGHT)
        self.lbl_etq_estado.Wrap(-1)
        bSizer5.Add(self.lbl_etq_estado, 0, wx.ALL, 5)

        comboBox_estadoChoices = []
        self.comboBox_estado = wx.ComboBox(self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                           comboBox_estadoChoices, wx.CB_READONLY)
        bSizer5.Add(self.comboBox_estado, 1, wx.ALL, 5)

        bSizer6.Add(bSizer5, 0, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_estado = wx.StaticText(self, wx.ID_ANY, u"REVISADO", wx.DefaultPosition, wx.Size(-1, 30),
                                        wx.ALIGN_CENTRE)
        self.lbl_estado.Wrap(-1)
        self.lbl_estado.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))
        self.lbl_estado.SetBackgroundColour(wx.Colour(255, 255, 149))

        bSizer8.Add(self.lbl_estado, 1, wx.ALL, 5)

        bSizer6.Add(bSizer8, 0, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_nota = wx.StaticText(self, wx.ID_ANY, u"Nota:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_nota.Wrap(-1)
        bSizer9.Add(self.lbl_etq_nota, 0, wx.ALL, 5)

        self.txt_nota = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer9.Add(self.txt_nota, 1, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer91 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_contranota = wx.StaticText(self, wx.ID_ANY, u"Contranota:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_contranota.Wrap(-1)
        bSizer91.Add(self.lbl_etq_contranota, 0, wx.ALL, 5)

        self.txt_contranota = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_MULTILINE)
        bSizer91.Add(self.txt_contranota, 1, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(bSizer91, 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        bSizer13.Add(self.m_staticText12, 1, wx.ALL, 5)

        self.btn_guardar = wx.Button(self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.btn_guardar.SetBackgroundColour(wx.Colour(128, 255, 128))

        bSizer13.Add(self.btn_guardar, 0, wx.ALL, 5)

        bSizer6.Add(bSizer13, 0, wx.EXPAND, 5)

        bSizer3.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        ## CARGAR VALORES INICIALES
        self.cargar_valores_iniicales()

        # Connect Events
        self.checkBox_estado.Bind(wx.EVT_CHECKBOX, self.checkBox_estadoOnCheckBox)
        self.comboBox_estado.Bind(wx.EVT_COMBOBOX, self.comboBox_estadoOnCombobox)
        self.btn_guardar.Bind(wx.EVT_BUTTON, self.btn_guardarOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class

    def checkBox_estadoOnCheckBox(self, event):
        is_activo = self.checkBox_estado.GetValue()
        if is_activo == True:
            self.colorear_col_estado()
        else:
            self.lbl_estado.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.Layout()
        event.Skip()

    def comboBox_estadoOnCombobox(self, event):
        self.colorear_col_estado()
        self.lbl_estado.SetLabel(self.comboBox_estado.GetValue())
        self.Layout()
        event.Skip()

    def btn_guardarOnButtonClick(self, event):

        activo =  self.checkBox_estado.GetValue()
        relevancia = self.comboBox_relevancia.GetValue()
        estado = self.comboBox_estado.GetValue()
        nota = self.txt_nota.GetValue()
        contranota = self.txt_contranota.GetValue()
        id_nota = self.dic_nota['id']

        sSql = """ UPDATE notas_por_proceso SET activo = '{0}', relevancia = '{1}',  estado = '{2}', nota = '{3}', 
                            contranota = '{4}'
                    WHERE id = {5}
        """.format(activo, relevancia, estado, nota.upper(), contranota.upper(), id_nota)

        rta = Ejecutar_SQL.update_filas(sSql, 'btn_guardar  en frm_detalle_nota', BasesDeDatos.DB_PRINCIPAL)

        if rta == 1:
            wx.MessageBox(u'La nota fue actualizada correctamente', u'Atención', wx.OK | wx.ICON_INFORMATION)
            self.Destroy()
            self.padre.func_buscar()
        else:
            wx.MessageBox(u'Hemos tenido un imprevisto, no fue posible actualizar la Nota, intentalo de nuevo', u'Atención', wx.OK | wx.ICON_INFORMATION)


        event.Skip()

    ## FUNCNIONES EAY

    def cargar_valores_iniicales(self):
        self.lbl_area.SetLabel(self.dic_nota['area'])
        self.lbl_contexto.SetLabel(self.dic_nota['contexto'])
        self.lbl_fecha.SetLabel(self.dic_nota['fecha'])
        self.lbl_estado.SetLabel(self.dic_nota['estado'])
        self.txt_nota.SetLabel(self.dic_nota['nota'])
        self.txt_contranota.SetLabel(self.dic_nota['contranota'])

        self.comboBox_relevancia.Set(self.lista_relevancias)
        self.comboBox_estado.Set(['INDEFINIDO', 'REVISADO', 'PENDIENTE', 'TRAMITADO'])

        self.comboBox_relevancia.SetValue(self.dic_nota['relevancia'])
        self.comboBox_estado.SetValue(self.dic_nota['estado'])

        is_activo = self.dic_nota['activo']
        if is_activo == 'True':
            is_activo = True
            self.checkBox_estado.SetValue(is_activo)
            self.colorear_col_estado()
        else:
            is_activo = False
            self.checkBox_estado.SetValue(is_activo)
            self.lbl_estado.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.Layout()

    def colorear_col_estado(self):
        estado = self.comboBox_estado.GetValue()

        is_activo = self.checkBox_estado.GetValue()
        if is_activo == True:
            AMARILLO = wx.Colour(255, 255, 150)
            ROSADO = wx.Colour(255, 217, 230)
            AGUAMARINA = wx.Colour(208, 255, 248)

            dic_color = {'INDEFINIDO': wx.WHITE, 'REVISADO': AMARILLO, 'PENDIENTE':ROSADO , 'TRAMITADO': AGUAMARINA}

            color = dic_color[estado]
            self.lbl_estado.SetBackgroundColour(color)
        else:
            self.lbl_estado.SetBackgroundColour(wx.Colour(192, 192, 192))


