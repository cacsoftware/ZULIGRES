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
from pyeay.validator import validador_solo_digitos

############# ##############################################################
## Class GestionarProductos
###########################################################################

class GestionarProductos(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Gestionar Productos", pos=wx.DefaultPosition,
                          size=wx.Size(906, 729), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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

        self.m_staticText29 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Gestión de Productos", wx.DefaultPosition,
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

        bSizer29 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_id = wx.StaticText(self.m_panel3, wx.ID_ANY, u"id:", wx.DefaultPosition, wx.Size(15, -1),
                                        wx.ALIGN_RIGHT)
        self.lbl_etq_id.Wrap(-1)
        bSizer29.Add(self.lbl_etq_id, 0, wx.ALL, 5)

        self.lbl_id = wx.StaticText(self.m_panel3, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size(35, -1), 0)
        self.lbl_id.Wrap(-1)
        bSizer29.Add(self.lbl_id, 0, wx.ALL, 5)

        self.lbl_etq_producto = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Producto:", wx.DefaultPosition,
                                              wx.Size(55, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_producto.Wrap(-1)
        bSizer29.Add(self.lbl_etq_producto, 0, wx.ALL, 5)

        self.txt_producto = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1),
                                        0)
        bSizer29.Add(self.txt_producto, 2, wx.ALL, 5)

        self.lbl_etq_cat = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Cat:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_cat.Wrap(-1)
        bSizer29.Add(self.lbl_etq_cat, 0, wx.ALL, 5)

        comboBox_categoriaChoices = [u"A", u"B", u"C"]
        self.comboBox_categoria = wx.ComboBox(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, comboBox_categoriaChoices, wx.CB_READONLY)
        bSizer29.Add(self.comboBox_categoria, 0, wx.ALL, 5)

        self.checkBox_activo = wx.CheckBox(self.m_panel3, wx.ID_ANY, u"Activo", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer29.Add(self.checkBox_activo, 1, wx.ALL, 5)

        bSizer27.Add(bSizer29, 3, wx.EXPAND, 5)

        bSizer30 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_limpiar = wx.Button(self.m_panel3, wx.ID_ANY, u"&Limpiar", wx.DefaultPosition, wx.DefaultSize,
                                     wx.NO_BORDER)
        self.btn_limpiar.SetBackgroundColour(wx.Colour(183, 183, 255))

        bSizer30.Add(self.btn_limpiar, 0, wx.ALL, 5)

        self.btn_guardar = wx.Button(self.m_panel3, wx.ID_ANY, u"&Crear Producto", wx.DefaultPosition, wx.DefaultSize,
                                     wx.NO_BORDER)
        self.btn_guardar.SetBackgroundColour(wx.Colour(117, 255, 186))

        bSizer30.Add(self.btn_guardar, 0, wx.ALL, 5)

        bSizer27.Add(bSizer30, 0, wx.EXPAND, 5)

        bSizer_principal.Add(bSizer27, 0, wx.EXPAND, 5)

        bSizer31 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_peso = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Peso (gr):", wx.DefaultPosition, wx.Size(125, -1),
                                          wx.ALIGN_RIGHT)
        self.lbl_etq_peso.Wrap(-1)
        bSizer31.Add(self.lbl_etq_peso, 0, wx.ALL, 5)

        self.txt_peso = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, validator= validador_solo_digitos())
        bSizer31.Add(self.txt_peso, 1, wx.ALL, 5)

        self.lbl_etq_largo = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Largo (cm):", wx.DefaultPosition,
                                           wx.Size(80, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_largo.Wrap(-1)
        bSizer31.Add(self.lbl_etq_largo, 0, wx.ALL, 5)

        self.txt_largo = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer31.Add(self.txt_largo, 1, wx.ALL, 5)

        self.lbl_etq_ancho = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Ancho (cm):", wx.DefaultPosition,
                                           wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_ancho.Wrap(-1)
        bSizer31.Add(self.lbl_etq_ancho, 0, wx.ALL, 5)

        self.txt_ancho = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer31.Add(self.txt_ancho, 1, wx.ALL, 5)

        self.lbl_alto = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Alto (cm):", wx.DefaultPosition, wx.Size(70, -1),
                                      wx.ALIGN_RIGHT)
        self.lbl_alto.Wrap(-1)
        bSizer31.Add(self.lbl_alto, 0, wx.ALL, 5)

        self.txt_alto = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer31.Add(self.txt_alto, 1, wx.ALL, 5)

        bSizer_principal.Add(bSizer31, 0, wx.EXPAND, 5)

        bSizer33 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_stock_min = wx.StaticText(self.m_panel3, wx.ID_ANY, u"stock Minimo:", wx.DefaultPosition,
                                           wx.Size(125, -1), wx.ALIGN_RIGHT)
        self.lbl_stock_min.Wrap(-1)
        bSizer33.Add(self.lbl_stock_min, 0, wx.ALL, 5)

        self.txt_stock_minimo = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(-1, -1), validator= validador_solo_digitos())
        self.txt_stock_minimo.SetMinSize(wx.Size(60, -1))

        bSizer33.Add(self.txt_stock_minimo, 1, wx.ALL, 5)

        self.lbl_etq_stock_maximo = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Stock Máximo:", wx.DefaultPosition,
                                                  wx.Size(-1, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_stock_maximo.Wrap(-1)
        bSizer33.Add(self.lbl_etq_stock_maximo, 0, wx.ALL, 5)

        self.txt_stock_maximo = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(-1, -1), validator= validador_solo_digitos())
        self.txt_stock_maximo.SetMinSize(wx.Size(60, -1))

        bSizer33.Add(self.txt_stock_maximo, 1, wx.ALL, 5)

        ## ************************************************
        self.lbl_etq_unid_coche = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Unid / coche:", wx.DefaultPosition,
                                                   wx.Size(-1, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_unid_coche.Wrap(-1)
        bSizer33.Add(self.lbl_etq_unid_coche, 0, wx.ALL, 5)

        self.txt_unid_x_coche = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.Size(-1, -1), validator=validador_solo_digitos())
        self.txt_unid_x_coche.SetMinSize(wx.Size(60, -1))

        bSizer33.Add(self.txt_unid_x_coche, 1, wx.ALL, 5)

        self.lbl_etq_unid_estiba = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Unid / Estiba:", wx.DefaultPosition,
                                                wx.Size(-1, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_unid_estiba.Wrap(-1)
        bSizer33.Add(self.lbl_etq_unid_estiba, 0, wx.ALL, 5)

        self.txt_unid_x_estiba = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(-1, -1), validator=validador_solo_digitos())
        self.txt_unid_x_estiba.SetMinSize(wx.Size(60, -1))

        bSizer33.Add(self.txt_unid_x_estiba, 1, wx.ALL, 5)


        ## ________________________________________________
        self.lbl_etq_unid_vagoneta = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Unid / Vagoneta:", wx.DefaultPosition,
                                                  wx.Size(-1, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_unid_vagoneta.Wrap(-1)
        bSizer33.Add(self.lbl_etq_unid_vagoneta, 0, wx.ALL, 5)

        self.txt_unid_x_vagoneta = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(-1, -1), validator=validador_solo_digitos())
        self.txt_unid_x_vagoneta.SetMinSize(wx.Size(60, -1))

        bSizer33.Add(self.txt_unid_x_vagoneta, 1, wx.ALL, 5)


        ## _________________________________________________



        bSizer_principal.Add(bSizer33, 0, wx.EXPAND, 5)

        self.grid_productos = wx.grid.Grid(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_productos.CreateGrid(0, 13)
        self.grid_productos.EnableEditing(False)
        self.grid_productos.EnableGridLines(True)
        self.grid_productos.EnableDragGridSize(False)
        self.grid_productos.SetMargins(0, 0)

        # Columns
        self.grid_productos.AutoSizeColumns()
        self.grid_productos.EnableDragColMove(False)
        self.grid_productos.EnableDragColSize(True)
        self.grid_productos.SetColLabelSize(30)
        self.grid_productos.SetColLabelValue(0, u"id")
        self.grid_productos.SetColLabelValue(1, u"Producto")
        self.grid_productos.SetColLabelValue(2, u"Cat")
        self.grid_productos.SetColLabelValue(3, u"Peso gr")
        self.grid_productos.SetColLabelValue(4, u"Largo")
        self.grid_productos.SetColLabelValue(5, u"Ancho")
        self.grid_productos.SetColLabelValue(6, u"Alto")
        self.grid_productos.SetColLabelValue(7, u"Stock Min")
        self.grid_productos.SetColLabelValue(8, u"Stock Max")
        self.grid_productos.SetColLabelValue(9, u"Unid / Vagoneta")
        self.grid_productos.SetColLabelValue(10, u"Unid / Coche")
        self.grid_productos.SetColLabelValue(11, u"Unid / Estiba")
        self.grid_productos.SetColLabelValue(12, u"Activo")
        self.grid_productos.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_productos.EnableDragRowSize(True)
        self.grid_productos.SetRowLabelSize(50)
        self.grid_productos.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_productos.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_productos.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.grid_productos.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        bSizer_principal.Add(self.grid_productos, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer_principal)
        self.m_panel3.Layout()
        bSizer_principal.Fit(self.m_panel3)
        bSizer23.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer23)

        self.func_valores_iniciales()

        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.comboBox_mostrar.Bind(wx.EVT_COMBOBOX, self.comboBox_mostrarOnCombobox)
        self.btn_guardar.Bind(wx.EVT_BUTTON, self.btn_guardarOnButtonClick)
        self.btn_actualizar.Bind(wx.EVT_BUTTON, self.btn_actualizarOnButtonClick)
        self.btn_limpiar.Bind(wx.EVT_BUTTON, self.btn_limpiarOnButtonClick)

        self.grid_productos.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_productosOnGridCellLeftClick)
        self.grid_productos.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK,
                                          self.grid_productosOnGridLabelLeftDClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class

    def btn_actualizarOnButtonClick(self, event):
        self.func_valores_iniciales()
        self.func_limpiar_controles()
        self.comboBox_mostrar.SetValue('ACTIVOS')
        self.Layout()

        event.Skip()

    def btn_limpiarOnButtonClick(self, event):
        self.func_limpiar_controles()
        event.Skip()

    def comboBox_mostrarOnCombobox(self, event):
        seleccion = self.comboBox_mostrar.GetValue()
        self.func_cargar_grilla_productos(seleccion)
        event.Skip()

    def btn_guardarOnButtonClick(self, event):
        rta = self.func_validar_entrada_datos()
        if rta == 0:
            return 0
        else:
            tipo_guardar = self.btn_guardar.GetLabel()
            if tipo_guardar == 'Crear Producto':
                rta = self.func_guardar_nuevo_producto()
            if tipo_guardar == 'Guardar Cambios':
                rta = self.func_actualizar_producto()
            if rta == 1:
                wx.MessageBox(u'El proceso se ha realizado de manera correcta', u'Atención', wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox(u'Se ha presentado un inconveniente, no fue posible realizar la operación', u'Atención',
                              wx.OK | wx.ICON_INFORMATION)
                
            seleccion = self.comboBox_mostrar.GetValue()
            self.func_cargar_grilla_productos(seleccion)

            self.func_ordenarGrillaPorColumna(self.columna, self.orden_ascendente)

        event.Skip()

    def grid_productosOnGridCellLeftClick(self, event):
        fila = event.GetRow()

        is_activo = 0

        self.lbl_id.SetLabel(self.grid_productos.GetCellValue(fila, 0))
        self.txt_producto.SetValue(self.grid_productos.GetCellValue(fila, 1))

        self.comboBox_categoria.SetValue(self.grid_productos.GetCellValue(fila, 2))

        self.txt_peso.SetValue(self.grid_productos.GetCellValue(fila, 3))
        self.txt_largo.SetValue(self.grid_productos.GetCellValue(fila, 4))
        self.txt_ancho.SetValue(self.grid_productos.GetCellValue(fila, 5))
        self.txt_alto.SetValue(self.grid_productos.GetCellValue(fila, 6))
        self.txt_stock_minimo.SetValue(self.grid_productos.GetCellValue(fila, 7))
        self.txt_stock_maximo.SetValue(self.grid_productos.GetCellValue(fila, 8))
        self.txt_unid_x_vagoneta.SetValue(self.grid_productos.GetCellValue(fila, 9))

        self.txt_unid_x_coche.SetValue(self.grid_productos.GetCellValue(fila, 10))
        self.txt_unid_x_estiba.SetValue(self.grid_productos.GetCellValue(fila, 11))

        if self.grid_productos.GetCellValue(fila, 9) == 'True':
            is_activo = 1
        else:
            is_activo = 0
        self.checkBox_activo.SetValue(is_activo)

        self.btn_guardar.SetLabel('Guardar Cambios')
        self.Layout()

        event.Skip()

    def grid_productosOnGridLabelLeftDClick(self, event):
        columna = event.GetCol()

        if self.orden_ascendente == True:
            self.orden_ascendente = False
        else:
            self.orden_ascendente = True

        self.func_ordenarGrillaPorColumna(columna, self.orden_ascendente)

        #self.colorearGrilla()
        event.Skip()


    ## funciones eay
    def func_guardar_nuevo_producto(self):
        producto     = self.txt_producto.GetValue()
        peso         = self.txt_peso.GetValue()
        largo        = self.txt_largo.GetValue()
        ancho        = self.txt_ancho.GetValue()
        alto         = self.txt_alto.GetValue()
        stock_minimo = self.txt_stock_minimo.GetValue()
        stock_maximo = self.txt_stock_maximo.GetValue()
        categoria   = self.comboBox_categoria.GetValue()
        unid_x_vagoneta = self.txt_unid_x_vagoneta.GetValue()

        unid_x_coche = self.txt_unid_x_coche.GetValue()
        unid_x_estiba = self.txt_unid_x_estiba.GetValue()

        activo =  True  #self.checkBox_activo.GetValue()

        sSql = """
                INSERT INTO producto (  nom_producto,  Peso,  Largo,  Ancho,  Alto,  Stock_min,  Stock_max,  categoria, 
                                        unid_x_vagoneta, unid_coche, unid_estiba) 
                                VALUES (
                                '{0}', {1}, {2}, {3}, {4}, {5}, {6}, '{7}', {8}, {9}, {10}                                
                                )
        """.format(producto, peso, largo, ancho, alto,  stock_minimo, stock_maximo,  categoria, unid_x_vagoneta, unid_x_coche, unid_x_estiba)

        rta = Ejecutar_SQL.insert_filas(sSql.upper(),'frm_gestionar_productos/func_guardar_nuevo_producto', BasesDeDatos.DB_PRINCIPAL)
        return  rta

    def func_actualizar_producto(self):
        id_producto = self.lbl_id.GetLabel()
        producto = self.txt_producto.GetValue()
        peso = self.txt_peso.GetValue()
        largo = self.txt_largo.GetValue()
        ancho = self.txt_ancho.GetValue()
        alto = self.txt_alto.GetValue()
        stock_minimo = self.txt_stock_minimo.GetValue()
        stock_maximo = self.txt_stock_maximo.GetValue()
        categoria = self.comboBox_categoria.GetValue()
        unid_x_vagoneta = self.txt_unid_x_vagoneta.GetValue()

        unid_x_coche = self.txt_unid_x_coche.GetValue()
        unid_x_estiba = self.txt_unid_x_estiba.GetValue()

        activo = self.checkBox_activo.GetValue()

        sSql = """
                    UPDATE producto SET 
                        nom_producto = '{0}',  Peso = {1},  Largo = {2},  Ancho = {3},  Alto = {4},  Stock_min = {5},  
                        Stock_max = {6},  activo = '{7}',categoria = '{9}', unid_x_vagoneta = {10}, unid_x_coche = {11}, unid_x_estiba = {12}
                    WHERE id_producto = {8}
                """.format(producto, peso, largo, ancho, alto, stock_minimo, stock_maximo,
                           activo, id_producto, categoria, unid_x_vagoneta, unid_x_coche, unid_x_estiba)

        rta = Ejecutar_SQL.update_filas(sSql.upper(), 'frm_gestionar_productos/func_actualizar_producto', BasesDeDatos.DB_PRINCIPAL)
        return rta

    def func_limpiar_controles(self):
        is_activo = 0

        self.lbl_id.SetLabel('')
        self.txt_producto.SetValue('')
        self.txt_peso.SetValue('')
        self.txt_largo.SetValue('')
        self.txt_ancho.SetValue('')
        self.txt_alto.SetValue('')
        self.txt_stock_minimo.SetValue('')
        self.txt_stock_maximo.SetValue('')
        self.txt_unid_x_vagoneta.SetValue('')

        self.txt_unid_x_coche.SetValue('')
        self.txt_unid_x_estiba.SetValue('')

        self.checkBox_activo.SetValue(is_activo)

        self.comboBox_categoria.SetSelection(-1)

        self.btn_guardar.SetLabel('Crear Producto')
        self.Layout()

    def func_valores_iniciales(self):
        self.grid_productos.AutoSizeColumns()
        self.btn_guardar.SetLabel('Crear Producto')
        self.func_cargar_grilla_productos('ACTIVOS')

    def func_cargar_grilla_productos(self, opcion_carga):
        dic_sel_carga = {'ACTIVOS': ' WHERE activo = True', 'NO ACTIVOS': ' WHERE activo = False', 'TODOS': ' '}

        sSql = """
                SELECT id_producto,  nom_producto, categoria,  Peso,  Largo,  Ancho,  Alto,  Stock_min,  Stock_max, 
                        unid_x_vagoneta, unid_x_coche, unid_x_estiba, Activo
                FROM producto
                {0}
        """.format(dic_sel_carga[opcion_carga])

        cabeceras = ['id_producto','Categoria', 'Producto', 'Peso', 'Largo', 'Ancho', 'Alto', 'Stock Min', 'Stock Max',
                     'Unid / Vagoneta', 'Unid / Coche', 'Unid / Estiba',  'Activo']

        rows = Ejecutar_SQL.select_varios_registros(sSql,  'frm_gestionarproductos/func_cargar_grilla_productos', 500, BasesDeDatos.DB_PRINCIPAL)

        ManipularGrillas.llenarGrilla(self.grid_productos, rows)

    def func_ordenarGrillaPorColumna(self, columna, orden_ascendente):

        self.columna = columna

        lista_tipoColumna = ['int', 'str', 'str', 'int', 'float', 'float', 'float', 'int', 'int', 'int', 'int', 'int', 'str']

        ManipularGrillas.ordenarGrillaPorColumna(self.grid_productos,  self.columna, lista_tipoColumna,
                                                 orden_ascendente)

    def func_validar_entrada_datos(self):

        if self.txt_producto.GetValue() == '':
            wx.MessageBox(u'Debes ingresar un nombre valido para el Producto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        if self.comboBox_categoria.GetValue() == '':
            wx.MessageBox(u'Debes seleccionar una Categoria de Producto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        try:
            peso = int(self.txt_peso.GetValue())
        except:
            wx.MessageBox(u'Debes ingresar un valor entero para el peso', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        try:
            largo = float(self.txt_largo.GetValue())
        except:
            wx.MessageBox(u'Debes ingresar un valor entero para el Largo', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0
        try:
            ancho = float(self.txt_ancho.GetValue())
        except:
            wx.MessageBox(u'Debes ingresar un valor entero para el Ancho', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0
        try:
            alto = float(self.txt_alto.GetValue())
        except:
            wx.MessageBox(u'Debes ingresar un valor entero para el Alto', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0
        try:
            stock_minimo = int(self.txt_stock_minimo.GetValue())
        except:
            wx.MessageBox(u'Debes ingresar un valor entero para el Stock Mínimo', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        try:
            stock_maximo = int(self.txt_stock_maximo.GetValue())
        except:
            wx.MessageBox(u'Debes ingresar un valor entero para el Stock Máximo', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0
        try:
            unid_x_vagoneta = int(self.txt_unid_x_vagoneta.GetValue())
        except:
            wx.MessageBox(u'Debes ingresar un valor de Unidades por vagoneta', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0


        ## si esta todo bien
        return 1







