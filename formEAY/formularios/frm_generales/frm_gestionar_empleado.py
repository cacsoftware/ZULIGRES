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

from formEAY.constantesCAC.imgCAC import Img_grillas, Img_formularios_general
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

from pyeay.dbcac.conexiondb import Ejecutar_SQL
from pyeay.grillas import ManipularGrillas


###########################################################################
## Class GestionarProductos
###########################################################################

class GestionarEmpleado(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Gestionar Empleados", pos=wx.DefaultPosition,
                          size=wx.Size(971, 729), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(760, -1), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.orden_ascendente = True
        self.columna = 0

        icono_formularios = Img_formularios_general()

        bSizer23 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel3.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_principal = wx.BoxSizer(wx.VERTICAL)

        bSizer25 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText29 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Gestión de Empleados", wx.DefaultPosition,
                                            wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText29.Wrap(-1)
        self.m_staticText29.SetFont(wx.Font(11, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText29.SetForegroundColour(wx.Colour(255, 128, 64))

        bSizer25.Add(self.m_staticText29, 1, wx.ALL, 5)

        bSizer26 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_mostrar = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Mostrar:", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.lbl_etq_mostrar.Wrap(-1)
        bSizer26.Add(self.lbl_etq_mostrar, 0, wx.ALL, 5)

        comboBox_mostrarChoices = [u"ACTIVOS", u"NO ACTIVOS", u"TODOS"]
        self.comboBox_mostrar = wx.ComboBox(self.m_panel3, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize,
                                            comboBox_mostrarChoices, wx.CB_READONLY)
        self.comboBox_mostrar.SetSelection(0)
        bSizer26.Add(self.comboBox_mostrar, 0, wx.ALL, 5)

        self.btn_actualizar = wx.BitmapButton(self.m_panel3, wx.ID_ANY, wx.Bitmap(
            icono_formularios.ACTUALIZAR_FORMULARIO, wx.BITMAP_TYPE_ANY),
                                              wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW | wx.NO_BORDER)

        self.btn_actualizar.SetBitmapCurrent(
            wx.Bitmap(icono_formularios.ACTUALIZAR_FORMULARIO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer26.Add(self.btn_actualizar, 0, wx.ALL, 5)

        bSizer25.Add(bSizer26, 0, 0, 5)

        bSizer_principal.Add(bSizer25, 0, wx.EXPAND, 5)

        bSizer28 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline1 = wx.StaticLine(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer28.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_principal.Add(bSizer28, 0, wx.EXPAND, 5)

        bSizer27 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_vacio = wx.StaticText(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.lbl_etq_vacio.Wrap(-1)
        bSizer27.Add(self.lbl_etq_vacio, 1, wx.ALL, 5)

        self.btn_limpiar = wx.Button(self.m_panel3, wx.ID_ANY, u"&Limpiar", wx.DefaultPosition, wx.DefaultSize,
                                     wx.NO_BORDER)
        self.btn_limpiar.SetBackgroundColour(wx.Colour(183, 183, 255))

        bSizer27.Add(self.btn_limpiar, 0, wx.ALL, 5)

        self.btn_guardar = wx.Button(self.m_panel3, wx.ID_ANY, u"&Crear Empleado", wx.DefaultPosition, wx.DefaultSize,
                                     wx.NO_BORDER)
        self.btn_guardar.SetBackgroundColour(wx.Colour(117, 255, 186))

        bSizer27.Add(self.btn_guardar, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer_principal.Add(bSizer27, 0, wx.EXPAND, 5)

        bSizer29 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_id = wx.StaticText(self.m_panel3, wx.ID_ANY, u"id:", wx.DefaultPosition, wx.Size(15, -1),
                                        wx.ALIGN_RIGHT)
        self.lbl_etq_id.Wrap(-1)
        bSizer29.Add(self.lbl_etq_id, 0, wx.ALL, 5)

        self.lbl_id = wx.StaticText(self.m_panel3, wx.ID_ANY, u"1025", wx.DefaultPosition, wx.Size(35, -1), 0)
        self.lbl_id.Wrap(-1)
        bSizer29.Add(self.lbl_id, 0, wx.ALL, 5)

        self.lbl_etq_producto = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.Size(55, -1),
                                              wx.ALIGN_RIGHT)
        self.lbl_etq_producto.Wrap(-1)
        bSizer29.Add(self.lbl_etq_producto, 0, wx.ALL, 5)

        self.txt_nombre = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        bSizer29.Add(self.txt_nombre, 1, wx.ALL, 5)

        self.lbl_etq_apellido1 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Apellido 1:", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.lbl_etq_apellido1.Wrap(-1)
        bSizer29.Add(self.lbl_etq_apellido1, 0, wx.ALL, 5)

        self.txt_apellido1 = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                         0)
        bSizer29.Add(self.txt_apellido1, 1, wx.ALL, 5)

        self.lbl_etq_apellido2 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Apellido 2:", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.lbl_etq_apellido2.Wrap(-1)
        bSizer29.Add(self.lbl_etq_apellido2, 0, wx.ALL, 5)

        self.txt_apellido2 = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                         0)
        bSizer29.Add(self.txt_apellido2, 1, wx.ALL, 5)

        self.checkBox_activo = wx.CheckBox(self.m_panel3, wx.ID_ANY, u"Activo", wx.DefaultPosition, wx.Size(80, -1), 0)
        self.checkBox_activo.SetValue(True)
        bSizer29.Add(self.checkBox_activo, 0, wx.ALL, 5)

        bSizer_principal.Add(bSizer29, 0, wx.EXPAND, 5)

        bSizer31 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_nit = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Nit:", wx.DefaultPosition, wx.Size(125, -1),
                                         wx.ALIGN_RIGHT)
        self.lbl_etq_nit.Wrap(-1)
        bSizer31.Add(self.lbl_etq_nit, 0, wx.ALL, 5)

        self.txt_nit = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer31.Add(self.txt_nit, 1, wx.ALL, 5)

        self.lbl_etq_celular = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Celular:", wx.DefaultPosition, wx.Size(80, -1),
                                             wx.ALIGN_RIGHT)
        self.lbl_etq_celular.Wrap(-1)
        bSizer31.Add(self.lbl_etq_celular, 0, wx.ALL, 5)

        self.txt_celular = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer31.Add(self.txt_celular, 1, wx.ALL, 5)

        self.lbl_etq_telefono = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Telf:", wx.DefaultPosition, wx.Size(70, -1),
                                              wx.ALIGN_RIGHT)
        self.lbl_etq_telefono.Wrap(-1)
        bSizer31.Add(self.lbl_etq_telefono, 0, wx.ALL, 5)

        self.txt_telefono = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer31.Add(self.txt_telefono, 1, wx.ALL, 5)

        self.lbl_fecha_nacimiento = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Fecha Nacimiento:", wx.DefaultPosition,
                                                  wx.Size(-1, -1), wx.ALIGN_RIGHT)
        self.lbl_fecha_nacimiento.Wrap(-1)
        bSizer31.Add(self.lbl_fecha_nacimiento, 0, wx.ALL, 5)

        self.txt_fecha_nacimiento = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        bSizer31.Add(self.txt_fecha_nacimiento, 0, wx.ALL, 5)

        bSizer_principal.Add(bSizer31, 0, wx.EXPAND, 5)

        bSizer33 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_rh = wx.StaticText(self.m_panel3, wx.ID_ANY, u"RH:", wx.DefaultPosition, wx.Size(125, -1),
                                        wx.ALIGN_RIGHT)
        self.lbl_etq_rh.Wrap(-1)
        bSizer33.Add(self.lbl_etq_rh, 0, wx.ALL, 5)

        comboBox_rhChoices = [u"A+", u"A-", u"B+", u"AB+", u"AB-", u"B-",  u"O+",  u"O-"]
        self.comboBox_rh = wx.ComboBox(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       comboBox_rhChoices, wx.CB_READONLY)
        bSizer33.Add(self.comboBox_rh, 0, wx.ALL, 5)

        self.lbl_etq_direccion = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Dirección:", wx.DefaultPosition,
                                               wx.Size(-1, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_direccion.Wrap(-1)
        bSizer33.Add(self.lbl_etq_direccion, 0, wx.ALL, 5)

        self.txt_direccion = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                         0)
        self.txt_direccion.SetMinSize(wx.Size(60, -1))

        bSizer33.Add(self.txt_direccion, 3, wx.ALL, 5)

        self.lbl_etq_ciudad = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Ciudad:", wx.DefaultPosition, wx.Size(-1, -1),
                                            wx.ALIGN_RIGHT)
        self.lbl_etq_ciudad.Wrap(-1)
        bSizer33.Add(self.lbl_etq_ciudad, 0, wx.ALL, 5)

        self.txt_ciudad = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.txt_ciudad.SetMinSize(wx.Size(60, -1))

        bSizer33.Add(self.txt_ciudad, 1, wx.ALL, 5)

        bSizer_principal.Add(bSizer33, 0, wx.EXPAND, 5)

        bSizer331 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_area_de_trabajo = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Area de Trabajo:", wx.DefaultPosition,
                                                     wx.Size(125, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_area_de_trabajo.Wrap(-1)
        bSizer331.Add(self.lbl_etq_area_de_trabajo, 0, wx.ALL, 5)

        comboBox_area_trabajoChoices = [u"A", u"B", u"CARGUE DE VAGONETAS"]
        self.comboBox_area_trabajo = wx.ComboBox(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                 wx.DefaultSize, comboBox_area_trabajoChoices, wx.CB_READONLY)
        bSizer331.Add(self.comboBox_area_trabajo, 0, wx.ALL, 5)

        self.chk_obrero = wx.CheckBox(self.m_panel3, wx.ID_ANY, u"Obrero", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer331.Add(self.chk_obrero, 0, wx.ALL, 5)

        self.chk_adminitrativo = wx.CheckBox(self.m_panel3, wx.ID_ANY, u"Administrativo", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        bSizer331.Add(self.chk_adminitrativo, 0, wx.ALL, 5)

        self.chk_directivo = wx.CheckBox(self.m_panel3, wx.ID_ANY, u"Directivo", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer331.Add(self.chk_directivo, 0, wx.ALL, 5)

        bSizer_principal.Add(bSizer331, 0, wx.EXPAND, 5)

        bSizer311 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_contacto = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Contacto:", wx.DefaultPosition,
                                              wx.Size(125, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_contacto.Wrap(-1)
        bSizer311.Add(self.lbl_etq_contacto, 0, wx.ALL, 5)

        self.txt_contacto = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer311.Add(self.txt_contacto, 3, wx.ALL, 5)

        self.lbl_etq_celular_contacto = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Celular Contacto:",
                                                      wx.DefaultPosition, wx.Size(-1, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_celular_contacto.Wrap(-1)
        bSizer311.Add(self.lbl_etq_celular_contacto, 0, wx.ALL, 5)

        self.txt_cel_contacto = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bSizer311.Add(self.txt_cel_contacto, 1, wx.ALL, 5)

        bSizer_principal.Add(bSizer311, 0, wx.EXPAND, 5)

        self.grid_empleados = wx.grid.Grid(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_empleados.CreateGrid(0, 18)
        self.grid_empleados.EnableEditing(False)
        self.grid_empleados.EnableGridLines(True)
        self.grid_empleados.EnableDragGridSize(False)
        self.grid_empleados.SetMargins(0, 0)

        # Columns
        self.grid_empleados.AutoSizeColumns()
        self.grid_empleados.EnableDragColMove(False)
        self.grid_empleados.EnableDragColSize(True)
        self.grid_empleados.SetColLabelSize(30)
        self.grid_empleados.SetColLabelValue(0, u"id")
        self.grid_empleados.SetColLabelValue(1, u"Nombre")
        self.grid_empleados.SetColLabelValue(2, u"Apellido 1")
        self.grid_empleados.SetColLabelValue(3, u"apellido 2")
        self.grid_empleados.SetColLabelValue(4, u"Nit")
        self.grid_empleados.SetColLabelValue(5, u"Celular")
        self.grid_empleados.SetColLabelValue(6, u"RH")
        self.grid_empleados.SetColLabelValue(7, u"Area de Trabajo")
        self.grid_empleados.SetColLabelValue(8, u"Obrero")
        self.grid_empleados.SetColLabelValue(9, u"Administrativo")
        self.grid_empleados.SetColLabelValue(10, u"Directivo")
        self.grid_empleados.SetColLabelValue(11, u"Activo")

        self.grid_empleados.SetColLabelValue(12, u"telefono")
        self.grid_empleados.SetColLabelValue(13, u"Fecha Nacimiento")
        self.grid_empleados.SetColLabelValue(14, u"Direccion")
        self.grid_empleados.SetColLabelValue(15, u"Ciudad")
        self.grid_empleados.SetColLabelValue(16, u"Contacto")
        self.grid_empleados.SetColLabelValue(17, u"Celular contacto")
        self.grid_empleados.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_empleados.EnableDragRowSize(True)
        self.grid_empleados.SetRowLabelSize(50)
        self.grid_empleados.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_empleados.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_empleados.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.grid_empleados.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        bSizer_principal.Add(self.grid_empleados, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer_principal)
        self.m_panel3.Layout()
        bSizer_principal.Fit(self.m_panel3)
        bSizer23.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer23)

        ## VALORES INICIALEAS EAY
        self.cargar_valores_de_inicializacion()
        self.grid_empleados.AutoSizeColumns()


        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.comboBox_mostrar.Bind(wx.EVT_COMBOBOX, self.comboBox_mostrarOnCombobox)
        self.btn_actualizar.Bind(wx.EVT_BUTTON, self.btn_actualizarOnButtonClick)
        self.btn_limpiar.Bind(wx.EVT_BUTTON, self.btn_limpiarOnButtonClick)
        self.btn_guardar.Bind(wx.EVT_BUTTON, self.btn_guardarOnButtonClick)
        self.comboBox_rh.Bind(wx.EVT_COMBOBOX, self.comboBox_mostrarOnCombobox)
        self.comboBox_area_trabajo.Bind(wx.EVT_COMBOBOX, self.comboBox_mostrarOnCombobox)
        self.grid_empleados.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_empleadosOnGridCellLeftClick)
        self.grid_empleados.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK,
                                 self.grid_empleadosOnGridLabelLeftDClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def comboBox_mostrarOnCombobox(self, event):
        seleccion = self.comboBox_mostrar.GetValue()
        self.cargar_grid_empleados(seleccion)
        event.Skip()

    def btn_actualizarOnButtonClick(self, event):
        self.cargar_valores_de_inicializacion()
        self.func_limpiar_controles()
        self.comboBox_mostrar.SetValue('ACTIVOS')
        event.Skip()

    def btn_limpiarOnButtonClick(self, event):
        self.func_limpiar_controles()
        event.Skip()

    def btn_guardarOnButtonClick(self, event):
        #rta = self.func_validar_entrada_datos()
        rta = 1
        if rta == 0:
            return 0
        else:
            tipo_guardar = self.btn_guardar.GetLabel()
            if tipo_guardar == 'Crear Empleado':
                rta = self.func_guardar_nuevo_empleado()
            if tipo_guardar == 'Guardar Cambios':
                rta = self.func_actualizar_producto()
            if rta == 1:
                wx.MessageBox(u'El proceso se ha realizado de manera correcta', u'Atención',
                              wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox(u'Se ha presentado un inconveniente, no fue posible realizar la operación', u'Atención',
                              wx.OK | wx.ICON_INFORMATION)

            seleccion = self.comboBox_mostrar.GetValue()
            self.cargar_grid_empleados(seleccion)

            self.func_ordenarGrillaPorColumna(self.columna, self.orden_ascendente)
        event.Skip()

    def grid_empleadosOnGridCellLeftClick(self, event):
        fila = event.GetRow()

        is_activo = 0

        self.lbl_id.SetLabel(self.grid_empleados.GetCellValue(fila, 0))
        self.txt_nombre.SetValue(self.grid_empleados.GetCellValue(fila, 1))

        self.txt_apellido1.SetValue(self.grid_empleados.GetCellValue(fila, 2))

        self.txt_apellido2.SetValue(self.grid_empleados.GetCellValue(fila, 3))
        self.txt_nit.SetValue(self.grid_empleados.GetCellValue(fila, 4))
        self.txt_celular.SetValue(self.grid_empleados.GetCellValue(fila, 5))
        self.comboBox_rh.SetValue(self.grid_empleados.GetCellValue(fila, 6))
        self.comboBox_area_trabajo.SetValue(self.grid_empleados.GetCellValue(fila, 7))

        if self.grid_empleados.GetCellValue(fila, 8) == 'True':
            is_obrero = 1
        else:
            is_obrero = 0
        self.chk_obrero.SetValue(is_obrero)

        if self.grid_empleados.GetCellValue(fila, 9) == 'True':
            is_administrativo = 1
        else:
            is_administrativo = 0
        self.chk_adminitrativo.SetValue(is_administrativo)

        if self.grid_empleados.GetCellValue(fila, 10) == 'True':
            is_directivo = 1
        else:
            is_directivo = 0
        self.chk_directivo.SetValue(is_directivo)


        if self.grid_empleados.GetCellValue(fila, 11) == 'True':
            is_activo = 1
        else:
            is_activo = 0
        self.checkBox_activo.SetValue(is_activo)

        self.txt_telefono.SetValue(self.grid_empleados.GetCellValue(fila, 12))
        self.txt_fecha_nacimiento.SetValue(self.grid_empleados.GetCellValue(fila, 13))
        self.txt_direccion.SetValue(self.grid_empleados.GetCellValue(fila, 14))
        self.txt_ciudad.SetValue(self.grid_empleados.GetCellValue(fila, 15))
        self.txt_contacto.SetValue(self.grid_empleados.GetCellValue(fila, 16))
        self.txt_cel_contacto.SetValue(self.grid_empleados.GetCellValue(fila, 17))

        self.btn_guardar.SetLabel('Guardar Cambios')
        self.Layout()

        event.Skip()


    def grid_empleadosOnGridLabelLeftDClick(self, event):
        columna = event.GetCol()

        if self.orden_ascendente == True:
            self.orden_ascendente = False
        else:
            self.orden_ascendente = True

        self.func_ordenarGrillaPorColumna(columna, self.orden_ascendente)

        # self.colorearGrilla()
        event.Skip()

    ##  FUNCIONES EAY
    def func_guardar_nuevo_empleado(self):
        nombre            = self.txt_nombre.GetValue()
        apellido1         = self.txt_apellido1.GetValue()
        apellido2         = self.txt_apellido2.GetValue()
        nit               = self.txt_nit.GetValue()
        celular           = self.txt_celular.GetValue()
        telf              = self.txt_telefono.GetValue()
        rh                = self.comboBox_rh.GetValue()
        direccion         = self.txt_direccion.GetValue()
        ciudad            = self.txt_ciudad.GetValue()
        area_trabajo      = self.comboBox_area_trabajo.GetValue()
        contacto          = self.txt_contacto.GetValue()
        celular_contacto  = self.txt_cel_contacto.GetValue()

        is_obrero         = self.chk_obrero.GetValue()
        is_administrativo = self.chk_adminitrativo.GetValue()
        is_directivo      = self.chk_directivo.GetValue()

        activo =  True  #self.checkBox_activo.GetValue()

        sSql = """
                INSERT INTO empleado (  nom, ape1, ape2, nit, celular, telf, rh, dir, ciudad,
                                        area_trabajo, nomcontacto1, celcontacto1, is_obrero, is_administrativo, 
                                        is_directivo, activo) 
                                VALUES (
                                        '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', 
                                        '{9}', '{10}', '{11}', '{12}', '{13}', 
                                        '{14}', '{15}'                                
                                )
        """.format(nombre, apellido1, apellido2, nit, celular, telf, rh, direccion, ciudad, area_trabajo, contacto,
                   celular_contacto, is_obrero, is_administrativo, is_directivo, activo)

        rta = Ejecutar_SQL.insert_filas(sSql.upper(),'frm_gestionar_empleado/func_guardar_nuevo_empleado', BasesDeDatos.DB_PRINCIPAL)
        return  rta

    def func_actualizar_producto(self):
        id_empleado = self.lbl_id.GetLabel()
        nombre = self.txt_nombre.GetValue()
        apellido1 = self.txt_apellido1.GetValue()
        apellido2 = self.txt_apellido2.GetValue()
        nit = self.txt_nit.GetValue()
        celular = self.txt_celular.GetValue()
        telf = self.txt_telefono.GetValue()
        rh = self.comboBox_rh.GetValue()
        direccion = self.txt_direccion.GetValue()
        ciudad = self.txt_ciudad.GetValue()
        area_trabajo = self.comboBox_area_trabajo.GetValue()
        contacto = self.txt_contacto.GetValue()
        celular_contacto = self.txt_cel_contacto.GetValue()
        is_obrero = self.chk_obrero.GetValue()
        is_administrativo = self.chk_adminitrativo.GetValue()
        is_directivo = self.chk_directivo.GetValue()
        activo = True  # self.checkBox_activo.GetValue()

        sSql = """
                    UPDATE empleado SET 
                        nom = '{0}',  ape1 = '{1}',  ape2 = '{2}',  nit= '{3}',  celular = '{4}',  telf = '{5}',  rh = '{6}', dir = '{7}',  ciudad = '{8}',
                        area_trabajo = '{9}',  nomcontacto1 = '{10}',  celcontacto1 = '{11}',  is_obrero = '{12}',  is_administrativo = '{13}',  
                        is_directivo = '{14}', activo = '{15}'
                    WHERE id_empleado = {16}
                """.format(nombre, apellido1, apellido2, nit, celular, telf, rh, direccion, ciudad, area_trabajo, contacto,
                   celular_contacto, is_obrero, is_administrativo, is_directivo, activo, id_empleado)

        rta = Ejecutar_SQL.update_filas(sSql.upper(), 'frm_gestionar_productos/func_actualizar_producto', BasesDeDatos.DB_PRINCIPAL)
        return rta

    def func_ordenarGrillaPorColumna(self, columna, orden_ascendente):

        self.columna = columna

        lista_tipoColumna = ['int', 'str', 'str', 'str', 'str', 'str', 'str',
                             'str', 'str', 'str', 'str', 'str', 'str',
                             'str', 'str', 'str', 'str', 'str', 'str', 'str']

        ManipularGrillas.ordenarGrillaPorColumna(self.grid_empleados,  self.columna, lista_tipoColumna,
                                                 orden_ascendente)

    def func_limpiar_controles(self):
        is_activo = 0

        self.lbl_id.SetLabel('')
        self.txt_nombre.SetValue('')
        self.txt_apellido1.SetValue('')
        self.txt_apellido2.SetValue('')
        self.txt_nit.SetValue('')
        self.txt_celular.SetValue('')
        self.txt_telefono.SetValue('')
        self.txt_ciudad.SetValue('')
        self.txt_contacto.SetValue('')
        self.txt_cel_contacto.SetValue('')
        self.txt_direccion.SetValue('')

        self.checkBox_activo.SetValue(is_activo)

        self.chk_directivo.SetValue(is_activo)
        self.chk_obrero.SetValue(is_activo)
        self.chk_adminitrativo.SetValue(is_activo)

        self.comboBox_area_trabajo.SetSelection(-1)
        self.comboBox_rh.SetSelection(-1)

        self.btn_guardar.SetLabel('Crear Empleado')
        self.Layout()

    def cargar_valores_de_inicializacion(self):
        from formEAY.constantesCAC.constantesCAC import AreasProduccion

        list_columnas = [12, 13, 14, 15, 16, 17]
        ManipularGrillas.ocultarColumnasGrilla(self.grid_empleados, list_columnas)

        self.lbl_fecha_nacimiento.Hide()
        self.txt_fecha_nacimiento.Hide()

        lista_areas_producccion = AreasProduccion.list_areas_produccion
        self.comboBox_area_trabajo.Set(lista_areas_producccion)

        self.grid_empleados.AutoSizeColumns()
        self.btn_guardar.SetLabel('Crear Empleado')
        self.cargar_grid_empleados('ACTIVOS')

    def cargar_grid_empleados(self, opcion_carga):
        dic_sel_carga = {'ACTIVOS': ' WHERE activo = True',
                         'NO ACTIVOS': ' WHERE activo = False',
                         'TODOS': ' '}

        sSql = """
                SELECT id_empleado, nom, ape1, ape2, nit, celular, rh, area_trabajo, is_obrero, is_administrativo, 
                        is_directivo, activo, telf, fecha_nacimiento, dir, ciudad, nomcontacto1, celcontacto1
                FROM empleado
                {0}
        """.format(dic_sel_carga[opcion_carga])

        rows = Ejecutar_SQL.select_varios_registros(sSql,  'frm_gestionarproductos/func_cargar_grilla_productos', 500, BasesDeDatos.DB_PRINCIPAL)

        ManipularGrillas.llenarGrilla(self.grid_empleados, rows)


