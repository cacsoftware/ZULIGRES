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

import os
import time

from uuid import uuid4
import pandas as pd

from pyeay.validator import validador_solo_digitos
from formEAY.constantesCAC.imgCAC import Img_grillas, Img_formularios_general
from pyeay.dbcac.conexiondb import Ejecutar_SQL, GenerarSql
from pyeay.formato import FormatearNumeros
from pyeay.rows import ManipularRows
from pyeay.grillas import ManipularGrillas

from formEAY.constantesCAC.constantesCAC import BasesDeDatos
from formEAY.constantesCAC.coloresCAC import ColorsFondoCellGrilla
COLOR_RESALTE1 = ColorsFondoCellGrilla.RESALTE_2


###########################################################################
## Class AjusteInventarioPatio
###########################################################################

class AjusteInventarioPatio(wx.Frame):

    def __init__(self, parent, usuario='usuario1', dir_mac = 'la dir mac del pc'):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Ajustar Inventario Patio", pos=wx.DefaultPosition,
                          size=wx.Size(827, 611), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(820, 400), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        icono_grillas = Img_grillas()
        icono_formularios = Img_formularios_general()

        self.uuid_eay = uuid4()
        self.usuario = usuario
        self.dir_mac = dir_mac


        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.panel_principal = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_ajuste_inventario_patio = wx.StaticText(self.panel_principal, wx.ID_ANY,
                                                             u"Ajuste Inventario Patio", wx.DefaultPosition,
                                                             wx.DefaultSize, 0)
        self.lbl_etq_ajuste_inventario_patio.Wrap(-1)
        self.lbl_etq_ajuste_inventario_patio.SetFont(wx.Font(11, 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_ajuste_inventario_patio.SetForegroundColour(wx.Colour(255, 128, 64))

        bSizer3.Add(self.lbl_etq_ajuste_inventario_patio, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add(bSizer3, 0, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fecha = wx.StaticText(self.panel_principal, wx.ID_ANY, u"Fecha:", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lbl_etq_fecha.Wrap(-1)
        bSizer4.Add(self.lbl_etq_fecha, 1, wx.ALL, 5)

        self.datePicker_fecha = wx.adv.DatePickerCtrl(self.panel_principal, wx.ID_ANY, wx.DefaultDateTime,
                                                  wx.DefaultPosition, wx.Size(130, -1), style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer4.Add(self.datePicker_fecha, 0, wx.ALL, 5)

        bSizer2.Add(bSizer4, 0, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_producto = wx.StaticText(self.panel_principal, wx.ID_ANY, u"Producto:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_etq_producto.Wrap(-1)
        bSizer5.Add(self.lbl_etq_producto, 0, wx.ALL, 5)

        comboBox_productoChoices = []
        self.comboBox_producto = wx.ComboBox(self.panel_principal, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                             wx.Size(155, -1), comboBox_productoChoices, wx.CB_READONLY)
        bSizer5.Add(self.comboBox_producto, 0, wx.ALL, 5)

        self.lbl_estado_inicial = wx.StaticText(self.panel_principal, wx.ID_ANY, u"Estado Inicial:", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.lbl_estado_inicial.Wrap(-1)
        bSizer5.Add(self.lbl_estado_inicial, 0, wx.ALL, 5)

        comboBox_estado_inicialChoices = [u"PRIMERA", u"SEGUNDA"]
        self.comboBox_estado_inicial = wx.ComboBox(self.panel_principal, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                                   wx.DefaultSize, comboBox_estado_inicialChoices, wx.CB_READONLY)
        bSizer5.Add(self.comboBox_estado_inicial, 0, wx.ALL, 5)

        self.lbl_etq_cant = wx.StaticText(self.panel_principal, wx.ID_ANY, u"Cantidad:", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.lbl_etq_cant.Wrap(-1)
        bSizer5.Add(self.lbl_etq_cant, 0, wx.ALL, 5)

        self.txt_cant = wx.TextCtrl(self.panel_principal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(50, -1), validator= validador_solo_digitos())
        bSizer5.Add(self.txt_cant, 0, wx.ALL, 5)

        self.lbl_etq_nuevo_estado = wx.StaticText(self.panel_principal, wx.ID_ANY, u"Nuevo Estado:", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.lbl_etq_nuevo_estado.Wrap(-1)
        bSizer5.Add(self.lbl_etq_nuevo_estado, 0, wx.ALL, 5)

        comboBox_nuevo_estadoChoices = [u"PRIMERA", u"SEGUNDA", u"ROTURA"]
        self.comboBox_nuevo_estado = wx.ComboBox(self.panel_principal, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                                 wx.DefaultSize, comboBox_nuevo_estadoChoices, wx.CB_READONLY)
        bSizer5.Add(self.comboBox_nuevo_estado, 0, wx.ALL, 5)

        self.btn_a_lista = wx.Button(self.panel_principal, wx.ID_ANY, u"--> Lista", wx.DefaultPosition, wx.DefaultSize,
                                     wx.NO_BORDER)
        self.btn_a_lista.SetBackgroundColour(wx.Colour(254, 230, 90))

        bSizer5.Add(self.btn_a_lista, 0, wx.ALL, 5)

        bSizer2.Add(bSizer5, 0, wx.EXPAND, 5)

        bSizer11_linea = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline2 = wx.StaticLine(self.panel_principal, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer11_linea.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer2.Add(bSizer11_linea, 0, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.grid_producto = wx.grid.Grid(self.panel_principal, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_producto.CreateGrid(0, 6)
        self.grid_producto.EnableEditing(True)
        self.grid_producto.EnableGridLines(True)
        self.grid_producto.EnableDragGridSize(False)
        self.grid_producto.SetMargins(0, 0)

        # Columns
        self.grid_producto.SetColSize(0, 80)
        self.grid_producto.SetColSize(1, 80)
        self.grid_producto.SetColSize(2, 77)
        self.grid_producto.SetColSize(3, 80)
        self.grid_producto.SetColSize(4, 80)
        self.grid_producto.SetColSize(5, 80)
        self.grid_producto.EnableDragColMove(False)
        self.grid_producto.EnableDragColSize(True)
        self.grid_producto.SetColLabelSize(30)
        self.grid_producto.SetColLabelValue(0, u"id")
        self.grid_producto.SetColLabelValue(1, u"Producto")
        self.grid_producto.SetColLabelValue(2, u"Estado Inicial")
        self.grid_producto.SetColLabelValue(3, u"Cantidad")
        self.grid_producto.SetColLabelValue(4, u"Nuevo Estado")
        self.grid_producto.SetColLabelValue(5, u"Sel")
        self.grid_producto.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_producto.EnableDragRowSize(True)
        self.grid_producto.SetRowLabelSize(45)
        self.grid_producto.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_producto.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_producto.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.grid_producto.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer9.Add(self.grid_producto, 1, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.bpButton_eliminar_item_seleccionado_grid_producto = wx.BitmapButton(self.panel_principal, wx.ID_ANY,
                                                                                  wx.Bitmap(
                                                                                      icono_grillas.ELIMINAR_ITEM_SELECIONADO,
                                                                                      wx.BITMAP_TYPE_ANY),
                                                                                  wx.DefaultPosition, wx.DefaultSize,
                                                                                  wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_eliminar_item_seleccionado_grid_producto.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.ELIMINAR_ITEM_SELECIONADO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer10.Add(self.bpButton_eliminar_item_seleccionado_grid_producto, 0, wx.ALL, 5)

        self.bpButton_deseleccionar_todo_grid_producto = wx.BitmapButton(self.panel_principal, wx.ID_ANY,
                                                                          wx.Bitmap(
                                                                              icono_grillas.DESELECCIONAR_TODO,
                                                                              wx.BITMAP_TYPE_ANY),
                                                                          wx.DefaultPosition, wx.DefaultSize,
                                                                          wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_deseleccionar_todo_grid_producto.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer10.Add(self.bpButton_deseleccionar_todo_grid_producto, 0, wx.ALL, 5)

        # self.m_staticline1 = wx.StaticLine(self.panel1_extrusion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
        #                                    wx.LI_HORIZONTAL)
        # bSizer41.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.bpButton_limpiar_grid_producto = wx.BitmapButton(self.panel_principal, wx.ID_ANY, wx.Bitmap(
            icono_grillas.LIMPIAR_GRILLA, wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                                               wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_limpiar_grid_producto.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.LIMPIAR_GRILLA_SEL, wx.BITMAP_TYPE_ANY))
        bSizer10.Add(self.bpButton_limpiar_grid_producto, 0, wx.ALL, 5)


        bSizer6.Add(bSizer10, 0, wx.EXPAND, 5)

        bSizer2.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self.panel_principal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer8.Add(self.m_staticText7, 1, wx.ALL, 5)

        self.btn_guardar = wx.Button(self.panel_principal, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize,
                                     wx.NO_BORDER)
        self.btn_guardar.SetForegroundColour(wx.Colour(255, 255, 255))
        self.btn_guardar.SetBackgroundColour(wx.Colour(110, 180, 66))

        bSizer8.Add(self.btn_guardar, 0, wx.ALL, 5)

        bSizer2.Add(bSizer8, 0, wx.EXPAND, 5)

        self.panel_principal.SetSizer(bSizer2)
        self.panel_principal.Layout()
        bSizer2.Fit(self.panel_principal)
        bSizer1.Add(self.panel_principal, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)

        self.inicializacion()

        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_a_lista.Bind(wx.EVT_BUTTON, self.btn_a_listaOnButtonClick)
        self.btn_guardar.Bind(wx.EVT_BUTTON, self.btn_guardarOnButtonClick)
        self.bpButton_eliminar_item_seleccionado_grid_producto.Bind(wx.EVT_BUTTON,
                                                                    self.bpButton_eliminar_item_seleccionado_grid_productoOnButtonClick)
        self.bpButton_deseleccionar_todo_grid_producto.Bind(wx.EVT_BUTTON,
                                                            self.bpButton_deseleccionar_todo_grid_productoOnButtonClick)
        self.bpButton_limpiar_grid_producto.Bind(wx.EVT_BUTTON, self.bpButton_limpiar_grid_productoOnButtonClick)

    def bpButton_eliminar_item_seleccionado_grid_productoOnButtonClick(self, event):
        col_verificacion = 5
        self.punteroFilaProducto = ManipularGrillas.delFilasCHK(self.grid_producto, col_verificacion)
        dic_color = {3: COLOR_RESALTE1}
        ManipularGrillas.setColorFondoCeldaGrilla(self.grid_producto, dic_color)
        event.Skip()

    def bpButton_deseleccionar_todo_grid_productoOnButtonClick(self, event):
        col_verificacion = 5
        ManipularGrillas.deseleccionarFilasCHK(self.grid_producto, col_verificacion)
        event.Skip()

    def bpButton_limpiar_grid_productoOnButtonClick(self, event):
        self.punteroFilaProducto = ManipularGrillas.limpiarGrilla(self.grid_producto)
        event.Skip()


    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def btn_a_listaOnButtonClick(self, event):
        producto = self.comboBox_producto.GetValue()
        if producto == '':
            wx.MessageBox(u'Debes seleccionar un Producto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        try:
            id_producto = self.dic_productos[producto][0]
        except:
            return 0
        estadoInicial = self.comboBox_estado_inicial.GetValue()
        nuevoEstado = self.comboBox_nuevo_estado.GetValue()
        cant = self.txt_cant.GetValue()

        if estadoInicial == '':
            wx.MessageBox(u'Debes seleccionar un Estado Inicial', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if nuevoEstado == '':
            wx.MessageBox(u'Debes seleccionar un Nuevo Estado', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if cant == '' or cant == '0':
            wx.MessageBox(u'Debes ingresar un número valido de unidades', u'Atención',  wx.OK | wx.ICON_INFORMATION)
            return 0

        if estadoInicial != nuevoEstado:
            row = [id_producto, producto, estadoInicial, cant, nuevoEstado]
            self.punteroFilaProducto = ManipularGrillas.nuevaFilaGrilla(self.grid_producto, row, self.punteroFilaProducto)

            dic_color = {3: COLOR_RESALTE1}
            ManipularGrillas.setColorFondoCeldaGrilla(self.grid_producto, dic_color)
        event.Skip()

    def btn_guardarOnButtonClick(self, event):
        from pyeay.fechasHoras import ManejoFechasHoras
        fecha = self.datePicker_fecha.GetValue()
        fechaActual, horaActual = ManejoFechasHoras.getFechaHoraActual()

        activo = 'True'
        fecha = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha)

        cant_filas = self.grid_producto.GetNumberRows()
        fila = []
        rows = []
        rows_estadoInicialPrimera = []
        rows_estadoInicialSegunda = []
        rows_nuevoEstadoPrimera   = []
        rows_nuevoEstadoSegunda   = []

        for i in range(cant_filas):
            id_producto = self.grid_producto.GetCellValue(i, 0)
            producto = self.grid_producto.GetCellValue(i, 1)
            estadoInicial = self.grid_producto.GetCellValue(i, 2)
            cant = int(self.grid_producto.GetCellValue(i, 3))
            nuevoEstado = self.grid_producto.GetCellValue(i, 4)
            fila = [fecha, id_producto, producto, estadoInicial, cant, nuevoEstado, activo, self.usuario, self.dir_mac,
                    self.uuid_eay, fechaActual, horaActual]
            rows.append(fila)
            if estadoInicial == 'PRIMERA':
                rows_estadoInicialPrimera.append([id_producto, cant])
            if estadoInicial == 'SEGUNDA':
                rows_estadoInicialSegunda.append([id_producto, cant])
            if nuevoEstado == 'PRIMERA':
                rows_nuevoEstadoPrimera.append([id_producto, cant])
            if nuevoEstado == 'SEGUNDA':
                rows_nuevoEstadoSegunda.append([id_producto, cant])

        nom_tabla = 'ajuste_inventario'
        dic_campos = {'fecha':'str', 'id_producto': 'int', 'producto': 'str', 'estado_inicial': 'str', 'cant': 'int',
                      'nuevo_estado': 'str', 'activo':'str', 'usuario':'str', 'mac': 'str', 'uuid':'str',
                      'fecha_transaccion': 'str', 'hora_transaccion': 'str'}
        sSql = GenerarSql.crearMultiInsertSql(nom_tabla, dic_campos, rows)

        rta = Ejecutar_SQL.insert_filas(sSql.upper(), 'frm_ajustar_inventario/btn_guardarOnButtonClick',
                                        BasesDeDatos.DB_PRINCIPAL)

        if rows_estadoInicialPrimera != []:
            rta = self.actualizarStocksProductos_estadoInicialPrimera(rows_estadoInicialPrimera)
        if rows_estadoInicialSegunda != []:
            rta = self.actualizarStocksProductos_estadoInicialSegunda(rows_estadoInicialSegunda)
        if rows_nuevoEstadoPrimera   != []:
            rta = self.actualizarStocksProductos_nuevoEstadoPrimera(rows_nuevoEstadoPrimera)
        if rows_nuevoEstadoSegunda   != []:
            rta = self.actualizarStocksProductos_nuevoEstadoSegunda(rows_nuevoEstadoSegunda)

        if rta == 1:
            mensaje = u'El proceso se llevo a cabo correctamente, Desea Imprimir?'

            dlg = wx.MessageDialog(None, mensaje,
                                   u'Atención...',
                                   wx.YES_NO | wx.ICON_QUESTION)
            retCode = dlg.ShowModal()
            if (retCode == wx.ID_YES):  # PARA MANDAR A IMPRIMIR

                self.func_imprimir_ajusteInventarioPatio(rows)


                # os.startfile('despachoMercancia.pdf', 'print')
                # time.sleep(1)  # pause 0.5 seconds
                # os.remove("despachoMercancia.pdf")
            else:
                pass
                # os.startfile('despachoMercancia.pdf')

            self.Destroy()


        event.Skip()

    ## FUNCIONES EAY

    def get_ultimoAjusteInventario(self):
        sSql = """
                    SELECT id_ajuste, fecha, fecha_transaccion, hora_transaccion, usuario, mac
                    FROM ajuste_inventario
                    WHERE activo = 'True'
                    GROUP BY id_ajuste
                    HAVING id_ajuste = (
                                        SELECT MAX(id_ajuste)
                                                        FROM ajuste_inventario
                                                        WHERE activo = 'True'
                                        )
        """

        row = Ejecutar_SQL.select_un_registro(sSql, 'frm_ajuste_mercancia_patio/get_numAjusteInventario', BasesDeDatos.DB_PRINCIPAL)

        return row

    def func_imprimir_ajusteInventarioPatio(self, rows):
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas

        row_ajuste = self.get_ultimoAjusteInventario()

        IMG_CABECERA = Img_formularios_general.CABECERA_ORDEN_SERVICIO
        #IMG_PIE_PAGINA = Img_formularios_general.PIE_DE_PAGINA_ORDEN_SERVICIO

        ## carta = (612.0, 792.0)

        ajuste_y = 396

        c = canvas.Canvas("ajusteInventarioPatio.pdf", pagesize=letter)

        w, h = letter

        MARGEN_IZQ = 70

        CANT_FILAS_POR_HOJA = 11
        cant_filas_rows = len(rows)

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

            #---------------------------------------------------------
            fecha = str(row_ajuste['fecha'])
            fecha_transaccion = str(row_ajuste['fecha_transaccion'])
            hora_transaccion = str(row_ajuste['hora_transaccion'])
            usuario = row_ajuste['usuario']
            mac = row_ajuste['mac']
            id_ajuste = str(row_ajuste['id_ajuste'])

            #////////////////////

            text = c.beginText(360, h - 80)
            text.setFont("Courier-Bold", 10)
            cad_orden = 'Ajuste de Inventario: '
            text.textLine(cad_orden)
            c.drawText(text)

            text = c.beginText(425 + MARGEN_IZQ, h - 80)
            text.setFont("Courier-Bold", 12)
            text.setFillColorRGB(1, 0, 0)
            cad_orden = str(id_ajuste)
            text.textLine(cad_orden)
            c.drawText(text)
            #////////////////////

            text = c.beginText(MARGEN_IZQ, h - 105)
            text.setFont("Courier", 10)
            text.setFillColorRGB(0, 0, 0)

            cad_fecha = 'Fecha Ajuste:'.ljust(17) + fecha.ljust(51)
            text.textLine(cad_fecha)
            fecha_hora_transaccion = fecha_transaccion + '  ' + hora_transaccion
            cad_fechaRegistro =  'Fecha Registro:'.ljust(17) + fecha_hora_transaccion.ljust(50)
            text.textLine(cad_fechaRegistro)
            c.drawText(text)
            cad_fechaRegistro = 'Usuario:'.ljust(17) + usuario.ljust(32) + 'Mac: ' + mac.ljust(20)
            text.textLine(cad_fechaRegistro)
            c.drawText(text)

            # ---------------------------------------------------------

            text = c.beginText(MARGEN_IZQ, h - 147)
            text.setFont("Courier-Bold", 10)
            cad_cabecera = '%-5s     %-20s  %-16s  %-10s %-8s'  % ('id', 'Producto', 'Estado Inicial', 'Cant', 'Nuevo Estado')
            text.textLine(cad_cabecera)
            c.drawText(text)

            c.setStrokeColorRGB(0.678, 0.78, 0.811)
            c.line(MARGEN_IZQ, h - 155, 545, h - 155)

            text = c.beginText(MARGEN_IZQ, h - 170)
            text.setFont("Courier", 10)

            for i in range((hoja) * 12,  list_rangos[hoja], 1):
                fila = rows[i]
                # fila = [fecha, id_producto, producto, estadoInicial, cant, nuevoEstado, activo, self.usuario, self.dir_mac,
                #                     self.uuid_eay, fechaActual, horaActual]

                cant = fila[4]
                if cant == '0':
                    cant = fila[4]
                producto = fila[2]
                id_producto = fila[1]
                estado_inicial = fila[3]
                nuevo_estado = fila[5]


                cad_fila = '%-5s     %-20s  %-16s  %-10s %-8s' % (id_producto, producto, estado_inicial, cant, nuevo_estado)

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


    def actualizarStocksProductos_estadoInicialPrimera(self, rows):
        ## al stock actual se le resta el valor de cant
        df = pd.DataFrame(rows, columns = ['id', 'cant'])
        df = df.groupby(['id']).sum()

        rows = df.to_records().tolist()

        nom_tabla = 'producto'
        cols_busqueda = [0]
        cols_a_modificar = [1]

        nom_campos = ['id_producto', 'stock_primera']

        dic_operaciones = {'stock_primera': 'stock_primera - '}


        tipo_campos = ['int', 'int']

        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows, cols_busqueda, cols_a_modificar, nom_campos,
                                                          tipo_campos, dic_operaciones)

        rta = Ejecutar_SQL.update_filas(sSql, 'frm_ajuste_inventario_patio/actualizarStocksProductos_estadoInicialPrimera',
                                        BasesDeDatos.DB_PRINCIPAL)

        return rta

    def actualizarStocksProductos_estadoInicialSegunda(self, rows):

        df = pd.DataFrame(rows, columns=['id', 'cant'])
        df = df.groupby(['id']).sum()

        rows = df.to_records().tolist()

        nom_tabla = 'producto'
        cols_busqueda = [0]
        cols_a_modificar = [1]

        nom_campos = ['id_producto', 'stock_segunda']

        dic_operaciones = {'stock_segunda': 'stock_segunda - '}

        tipo_campos = ['int', 'int']

        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows, cols_busqueda, cols_a_modificar, nom_campos,
                                                          tipo_campos, dic_operaciones)

        rta = Ejecutar_SQL.update_filas(sSql, 'frm_ajuste_inventario_patio/actualizarStocksProductos_estadoInicialSegunda',
                                        BasesDeDatos.DB_PRINCIPAL)

        return rta

    def actualizarStocksProductos_nuevoEstadoPrimera(self, rows):
        ## al stock actual se le resta el valor de cant
        df = pd.DataFrame(rows, columns = ['id', 'cant'])
        df = df.groupby(['id']).sum()

        rows = df.to_records().tolist()

        nom_tabla = 'producto'
        cols_busqueda = [0]
        cols_a_modificar = [1]

        nom_campos = ['id_producto', 'stock_primera']

        dic_operaciones = {'stock_primera': 'stock_primera + '}


        tipo_campos = ['int', 'int']

        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows, cols_busqueda, cols_a_modificar, nom_campos,
                                                          tipo_campos, dic_operaciones)

        rta = Ejecutar_SQL.update_filas(sSql, 'frm_ajuste_inventario_patio/actualizarStocksProductos_nuevoEstadoPrimera',
                                        BasesDeDatos.DB_PRINCIPAL)

        return rta

    def actualizarStocksProductos_nuevoEstadoSegunda(self, rows):
        ## al stock actual se le resta el valor de cant
        df = pd.DataFrame(rows, columns=['id', 'cant'])
        df = df.groupby(['id']).sum()

        rows = df.to_records().tolist()

        nom_tabla = 'producto'
        cols_busqueda = [0]
        cols_a_modificar = [1]

        nom_campos = ['id_producto', 'stock_segunda']

        dic_operaciones = {'stock_segunda': 'stock_segunda + '}

        tipo_campos = ['int', 'int']

        sSql = GenerarSql.crearMultiUpdateSql_operaciones(nom_tabla, rows, cols_busqueda, cols_a_modificar, nom_campos,
                                                          tipo_campos, dic_operaciones)

        rta = Ejecutar_SQL.update_filas(sSql, 'frm_ajuste_inventario_patio/actualizarStocksProductos_nuevoEstadoSegunda',
                                        BasesDeDatos.DB_PRINCIPAL)

        return rta

    def inicializacion(self):
        self.punteroFilaProducto = 0
        self.cargar_combo_productos()
        self.set_configuaracion_grilla_producto()


    def cargar_combo_productos(self):
        from formEAY.dbaseCAC.dbProductos import Get_productos
        obj_sql = Get_productos()

        rows = obj_sql.listaBasica(cant_registros=100)

        if rows != None:
            la_lista = ManipularRows.crearListaValores(rows, 1)
            self.dic_productos = ManipularRows.crearDiccionarioTodosLosCampos(rows, 1)
            self.comboBox_producto.Set(la_lista)


    def set_configuaracion_grilla_producto(self):
        list_columnas = [0,1, 2, 4]
        ManipularGrillas.setColumnasSoloLectura(self.grid_producto, list_columnas)

        list_columnas = [5]
        ManipularGrillas.setColumnasFormatoCHK(self.grid_producto, list_columnas)

        list_columnas = [3]
        ManipularGrillas.setColumnasSoloNumeros(self.grid_producto, list_columnas)


        self.grid_producto.AutoSizeColumns()

        #self.grid_producto.SetSortingColumn(1)


