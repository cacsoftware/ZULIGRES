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

from formEAY.utilCAC.ClasesValidatorEAY import MyValidator, DIGIT_ONLY

from formEAY.utilCAC.FormatoEAY import ManipularRows
from formEAY.constantesCAC.imgCAC import Img_grillas, Img_produccion
from formEAY.utilCAC.FormatoEAY import ManipularGrillas


###########################################################################
## Class Extrusion
###########################################################################

class Extrusion(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Registrar de Extrusión", pos=wx.DefaultPosition,
                          size=wx.Size(1040, 680), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(1040, 680), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        validador_in_solo_digitos = MyValidator(DIGIT_ONLY)

        icono_grillas = Img_grillas()
        img_produccion = Img_produccion()

        bSizer_extrusion = wx.BoxSizer(wx.VERTICAL)

        bSizer_panel_principal = wx.BoxSizer(wx.VERTICAL)

        bSizer_panel_cabecera = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_cabecera = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel_cabecera.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.bitmap_logo_proceso = wx.StaticBitmap(self.panel_cabecera, wx.ID_ANY,
                                                   wx.Bitmap(img_produccion.EXTRUSION,
                                                             wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.bitmap_logo_proceso, 0, wx.ALL, 5)

        bSizer9.Add(bSizer7, 0, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_turno = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Turno:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.lbl_etq_turno.Wrap(-1)
        bSizer14.Add(self.lbl_etq_turno, 0, wx.ALL, 5)

        comboBox_turnoChoices = []
        self.comboBox_turno = wx.ComboBox(self.panel_cabecera, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                          wx.Size(190, -1), comboBox_turnoChoices, wx.CB_READONLY | wx.CB_SORT)
        bSizer14.Add(self.comboBox_turno, 1, wx.ALL, 5)

        self.lbl_etq_total_coches = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Total coches:", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        self.lbl_etq_total_coches.Wrap(-1)
        bSizer14.Add(self.lbl_etq_total_coches, 0, wx.ALL, 5)

        self.txt_total_coches = wx.TextCtrl(self.panel_cabecera, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(55, -1), validator=validador_in_solo_digitos)
        bSizer14.Add(self.txt_total_coches, 0, wx.ALL, 5)

        self.lbl_etq_total_unidades = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Total Unidades:",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_total_unidades.Wrap(-1)
        bSizer14.Add(self.lbl_etq_total_unidades, 0, wx.ALL, 5)

        self.txt_total_unidades = wx.TextCtrl(self.panel_cabecera, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.Size(65, -1), validator=validador_in_solo_digitos)

        bSizer14.Add(self.txt_total_unidades, 0, wx.ALL, 5)

        bSizer6.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer81 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fecha_inicio = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Inicio:", wx.DefaultPosition,
                                                  wx.Size(70, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_fecha_inicio.Wrap(-1)
        bSizer81.Add(self.lbl_etq_fecha_inicio, 0, wx.ALL, 5)

        self.datePicker_fecha_inicio_extrusion = wx.adv.DatePickerCtrl(self.panel_cabecera, wx.ID_ANY,
                                                                       wx.DefaultDateTime,
                                                                       wx.DefaultPosition, wx.DefaultSize,
                                                                       style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer81.Add(self.datePicker_fecha_inicio_extrusion, 0, wx.ALL, 5)

        self.timePicker_hora_inicio_extrusion = wx.adv.TimePickerCtrl(self.panel_cabecera, id=wx.ID_ANY,
                                                                      dt=wx.DefaultDateTime,
                                                                      pos=wx.DefaultPosition, size=wx.Size(110, -1),
                                                                      style=wx.FNTP_DEFAULT_STYLE,
                                                                      validator=wx.DefaultValidator)

        bSizer81.Add(self.timePicker_hora_inicio_extrusion, 0, wx.ALL, 5)

        bSizer13.Add(bSizer81, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fecha_fin = wx.StaticText(self.panel_cabecera, wx.ID_ANY, u"Fecha Fin:", wx.DefaultPosition,
                                               wx.DefaultSize, wx.ALIGN_RIGHT)
        self.lbl_etq_fecha_fin.Wrap(-1)
        bSizer8.Add(self.lbl_etq_fecha_fin, 1, wx.ALIGN_LEFT | wx.ALL, 5)

        self.datePicker_fecha_fin = wx.adv.DatePickerCtrl(self.panel_cabecera, wx.ID_ANY, wx.DefaultDateTime,
                                                          wx.DefaultPosition, wx.Size(90, -1),
                                                          style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer8.Add(self.datePicker_fecha_fin, 0, wx.ALL, 5)

        self.timePicker_hora_fin_extrusion = wx.adv.TimePickerCtrl(self.panel_cabecera, id=wx.ID_ANY,
                                                                   dt=wx.DefaultDateTime,
                                                                   pos=wx.DefaultPosition, size=wx.Size(110, -1),
                                                                   style=wx.FNTP_DEFAULT_STYLE,
                                                                   validator=wx.DefaultValidator)

        bSizer8.Add(self.timePicker_hora_fin_extrusion, 0, wx.ALL, 5)

        bSizer13.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer6.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer9.Add(bSizer6, 1, wx.EXPAND, 5)

        self.panel_cabecera.SetSizer(bSizer9)
        self.panel_cabecera.Layout()
        bSizer9.Fit(self.panel_cabecera)
        bSizer_panel_cabecera.Add(self.panel_cabecera, 1, wx.EXPAND | wx.ALL, 5)

        bSizer_panel_principal.Add(bSizer_panel_cabecera, 0, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_panel_empleado = wx.BoxSizer(wx.VERTICAL)

        self.panel_empleado = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel_empleado.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer47 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_selecciona_personal = wx.StaticText(self.panel_empleado, wx.ID_ANY, u"Seleciona el Personal",
                                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_selecciona_personal.Wrap(-1)
        bSizer47.Add(self.lbl_etq_selecciona_personal, 0, wx.ALL, 5)

        checkList_personalChoices = [u"A", u"B", u"C", u"D", u"E"]
        self.checkList_personal = wx.CheckListBox(self.panel_empleado, wx.ID_ANY, wx.DefaultPosition, wx.Size(200, 200),
                                                  checkList_personalChoices, wx.LB_MULTIPLE)
        bSizer47.Add(self.checkList_personal, 1, wx.ALL | wx.EXPAND, 5)

        self.panel_empleado.SetSizer(bSizer47)
        self.panel_empleado.Layout()
        bSizer47.Fit(self.panel_empleado)
        bSizer_panel_empleado.Add(self.panel_empleado, 1, wx.EXPAND | wx.ALL, 5)

        bSizer4.Add(bSizer_panel_empleado, 1, wx.EXPAND, 5)

        bSizer_panel_extrusion1 = wx.BoxSizer(wx.VERTICAL)

        self.panel1_extrusion = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel1_extrusion.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_panel_extrusion = wx.BoxSizer(wx.VERTICAL)

        bSizer141 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_producto = wx.StaticText(self.panel1_extrusion, wx.ID_ANY, u"Producto:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_etq_producto.Wrap(-1)
        bSizer141.Add(self.lbl_etq_producto, 0, wx.ALL, 5)

        comboBox_productoChoices = []
        self.comboBox_producto = wx.ComboBox(self.panel1_extrusion, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                             wx.DefaultSize, comboBox_productoChoices, wx.CB_READONLY)
        bSizer141.Add(self.comboBox_producto, 2, wx.ALL, 5)

        self.lbl_etq_coche = wx.StaticText(self.panel1_extrusion, wx.ID_ANY, u"Coche-Est:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.lbl_etq_coche.Wrap(-1)
        bSizer141.Add(self.lbl_etq_coche, 0, wx.ALL, 5)

        comboBox_cocheChoices = []
        self.comboBox_coche = wx.ComboBox(self.panel1_extrusion, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                          wx.DefaultSize, comboBox_cocheChoices, wx.CB_READONLY)
        bSizer141.Add(self.comboBox_coche, 1, wx.ALL, 5)

        self.lbl_etq_cant_coches = wx.StaticText(self.panel1_extrusion, wx.ID_ANY, u"Cant Coches:", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.lbl_etq_cant_coches.Wrap(-1)
        bSizer141.Add(self.lbl_etq_cant_coches, 0, wx.ALL, 5)

        self.txt_cant_coches = wx.TextCtrl(self.panel1_extrusion, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(45, -1), validator=validador_in_solo_digitos)
        bSizer141.Add(self.txt_cant_coches, 0, wx.ALL, 5)

        self.lbl_etq_x_coche = wx.StaticText(self.panel1_extrusion, wx.ID_ANY, u"Unidades:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.lbl_etq_x_coche.Wrap(-1)
        bSizer141.Add(self.lbl_etq_x_coche, 0, wx.ALL, 5)

        self.txt_unidades_x_coche = wx.TextCtrl(self.panel1_extrusion, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.Size(55, -1), validator=validador_in_solo_digitos)
        bSizer141.Add(self.txt_unidades_x_coche, 0, wx.ALL, 5)

        self.btn_a_lista_extrusion = wx.Button(self.panel1_extrusion, wx.ID_ANY, u"--> Lista", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        bSizer141.Add(self.btn_a_lista_extrusion, 0, wx.ALL, 5)

        bSizer_panel_extrusion.Add(bSizer141, 0, wx.EXPAND, 5)

        bSizer46 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline2 = wx.StaticLine(self.panel1_extrusion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer46.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer_panel_extrusion.Add(bSizer46, 0, wx.EXPAND, 5)

        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

        self.grid_extrusion = wx.grid.Grid(self.panel1_extrusion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_extrusion.CreateGrid(5, 6

                                       )
        self.grid_extrusion.EnableEditing(True)
        self.grid_extrusion.EnableGridLines(True)
        self.grid_extrusion.EnableDragGridSize(False)
        self.grid_extrusion.SetMargins(0, 0)

        # Columns
        self.grid_extrusion.EnableDragColMove(False)
        self.grid_extrusion.EnableDragColSize(True)
        self.grid_extrusion.SetColLabelSize(30)
        self.grid_extrusion.SetColLabelValue(0, u"id")
        self.grid_extrusion.SetColLabelValue(1, u"Producto")
        self.grid_extrusion.SetColLabelValue(2, u"Coche")
        self.grid_extrusion.SetColLabelValue(3, u"Cant Coches")
        self.grid_extrusion.SetColLabelValue(4, u"Unid Producto")
        self.grid_extrusion.SetColLabelValue(5, u"Sel")
        self.grid_extrusion.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_extrusion.EnableDragRowSize(True)
        self.grid_extrusion.SetRowLabelSize(40)
        self.grid_extrusion.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_extrusion.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.grid_extrusion.AutoSizeColumns()
        bSizer16.Add(self.grid_extrusion, 1, wx.ALL | wx.EXPAND, 5)

        bSizer41 = wx.BoxSizer(wx.VERTICAL)

        self.bpButton_eliminar_item_seleccionado_grid_extrusion = wx.BitmapButton(self.panel1_extrusion, wx.ID_ANY,
                                                                                  wx.Bitmap(
                                                                                      icono_grillas.ELIMINAR_ITEM_SELECIONADO,
                                                                                      wx.BITMAP_TYPE_ANY),
                                                                                  wx.DefaultPosition, wx.DefaultSize,
                                                                                  wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_eliminar_item_seleccionado_grid_extrusion.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.ELIMINAR_ITEM_SELECIONADO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer41.Add(self.bpButton_eliminar_item_seleccionado_grid_extrusion, 0, wx.ALL, 5)

        self.bpButton_deseleccionar_todo_grid_extrusion = wx.BitmapButton(self.panel1_extrusion, wx.ID_ANY,
                                                                          wx.Bitmap(
                                                                              icono_grillas.DESELECCIONAR_TODO,
                                                                              wx.BITMAP_TYPE_ANY),
                                                                          wx.DefaultPosition, wx.DefaultSize,
                                                                          wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_deseleccionar_todo_grid_extrusion.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer41.Add(self.bpButton_deseleccionar_todo_grid_extrusion, 0, wx.ALL, 5)

        self.m_staticline1 = wx.StaticLine(self.panel1_extrusion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer41.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.bpButton_limpiar_grid_extrusion1 = wx.BitmapButton(self.panel1_extrusion, wx.ID_ANY, wx.Bitmap(
            icono_grillas.LIMPIAR_GRILLA, wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                                                wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_limpiar_grid_extrusion1.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.LIMPIAR_GRILLA_SEL, wx.BITMAP_TYPE_ANY))
        bSizer41.Add(self.bpButton_limpiar_grid_extrusion1, 0, wx.ALL, 5)

        bSizer16.Add(bSizer41, 0, wx.EXPAND, 5)

        bSizer_panel_extrusion.Add(bSizer16, 1, wx.EXPAND, 5)

        self.panel1_extrusion.SetSizer(bSizer_panel_extrusion)
        self.panel1_extrusion.Layout()
        bSizer_panel_extrusion.Fit(self.panel1_extrusion)
        bSizer_panel_extrusion1.Add(self.panel1_extrusion, 1, wx.EXPAND | wx.ALL, 5)

        bSizer4.Add(bSizer_panel_extrusion1, 2, wx.EXPAND, 5)

        bSizer_panel_principal.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer_notebook = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       0 | wx.FULL_REPAINT_ON_RESIZE)
        self.panel_notebook_boquillas = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                 wx.TAB_TRAVERSAL)
        self.panel_notebook_boquillas.SetBackgroundColour(wx.Colour(255, 255, 255))
        bSizer_panel_notebook_boquillas = wx.BoxSizer(wx.VERTICAL)

        bSizer32 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_informacion_boquillas = wx.StaticText(self.panel_notebook_boquillas, wx.ID_ANY,
                                                           u"//  Se registra la hora de inico de la extrusión con determinada Boquilla",
                                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_informacion_boquillas.Wrap(-1)
        self.lbl_etq_informacion_boquillas.SetForegroundColour(wx.Colour(0, 128, 0))

        bSizer32.Add(self.lbl_etq_informacion_boquillas, 0, wx.ALL, 5)

        bSizer_panel_notebook_boquillas.Add(bSizer32, 0, wx.EXPAND, 5)

        bSizer33 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_boquilla = wx.StaticText(self.panel_notebook_boquillas, wx.ID_ANY, u"Boquilla:",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_boquilla.Wrap(-1)
        bSizer33.Add(self.lbl_etq_boquilla, 0, wx.ALL, 5)

        comboBox_boquillasChoices = []
        self.comboBox_boquillas = wx.ComboBox(self.panel_notebook_boquillas, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                              wx.DefaultSize, comboBox_boquillasChoices, wx.CB_READONLY)
        bSizer33.Add(self.comboBox_boquillas, 0, wx.ALL, 5)

        self.lbl_etq_hora_1_extrusion = wx.StaticText(self.panel_notebook_boquillas, wx.ID_ANY, u"Hora 1:",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_hora_1_extrusion.Wrap(-1)
        bSizer33.Add(self.lbl_etq_hora_1_extrusion, 0, wx.ALL, 5)

        self.timePicker_hora_1 = wx.adv.TimePickerCtrl(self.panel_notebook_boquillas, id=wx.ID_ANY,
                                                       dt=wx.DefaultDateTime,
                                                       pos=wx.DefaultPosition, size=wx.Size(110, -1),
                                                       style=wx.FNTP_DEFAULT_STYLE,
                                                       validator=wx.DefaultValidator)
        bSizer33.Add(self.timePicker_hora_1, 0, wx.ALL, 5)

        self.lbl_etq_hora_2_extrusion = wx.StaticText(self.panel_notebook_boquillas, wx.ID_ANY, u"Hora 2:",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_hora_2_extrusion.Wrap(-1)
        bSizer33.Add(self.lbl_etq_hora_2_extrusion, 0, wx.ALL, 5)

        self.timePicker_hora_2 = wx.adv.TimePickerCtrl(self.panel_notebook_boquillas, id=wx.ID_ANY,
                                                       dt=wx.DefaultDateTime,
                                                       pos=wx.DefaultPosition, size=wx.Size(110, -1),
                                                       style=wx.FNTP_DEFAULT_STYLE,
                                                       validator=wx.DefaultValidator)
        bSizer33.Add(self.timePicker_hora_2, 0, wx.ALL, 5)

        self.lbl_etq_contador_1 = wx.StaticText(self.panel_notebook_boquillas, wx.ID_ANY, u"Contador 1:",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_contador_1.Wrap(-1)
        bSizer33.Add(self.lbl_etq_contador_1, 0, wx.ALL, 5)

        self.txt_contador_1 = wx.TextCtrl(self.panel_notebook_boquillas, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(110, -1), validator=validador_in_solo_digitos)
        self.txt_contador_1.SetMaxLength(12)
        bSizer33.Add(self.txt_contador_1, 0, wx.ALL, 5)

        self.lbl_etq_contador_2 = wx.StaticText(self.panel_notebook_boquillas, wx.ID_ANY, u"Contador 2:",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_contador_2.Wrap(-1)
        bSizer33.Add(self.lbl_etq_contador_2, 0, wx.ALL, 5)

        self.txt_contador_2 = wx.TextCtrl(self.panel_notebook_boquillas, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(110, -1), validator=validador_in_solo_digitos)
        self.txt_contador_2.SetMaxLength(12)
        bSizer33.Add(self.txt_contador_2, 0, wx.ALL, 5)

        self.btn_a_lista_boquilla = wx.Button(self.panel_notebook_boquillas, wx.ID_ANY, u"--> Lista",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer33.Add(self.btn_a_lista_boquilla, 0, wx.ALL, 5)

        bSizer_panel_notebook_boquillas.Add(bSizer33, 0, wx.EXPAND, 5)

        bSizer34 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer52 = wx.BoxSizer(wx.VERTICAL)

        self.grid_boquilla = wx.grid.Grid(self.panel_notebook_boquillas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          0)

        # Grid
        self.grid_boquilla.CreateGrid(5, 7)
        self.grid_boquilla.EnableEditing(True)
        self.grid_boquilla.EnableGridLines(True)
        self.grid_boquilla.EnableDragGridSize(False)
        self.grid_boquilla.SetMargins(0, 0)

        # Columns
        self.grid_boquilla.EnableDragColMove(False)
        self.grid_boquilla.EnableDragColSize(True)
        self.grid_boquilla.SetColLabelSize(30)
        self.grid_boquilla.SetColLabelValue(0, u"id")
        self.grid_boquilla.SetColLabelValue(1, u"Boquilla")
        self.grid_boquilla.SetColLabelValue(2, u"Contador 1")
        self.grid_boquilla.SetColLabelValue(3, u"Contador 2")
        self.grid_boquilla.SetColLabelValue(4, u"Hora 1")
        self.grid_boquilla.SetColLabelValue(5, u"Hora 2")
        self.grid_boquilla.SetColLabelValue(6, u"Sel")
        self.grid_boquilla.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_boquilla.SetRowSize(0, 19)
        self.grid_boquilla.SetRowSize(1, 18)
        self.grid_boquilla.SetRowSize(2, 19)
        self.grid_boquilla.SetRowSize(3, 19)
        self.grid_boquilla.SetRowSize(4, 19)
        self.grid_boquilla.EnableDragRowSize(True)
        self.grid_boquilla.SetRowLabelSize(40)
        self.grid_boquilla.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_boquilla.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.grid_boquilla.AutoSizeColumns()

        bSizer52.Add(self.grid_boquilla, 1, wx.ALL | wx.EXPAND, 5)

        bSizer34.Add(bSizer52, 1, wx.EXPAND, 5)

        bSizer412 = wx.BoxSizer(wx.VERTICAL)

        self.bpButton_eliminar_item_seleccionado_grid_boquilla = wx.BitmapButton(self.panel_notebook_boquillas,
                                                                                 wx.ID_ANY, wx.Bitmap(
                icono_grillas.ELIMINAR_ITEM_SELECIONADO, wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                                                 wx.DefaultSize,
                                                                                 wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_eliminar_item_seleccionado_grid_boquilla.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.ELIMINAR_ITEM_SELECIONADO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer412.Add(self.bpButton_eliminar_item_seleccionado_grid_boquilla, 0, wx.ALL, 5)

        self.bpButton_deseleccionar_todo_grid_boquilla = wx.BitmapButton(self.panel_notebook_boquillas, wx.ID_ANY,
                                                                         wx.Bitmap(
                                                                             icono_grillas.DESELECCIONAR_TODO,
                                                                             wx.BITMAP_TYPE_ANY),
                                                                         wx.DefaultPosition, wx.DefaultSize,
                                                                         wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_deseleccionar_todo_grid_boquilla.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer412.Add(self.bpButton_deseleccionar_todo_grid_boquilla, 0, wx.ALL, 5)

        self.m_staticline12 = wx.StaticLine(self.panel_notebook_boquillas, wx.ID_ANY, wx.DefaultPosition,
                                            wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer412.Add(self.m_staticline12, 0, wx.EXPAND | wx.ALL, 5)

        self.bpButton_limpiar_grid_boquilla = wx.BitmapButton(self.panel_notebook_boquillas, wx.ID_ANY,
                                                              wx.Bitmap(
                                                                  icono_grillas.LIMPIAR_GRILLA,
                                                                  wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                              wx.DefaultSize, wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_limpiar_grid_boquilla.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.LIMPIAR_GRILLA_SEL, wx.BITMAP_TYPE_ANY))
        bSizer412.Add(self.bpButton_limpiar_grid_boquilla, 0, wx.ALL, 5)

        bSizer34.Add(bSizer412, 0, wx.EXPAND, 5)

        bSizer_panel_notebook_boquillas.Add(bSizer34, 1, wx.EXPAND, 5)

        self.panel_notebook_boquillas.SetSizer(bSizer_panel_notebook_boquillas)
        self.panel_notebook_boquillas.Layout()
        bSizer_panel_notebook_boquillas.Fit(self.panel_notebook_boquillas)
        self.m_notebook1.AddPage(self.panel_notebook_boquillas, u"Boquillas", True)
        self.panel_notebook_recesos = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                               wx.TAB_TRAVERSAL)
        self.panel_notebook_recesos.SetBackgroundColour(wx.Colour(255, 255, 255))
        bSizer_panel_notebook_recesos = wx.BoxSizer(wx.VERTICAL)

        bSizer36 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_informacion_recesos = wx.StaticText(self.panel_notebook_recesos, wx.ID_ANY,
                                                         u"//  La cantidad de minutos que tarda el  receso puede ser editada directamente en la grilla",
                                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_informacion_recesos.Wrap(-1)
        self.lbl_etq_informacion_recesos.SetForegroundColour(wx.Colour(0, 128, 0))

        bSizer36.Add(self.lbl_etq_informacion_recesos, 0, wx.ALL, 5)

        bSizer_panel_notebook_recesos.Add(bSizer36, 0, wx.EXPAND, 5)

        bSizer341 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer48 = wx.BoxSizer(wx.VERTICAL)

        self.grid_recesos = wx.grid.Grid(self.panel_notebook_recesos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_recesos.CreateGrid(5, 3)
        self.grid_recesos.EnableEditing(True)
        self.grid_recesos.EnableGridLines(True)
        self.grid_recesos.EnableDragGridSize(False)
        self.grid_recesos.SetMargins(0, 0)

        # Columns
        self.grid_recesos.EnableDragColMove(False)
        self.grid_recesos.EnableDragColSize(True)
        self.grid_recesos.SetColLabelSize(30)
        self.grid_recesos.SetColLabelValue(0, u"id")
        self.grid_recesos.SetColLabelValue(1, u"Receso")
        self.grid_recesos.SetColLabelValue(2, u"Minutos")
        self.grid_recesos.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_recesos.EnableDragRowSize(True)
        self.grid_recesos.SetRowLabelSize(40)
        self.grid_recesos.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_recesos.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)

        self.grid_recesos.AutoSizeColumns()

        bSizer48.Add(self.grid_recesos, 1, wx.ALL | wx.EXPAND, 5)

        bSizer341.Add(bSizer48, 1, wx.EXPAND, 5)

        bSizer_panel_notebook_recesos.Add(bSizer341, 1, wx.EXPAND, 5)

        self.panel_notebook_recesos.SetSizer(bSizer_panel_notebook_recesos)
        self.panel_notebook_recesos.Layout()
        bSizer_panel_notebook_recesos.Fit(self.panel_notebook_recesos)
        self.m_notebook1.AddPage(self.panel_notebook_recesos, u"Recesos Programados", False)
        self.panel_notebook_novedades1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                  wx.TAB_TRAVERSAL)
        self.panel_notebook_novedades1.SetBackgroundColour(wx.Colour(255, 255, 255))
        panel_notebook_novedades = wx.BoxSizer(wx.VERTICAL)

        bSizer321 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_informacion_novedades = wx.StaticText(self.panel_notebook_novedades1, wx.ID_ANY,
                                                           u"//  Se registran  acontecimientos ocurridos en el turno de trabajo, por ejemplo:  Averia banda transportadora",
                                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_informacion_novedades.Wrap(-1)
        self.lbl_etq_informacion_novedades.SetForegroundColour(wx.Colour(0, 128, 0))

        bSizer321.Add(self.lbl_etq_informacion_novedades, 0, wx.ALL, 5)

        panel_notebook_novedades.Add(bSizer321, 0, wx.EXPAND, 5)

        bSizer331 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_novedad = wx.StaticText(self.panel_notebook_novedades1, wx.ID_ANY, u"Novedad:", wx.DefaultPosition,
                                             wx.Size(75, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_novedad.Wrap(-1)
        bSizer331.Add(self.lbl_etq_novedad, 0, wx.ALL, 5)

        self.txt_novedad = wx.TextCtrl(self.panel_notebook_novedades1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer331.Add(self.txt_novedad, 1, wx.ALL, 5)

        panel_notebook_novedades.Add(bSizer331, 0, wx.EXPAND, 5)

        bSizer3311 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fecha_hora_novedades = wx.StaticText(self.panel_notebook_novedades1, wx.ID_ANY, u"Fecha - Hora:",
                                                          wx.DefaultPosition, wx.Size(75, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_fecha_hora_novedades.Wrap(-1)
        bSizer3311.Add(self.lbl_etq_fecha_hora_novedades, 0, wx.ALL, 5)

        self.datePicker_fecha_novedad = wx.adv.DatePickerCtrl(self.panel_notebook_novedades1, wx.ID_ANY,
                                                              wx.DefaultDateTime,
                                                              wx.DefaultPosition, wx.DefaultSize,
                                                              style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer3311.Add(self.datePicker_fecha_novedad, 0, wx.ALL, 5)

        self.timePicker_hora_novedad = wx.adv.TimePickerCtrl(self.panel_notebook_novedades1, id=wx.ID_ANY,
                                                             dt=wx.DefaultDateTime,
                                                             pos=wx.DefaultPosition, size=wx.Size(110, -1),
                                                             style=wx.FNTP_DEFAULT_STYLE,
                                                             validator=wx.DefaultValidator)
        bSizer3311.Add(self.timePicker_hora_novedad, 0, wx.ALL, 5)

        self.lbl_etq_tiempor_parada_novedad = wx.StaticText(self.panel_notebook_novedades1, wx.ID_ANY,
                                                            u"Tiempo Parada (minutos):", wx.DefaultPosition,
                                                            wx.DefaultSize, 0)
        self.lbl_etq_tiempor_parada_novedad.Wrap(-1)
        bSizer3311.Add(self.lbl_etq_tiempor_parada_novedad, 0, wx.ALL, 5)

        self.txt_tiempo_parada_minutos = wx.TextCtrl(self.panel_notebook_novedades1, wx.ID_ANY, u"0",
                                                     wx.DefaultPosition, wx.Size(80, -1),
                                                     validator=validador_in_solo_digitos)

        bSizer3311.Add(self.txt_tiempo_parada_minutos, 0, wx.ALL, 5)

        self.btn_a_lista_novedades = wx.Button(self.panel_notebook_novedades1, wx.ID_ANY, u"--> Lista",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3311.Add(self.btn_a_lista_novedades, 0, wx.ALL, 5)

        panel_notebook_novedades.Add(bSizer3311, 0, wx.EXPAND, 5)

        bSizer342 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer521 = wx.BoxSizer(wx.VERTICAL)

        self.grid_novedades = wx.grid.Grid(self.panel_notebook_novedades1, wx.ID_ANY, wx.DefaultPosition,
                                           wx.DefaultSize, 0)

        # Grid
        self.grid_novedades.CreateGrid(5, 5)
        self.grid_novedades.EnableGridLines(True)
        self.grid_novedades.EnableDragGridSize(False)
        self.grid_novedades.SetMargins(0, 0)

        # Columns
        self.grid_novedades.EnableDragColMove(False)
        self.grid_novedades.EnableDragColSize(True)
        self.grid_novedades.SetColLabelSize(30)
        self.grid_novedades.SetColLabelValue(0, u"Fecha")
        self.grid_novedades.SetColLabelValue(1, u"Hora")
        self.grid_novedades.SetColLabelValue(2, u"parada (min)")
        self.grid_novedades.SetColLabelValue(3, u"Novedad")
        self.grid_novedades.SetColLabelValue(4, u"Sel")
        self.grid_novedades.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_novedades.SetRowSize(0, 19)
        self.grid_novedades.SetRowSize(1, 18)
        self.grid_novedades.SetRowSize(2, 19)
        self.grid_novedades.SetRowSize(3, 19)
        self.grid_novedades.SetRowSize(4, 19)
        self.grid_novedades.EnableDragRowSize(True)
        self.grid_novedades.SetRowLabelSize(40)
        self.grid_novedades.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_novedades.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)

        self.grid_novedades.AutoSizeColumns()

        bSizer521.Add(self.grid_novedades, 1, wx.ALL | wx.EXPAND, 5)

        bSizer342.Add(bSizer521, 1, wx.EXPAND, 5)

        bSizer4121 = wx.BoxSizer(wx.VERTICAL)

        self.bpButton_eliminar_item_seleccionado_grid_novedades = wx.BitmapButton(self.panel_notebook_novedades1,
                                                                                  wx.ID_ANY, wx.Bitmap(
                icono_grillas.ELIMINAR_ITEM_SELECIONADO, wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                                                  wx.DefaultSize,
                                                                                  wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_eliminar_item_seleccionado_grid_novedades.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.ELIMINAR_ITEM_SELECIONADO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer4121.Add(self.bpButton_eliminar_item_seleccionado_grid_novedades, 0, wx.ALL, 5)

        self.bpButton_deseleccionar_todo_grid_novedades = wx.BitmapButton(self.panel_notebook_novedades1, wx.ID_ANY,
                                                                          wx.Bitmap(
                                                                              icono_grillas.DESELECCIONAR_TODO,
                                                                              wx.BITMAP_TYPE_ANY),
                                                                          wx.DefaultPosition, wx.DefaultSize,
                                                                          wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_deseleccionar_todo_grid_novedades.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer4121.Add(self.bpButton_deseleccionar_todo_grid_novedades, 0, wx.ALL, 5)

        self.m_staticline121 = wx.StaticLine(self.panel_notebook_novedades1, wx.ID_ANY, wx.DefaultPosition,
                                             wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer4121.Add(self.m_staticline121, 0, wx.EXPAND | wx.ALL, 5)

        self.bpButton_limpiar_grid_extrusion2 = wx.BitmapButton(self.panel_notebook_novedades1, wx.ID_ANY,
                                                                wx.Bitmap(
                                                                    icono_grillas.LIMPIAR_GRILLA,
                                                                    wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                                wx.DefaultSize,
                                                                wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_limpiar_grid_extrusion2.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.LIMPIAR_GRILLA_SEL, wx.BITMAP_TYPE_ANY))
        bSizer4121.Add(self.bpButton_limpiar_grid_extrusion2, 0, wx.ALL, 5)

        bSizer342.Add(bSizer4121, 0, wx.EXPAND, 5)

        panel_notebook_novedades.Add(bSizer342, 1, wx.EXPAND, 5)

        self.panel_notebook_novedades1.SetSizer(panel_notebook_novedades)
        self.panel_notebook_novedades1.Layout()
        panel_notebook_novedades.Fit(self.panel_notebook_novedades1)
        self.m_notebook1.AddPage(self.panel_notebook_novedades1, u"Novedades", False)
        self.panel_notebook_notas1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.TAB_TRAVERSAL)
        self.panel_notebook_notas1.SetBackgroundColour(wx.Colour(255, 255, 255))
        panel_notebook_notas = wx.BoxSizer(wx.VERTICAL)

        bSizer3211 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_etq_informacion_notas = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY,
                                                       u"//  Fecha Evento, indica cuando puede ser relevante una Nota",
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_informacion_notas.Wrap(-1)
        self.lbl_etq_informacion_notas.SetForegroundColour(wx.Colour(0, 128, 0))

        bSizer3211.Add(self.lbl_etq_informacion_notas, 0, wx.ALL, 5)

        panel_notebook_notas.Add(bSizer3211, 0, wx.EXPAND, 5)

        bSizer3312 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_nota = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"Nota:", wx.DefaultPosition,
                                          wx.Size(75, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_nota.Wrap(-1)
        bSizer3312.Add(self.lbl_etq_nota, 0, wx.ALL, 5)

        self.txt_nota = wx.TextCtrl(self.panel_notebook_notas1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizer3312.Add(self.txt_nota, 1, wx.ALL, 5)

        panel_notebook_notas.Add(bSizer3312, 0, wx.EXPAND, 5)

        bSizer33111 = wx.BoxSizer(wx.HORIZONTAL)

        self.lbl_etq_fecha_evento = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"Fecha Evento:",
                                                  wx.DefaultPosition, wx.Size(75, -1), wx.ALIGN_RIGHT)
        self.lbl_etq_fecha_evento.Wrap(-1)
        bSizer33111.Add(self.lbl_etq_fecha_evento, 0, wx.ALL, 5)

        self.datePicker_fecha_evento_nota = wx.adv.DatePickerCtrl(self.panel_notebook_notas1, wx.ID_ANY,
                                                                  wx.DefaultDateTime,
                                                                  wx.DefaultPosition, wx.DefaultSize,
                                                                  style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        bSizer33111.Add(self.datePicker_fecha_evento_nota, 0, wx.ALL, 5)

        self.lbl_etq_area = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"Area:", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.lbl_etq_area.Wrap(-1)
        bSizer33111.Add(self.lbl_etq_area, 0, wx.ALL, 5)

        self.lbl_extrusion = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"EXTRUSION", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.lbl_extrusion.Wrap(-1)
        bSizer33111.Add(self.lbl_extrusion, 0, wx.ALL, 5)

        self.lbl_etq_relevancia = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"Relevancia:",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_etq_relevancia.Wrap(-1)
        bSizer33111.Add(self.lbl_etq_relevancia, 0, wx.ALL, 5)

        comboBox_relevancia_notaChoices = []
        self.comboBox_relevancia_nota = wx.ComboBox(self.panel_notebook_notas1, wx.ID_ANY, u"Combo!",
                                                    wx.DefaultPosition, wx.DefaultSize, comboBox_relevancia_notaChoices,
                                                    wx.CB_READONLY)
        bSizer33111.Add(self.comboBox_relevancia_nota, 1, wx.ALL, 5)

        self.lbl_etq_contexto = wx.StaticText(self.panel_notebook_notas1, wx.ID_ANY, u"Contexto:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.lbl_etq_contexto.Wrap(-1)
        bSizer33111.Add(self.lbl_etq_contexto, 0, wx.ALL, 5)

        comboBox_contextoChoices = []
        self.comboBox_contexto = wx.ComboBox(self.panel_notebook_notas1, wx.ID_ANY, u"Combo!", wx.DefaultPosition,
                                             wx.DefaultSize, comboBox_contextoChoices, wx.CB_READONLY)
        bSizer33111.Add(self.comboBox_contexto, 1, wx.ALL, 5)

        self.btn_a_lista_notas = wx.Button(self.panel_notebook_notas1, wx.ID_ANY, u"--> Lista", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        bSizer33111.Add(self.btn_a_lista_notas, 0, wx.ALL, 5)

        panel_notebook_notas.Add(bSizer33111, 0, wx.EXPAND, 5)

        bSizer3421 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5211 = wx.BoxSizer(wx.VERTICAL)

        self.grid_notas = wx.grid.Grid(self.panel_notebook_notas1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_notas.CreateGrid(5, 5)
        self.grid_notas.EnableEditing(True)
        self.grid_notas.EnableGridLines(True)
        self.grid_notas.EnableDragGridSize(False)
        self.grid_notas.SetMargins(0, 0)

        # Columns
        self.grid_notas.EnableDragColMove(False)
        self.grid_notas.EnableDragColSize(True)
        self.grid_notas.SetColLabelSize(30)
        self.grid_notas.SetColLabelValue(0, u"Fecha")
        self.grid_notas.SetColLabelValue(1, u"Relevancia")
        self.grid_notas.SetColLabelValue(2, u"Contexto")
        self.grid_notas.SetColLabelValue(3, u"Nota")
        self.grid_notas.SetColLabelValue(4, u"Sel")
        self.grid_notas.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_notas.SetRowSize(0, 19)
        self.grid_notas.SetRowSize(1, 18)
        self.grid_notas.SetRowSize(2, 19)
        self.grid_notas.SetRowSize(3, 19)
        self.grid_notas.SetRowSize(4, 19)
        self.grid_notas.EnableDragRowSize(True)
        self.grid_notas.SetRowLabelSize(40)
        self.grid_notas.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_notas.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)

        self.grid_notas.AutoSizeColumns()

        bSizer5211.Add(self.grid_notas, 1, wx.ALL | wx.EXPAND, 5)

        bSizer3421.Add(bSizer5211, 1, wx.EXPAND, 5)

        bSizer41211 = wx.BoxSizer(wx.VERTICAL)

        self.bpButton_eliminar_item_seleccionado_grid_notas = wx.BitmapButton(self.panel_notebook_notas1, wx.ID_ANY,
                                                                              wx.Bitmap(
                                                                                  icono_grillas.ELIMINAR_ITEM_SELECIONADO,
                                                                                  wx.BITMAP_TYPE_ANY),
                                                                              wx.DefaultPosition, wx.DefaultSize,
                                                                              wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_eliminar_item_seleccionado_grid_notas.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.ELIMINAR_ITEM_SELECIONADO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer41211.Add(self.bpButton_eliminar_item_seleccionado_grid_notas, 0, wx.ALL, 5)

        self.bpButton_deseleccionar_todo_grid_notas = wx.BitmapButton(self.panel_notebook_notas1, wx.ID_ANY,
                                                                      wx.Bitmap(
                                                                          icono_grillas.DESELECCIONAR_TODO,
                                                                          wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                                      wx.DefaultSize, wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_deseleccionar_todo_grid_notas.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.DESELECCIONAR_TODO_SEL, wx.BITMAP_TYPE_ANY))
        bSizer41211.Add(self.bpButton_deseleccionar_todo_grid_notas, 0, wx.ALL, 5)

        self.m_staticline1211 = wx.StaticLine(self.panel_notebook_notas1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.LI_HORIZONTAL)
        bSizer41211.Add(self.m_staticline1211, 0, wx.EXPAND | wx.ALL, 5)

        self.bpButton_limpiar_grid_extrusion = wx.BitmapButton(self.panel_notebook_notas1, wx.ID_ANY,
                                                               wx.Bitmap(
                                                                   icono_grillas.LIMPIAR_GRILLA,
                                                                   wx.BITMAP_TYPE_ANY), wx.DefaultPosition,
                                                               wx.DefaultSize, wx.BU_AUTODRAW | wx.NO_BORDER)

        self.bpButton_limpiar_grid_extrusion.SetBitmapCurrent(
            wx.Bitmap(icono_grillas.LIMPIAR_GRILLA_SEL, wx.BITMAP_TYPE_ANY))
        bSizer41211.Add(self.bpButton_limpiar_grid_extrusion, 0, wx.ALL, 5)

        bSizer3421.Add(bSizer41211, 0, wx.EXPAND, 5)

        panel_notebook_notas.Add(bSizer3421, 1, wx.EXPAND, 5)

        self.panel_notebook_notas1.SetSizer(panel_notebook_notas)
        self.panel_notebook_notas1.Layout()
        panel_notebook_notas.Fit(self.panel_notebook_notas1)
        self.m_notebook1.AddPage(self.panel_notebook_notas1, u"Notas", False)

        bSizer_notebook.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        bSizer_panel_principal.Add(bSizer_notebook, 1, wx.EXPAND, 5)

        bSizer_pie_de_formulario = wx.BoxSizer(wx.HORIZONTAL)

        bSizer56 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_ver_formato = wx.Button(self, wx.ID_ANY, u"Ver formato", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer56.Add(self.btn_ver_formato, 0, wx.ALL, 5)

        self.btn_ver_procedimiento = wx.Button(self, wx.ID_ANY, u"Ver Procedimiento", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        bSizer56.Add(self.btn_ver_procedimiento, 0, wx.ALL, 5)

        bSizer_pie_de_formulario.Add(bSizer56, 1, wx.EXPAND, 5)

        bSizer55 = wx.BoxSizer(wx.VERTICAL)

        self.btn_guardar = wx.Button(self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)
        self.btn_guardar.SetBackgroundColour(wx.Colour(128, 255, 128))

        bSizer55.Add(self.btn_guardar, 0, wx.ALL, 5)

        bSizer_pie_de_formulario.Add(bSizer55, 0, wx.EXPAND, 5)

        bSizer_panel_principal.Add(bSizer_pie_de_formulario, 0, wx.EXPAND, 5)

        bSizer_extrusion.Add(bSizer_panel_principal, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer_extrusion)
        self.Layout()

        self.Centre(wx.BOTH)

        ## OPERACIONES INICIALES EAY
        self.cargar_valores_de_inicializacion()

        # Connect Events
        self.comboBox_boquillas.Bind(wx.EVT_COMBOBOX, self.comboBox_boquillasOnCombobox)
        self.comboBox_boquillas.Bind(wx.EVT_LEFT_DOWN, self.comboBox_boquillasOnLeftDown)

        self.comboBox_turno.Bind(wx.EVT_COMBOBOX, self.comboBox_turnoOnCombobox)
        self.btn_a_lista_extrusion.Bind(wx.EVT_BUTTON, self.btn_a_lista_extrusionOnButtonClick)
        self.bpButton_eliminar_item_seleccionado_grid_extrusion.Bind(wx.EVT_BUTTON,
                                                                     self.bpButton_eliminar_item_seleccionado_grid_extrusionOnButtonClick)
        self.bpButton_deseleccionar_todo_grid_extrusion.Bind(wx.EVT_BUTTON,
                                                             self.bpButton_deseleccionar_todo_grid_extrusionOnButtonClick)
        self.bpButton_limpiar_grid_extrusion1.Bind(wx.EVT_BUTTON,
                                                   self.bpButton_limpiar_grid_extrusionOnButtonClick)
        self.btn_a_lista_boquilla.Bind(wx.EVT_BUTTON, self.btn_a_lista_boquillaOnButtonClick)
        self.grid_boquilla.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_boquillaOnGridCellLeftClick)
        self.bpButton_eliminar_item_seleccionado_grid_boquilla.Bind(wx.EVT_BUTTON,
                                                                    self.bpButton_eliminar_item_seleccionado_grid_boquillaOnButtonClick)
        self.bpButton_deseleccionar_todo_grid_boquilla.Bind(wx.EVT_BUTTON,
                                                            self.bpButton_deseleccionar_todo_grid_boquillaOnButtonClick)
        self.bpButton_limpiar_grid_boquilla.Bind(wx.EVT_BUTTON,
                                                 self.bpButton_limpiar_grid_boquillaOnButtonClick)
        self.btn_a_lista_novedades.Bind(wx.EVT_BUTTON, self.btn_a_lista_novedadesOnButtonClick)
        self.grid_novedades.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_novedadesOnGridCellLeftClick)
        self.bpButton_eliminar_item_seleccionado_grid_novedades.Bind(wx.EVT_BUTTON,
                                                                     self.bpButton_eliminar_item_seleccionado_grid_novedadesOnButtonClick)
        self.bpButton_deseleccionar_todo_grid_novedades.Bind(wx.EVT_BUTTON,
                                                             self.bpButton_deseleccionar_todo_grid_novedadesOnButtonClick)
        self.bpButton_limpiar_grid_extrusion2.Bind(wx.EVT_BUTTON,
                                                   self.bpButton_limpiar_grid_extrusionOnButtonClick)
        self.btn_a_lista_notas.Bind(wx.EVT_BUTTON, self.btn_a_lista_notasOnButtonClick)
        self.grid_notas.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_notasOnGridCellLeftClick)
        self.bpButton_eliminar_item_seleccionado_grid_notas.Bind(wx.EVT_BUTTON,
                                                                 self.bpButton_eliminar_item_seleccionado_grid_notasOnButtonClick)
        self.bpButton_deseleccionar_todo_grid_notas.Bind(wx.EVT_BUTTON,
                                                         self.bpButton_deseleccionar_todo_grid_notasOnButtonClick)
        self.bpButton_limpiar_grid_extrusion.Bind(wx.EVT_BUTTON,
                                                  self.bpButton_limpiar_grid_extrusionOnButtonClick)
        self.btn_ver_formato.Bind(wx.EVT_BUTTON, self.btn_ver_formatoOnButtonClick)
        self.btn_ver_procedimiento.Bind(wx.EVT_BUTTON, self.btn_ver_procedimientoOnButtonClick)
        self.btn_guardar.Bind(wx.EVT_BUTTON, self.btn_guardarOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class

    def comboBox_boquillasOnCombobox(self, event):

        event.Skip()

    def comboBox_boquillasOnLeftDown(self, event):
        if self.comboBox_boquillas.GetItems() == []:
            self.cargar_combo_boquillas()
        event.Skip()

    def comboBox_turnoOnCombobox(self, event):

        str_turno = self.comboBox_turno.GetValue()
        lista_turnos = self.dic_turnos_todos[str_turno]

        h1 = lista_turnos[2]
        h2 = lista_turnos[3]

        self.timePicker_hora_inicio_extrusion.SetTime(h1.hour, h1.minute, h1.second)
        self.timePicker_hora_fin_extrusion.SetTime(h2.hour, h2.minute, h2.second)
        event.Skip()

    def btn_a_lista_notasOnButtonClick(self, event):
        from formEAY.utilCAC.FormatoEAY import ManipularGrillas, FormatearNumeros
        manipular_grilla = ManipularGrillas()

        nota = self.txt_nota.GetValue()
        area = U'EXTRUSION'
        relevancia = self.comboBox_relevancia_nota.GetValue()
        contexto = self.comboBox_contexto.GetValue()

        if nota == '':
            wx.MessageBox(u'Debes ingresar una Nota', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if relevancia == '':
            wx.MessageBox(u'Debes seleccionar una relevancia', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if contexto == '':
            wx.MessageBox(u'Debes seleccionar un contexto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        fecha = self.datePicker_fecha_evento_nota.GetValue()
        fecha = fecha.Format("%d/%m/%y")

        row = [fecha, relevancia, contexto, nota]
        self.puntero_fila_notas = manipular_grilla.nuevaFilaGrilla(self.grid_notas, row,
                                                                   self.puntero_fila_notas)
        event.Skip()

    def btn_a_lista_novedadesOnButtonClick(self, event):
        from formEAY.utilCAC.FormatoEAY import ManipularGrillas, FormatearNumeros
        manipular_grilla = ManipularGrillas()
        formato_numeros = FormatearNumeros()

        novedad = self.txt_novedad.GetValue()
        tiempo_parada = self.txt_tiempo_parada_minutos.GetValue()

        if novedad == '':
            wx.MessageBox(u'Debes ingresar una Novedad', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if tiempo_parada == '':
            wx.MessageBox(u'Debes ingresar un número valido para el tiempo de parada', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        tiempo_parada = formato_numeros.toNumMilesSigno(tiempo_parada)

        la_fecha = self.datePicker_fecha_novedad.GetValue()
        la_hora = self.timePicker_hora_novedad.GetValue()
        fecha = la_fecha.Format("%d/%m/%y")
        hora = la_hora.Format("%H:%M:%S")

        id_novedad = 25

        row = [fecha, hora, tiempo_parada, novedad]
        self.puntero_fila_novedades = manipular_grilla.nuevaFilaGrilla(self.grid_novedades, row,
                                                                       self.puntero_fila_novedades)
        event.Skip()

    def btn_a_lista_extrusionOnButtonClick(self, event):
        from formEAY.utilCAC.FormatoEAY import ManipularGrillas, FormatearNumeros
        manipular_grilla = ManipularGrillas()
        formato_numeros = FormatearNumeros()

        producto = self.comboBox_producto.GetValue()
        print(self.dic_extrusion)
        id_producto = self.dic_extrusion[producto]

        coche = self.comboBox_coche.GetValue()
        cant_coches = self.txt_cant_coches.GetValue()
        unidades_x_coche = self.txt_unidades_x_coche.GetValue()

        if producto == '':
            wx.MessageBox(u'Debes seleccionar un Producto', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if coche == '':
            wx.MessageBox(u'Debes seleccionar un tipo de coche', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if cant_coches == '' or cant_coches == '0':
            wx.MessageBox(u'Debes ingresar un número valido de coches', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        if unidades_x_coche == '' or unidades_x_coche == '0':
            wx.MessageBox(u'Debes ingresar un número valido de unidades por coche', u'Atención',
                          wx.OK | wx.ICON_INFORMATION)
            return 0

        # cant_coches = formato_numeros.toNumMilesSigno(cant_coches, '')
        # unidades_x_coche = formato_numeros.toNumMilesSigno(unidades_x_coche, '')

        row = [id_producto, producto, coche, cant_coches, unidades_x_coche]

        self.puntero_fila_extrusion = manipular_grilla.nuevaFilaGrilla(self.grid_extrusion, row,
                                                                       self.puntero_fila_extrusion)

        event.Skip()

    def btn_a_lista_boquillaOnButtonClick(self, event):
        from formEAY.utilCAC.FormatoEAY import ManipularGrillas, FormatearNumeros
        manipular_grilla = ManipularGrillas()
        formato_numeros = FormatearNumeros()

        boquilla = self.comboBox_boquillas.GetValue()
        id_boquilla = self.dic_boquillas[boquilla]
        if boquilla == '':
            wx.MessageBox(u'Debes seleccionar una Boquilla', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        contador1 = self.txt_contador_1.GetValue()
        if contador1 == '' or contador1 == '0':
            wx.MessageBox(u'Debes un número valido para el contador 1', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        contador1 = formato_numeros.toNumMilesSigno(int(contador1), '')

        contador2 = self.txt_contador_2.GetValue()
        if contador2 == '' or contador2 == '0':
            wx.MessageBox(u'Debes un número valido para el contador 2', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0
        contador2 = formato_numeros.toNumMilesSigno(int(contador2), '')

        hora1 = self.timePicker_hora_1.GetValue()
        hora2 = self.timePicker_hora_2.GetValue()

        hora1 = hora1.Format("%d/%m/%y")
        hora2 = hora2.Format("%d/%m/%y")

        row = [id_boquilla, boquilla, contador1, contador2, hora1, hora2]

        self.puntero_fila_boquilla = manipular_grilla.nuevaFilaGrilla(self.grid_boquilla, row,
                                                                      self.puntero_fila_boquilla)
        event.Skip()

    def bpButton_eliminar_item_seleccionado_grid_extrusionOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 5
        self.puntero_fila_extrusion = manipular_grilla.delFilasCHK(self.grid_extrusion, col_verificacion)
        event.Skip()

    def bpButton_deseleccionar_todo_grid_extrusionOnButtonClick(self, event):
        event.Skip()

    def bpButton_limpiar_grid_extrusionOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        self.puntero_fila_extrusion = manipular_grilla.limpiarGrilla(self.grid_extrusion)

        event.Skip()

    def grid_boquillaOnGridCellLeftClick(self, event):
        event.Skip()

    def bpButton_eliminar_item_seleccionado_grid_boquillaOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 6
        self.puntero_fila_boquilla = manipular_grilla.delFilasCHK(self.grid_boquilla, col_verificacion)
        event.Skip()

    def bpButton_deseleccionar_todo_grid_boquillaOnButtonClick(self, event):
        event.Skip()

    def bpButton_limpiar_grid_boquillaOnButtonClick(self, event):
        event.Skip()

    def grid_novedadesOnGridCellLeftClick(self, event):
        event.Skip()

    def bpButton_eliminar_item_seleccionado_grid_novedadesOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 4
        self.puntero_fila_novedades = manipular_grilla.delFilasCHK(self.grid_novedades, col_verificacion)
        event.Skip()

    def bpButton_deseleccionar_todo_grid_novedadesOnButtonClick(self, event):
        event.Skip()

    def grid_notasOnGridCellLeftClick(self, event):
        event.Skip()

    def bpButton_eliminar_item_seleccionado_grid_notasOnButtonClick(self, event):
        manipular_grilla = ManipularGrillas()
        col_verificacion = 4
        self.puntero_fila_notas = manipular_grilla.delFilasCHK(self.grid_notas, col_verificacion)
        event.Skip()

    def bpButton_deseleccionar_todo_grid_notasOnButtonClick(self, event):
        event.Skip()

    def btn_ver_formatoOnButtonClick(self, event):
        event.Skip()

    def btn_ver_procedimientoOnButtonClick(self, event):
        event.Skip()

    def btn_guardarOnButtonClick(self, event):

        turno = self.comboBox_turno.GetValue()
        if turno == '':
            wx.MessageBox(u'Debes seleccionar un turno', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        total_coches = self.txt_unidades_x_coche.GetValue()
        if total_coches == '' or total_coches == '0':
            wx.MessageBox(u'Debes ingresar un número valido de coches', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        total_unidades = self.txt_unidades_x_coche.GetValue()
        if total_unidades == '' or total_unidades == '0':
            wx.MessageBox(u'Debes ingresar un número valido de unidades', u'Atención', wx.OK | wx.ICON_INFORMATION)
            return 0

        id_turno = self.dic_turnos_todos[turno]

        event.Skip()

    ##  FUNCIONES EAY
    def cargar_valores_de_inicializacion(self):

        self.txt_total_coches.SetMaxLength(6)
        self.txt_total_unidades.SetMaxLength(9)
        self.txt_cant_coches.SetMaxLength(5)
        self.txt_unidades_x_coche.SetMaxLength(7)
        self.txt_contador_1.SetMaxLength(12)
        self.txt_contador_1.SetMaxLength(12)
        self.txt_tiempo_parada_minutos.SetMaxLength(4)

        self.puntero_fila_extrusion = 0
        self.puntero_fila_boquilla = 0
        self.puntero_fila_notas = 0
        self.puntero_fila_novedades = 0

        self.cargar_combo_productos()
        self.cargar_checkList_personal()
        self.cargar_combo_turnos()
        self.cargar_combo_coches()
        # self.cargar_combo_boquillas()
        self.cargar_combo_contexto_nota()
        self.cargar_combo_relevancia_nota()
        self.cargar_grid_receso_programado()
        self.limpiar_todas_las_grillas()

        self.set_configuracion_grillas()

    def set_configuracion_grillas(self):
        self.set_configuaracion_grilla_extrusion()
        self.set_configuaracion_grilla_boquilla()
        self.set_configuaracion_grilla_recesos()
        self.set_configuaracion_grilla_novedades()
        self.set_configuaracion_grilla_notas()

    def set_configuaracion_grilla_notas(self):
        manipular_grilla = ManipularGrillas()

        list_columnas = [0, 1, 2, 3]
        manipular_grilla.setColumnasSoloLectura(self.grid_notas, list_columnas)

        list_columnas = [4]
        manipular_grilla.setColumnasFormatoCHK(self.grid_notas, list_columnas)

    def set_configuaracion_grilla_novedades(self):
        manipular_grilla = ManipularGrillas()

        list_columnas = [0, 1, 2, 3]
        manipular_grilla.setColumnasSoloLectura(self.grid_novedades, list_columnas)

        list_columnas = [4]
        manipular_grilla.setColumnasFormatoCHK(self.grid_novedades, list_columnas)

    def set_configuaracion_grilla_boquilla(self):
        manipular_grilla = ManipularGrillas()

        list_columnas = [0, 1, 2, 3, 4, 5]
        manipular_grilla.setColumnasSoloLectura(self.grid_boquilla, list_columnas)

        list_columnas = [6]
        manipular_grilla.setColumnasFormatoCHK(self.grid_boquilla, list_columnas)

    def set_configuaracion_grilla_extrusion(self):
        manipular_grilla = ManipularGrillas()

        list_columnas = [0, 1, 2, 3, 4]
        manipular_grilla.setColumnasSoloLectura(self.grid_extrusion, list_columnas)

        list_columnas = [5]
        manipular_grilla.setColumnasFormatoCHK(self.grid_extrusion, list_columnas)

    def set_configuaracion_grilla_recesos(self):
        manipular_grilla = ManipularGrillas()

        list_columnas = [0, 1]
        manipular_grilla.setColumnasSoloLectura(self.grid_recesos, list_columnas)
        list_columnas = [2]
        manipular_grilla.setColumnasSoloNumeros(self.grid_recesos, list_columnas)

    def limpiar_todas_las_grillas(self):
        manipular_grilla = ManipularGrillas()

        self.puntero_fila_extrusion = manipular_grilla.limpiarGrilla(self.grid_extrusion)
        self.puntero_fila_boquilla = manipular_grilla.limpiarGrilla(self.grid_boquilla)
        self.puntero_fila_notas = manipular_grilla.limpiarGrilla(self.grid_notas)
        self.puntero_fila_novedades = manipular_grilla.limpiarGrilla(self.grid_novedades)

    def cargar_grid_receso_programado(self):
        from formEAY.dbaseCAC.dbVarios import DbGetVarios
        from formEAY.utilCAC.FormatoEAY import ManipularGrillas

        manipular_grilla = ManipularGrillas()
        obj_sql = DbGetVarios()

        rows, cabeceras = get_receso_programado(True)
        # id_receso, nom_receso, minutos_descanso

        manipular_grilla.llenarGrilla(self.grid_recesos, rows)

        cabeceras_grilla = [u' id', u'Receso', u'Minutos Descanso']
        manipular_grilla.setCabecerasGrilla(self.grid_recesos, cabeceras_grilla)

        # COLOR_AMARILLO_CLARO = wx.Colour(255, 255, 170)
        # dic_color = {1: COLOR_AMARILLO_CLARO, 2:wx.RED}
        # manipular_grilla.set_color_fondo_celda_grilla(self.grid_recesos, dic_color)

    def cargar_combo_relevancia_nota(self):
        from formEAY.dbaseCAC.dbVarios import DbGetVarios
        obj_sql = DbGetVarios()
        obj_formato = ManipularRows()

        rows, cabeceras = obj_sql.listaRelevanciaNota(True)
        # id_relevancia_nota, nom_relevancia

        if rows != None:
            la_lista = obj_formato.crearListaValores(rows, 1)
            self.dic_relevancia_nota = obj_formato.crearDiccionario(rows, 1, 0)
            self.comboBox_relevancia_nota.Set(la_lista)

    def cargar_combo_contexto_nota(self):
        from formEAY.dbaseCAC.dbVarios import DbGetVarios
        obj_sql = DbGetVarios()
        obj_formato = ManipularRows()

        rows, cabeceras = obj_sql.listaContextoNota(True)
        # id_contexto_nota, nom_contexto

        if rows != None:
            la_lista = obj_formato.crearListaValores(rows, 1)
            self.dic_contexto_nota = obj_formato.crearDiccionario(rows, 1, 0)
            self.comboBox_contexto.Set(la_lista)

    def cargar_combo_boquillas(self):
        from formEAY.dbaseCAC.dbVarios import DbGetVarios
        obj_sql = DbGetVarios()
        obj_formato = ManipularRows()

        rows, cabeceras = obj_sql.listaBoquillas(True)
        # id_coche, nom_coche

        if rows != None:
            la_lista = obj_formato.crearListaValores(rows, 1)
            self.dic_boquillas = obj_formato.crearDiccionario(rows, 1, 0)
            self.comboBox_boquillas.Set(la_lista)

    def cargar_combo_productos(self):
        from formEAY.dbaseCAC.dbProductos import Get_productos
        obj_sql = Get_productos()
        obj_formato = ManipularRows()

        rows, cabeceras = obj_sql.listaBasica(True)

        if rows != None:
            la_lista = obj_formato.crearListaValores(rows, 1)
            self.dic_extrusion = obj_formato.crearDiccionario(rows, 1, 0)
            self.comboBox_producto.Set(la_lista)

    def cargar_combo_turnos(self):
        from formEAY.dbaseCAC.dbVarios import DbGetVarios
        obj_sql = DbGetVarios()
        obj_formato = ManipularRows()

        rows, cabeceras = obj_sql.listaTurnos('EXTRUSION', True)
        # id_turno, nom_turno, hora_inicio, hora_salida, activo

        if rows != None:
            la_lista = obj_formato.crearListaValores(rows, 1)
            self.dic_turnos_todos = obj_formato.crearDiccionarioTodosLosCampos(rows, 1)
            self.comboBox_turno.Set(la_lista)

    def cargar_combo_coches(self):
        from formEAY.dbaseCAC.dbVarios import DbGetVarios
        obj_sql = DbGetVarios()
        obj_formato = ManipularRows()

        rows, cabeceras = obj_sql.listaCoches(True)
        # id_coche, nom_coche

        if rows != None:
            la_lista = obj_formato.crearListaValores(rows, 1)
            self.dic_coches = obj_formato.crearDiccionario(rows, 1, 0)
            self.comboBox_coche.Set(la_lista)

    def cargar_checkList_personal(self):
        from formEAY.dbaseCAC.dbEmpleados import Get_empleados
        obj_sql = Get_empleados()
        obj_formato = ManipularRows()

        rows, cabeceras = obj_sql.lista_basica('EXTRUSION')

        if rows != None:
            la_lista, diccionario = obj_formato.crearListaValoresYDicccionario(rows, 0, 1)
            self.checkList_personal.Set(la_lista)


