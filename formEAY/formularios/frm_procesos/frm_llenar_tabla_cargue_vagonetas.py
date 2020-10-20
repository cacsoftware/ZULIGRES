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

from formEAY.dbaseCAC.dbVarios import DbGetVarios
from pyeay.rows import ManipularRows
from pyeay.grillas import ManipularGrillas

###########################################################################
## Class LlenarTablaCargueVagonetas
###########################################################################

class LlenarTablaCargueVagonetas(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Llenar Tabla Cargue de Vagonetas", pos=wx.DefaultPosition,
                          size=wx.Size(888, 569), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(500, 400), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.padre = parent

        self.list_vagonetas = []
        self.puntero_fila = 0
        self.puntero_columna = 1

        bSizer_principal = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_principal = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel_principal.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_cabecera = wx.BoxSizer(wx.VERTICAL)

        bSizer_titulo = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_cargueVagonetas = wx.StaticText(self.panel_principal, wx.ID_ANY, u"Cargue de Vagonetas",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_cargueVagonetas.Wrap(-1)
        self.lbl_etq_cargueVagonetas.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))
        self.lbl_etq_cargueVagonetas.SetForegroundColour(wx.Colour(255, 0, 0))

        bSizer_titulo.Add(self.lbl_etq_cargueVagonetas, 0, wx.ALL, 5)

        bSizer_cabecera.Add(bSizer_titulo, 0, wx.EXPAND, 5)

        bSizer_llenado = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel_vagonetasProductos = wx.Panel(self.panel_principal, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.TAB_TRAVERSAL)
        self.m_panel_vagonetasProductos.SetBackgroundColour(wx.Colour(232, 232, 232))

        bSizer_vagonetasProductos = wx.BoxSizer(wx.VERTICAL)

        bSizer22 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_vagonetas = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_vagonetas = wx.StaticText(self.m_panel_vagonetasProductos, wx.ID_ANY, u"Vagonetas",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_vagonetas.Wrap(-1)
        self.lbl_etq_vagonetas.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_vagonetas.SetForegroundColour(wx.Colour(0, 0, 0))

        bSizer_vagonetas.Add(self.lbl_etq_vagonetas, 0, wx.ALL, 5)

        checkList_vagonetaChoices = [u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09"]
        self.checkList_vagoneta = wx.CheckListBox(self.m_panel_vagonetasProductos, wx.ID_ANY, wx.DefaultPosition,
                                                  wx.DefaultSize, checkList_vagonetaChoices, 0 | wx.NO_BORDER)
        self.checkList_vagoneta.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_vagonetas.Add(self.checkList_vagoneta, 1, wx.ALL | wx.EXPAND, 5)

        bSizer22.Add(bSizer_vagonetas, 1, wx.EXPAND, 5)

        bSizer_producto = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_producto = wx.StaticText(self.m_panel_vagonetasProductos, wx.ID_ANY, u"Producto",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_producto.Wrap(-1)
        self.lbl_etq_producto.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_producto.SetForegroundColour(wx.Colour(0, 0, 0))

        bSizer_producto.Add(self.lbl_etq_producto, 0, wx.ALL, 5)

        checkList_productoChoices = [u"LADRILLO SALAZAR", u"H10 R"]
        self.checkList_producto = wx.CheckListBox(self.m_panel_vagonetasProductos, wx.ID_ANY, wx.DefaultPosition,
                                                  wx.DefaultSize, checkList_productoChoices, 0 | wx.NO_BORDER)
        bSizer_producto.Add(self.checkList_producto, 1, wx.ALL | wx.EXPAND, 5)

        bSizer22.Add(bSizer_producto, 2, wx.EXPAND, 5)

        bSizer_vagonetasProductos.Add(bSizer22, 1, wx.EXPAND, 5)

        # bSizer_botonesGenerarTabla = wx.BoxSizer(wx.HORIZONTAL)
        #
        # self.btn_generar_tabla = wx.Button(self.m_panel_vagonetasProductos, wx.ID_ANY, u"&Generar Tabla",
        #                                    wx.DefaultPosition, wx.DefaultSize, 0)
        # bSizer_botonesGenerarTabla.Add(self.btn_generar_tabla, 0, wx.ALL, 5)
        #
        # bSizer_vagonetasProductos.Add(bSizer_botonesGenerarTabla, 0, wx.EXPAND, 5)

        self.m_panel_vagonetasProductos.SetSizer(bSizer_vagonetasProductos)
        self.m_panel_vagonetasProductos.Layout()
        bSizer_vagonetasProductos.Fit(self.m_panel_vagonetasProductos)
        bSizer_llenado.Add(self.m_panel_vagonetasProductos, 1, wx.EXPAND | wx.ALL, 5)

        bSizer_grilla = wx.BoxSizer(wx.VERTICAL)

        self.m_panel_tabla = wx.Panel(self.panel_principal, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
        self.m_panel_tabla.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_tabla = wx.BoxSizer(wx.VERTICAL)

        self.grid_tabla = wx.grid.Grid(self.m_panel_tabla, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_tabla.CreateGrid(0, 1)
        self.grid_tabla.EnableEditing(True)
        self.grid_tabla.EnableGridLines(True)
        self.grid_tabla.EnableDragGridSize(False)
        self.grid_tabla.SetMargins(0, 0)

        # Columns
        self.grid_tabla.AutoSizeColumns()
        self.grid_tabla.EnableDragColMove(False)
        self.grid_tabla.EnableDragColSize(True)
        self.grid_tabla.SetColLabelSize(30)
        self.grid_tabla.SetColLabelValue(0, u"Vagoneta")
        self.grid_tabla.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_tabla.EnableDragRowSize(True)
        self.grid_tabla.SetRowLabelSize(1)
        self.grid_tabla.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_tabla.SetLabelBackgroundColour(wx.Colour(240, 240, 240))

        # Cell Defaults
        self.grid_tabla.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer_tabla.Add(self.grid_tabla, 1, wx.ALL | wx.EXPAND, 5)

        ### -----------------
        self.m_grid_totales = wx.grid.Grid(self.m_panel_tabla, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid_totales.CreateGrid(1, 0)
        self.m_grid_totales.EnableEditing(True)
        self.m_grid_totales.EnableGridLines(True)
        self.m_grid_totales.EnableDragGridSize(False)
        self.m_grid_totales.SetMargins(0, 0)

        # Columns
        self.m_grid_totales.EnableDragColMove(False)
        self.m_grid_totales.EnableDragColSize(True)
        self.m_grid_totales.SetColLabelSize(30)
        self.m_grid_totales.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid_totales.EnableDragRowSize(True)
        self.m_grid_totales.SetRowLabelSize(80)
        self.m_grid_totales.SetRowLabelValue(0, u"Sumas")
        self.m_grid_totales.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.m_grid_totales.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.m_grid_totales.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.m_grid_totales.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer_tabla.Add(self.m_grid_totales, 0, wx.ALL | wx.EXPAND, 5)
        ### -----------------

        bSizer_botonesTabla = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText61 = wx.StaticText(self.m_panel_tabla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText61.Wrap(-1)
        bSizer_botonesTabla.Add(self.m_staticText61, 0, wx.ALL, 5)

        self.btn_limpiar = wx.Button(self.m_panel_tabla, wx.ID_ANY, u"&Limpiar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_botonesTabla.Add(self.btn_limpiar, 0, wx.ALL, 5)

        self.btn_enviar = wx.Button(self.m_panel_tabla, wx.ID_ANY, u"Enviar al Formulario", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizer_botonesTabla.Add(self.btn_enviar, 0, wx.ALL, 5)

        bSizer_tabla.Add(bSizer_botonesTabla, 0, wx.EXPAND, 5)

        self.m_panel_tabla.SetSizer(bSizer_tabla)
        self.m_panel_tabla.Layout()
        bSizer_tabla.Fit(self.m_panel_tabla)
        bSizer_grilla.Add(self.m_panel_tabla, 1, wx.EXPAND | wx.ALL, 5)

        bSizer_llenado.Add(bSizer_grilla, 2, wx.EXPAND, 5)

        bSizer_cabecera.Add(bSizer_llenado, 1, wx.EXPAND, 5)

        self.panel_principal.SetSizer(bSizer_cabecera)
        self.panel_principal.Layout()
        bSizer_cabecera.Fit(self.panel_principal)
        bSizer_principal.Add(self.panel_principal, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer_principal)
        self.Layout()

        self.Centre(wx.BOTH)

        ## valores iniciales
        self.inicializar_valores()

        # Connect Events
        self.checkList_producto.Bind(wx.EVT_CHECKLISTBOX, self.checkList_productoOnCheckListBoxToggled)
        self.checkList_vagoneta.Bind(wx.EVT_CHECKLISTBOX, self.checkList_vagonetaOnCheckListBoxToggled)
        #self.btn_generar_tabla.Bind(wx.EVT_BUTTON, self.btn_generar_tablaOnButtonClick)
        self.grid_tabla.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.grid_tablaOnGridCellChange)
        self.grid_tabla.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.grid_resultado_busquedaOnGridCellLeftDClick)
        self.btn_limpiar.Bind(wx.EVT_BUTTON, self.btn_limpiarOnButtonClick)
        self.btn_enviar.Bind(wx.EVT_BUTTON, self.btn_enviarOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def grid_tablaOnGridCellChange(self, event):
        columna = event.GetCol()
        can_filas = self.grid_tabla.GetNumberRows()
        total = 0
        for i in range(can_filas):
            dato = self.grid_tabla.GetCellValue(i, columna)
            if dato == '':
                dato = 0
            total += int(dato)
        self.m_grid_totales.SetCellValue(0, columna-1, str(total))

        event.Skip()

    def checkList_productoOnCheckListBoxToggled(self, event):
        indice_checkeado = event.GetInt()
        cad_checkeado = self.checkList_producto.GetString(indice_checkeado)
        if self.checkList_producto.IsChecked(indice_checkeado):
            self.puntero_columna = ManipularGrillas.nuevaColumnaVaciaGrilla(self.grid_tabla, self.puntero_columna)
            self.grid_tabla.SetColLabelValue(self.puntero_columna - 1, cad_checkeado)

            puntero_columna_totales = ManipularGrillas.nuevaColumnaVaciaGrilla(self.m_grid_totales, self.puntero_columna-1)
            self.m_grid_totales.SetColLabelValue(self.puntero_columna - 2, cad_checkeado)

        else:
            cant_columnas = self.grid_tabla.GetNumberCols()
            posicion = 0
            for i in range(cant_columnas):
                dato = self.grid_tabla.GetColLabelValue(i)
                if dato == cad_checkeado:
                    posicion = i
                    self.puntero_columna = ManipularGrillas.delColumna(self.grid_tabla, posicion)

                    puntero_columna_totales = ManipularGrillas.delColumna(self.m_grid_totales, posicion-1)  ## -1 porque grid_tabla empieza en la segunda columna

                    cant_filas_total = self.m_grid_totales.GetNumberRows()
                    if cant_filas_total == 0:
                        self.m_grid_totales.InsertRows(0, 1)

                    break

        dic_color = {0: wx.Colour(240, 240, 240)}
        ManipularGrillas.setColorFondoCeldaGrilla(self.grid_tabla, dic_color)

        list_columnas = self.columnasGrillaSoloNumeros()
        ManipularGrillas.setColumnasSoloNumeros(self.grid_tabla, list_columnas)

        list_columnas = [0]
        ManipularGrillas.setColumnasSoloLectura(self.grid_tabla, list_columnas)

        self.grid_tabla.AutoSizeColumns()
        self.m_grid_totales.AutoSizeColumns()
        event.Skip()

    def checkList_vagonetaOnCheckListBoxToggled(self, event):

        indice_checkeado = event.GetInt()
        cad_checkeado = self.checkList_vagoneta.GetString(indice_checkeado)
        if self.checkList_vagoneta.IsChecked(indice_checkeado):
            self.puntero_fila = ManipularGrillas.nuevaFilaVaciaGrilla(self.grid_tabla, self.puntero_fila)
            self.grid_tabla.SetCellValue(self.puntero_fila - 1, 0, cad_checkeado)
        else:
            cant_filas = self.grid_tabla.GetNumberRows()
            posicion = 0
            for i in range(cant_filas):
                dato = self.grid_tabla.GetCellValue(i, 0)
                if dato == cad_checkeado:
                    posicion = i
                    self.puntero_fila = ManipularGrillas.delFila(self.grid_tabla, posicion)
                    break

        dic_color = {0: wx.Colour(240, 240, 240)}
        ManipularGrillas.setColorFondoCeldaGrilla(self.grid_tabla, dic_color)

        list_columnas = self.columnasGrillaSoloNumeros()
        ManipularGrillas.setColumnasSoloNumeros(self.grid_tabla, list_columnas)

        list_columnas = [0]
        ManipularGrillas.setColumnasSoloLectura(self.grid_tabla, list_columnas)

        self.grid_tabla.AutoSizeColumns()
        event.Skip()

    def grid_resultado_busquedaOnGridCellLeftDClick(self, event):
        event.Skip()

    def btn_limpiarOnButtonClick(self, event):
        cant_filas = self.grid_tabla.GetNumberRows()
        cant_cols = self.grid_tabla.GetNumberCols()

        for i in range(cant_filas):
            for j in range(1, cant_cols):
                self.grid_tabla.SetCellValue(i, j, '')

        cant_filas_totales = self.m_grid_totales.GetNumberCols()
        for j in range(cant_filas_totales):
            self.m_grid_totales.SetCellValue(0, j, '')

        event.Skip()

    def btn_enviarOnButtonClick(self, event):
        rows = []
        row = []
        row_cabeceras = []

        cant_filas = self.grid_tabla.GetNumberRows()
        cant_cols = self.grid_tabla.GetNumberCols()

        for i in range(cant_filas):
            row = []
            for j in range(cant_cols):
                dato = self.grid_tabla.GetCellValue(i, j)
                row.append(dato)
            rows.append(row)

        for i in range(cant_cols):
            cabecera = self.grid_tabla.GetColLabelValue(i)
            row_cabeceras.append(cabecera)

        list_columnas_soloNumeros = self.columnasGrillaSoloNumeros()

        self.padre.cargar_grid_cargueVagonetas(rows, cant_cols, row_cabeceras, list_columnas_soloNumeros, self.dic_cargueVagonetas)




        event.Skip()

## FUNCIONES EAY

    def columnasGrillaSoloNumeros(self):
        cant_cols = self.grid_tabla.GetNumberCols()
        a = range(1, cant_cols)
        list_columnas = []
        for i in a:
            list_columnas.append(i)

        return list_columnas

    def inicializar_valores(self):
        self.grid_tabla.AutoSizeColumns()
        self.cargar_checkList_vagonetas()
        self.cargar_checkList_productos()


        # list_columnas = [2]
        # manipular_grilla.setColumnasSoloNumeros(self.grid_recesos, list_columnas)

    def cargar_checkList_vagonetas(self):
        rows = DbGetVarios.listaVagonetas(True)
        # id_vagoneta, nom_vagoneta

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            #self.dic_vagonetas = ManipularRows.crearDiccionario(rows, 1, 0)
            self.checkList_vagoneta.Set(la_lista)

    def cargar_checkList_productos(self):
        from formEAY.dbaseCAC.dbProductos import Get_productos

        cant_registros = 500
        rows = Get_productos.listaBasica(cant_registros, True)

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.dic_cargueVagonetas = ManipularRows.crearDiccionario(rows, 1, 0)
            self.checkList_producto.Set(la_lista)


