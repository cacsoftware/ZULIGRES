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

from pyeay.grillas import ManipularGrillas
from pyeay.dbcac.conexiondb import Ejecutar_SQL
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

from formEAY.constantesCAC.imgCAC import Img_formularios_general as Iconos

IMAGEN_EDITAR = Iconos.EDITAR
IMAGEN_EDITAR_SEL = Iconos.EDITAR_SEL

IMAGEN_NUEVO_CLIENTE = Iconos.NUEVO_CLIENTE
IMAGEN_NUEVO_CLIENTE_SEL = Iconos.NUEVO_CLIENTE_SEL

IMAGEN_LIMPIAR = Iconos.LIMPIAR_CONTROLES
IMAGEN_LIMPIAR_SEL = Iconos.LIMPIAR_CONTROLES_SEL


###########################################################################
## Class BuscarCliente
###########################################################################

class BuscarCliente(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Buscar Clientes", pos=wx.DefaultPosition,
                          size=wx.Size(1000, 650), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(745, 405), wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.padre = parent

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.m_panel4.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.m_panel4.SetMinSize(wx.Size(720, -1))

        bSizer_amarillo = wx.BoxSizer(wx.VERTICAL)

        bSizer_verde1 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_rojo1 = wx.BoxSizer(wx.VERTICAL)

        bSizer_morado5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText18 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Nit:", wx.DefaultPosition, wx.Size(55, -1),
                                            wx.ALIGN_RIGHT )
        self.m_staticText18.Wrap(-1)
        bSizer_morado5.Add(self.m_staticText18, 0, wx.ALL, 5)

        self.txt_nit = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer_morado5.Add(self.txt_nit, 0, wx.ALL, 5)

        self.m_staticText15 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"  R. Social:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        bSizer_morado5.Add(self.m_staticText15, 0, wx.ALL, 5)

        self.txt_razonSocial = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           wx.TE_PROCESS_ENTER)
        bSizer_morado5.Add(self.txt_razonSocial, 1, wx.ALL, 5)

        self.m_staticText151 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Id:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText151.Wrap(-1)
        bSizer_morado5.Add(self.m_staticText151, 0, wx.ALL, 5)

        self.lbl_id_cliente = wx.StaticText(self.m_panel4, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_id_cliente.Wrap(-1)
        bSizer_morado5.Add(self.lbl_id_cliente, 0, wx.ALL, 5)

        bSizer_rojo1.Add(bSizer_morado5, 0, wx.EXPAND, 5)

        bSizer_morado1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText16 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.Size(55, -1),
                                            wx.ALIGN_RIGHT)
        self.m_staticText16.Wrap(-1)
        bSizer_morado1.Add(self.m_staticText16, 0, wx.ALL, 5)

        self.txt_nombre = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
        self.txt_nombre.SetMinSize(wx.Size(100, -1))

        bSizer_morado1.Add(self.txt_nombre, 1, wx.ALL, 5)

        self.m_staticText23 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Apellido1:", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText23.Wrap(-1)
        bSizer_morado1.Add(self.m_staticText23, 0, wx.ALL, 5)

        self.txt_apellido = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer_morado1.Add(self.txt_apellido, 1, wx.ALL, 5)

        self.m_staticText17 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"apellido2:", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText17.Wrap(-1)
        bSizer_morado1.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.txt_apellido2 = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_PROCESS_ENTER)
        bSizer_morado1.Add(self.txt_apellido2, 1, wx.ALL, 5)

        bSizer_rojo1.Add(bSizer_morado1, 0, wx.EXPAND, 5)

        # bSizer_morado2 = wx.BoxSizer(wx.HORIZONTAL)
        #
        #
        #
        #
        # bSizer_rojo1.Add(bSizer_morado2, 0, wx.EXPAND, 5)

        bSizer_morado3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText12 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Celular:", wx.DefaultPosition, wx.Size(55, -1),
                                            wx.ALIGN_RIGHT)
        self.m_staticText12.Wrap(-1)
        bSizer_morado3.Add(self.m_staticText12, 0, wx.ALL, 5)

        self.txt_celular = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1),
                                       wx.TE_PROCESS_ENTER)
        bSizer_morado3.Add(self.txt_celular, 0, wx.ALL, 5)

        self.m_staticText131 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Dirección:", wx.DefaultPosition,
                                             wx.Size(55, -1), wx.ALIGN_RIGHT)
        self.m_staticText131.Wrap(-1)
        bSizer_morado3.Add(self.m_staticText131, 0, wx.ALL, 5)

        self.txt_dir = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer_morado3.Add(self.txt_dir, 1, wx.ALL, 5)



        self.m_staticText141 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Ciudad:", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText141.Wrap(-1)
        bSizer_morado3.Add(self.m_staticText141, 0, wx.ALL, 5)

        self.txt_ciudad = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(180, -1), wx.TE_PROCESS_ENTER)
        bSizer_morado3.Add(self.txt_ciudad, 0, wx.ALL, 5)

        bSizer_rojo1.Add(bSizer_morado3, 0, wx.EXPAND, 5)

        bSizer_morado4 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_rojo1.Add(bSizer_morado4, 0, wx.EXPAND, 5)

        bSizer_verde1.Add(bSizer_rojo1, 1, wx.EXPAND, 5)

        bSizer_rojo2 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2 = wx.Panel(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.Size(155, -1), wx.TAB_TRAVERSAL)
        self.m_panel2.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer_naranja2 = wx.BoxSizer(wx.VERTICAL)

        self.btn_buscar = wx.Button(self.m_panel2, wx.ID_ANY, u"&Buscar", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_naranja2.Add(self.btn_buscar, 0, wx.ALL | wx.EXPAND, 5)

        bSizer_naranja1 = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_limpiar = wx.BitmapButton(self.m_panel2, wx.ID_ANY,
                                           wx.Bitmap(IMAGEN_LIMPIAR,
                                                     wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                           wx.BU_AUTODRAW | wx.NO_BORDER)
        
        self.btn_limpiar.SetBitmapCurrent(
            wx.Bitmap(IMAGEN_LIMPIAR_SEL, wx.BITMAP_TYPE_ANY))
        bSizer_naranja1.Add(self.btn_limpiar, 0, wx.ALL, 5)

        self.btn_nuevo = wx.BitmapButton(self.m_panel2, wx.ID_ANY,
                                         wx.Bitmap(IMAGEN_NUEVO_CLIENTE,
                                                   wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                         wx.BU_AUTODRAW | wx.NO_BORDER)

        self.btn_nuevo.SetBitmapCurrent(
            wx.Bitmap(IMAGEN_NUEVO_CLIENTE_SEL, wx.BITMAP_TYPE_ANY))
        bSizer_naranja1.Add(self.btn_nuevo, 0, wx.ALL, 5)

        self.btn_editar = wx.BitmapButton(self.m_panel2, wx.ID_ANY,
                                          wx.Bitmap(IMAGEN_EDITAR,
                                                    wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                          wx.BU_AUTODRAW | wx.NO_BORDER)

        self.btn_editar.SetBitmapCurrent(
            wx.Bitmap(IMAGEN_EDITAR_SEL, wx.BITMAP_TYPE_ANY))

        bSizer_naranja1.Add(self.btn_editar, 0, wx.ALL, 5)

        bSizer_naranja2.Add(bSizer_naranja1, 0, wx.EXPAND, 5)

        self.btn_seleccionar = wx.Button(self.m_panel2, wx.ID_ANY, u"&Seleccionar", wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer_naranja2.Add(self.btn_seleccionar, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer_naranja2)
        self.m_panel2.Layout()
        bSizer_rojo2.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        bSizer_verde1.Add(bSizer_rojo2, 0, wx.EXPAND, 5)

        bSizer_amarillo.Add(bSizer_verde1, 0, wx.EXPAND, 5)

        bSizer_verde2 = wx.BoxSizer(wx.HORIZONTAL)

        self.grid_cliente = wx.grid.Grid(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_cliente.CreateGrid(0, 9)
        self.grid_cliente.EnableEditing(False)
        self.grid_cliente.EnableGridLines(True)
        self.grid_cliente.EnableDragGridSize(False)
        self.grid_cliente.SetMargins(0, 0)

        # Columns
        self.grid_cliente.AutoSizeColumns()
        self.grid_cliente.EnableDragColMove(True)
        self.grid_cliente.EnableDragColSize(True)
        self.grid_cliente.SetColLabelSize(30)
        self.grid_cliente.SetColLabelValue(0, u"id")
        self.grid_cliente.SetColLabelValue(1, u"R. Social")
        self.grid_cliente.SetColLabelValue(2, u"Nit")
        self.grid_cliente.SetColLabelValue(3, u"Nombre")
        self.grid_cliente.SetColLabelValue(4, u"Apellido 1")
        self.grid_cliente.SetColLabelValue(5, u"Apellido 2")
        self.grid_cliente.SetColLabelValue(6, u"celular")
        self.grid_cliente.SetColLabelValue(7, u"Dirección")
        self.grid_cliente.SetColLabelValue(8, u"Ciudad")
        self.grid_cliente.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_cliente.EnableDragRowSize(True)
        self.grid_cliente.SetRowLabelSize(50)
        self.grid_cliente.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.grid_cliente.SetLabelBackgroundColour(wx.Colour(245, 245, 245))

        # Cell Defaults
        self.grid_cliente.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        self.grid_cliente.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        bSizer_verde2.Add(self.grid_cliente, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_amarillo.Add(bSizer_verde2, 1, wx.EXPAND, 5)

        self.m_panel4.SetSizer(bSizer_amarillo)
        self.m_panel4.Layout()
        bSizer_amarillo.Fit(self.m_panel4)
        bSizer10.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer10)

        ## VALORES INICIALES EAY
        self.func_valores_iniciales()


        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btn_buscar.Bind(wx.EVT_BUTTON, self.btn_buscarOnButtonClick)
        self.btn_limpiar.Bind(wx.EVT_BUTTON, self.btn_limpiarOnButtonClick)
        self.btn_nuevo.Bind(wx.EVT_BUTTON, self.btn_nuevoOnButtonClick)
        self.btn_editar.Bind(wx.EVT_BUTTON, self.btn_editarOnButtonClick)
        self.btn_seleccionar.Bind(wx.EVT_BUTTON, self.btn_seleccionarOnButtonClick)
        self.grid_cliente.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_clienteOnGridCellLeftClick)

        self.txt_nit.Bind(wx.EVT_TEXT_ENTER, self.txt_nitOnTextEnter)
        self.txt_razonSocial.Bind(wx.EVT_TEXT_ENTER, self.txt_nitOnTextEnter)
        self.txt_nombre.Bind(wx.EVT_TEXT_ENTER, self.txt_nitOnTextEnter)
        self.txt_apellido.Bind(wx.EVT_TEXT_ENTER, self.txt_nitOnTextEnter)
        self.txt_apellido2.Bind(wx.EVT_TEXT_ENTER, self.txt_nitOnTextEnter)
        self.txt_celular.Bind(wx.EVT_TEXT_ENTER, self.txt_nitOnTextEnter)
        self.txt_dir.Bind(wx.EVT_TEXT_ENTER, self.txt_nitOnTextEnter)
        self.txt_ciudad.Bind(wx.EVT_TEXT_ENTER, self.txt_nitOnTextEnter)

    def __del__(self):
        pass

        # Virtual event handlers, overide them in your derived class

    def txt_nitOnTextEnter(self, event):
        self.func_buscar()
        event.Skip()

    def btn_buscarOnButtonClick(self, event):
        self.func_buscar()
        event.Skip()

    def btn_limpiarOnButtonClick(self, event):
        self.txt_nit.SetValue('')
        self.txt_razonSocial.SetValue('')
        self.txt_nombre.SetValue('')
        self.txt_apellido.SetValue('')
        self.txt_apellido2.SetValue('')
        self.txt_dir.SetValue('')
        self.txt_ciudad.SetValue('')
        self.lbl_id_cliente.SetLabel('')
        self.txt_celular.SetValue('')
        event.Skip()

    def btn_nuevoOnButtonClick(self, event):
        import formEAY.formularios.frm_generales.frm_nuevoCliente as frm_nuevoCliente
        frame_NuevoCliente = frm_nuevoCliente.NuevoCliente(self)
        frame_NuevoCliente.Center()
        frame_NuevoCliente.Show()
        event.Skip()

    def btn_editarOnButtonClick(self, event):
        nit = self.txt_nit.GetValue()
        razon_social = self.txt_razonSocial.GetValue()
        nom = self.txt_nombre.GetValue()
        ape1 = self.txt_apellido.GetValue()
        ape2 = self.txt_apellido2.GetValue()
        dir = self.txt_dir.GetValue()
        ciudad = self.txt_ciudad.GetValue()
        id_cliente = self.lbl_id_cliente.GetLabel()
        celular = self.txt_celular.GetValue()

        if id_cliente == '':
            return 0

        datos_cliente = [nom, ape1, ape2, nit, razon_social, dir, ciudad, celular, id_cliente]

        import formEAY.formularios.frm_generales.frm_editarCliente as frm_editarCliente
        frame_EditarCliente = frm_editarCliente.EditarCliente(self, datos_cliente)
        frame_EditarCliente.Center()
        frame_EditarCliente.Show()
        event.Skip()

    def btn_seleccionarOnButtonClick(self, event):
        dato = self.lbl_id_cliente.GetLabel()

        if dato == '':
            return 0

        nit = self.txt_nit.GetValue()
        razon_social = self.txt_razonSocial.GetValue()
        nom = self.txt_nombre.GetValue()
        ape1 = self.txt_apellido.GetValue()
        ape2 = self.txt_apellido2.GetValue()
        dir = self.txt_dir.GetValue()
        ciudad = self.txt_ciudad.GetValue()
        celular = self.txt_celular.GetValue()

        lista_valores = [nom, ape1, ape2, nit, razon_social, dir, ciudad, celular]

        self.padre.func_padreEayBuscarCliente(dato, lista_valores)
        self.Destroy()
        event.Skip()

    def grid_clienteOnGridCellLeftClick(self, event):
        fila = event.GetRow()

        self.lbl_id_cliente.SetLabel(self.grid_cliente.GetCellValue(fila, 0))
        self.txt_razonSocial.SetValue(self.grid_cliente.GetCellValue(fila, 1))
        self.txt_nit.SetValue(self.grid_cliente.GetCellValue(fila, 2))
        self.txt_nombre.SetValue(self.grid_cliente.GetCellValue(fila, 3))
        self.txt_apellido.SetValue(self.grid_cliente.GetCellValue(fila, 4))
        self.txt_apellido2.SetValue(self.grid_cliente.GetCellValue(fila, 5))
        self.txt_celular.SetValue(self.grid_cliente.GetCellValue(fila, 6))
        self.txt_dir.SetValue(self.grid_cliente.GetCellValue(fila, 7))
        self.txt_ciudad.SetValue(self.grid_cliente.GetCellValue(fila, 8))

        event.Skip()


    ## FUNCIONES EAY

    def func_padreEayNuevoCliente(self, nit):
        sSql = """
                    SELECT nit, id_cliente, razon_social, 
                                 nom, ape1, ape2,
                                 celular, dir, ciudad
                    FROM  cliente 
                    WHERE activo = 'True' AND nit = '{0}'
                """.format(nit)

        cabeceras = ['nit', 'id_cliente', 'razon_social', 'nom', 'ape1', 'ape2', 'dir', 'celular', 'ciudad']

        rows = Ejecutar_SQL.select_un_registro(sSql, 'frm_buscarCliente/buscar_cliente_por_nit', BasesDeDatos.DB_PRINCIPAL)

        if rows != None:
            el_id = str(rows[1])

            self.lbl_id_cliente.SetLabel(el_id)
            self.txt_nit.SetValue(rows[0])
            self.txt_razonSocial.SetValue(rows[2])
            self.txt_nombre.SetValue(rows[3])
            self.txt_apellido.SetValue(rows[4])
            self.txt_apellido2.SetValue(rows[5])
            self.txt_dir.SetValue(rows[7])
            self.txt_celular.SetValue(rows[6])
            self.txt_ciudad.SetValue(rows[8])

            self.Layout()


    def func_buscar(self):
        nit = self.txt_nit.GetValue()
        razon_social = self.txt_razonSocial.GetValue()
        nom = self.txt_nombre.GetValue()
        ape1 = self.txt_apellido.GetValue()
        ape2 = self.txt_apellido2.GetValue()
        dir = self.txt_dir.GetValue()
        ciudad = self.txt_ciudad.GetValue()
        id_cliente = self.lbl_id_cliente.GetLabel()
        celular = self.txt_celular.GetValue()

        lista_campos = ['nom', 'ape1', 'ape2', 'nit', 'razon_social', 'dir', 'ciudad', 'celular']
        lista_valores = [nom, ape1, ape2, nit, razon_social, dir, ciudad, celular]

        if ['', '', '', '', '', '', '', ''] == lista_valores:
            return 0

        cad_where = ' WHERE '
        cad_order_by = ' ORDER BY '
        i = 0

        for campo in lista_campos:
            if lista_valores[i] != '':
                cad_where += campo + " LIKE '%" + lista_valores[i] + "%' AND  "
                cad_order_by += campo + ', '
            i += 1

        cad_where = cad_where[:-5]
        cad_order_by = cad_order_by[:-2]

        cad_sql = """
                                SELECT id_cliente, razon_social, nit, nom, ape1, ape2, celular, dir, ciudad
                                FROM cliente   
                                {0}
                                {1}                            
                """.format(cad_where, cad_order_by)

        cabeceras = []
        try:
            rows = Ejecutar_SQL.select_varios_registros(cad_sql.upper(), 'frm_buscar_cliente/btn_buscarOnButtonClick',
                                                                   50, BasesDeDatos.DB_PRINCIPAL)
        except:
            pass  ## marca error porq no hay datos seleccionados

        ManipularGrillas.llenarGrilla(self.grid_cliente, rows)



    def func_valores_iniciales(self):
        self.grid_cliente.AutoSizeColumns()



