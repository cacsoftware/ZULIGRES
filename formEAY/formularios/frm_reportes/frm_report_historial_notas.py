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

from pyeay.rows import ManipularRows
from pyeay.grillas import ManipularGrillas
from pyeay.dbcac.conexiondb import Ejecutar_SQL
from formEAY.dbaseCAC.dbVarios import DbGetVarios
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

###########################################################################
## Class HistorialDeNotas
###########################################################################

class HistorialDeNotas(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Historial de Notas", pos=wx.DefaultPosition,
                          size=wx.Size(953, 605), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(750, 400), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        bSizer_principal = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_panelCabecera = wx.BoxSizer(wx.VERTICAL)

        self.panel_cabecera = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel_cabecera.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_cabecera = wx.BoxSizer(wx.VERTICAL)

        bSizer_rango_fechas = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_rangoFechas = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Rango Fechas", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.lbl_etq_rangoFechas.Wrap(-1)
        self.lbl_etq_rangoFechas.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_rangoFechas.SetForegroundColour(wx.Colour(255, 128, 64))

        bSizer_rango_fechas.Add(self.lbl_etq_rangoFechas, 0, wx.ALL, 5)

        bSizer_fecha1 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fechaInicial = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Inicial:", wx.DefaultPosition,
                                                  wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_fechaInicial.Wrap(-1)
        bSizer_fecha1.Add(self.lbl_etq_fechaInicial, 0, wx.ALL, 5)

        self.datePicker_fecha1 = wx.adv.DatePickerCtrl(self.panel_cabecera, wx.ID_ANY, wx.DefaultDateTime,
                                                   wx.DefaultPosition, wx.Size(-1, -1), style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer_fecha1.Add(self.datePicker_fecha1, 0, wx.ALL, 5)

        bSizer_rango_fechas.Add(bSizer_fecha1, 0, wx.EXPAND, 5)

        bSizer_fecha2 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fechaFinal = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Final:", wx.DefaultPosition,
                                                wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_fechaFinal.Wrap(-1)
        bSizer_fecha2.Add(self.lbl_etq_fechaFinal, 0, wx.ALL, 5)

        self.datePicker_fecha2 = wx.adv.DatePickerCtrl(self.panel_cabecera, wx.ID_ANY, wx.DefaultDateTime,
                                                   wx.DefaultPosition, wx.Size(-1, -1), style = wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer_fecha2.Add(self.datePicker_fecha2, 0, wx.ALL, 5)

        bSizer_rango_fechas.Add(bSizer_fecha2, 1, wx.EXPAND, 5)

        bSizer_cabecera.Add(bSizer_rango_fechas, 0, wx.EXPAND, 5)

        bSizer1611 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline311 = wx.StaticLine(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.LI_HORIZONTAL)
        bSizer1611.Add(self.m_staticline311, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_cabecera.Add(bSizer1611, 0, wx.EXPAND, 5)

        bSizer_area = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_area = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Area", wx.DefaultPosition, wx.DefaultSize,
                                          0)
        self.lbl_etq_area.Wrap(-1)
        self.lbl_etq_area.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_area.SetForegroundColour(wx.Colour(255, 128, 64))

        bSizer_area.Add(self.lbl_etq_area, 0, wx.ALL, 5)

        checkList_areaChoices = [u"EXTRUSION", u"CARGUE DE VAGONETAS", u"DESCARGUE DE VAGONETAS"]
        self.checkList_area = wx.CheckListBox(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              checkList_areaChoices, 0 | wx.NO_BORDER)
        bSizer_area.Add(self.checkList_area, 0, wx.ALL, 5)

        bSizer_cabecera.Add(bSizer_area, 0, wx.EXPAND, 5)

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline3 = wx.StaticLine(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer16.Add(self.m_staticline3, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_cabecera.Add(bSizer16, 0, wx.EXPAND, 5)

        bSizer_estado = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_estado = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Estado", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.lbl_etq_estado.Wrap(-1)
        self.lbl_etq_estado.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_estado.SetForegroundColour(wx.Colour(255, 128, 0))

        bSizer_estado.Add(self.lbl_etq_estado, 0, wx.ALL, 5)

        self.chk_activo = wx.CheckBox(self.panel_cabecera, wx.ID_ANY, u"Activo", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_estado.Add(self.chk_activo, 0, wx.ALL, 5)

        self.chk_inactivo = wx.CheckBox(self.panel_cabecera, wx.ID_ANY, u"Inactivo", wx.DefaultPosition, wx.DefaultSize,
                                       0)
        bSizer_estado.Add(self.chk_inactivo, 0, wx.ALL, 5)

        bSizer_cabecera.Add(bSizer_estado, 0, wx.EXPAND, 5)

        bSizer161 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline31 = wx.StaticLine(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_VERTICAL)
        bSizer161.Add(self.m_staticline31, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_cabecera.Add(bSizer161, 0, wx.EXPAND, 5)

        bSizer_area1 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_relevancia = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Relevancia", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.lbl_etq_relevancia.Wrap(-1)
        self.lbl_etq_relevancia.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_relevancia.SetForegroundColour(wx.Colour(255, 128, 64))

        bSizer_area1.Add(self.lbl_etq_relevancia, 0, wx.ALL, 5)

        checkList_relevanciaChoices = [u"EXTRUSION", u"CARGUE DE VAGONETAS", u"DESCARGUE DE VAGONETAS"]
        self.checkList_relevancia = wx.CheckListBox(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                    checkList_relevanciaChoices, 0 | wx.NO_BORDER)
        self.checkList_relevancia.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.checkList_relevancia.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer_area1.Add(self.checkList_relevancia, 0, wx.ALL | wx.EXPAND, 5)

        bSizer_cabecera.Add(bSizer_area1, 5, wx.EXPAND, 5)

        bSizer16111 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline3111 = wx.StaticLine(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.LI_HORIZONTAL)
        bSizer16111.Add(self.m_staticline3111, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_cabecera.Add(bSizer16111, 0, wx.EXPAND, 5)

        bSizer_area2 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_contexto = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Contexto", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_etq_contexto.Wrap(-1)
        self.lbl_etq_contexto.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_contexto.SetForegroundColour(wx.Colour(255, 128, 64))

        bSizer_area2.Add(self.lbl_etq_contexto, 0, wx.ALL, 5)

        checkList_contextoChoices = [u"EXTRUSION", u"CARGUE DE VAGONETAS", u"DESCARGUE DE VAGONETAS"]
        self.checkList_contexto = wx.CheckListBox(self.panel_cabecera, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                  checkList_contextoChoices, 0 | wx.NO_BORDER)
        bSizer_area2.Add(self.checkList_contexto, 0, wx.ALL | wx.EXPAND, 5)

        bSizer_cabecera.Add(bSizer_area2, 8, wx.EXPAND, 5)

        bSizer_botonesCabecera = wx.BoxSizer(wx.VERTICAL)

        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_estado_nota = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Estado", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.lbl_etq_estado_nota.Wrap(-1)
        self.lbl_etq_estado_nota.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))
        self.lbl_etq_estado_nota.SetForegroundColour(wx.Colour(255, 128, 64))

        bSizer19.Add(self.lbl_etq_estado_nota, 0, wx.ALL, 5)

        self.comboBox_estado_notaChoices = ['INDEFINIDO', 'REVISADO', 'PENDIENTE', 'TRAMITADO', 'TODOS']
        self.comboBox_estado_nota = wx.ComboBox(self.panel_cabecera, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                                wx.DefaultSize, self.comboBox_estado_notaChoices, wx.CB_READONLY)
        bSizer19.Add(self.comboBox_estado_nota, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_botonesCabecera.Add(bSizer19, 1, wx.EXPAND, 5)

        self.btn_buscar = wx.Button(self.panel_cabecera, wx.ID_ANY, u"&Buscar", wx.DefaultPosition, wx.DefaultSize,
                                    wx.NO_BORDER)
        self.btn_buscar.SetBackgroundColour(wx.Colour(0, 255, 255))

        bSizer_botonesCabecera.Add(self.btn_buscar, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_cabecera.Add(bSizer_botonesCabecera, 0, wx.EXPAND, 5)

        self.panel_cabecera.SetSizer(bSizer_cabecera)
        self.panel_cabecera.Layout()
        bSizer_cabecera.Fit(self.panel_cabecera)
        bSizer_panelCabecera.Add(self.panel_cabecera, 1, wx.EXPAND | wx.ALL, 5)

        bSizer_principal.Add(bSizer_panelCabecera, 0, wx.EXPAND, 5)

        bSizer_panelResultados = wx.BoxSizer(wx.VERTICAL)

        self.m_panel_resultados = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_resultados.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer_resultados = wx.BoxSizer(wx.VERTICAL)

        bSizer_totales = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_registros_encontrados = wx.StaticText(self.m_panel_resultados, wx.ID_ANY,
                                                           u"Registros visualizados:", wx.DefaultPosition,
                                                           wx.DefaultSize, 0)
        self.lbl_etq_registros_encontrados.Wrap(-1)
        bSizer_totales.Add(self.lbl_etq_registros_encontrados, 0, wx.ALL, 5)

        self.lbl_cant_registros = wx.StaticText(self.m_panel_resultados, wx.ID_ANY, u"0", wx.DefaultPosition,
                                                wx.Size(30, -1), 0)
        self.lbl_cant_registros.Wrap(-1)
        bSizer_totales.Add(self.lbl_cant_registros, 0, wx.ALL, 5)

        bSizer_resultados.Add(bSizer_totales, 0, wx.EXPAND, 5)

        self.grid_resultado_busqueda = wx.grid.Grid(self.m_panel_resultados, wx.ID_ANY, wx.DefaultPosition,
                                                    wx.DefaultSize, 0)

        # Grid
        self.grid_resultado_busqueda.CreateGrid(0, 10)
        self.grid_resultado_busqueda.EnableEditing(False)
        self.grid_resultado_busqueda.EnableGridLines(True)
        self.grid_resultado_busqueda.EnableDragGridSize(False)
        self.grid_resultado_busqueda.SetMargins(0, 0)

        # Columns
        self.grid_resultado_busqueda.AutoSizeColumns()
        self.grid_resultado_busqueda.EnableDragColMove(False)
        self.grid_resultado_busqueda.EnableDragColSize(True)
        self.grid_resultado_busqueda.SetColLabelSize(30)
        self.grid_resultado_busqueda.SetColLabelValue(0, u"id")
        self.grid_resultado_busqueda.SetColLabelValue(1, u"Fecha")
        self.grid_resultado_busqueda.SetColLabelValue(2, u"Area Producción")
        self.grid_resultado_busqueda.SetColLabelValue(3, u"Relevancia")
        self.grid_resultado_busqueda.SetColLabelValue(4, u"Contexto")
        self.grid_resultado_busqueda.SetColLabelValue(5, u"Estado")
        self.grid_resultado_busqueda.SetColLabelValue(6, u"Nota")
        self.grid_resultado_busqueda.SetColLabelValue(7, u"Contranota")
        self.grid_resultado_busqueda.SetColLabelValue(8, u"activo")
        self.grid_resultado_busqueda.SetColLabelValue(9, u"Uuid")

        #  cabeceras = ['id', 'Fecha', 'Area Produccion', 'Relevancia', 'Contexto',  'Estado', 'Nota', 'Contranota', 'activo', 'uuid', ]

        self.grid_resultado_busqueda.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_resultado_busqueda.EnableDragRowSize(True)
        self.grid_resultado_busqueda.SetRowLabelSize(1)
        self.grid_resultado_busqueda.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_resultado_busqueda.SetLabelBackgroundColour(wx.Colour(255, 255, 255))

        # Cell Defaults
        self.grid_resultado_busqueda.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer_resultados.Add(self.grid_resultado_busqueda, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel_resultados.SetSizer(bSizer_resultados)
        self.m_panel_resultados.Layout()
        bSizer_resultados.Fit(self.m_panel_resultados)
        bSizer_panelResultados.Add(self.m_panel_resultados, 1, wx.EXPAND | wx.ALL, 5)

        self.lbl_nota1 = wx.StaticText(self, wx.ID_ANY,
                                       u"// Para ver en detalle los registros --> DobleCliclik sobre la fila ",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_nota1.Wrap(-1)
        self.lbl_nota1.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.lbl_nota1.SetForegroundColour(wx.Colour(0, 128, 0))

        bSizer_panelResultados.Add(self.lbl_nota1, 0, wx.ALL, 5)

        bSizer_principal.Add(bSizer_panelResultados, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer_principal)
        self.Layout()

        self.Centre(wx.BOTH)

        ## VALORES INICIALES EAY
        self.inicializacion()

        # Connect Events
        self.btn_buscar.Bind(wx.EVT_BUTTON, self.btn_buscarOnButtonClick)
        self.grid_resultado_busqueda.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,
                                          self.grid_resultado_busquedaOnGridCellLeftDClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btn_buscarOnButtonClick(self, event):
        self.func_buscar()
        event.Skip()

    def grid_resultado_busquedaOnGridCellLeftDClick(self, event):
        import formEAY.formularios.frm_reportes.frm_detalle_nota as frm_detalle_nota
        fila = event.GetRow()

        dic_nota = {
            'id': self.grid_resultado_busqueda.GetCellValue(fila, 0),
            'fecha': self.grid_resultado_busqueda.GetCellValue(fila, 1),
            'area': self.grid_resultado_busqueda.GetCellValue(fila, 3),
            'relevancia': self.grid_resultado_busqueda.GetCellValue(fila, 4),
            'contexto': self.grid_resultado_busqueda.GetCellValue(fila, 5),
            'estado': self.grid_resultado_busqueda.GetCellValue(fila, 6),
            'nota': self.grid_resultado_busqueda.GetCellValue(fila, 7),
            'contranota': self.grid_resultado_busqueda.GetCellValue(fila, 8),
            'activo': self.grid_resultado_busqueda.GetCellValue(fila, 9)
        }


        frame_detalle_nota = frm_detalle_nota.DetalleNota(self, dic_nota, self.la_lista_relevancias )
        frame_detalle_nota.Center()
        frame_detalle_nota.Show()
        event.Skip()

    ###  FUNCIONES EAY

    def func_buscar(self):
        from formEAY.utilCAC.Utiles_proposito_general import ManejoFechasHoras

        cad_estado = ''

        if self.chk_activo.GetValue() == True:
            cad_estado += ' True,'
        if self.chk_inactivo.GetValue() == True:
            cad_estado += ' False'
        else:
            cad_estado = cad_estado[:-1]
        if cad_estado != '':
            cad_estado = ' and activo in (' + cad_estado + ')'
        else:
            wx.MessageBox(u'Debes seleccionar por lo menos un Estado de proceso', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        lista_areas_sel = self.checkList_area.GetCheckedStrings()
        if len(lista_areas_sel) == 0:
            wx.MessageBox(u'Debes seleccionar mínimo un Area de trabajo', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        cad_area = ''
        for area in lista_areas_sel:
            cad_area += "'" + area + "',"
        cad_area = cad_area[:-1]
        if cad_area != '':
            cad_area = ' and area_produccion in (' + cad_area + ' )'

        lista_relevancias_sel = self.checkList_relevancia.GetCheckedStrings()
        if len(lista_relevancias_sel) == 0:
            wx.MessageBox(u'Debes seleccionar mínimo una Relevancia', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        cad_relevancia = ''
        for relevancia in lista_relevancias_sel:
            cad_relevancia += "'" + relevancia + "',"
        cad_relevancia = cad_relevancia[:-1]
        if cad_relevancia != '':
            cad_relevancia = ' and relevancia in (' + cad_relevancia + ' )'

        lista_contextos_sel = self.checkList_contexto.GetCheckedStrings()
        if len(lista_contextos_sel) == 0:
            wx.MessageBox(u'Debes seleccionar mínimo un Contexto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        cad_contexto = ''
        for contexto in lista_contextos_sel:
            cad_contexto += "'" + contexto + "',"
        cad_contexto = cad_contexto[:-1]
        if cad_contexto != '':
            cad_contexto = ' and contexto in (' + cad_contexto + ' )'

        estado_nota = self.comboBox_estado_nota.GetValue()
        if estado_nota == '':
            wx.MessageBox(u'Debes seleccionar un estado Nota', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        else:
            if estado_nota != 'TODOS':
                cad_estado_nota = " AND estado = '" + estado_nota + "' "
            else:
                cad_estado_nota = ''

        fecha_inicio = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha1)
        fecha_fin = ManejoFechasHoras.formatearFechaXSql(self.datePicker_fecha2)

        cad_order_by = ' ORDER BY fecha DESC, area_produccion '

        sSql = """  SELECT id, fecha, current_date - fecha as dias, area_produccion, relevancia, contexto, estado, nota,  contranota, activo,  uuid
                            FROM notas_por_proceso
                            WHERE fecha >= '{0}'  and fecha <= '{1}'   {2}  {3}   {4}    {5}    {6}    {7}   
                                """.format(fecha_inicio, fecha_fin, cad_area, cad_estado, cad_relevancia, cad_contexto,
                                           cad_estado_nota, cad_order_by)

        cabeceras = ['id', 'Fecha', 'Dias', 'Area Produccion', 'Relevancia', 'Contexto', 'Estado', 'Nota', 'Contranota',
                     'activo', 'uuid', ]

        cant_columnas = len(cabeceras)
        ManipularGrillas.setCantidadColumnasGrilla(self.grid_resultado_busqueda, cant_columnas)
        ManipularGrillas.setCabecerasGrilla(self.grid_resultado_busqueda, cabeceras)

        self.grid_resultado_busqueda.HideCol(10)

        rows = Ejecutar_SQL.select_varios_registros(sSql, 'frm_report_historial_notas/buscar()', 150, BasesDeDatos.DB_PRINCIPAL)

        if rows == None:
            self.m_panel_resultados.Hide()
        else:
            self.m_panel_resultados.Show()
            ManipularGrillas.llenarGrilla(self.grid_resultado_busqueda, rows)

            cant_registros = len(rows)

            self.lbl_cant_registros.SetLabel(str(cant_registros))

        # dic_color = {4: COLOR_RESALTE1, 5: COLOR_RESALTE2}
        # ManipularGrillas.setColorFondoCeldaGrilla(self.grid_resultado_busqueda, dic_color)

        self.colorear_col_estado()

        ManipularGrillas.setColorGrisFilasEstadoTrueFalse(self.grid_resultado_busqueda, 9)

    def inicializacion(self):
        self.grid_resultado_busqueda.AutoSizeColumns()
        self.cargar_checkList_relevancia()
        self.cargar_checkList_contexto_nota()
        self.grid_resultado_busqueda.HideCol(9) ## uuid


    def colorear_col_estado(self):
        filas = self.grid_resultado_busqueda.GetNumberRows()
        cols = self.grid_resultado_busqueda.GetNumberCols()

        AMARILLO = wx.Colour(255, 255, 150)
        ROSADO = wx.Colour(255, 217, 230)
        AGUAMARINA = wx.Colour(208, 255, 248)

        dic_color = {'INDEFINIDO': wx.WHITE, 'REVISADO': AMARILLO, 'PENDIENTE':ROSADO , 'TRAMITADO': AGUAMARINA}
        for i in range(filas):
            dato = self.grid_resultado_busqueda.GetCellValue(i, 6)
            color = dic_color[dato]
            self.grid_resultado_busqueda.SetCellBackgroundColour(i, 6, color)

    def cargar_checkList_relevancia(self):
        rows = DbGetVarios.listaRelevanciaNota(True)
        # id_relevancia_nota, nom_relevancia

        if rows != None:
            self.la_lista_relevancias = ManipularRows.crearListaValores(rows, 1)
            self.dic_relevancia_nota = ManipularRows.crearDiccionario(rows, 1, 0)
            self.checkList_relevancia.Set(self.la_lista_relevancias)


    def cargar_checkList_contexto_nota(self):
        rows = DbGetVarios.listaContextoNota(True)
        # id_contexto_nota, nom_contexto

        if rows != None:
            la_lista_contexto_nota = ManipularRows.crearListaValores(rows, 1)
            self.dic_contexto_nota = ManipularRows.crearDiccionario(rows, 1, 0)
            self.checkList_contexto.Set(la_lista_contexto_nota)



