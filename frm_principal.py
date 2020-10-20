# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import time

from pyeay.red import Red

from formEAY.constantesCAC.imgCAC import Img_formularios_general as Img

WALLPAPER = Img.WALLPAPER_PRINCIPAL


###########################################################################
## Class Principal
###########################################################################

class Principal(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Producción Zuligres", pos=wx.DefaultPosition,
                          size=wx.Size(1171, 721), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(64, 64, 64))

        self.usuario = ''


        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel2.SetBackgroundColour(wx.Colour(64, 64, 64))

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel3 = wx.Panel(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel3.SetBackgroundColour(wx.Colour(64, 64, 64))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        ## ------------------------------------------------------------------------------------------------------------
        self.btn_login = wx.Button(self.m_panel3, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.Size(180, -1),
                                       wx.NO_BORDER)
        self.btn_login.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.btn_login.SetForegroundColour(wx.Colour(0, 0, 0))
        self.btn_login.SetBackgroundColour(wx.Colour(109, 253, 242))

        bSizer9.Add(self.btn_login, 0, wx.ALL, 5)

        self.m_staticline2 = wx.StaticLine(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer9.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        self.m_staticline3 = wx.StaticLine(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer9.Add(self.m_staticline3, 0, wx.EXPAND | wx.ALL, 5)

        ## ------------------------------------------------------------------------------------------------------------

        self.btn_extrusion = wx.Button(self.m_panel3, wx.ID_ANY, u"Extrusion", wx.DefaultPosition, wx.Size(180, -1),
                                       wx.NO_BORDER)
        self.btn_extrusion.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.btn_extrusion.SetForegroundColour(wx.Colour(255, 255, 255))
        self.btn_extrusion.SetBackgroundColour(wx.Colour(104, 182, 182))

        bSizer9.Add(self.btn_extrusion, 0, wx.ALL, 5)

        self.btn_cargue_vagonetas = wx.Button(self.m_panel3, wx.ID_ANY, u"Cargue Vagonetas", wx.DefaultPosition,
                                              wx.Size(180, -1), wx.NO_BORDER)
        self.btn_cargue_vagonetas.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.btn_cargue_vagonetas.SetBackgroundColour(wx.Colour(255, 201, 108))

        bSizer9.Add(self.btn_cargue_vagonetas, 0, wx.ALL, 5)

        self.btn_descargue_vagonetas = wx.Button(self.m_panel3, wx.ID_ANY, u"Descargue Vagonetas", wx.DefaultPosition,
                                                 wx.Size(180, -1), wx.NO_BORDER)
        self.btn_descargue_vagonetas.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.btn_descargue_vagonetas.SetForegroundColour(wx.Colour(255, 255, 255))
        self.btn_descargue_vagonetas.SetBackgroundColour(wx.Colour(255, 103, 102))

        bSizer9.Add(self.btn_descargue_vagonetas, 0, wx.ALL, 5)

        self.btn_cochado = wx.Button(self.m_panel3, wx.ID_ANY, u"Cochado", wx.DefaultPosition,
                                           wx.Size(180, -1),
                                           wx.NO_BORDER)
        self.btn_cochado.SetBackgroundColour(wx.Colour(187, 75, 123))
        self.btn_cochado.SetForegroundColour(wx.Colour(255, 255, 255))

        bSizer9.Add(self.btn_cochado, 0, wx.ALL, 5)



        self.btn_configuracion = wx.Button(self.m_panel3, wx.ID_ANY, u"Configuración", wx.DefaultPosition, wx.Size(180, -1),
                                      wx.NO_BORDER)
        self.btn_configuracion.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer9.Add(self.btn_configuracion, 0, wx.ALL, 5)


        self.btn_despachar_mercancia = wx.Button(self.m_panel3, wx.ID_ANY, u"Despachar Mercancia", wx.DefaultPosition, wx.Size(180, -1),
                                   wx.NO_BORDER)
        self.btn_despachar_mercancia.SetBackgroundColour(wx.Colour(109, 130, 253))
        self.btn_despachar_mercancia.SetForegroundColour(wx.Colour(255, 255, 255))

        bSizer9.Add(self.btn_despachar_mercancia, 0, wx.ALL, 5)

        self.m_staticline1 = wx.StaticLine(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer9.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)








        self.btn_configuracion_general = wx.Button(self.m_panel3, wx.ID_ANY, u"Configuración",
                                                    wx.DefaultPosition,
                                                    wx.Size(180, -1),
                                                    wx.NO_BORDER)
        self.btn_configuracion_general.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer9.Add(self.btn_configuracion_general, 0, wx.ALL, 5)

        ## _____________________________________________________________________________________________________________
        self.btn_Reportes = wx.Button(self.m_panel3, wx.ID_ANY, u"Reportes",
                                                   wx.DefaultPosition,
                                                   wx.Size(180, -1),
                                                   wx.NO_BORDER)
        self.btn_Reportes.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer9.Add(self.btn_Reportes, 0, wx.ALL, 5)
        ## _____________________________________________________________________________________________________________

        self.m_panel3.SetSizer(bSizer9)
        self.m_panel3.Layout()
        bSizer9.Fit(self.m_panel3)
        bSizer10.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        bSizer6.Add(bSizer10, 0, wx.EXPAND, 5)

        bSizer8.Add(bSizer6, 0, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap1 = wx.StaticBitmap(self.m_panel2, wx.ID_ANY,
                                         wx.Bitmap(WALLPAPER, wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer11.Add(self.m_bitmap1, 0, wx.ALL, 5)

        bSizer8.Add(bSizer11, 1, wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer8)
        self.m_panel2.Layout()
        bSizer8.Fit(self.m_panel2)
        bSizer7.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

    ## valores iniciales EAY

        self.btn_configuracion_general.Hide()
        self.ocultar_botones()

        self.Maximize()

        self.cargar_valores_de_inicializacion()

        # Connect Events
        self.btn_extrusion.Bind(wx.EVT_BUTTON, self.btn_extrusionOnButtonClick)
        self.btn_cargue_vagonetas.Bind(wx.EVT_BUTTON, self.btn_cargue_vagonetasOnButtonClick)
        self.btn_descargue_vagonetas.Bind(wx.EVT_BUTTON, self.btn_descargue_vagonetasOnButtonClick)
        self.btn_configuracion.Bind(wx.EVT_BUTTON, self.btn_configuracionOnButtonClick)
        self.btn_despachar_mercancia.Bind(wx.EVT_BUTTON, self.btn_despachar_mercanciaOnButtonClick)
        self.btn_configuracion_general.Bind(wx.EVT_BUTTON, self.btn_configuracion_generalOnButtonClick)
        self.btn_login.Bind(wx.EVT_BUTTON, self.btn_loginOnButtonClick)
        self.btn_Reportes.Bind(wx.EVT_BUTTON, self.btn_ReportesOnButtonClick)
        self.btn_cochado.Bind(wx.EVT_BUTTON, self.btn_cochadoOnButtonClick)


    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btn_cochadoOnButtonClick(self, event):
        obj_red = Red()
        dir_mac = obj_red.dir_mac

        import formEAY.formularios.frm_procesos.frm_cochado as frm_cochado
        frame_cochado = frm_cochado.Cochado(self, self.usuario, dir_mac)
        frame_cochado.Center()
        frame_cochado.Show()
        event.Skip()


    def btn_ReportesOnButtonClick(self, event):
        import formEAY.formularios.frm_reportes.frm_gestion_reportes as frm_gestion_reportes
        frame_gestion_reportes = frm_gestion_reportes.Reportes(self)
        frame_gestion_reportes.Center()
        frame_gestion_reportes.Show()
        event.Skip()

    def btn_loginOnButtonClick(self, event):
        if self.btn_login.GetLabel()  != 'Salir':
            import formEAY.formularios.frm_generales.frm_login as frm_login
            frame_login = frm_login.Login(self)
            frame_login.Center()
            frame_login.Show()
        else:
            self.Destroy()

        event.Skip()

    def btn_configuracion_generalOnButtonClick(self, event):
        # import formEAY.formularios.frm_generales.frm_configuracion_general as frm_configuracion_general
        # frame_ConfiguracionGeneral = frm_configuracion_general.ConfiguracionGeneral(self)
        # frame_ConfiguracionGeneral.Center()
        # frame_ConfiguracionGeneral.Show()



        event.Skip()

    def btn_produccion_por_periodoOnButtonClick(self, event):
        event.Skip()

    def btn_extrusionOnButtonClick(self, event):
        obj_red = Red()
        dir_mac = obj_red.dir_mac

        import formEAY.formularios.frm_procesos.frm_extrusion as frm_extrusion
        frame_extrusion = frm_extrusion.Extrusion(self, self.usuario, dir_mac)
        frame_extrusion.Center()
        frame_extrusion.Show()
        event.Skip()

    def btn_cargue_vagonetasOnButtonClick(self, event):
        obj_red = Red()
        dir_mac = obj_red.dir_mac

        import formEAY.formularios.frm_procesos.frm_cargue_vagonetas as frm_cargue_vagonetas
        frame_cargue_vagonetas = frm_cargue_vagonetas.CargueVagonetas(self, self.usuario, dir_mac)
        frame_cargue_vagonetas.Center()
        frame_cargue_vagonetas.Show()
        event.Skip()

    def btn_descargue_vagonetasOnButtonClick(self, event):
        obj_red = Red()
        dir_mac = obj_red.dir_mac

        import formEAY.formularios.frm_procesos.frm_descargue_vagonetas as frm_descargue_vagonetas
        frame_descargue_vagonetas = frm_descargue_vagonetas.DescargueVagonetas(self, self.usuario, dir_mac)
        frame_descargue_vagonetas.Center()
        frame_descargue_vagonetas.Show()
        event.Skip()

    def btn_configuracionOnButtonClick(self, event):
        import formEAY.formularios.frm_generales.frm_configuracion_general as frm_configuracion_general
        frame_configuracion_general = frm_configuracion_general.Configuracion(self)
        frame_configuracion_general.Center()
        frame_configuracion_general.Show()
        event.Skip()

    def btn_reporte_inventarioOnButtonClick(self, event):
        event.Skip()

    def btn_despachar_mercanciaOnButtonClick(self, event):
        obj_red = Red()
        dir_mac = obj_red.dir_mac

        import formEAY.formularios.frm_inventario.frm_despachar_mercancia  as frm_despachar_mercancia
        frame_despachar_mercancia = frm_despachar_mercancia.DespacharMercancia(self, self.usuario, dir_mac)
        frame_despachar_mercancia.Center()
        frame_despachar_mercancia.Show()
        event.Skip()

## FUNCIONES EAY

    def cargar_valores_de_inicializacion(self):
        #self.btn_configuracion.Hide()
        #self.btn_reporte_inventario.Hide()
        pass

    def ocultar_botones(self):
        self.btn_Reportes.Hide()
        self.btn_extrusion.Hide()
        self.btn_cargue_vagonetas.Hide()
        self.btn_descargue_vagonetas.Hide()
        self.btn_configuracion.Hide()
        self.btn_despachar_mercancia.Hide()
        self.btn_cochado.Hide()

    def mostrar_botones(self, acceso, usuario):
        obj_red = Red()

        nom_equipo = obj_red.nombre_equipo
        ip_lan = obj_red.ip_lan

        self.usuario = usuario
        self.ocultar_botones()


        cad = 'Produccón Zuligres     ' + nom_equipo + '/' + ip_lan + '@' + usuario

        self.SetLabel(cad)

        if acceso == 'EXTRUSION':
            self.btn_extrusion.Show()
        if acceso == 'CARGUE DE VAGONETAS':
            self.btn_cargue_vagonetas.Show()
        if acceso == 'DESCARGUE DE VAGONETAS':
            self.btn_descargue_vagonetas.Show()
        if acceso == 'COCHADO':
            self.btn_cochado.Show()
        if acceso == 'DESPACHO DE MERCANCIA':
            self.btn_despachar_mercancia.Show()
        if acceso == 'DIGITADOR PROCESOS':
            self.btn_extrusion.Show()
            self.btn_cargue_vagonetas.Show()
            self.btn_descargue_vagonetas.Show()
            self.btn_cochado.Show()
        if acceso == 'DIGITADOR':
            self.btn_extrusion.Show()
            self.btn_cargue_vagonetas.Show()
            self.btn_descargue_vagonetas.Show()
            self.btn_despachar_mercancia.Show()
            self.btn_cochado.Show()
        if acceso == 'ADMINISTRADOR':
            self.btn_extrusion.Show()
            self.btn_cargue_vagonetas.Show()
            self.btn_descargue_vagonetas.Show()
            self.btn_despachar_mercancia.Show()
            self.btn_configuracion.Show()
            self.btn_cochado.Show()
            self.btn_Reportes.Show()
        if acceso == 'SUPERUSUSARIO':
            self.btn_extrusion.Show()
            self.btn_cargue_vagonetas.Show()
            self.btn_descargue_vagonetas.Show()
            self.btn_despachar_mercancia.Show()
            self.btn_configuracion.Show()
            self.btn_cochado.Show()
            self.btn_Reportes.Show()
        if acceso == 'ROOT':
            self.btn_extrusion.Show()
            self.btn_cargue_vagonetas.Show()
            self.btn_descargue_vagonetas.Show()
            self.btn_despachar_mercancia.Show()
            self.btn_configuracion.Show()
            self.btn_cochado.Show()
            self.btn_Reportes.Show()

        self.btn_login.SetLabel('Salir')
        self.Refresh()
        self.Layout()
