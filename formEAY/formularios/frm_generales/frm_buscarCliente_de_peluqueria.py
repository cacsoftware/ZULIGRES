# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################


import formEAY.constantesCAC.themeCAC as themeCAC
import formEAY.constantesCAC.configCAC as configCAC

import formEAY.constantesCAC.imgCAC as imgCAC
import formEAY.dbaseCAC.dbClientes as oobbdd
import wx
import wx.xrc
import wx.grid as grid
import types
# import formEAY.utilCAC.formateoEAY as formateoEAY
import formEAY.utilCAC.ClasesValidatorEAY as cvEAY


# import formEAY.formularios.forms_cliente.frm_nuevoCliente as frm_nuevoCliente
# import formEAY.formularios.forms_cliente.frm_editarCliente as frm_editarCliente

import sys


ICONO_CAC = imgCAC.Img_formularios.ICONO_CAC

IMAGEN_EDITAR = imgCAC.Img_editar.EDITAR

IMAGEN_EDITAR_SEL = imgCAC.Img_editar.EDITAR_SEL

IMAGEN_NUEVO_CLIENTE = imgCAC.Img_usuarios.NUEVO_CLIENTE
IMAGEN_NUEVO_CLIENTE_SEL = imgCAC.Img_usuarios.NUEVO_CLIENTE_SEL

IMAGEN_LIMPIAR = imgCAC.Img_navegacionFormulario.LIMPIAR
IMAGEN_LIMPIAR_SEL = imgCAC.Img_navegacionFormulario.LIMPIAR_SEL


IMAGEN_SELECCIONAR = imgCAC.Img_navegacionFormulario.SELECCIONAR
IMAGEN_SELECCIONAR_SEL = imgCAC.Img_navegacionFormulario.SELECCIONAR_SEL

COLOR_FONDO= themeCAC.frm_buscarCliente.frm_fondoColor
COLOR_LETRA_FONDO=themeCAC.frm_buscarCliente.frm_letraColor
COLOR_PANEL_CONTROLES=themeCAC.frm_buscarCliente.panelControles_fondoColor

ALPHA_ONLY = 1
DIGIT_ONLY = 2

COL_GRID=14
FILA_GRID=configCAC.cant_filas_GridBuscarCliente

###########################################################################
## Class BuscarCliente
###########################################################################

class BuscarCliente ( wx.Frame ):
	##tipoTercero  1 cliente  2 proveedor   3 empleado

	def __init__( self, parent, titulo = u"Clientes",  tipoTercero=1, permiteAgregar=1, permiteEditar=1,
				  permiteSeleccionar=1,  tipo_busqueda='SOLO_CLIENTES'
				  ):  #tipo tercero: 1:clientes , 2:proveedores, 3:empleados
						#tipo_busqueda='SOLO_CLIENTES', FULL (MUESTRA AL EDITAR O AL CREAR  LAS OPCIONES IS_CLIENTE, IS_PROVEEDOR, IS_EMPLEADO)
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = titulo, pos = wx.DefaultPosition, size = wx.Size( 1000,650 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.padre=parent
		self.tipo_busqueda=tipo_busqueda

		self.swEAY=0
		self.contadorFrames=0
		self.permiteSeleccionar=permiteSeleccionar
		#self.mostrarCupo=mostrarCupo
		self.tipoTercero=tipoTercero
		self.permiteAgregar=permiteAgregar
		self.permiteEditar=permiteEditar

		self.titulo = titulo

		#print 'ojo edinson', self.tipoTercero

		ico = wx.Icon(ICONO_CAC, wx.BITMAP_TYPE_ICO)
		self.SetIcon(ico)

		self.SetSizeHints( wx.Size( 745,405 ), wx.DefaultSize )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetForegroundColour(COLOR_LETRA_FONDO )
		self.m_panel4.SetBackgroundColour( COLOR_FONDO )
		self.m_panel4.SetMinSize( wx.Size( 720,-1 ) )

		bSizer_amarillo = wx.BoxSizer( wx.VERTICAL )

		bSizer_verde1 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer_rojo1 = wx.BoxSizer( wx.VERTICAL )


		bSizer_morado5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"  R. Social:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer_morado5.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.txt_razonSocial = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer_morado5.Add( self.txt_razonSocial, 1, wx.ALL, 5)

		bSizer_rojo1.Add( bSizer_morado5, 1, wx.EXPAND, 5 )


		bSizer_morado1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText16 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"  Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer_morado1.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.txt_nombre = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER  )
		self.txt_nombre.SetMinSize( wx.Size( 100,-1 ) )
		bSizer_morado1.Add( self.txt_nombre, 1, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Apellido1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer_morado1.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.txt_apellido = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER  )
		self.txt_apellido.SetMinSize( wx.Size( 80,-1 ) )
		bSizer_morado1.Add( self.txt_apellido, 1, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"apellido2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer_morado1.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.txt_apellido2 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER  )
		self.txt_apellido2.SetMinSize( wx.Size( 80,-1 ) )
		bSizer_morado1.Add( self.txt_apellido2, 1, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Nit:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		bSizer_morado1.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.txt_nit = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER , validator=cvEAY.MyValidator(cvEAY.DIGIT_ONLY) )
		self.txt_nit.SetMinSize( wx.Size( 80,-1 ) )
		bSizer_morado1.Add( self.txt_nit, 0, wx.ALL, 5 )

		self.m_staticText121 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )
		bSizer_morado1.Add( self.m_staticText121, 0, wx.ALL, 5 )

		self.txt_div = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,-1 ), wx.TE_READONLY )
		bSizer_morado1.Add( self.txt_div, 0, wx.ALL, 5 )


		bSizer_rojo1.Add( bSizer_morado1, 0, wx.EXPAND, 5 )

		bSizer_morado2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"    Celular:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer_morado2.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.txt_celular = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_PROCESS_ENTER  | wx.TE_PASSWORD, validator=cvEAY.MyValidator(cvEAY.DIGIT_ONLY)  )
		bSizer_morado2.Add( self.txt_celular, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Teléfono:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer_morado2.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.txt_telefono = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_PROCESS_ENTER  )
		bSizer_morado2.Add( self.txt_telefono, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"E-mail:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer_morado2.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.txt_email = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER  )
		bSizer_morado2.Add( self.txt_email, 1, wx.ALL, 5 )

		self.m_staticText_cupo = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Cupo:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_cupo.Wrap( -1 )
		bSizer_morado2.Add( self.m_staticText_cupo, 0, wx.ALL, 5 )

		self.txt_cupo = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer_morado2.Add( self.txt_cupo, 0, wx.ALL, 5 )

		self.m_staticText_puntos = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Puntos:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_puntos.Wrap( -1 )
		bSizer_morado2.Add( self.m_staticText_puntos, 0, wx.ALL, 5 )

		self.txt_puntos = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer_morado2.Add( self.txt_puntos, 0, wx.ALL, 5 )


		bSizer_rojo1.Add( bSizer_morado2, 0, wx.EXPAND, 5 )

		bSizer_morado3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText131 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Dirección:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		bSizer_morado3.Add( self.m_staticText131, 0, wx.ALL, 5 )

		self.txt_dir = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER  )
		bSizer_morado3.Add( self.txt_dir, 1, wx.ALL, 5 )

		self.m_staticText141 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Ciudad:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )
		bSizer_morado3.Add( self.m_staticText141, 0, wx.ALL, 5 )

		self.txt_ciudad = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), wx.TE_PROCESS_ENTER  )
		bSizer_morado3.Add( self.txt_ciudad, 0, wx.ALL, 5 )

		self.m_staticText151 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Id:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		bSizer_morado3.Add( self.m_staticText151, 0, wx.ALL, 5 )

		self.txt_idCliente = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_READONLY )
		bSizer_morado3.Add( self.txt_idCliente, 0, wx.ALL, 5 )


		bSizer_rojo1.Add( bSizer_morado3, 0, wx.EXPAND, 5 )

		bSizer_morado4 = wx.BoxSizer( wx.HORIZONTAL )

		self.staticText_informacion = wx.StaticText( self.m_panel4, wx.ID_ANY, u"// Aca puedes Encontrar, Editar y Agregar Clientes ", wx.DefaultPosition, wx.Size( -1,100 ), 0 )
		self.staticText_informacion.Wrap( -1 )
		self.staticText_informacion.SetForegroundColour( themeCAC.frm_buscarCliente.labelInformacion_letraColor )
		self.staticText_informacion.SetBackgroundColour( themeCAC.frm_buscarCliente.labelInformacion_fondoColor )
		self.staticText_informacion.SetMinSize( wx.Size( -1,25 ) )

		bSizer_morado4.Add( self.staticText_informacion, 1, wx.ALL, 5 )


		bSizer_rojo1.Add( bSizer_morado4, 0, wx.EXPAND, 5 )


		bSizer_verde1.Add( bSizer_rojo1, 1, wx.EXPAND, 5 )

		bSizer_rojo2 = wx.BoxSizer( wx.VERTICAL )

# Se refiere al panel de controles
		self.m_panel2 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( COLOR_PANEL_CONTROLES )

		bSizer_naranja2 = wx.BoxSizer( wx.VERTICAL )

		bSizer_naranja1 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_limpiar = wx.BitmapButton( self.m_panel2, wx.ID_ANY, wx.Bitmap( IMAGEN_LIMPIAR, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.NO_BORDER )
		self.btn_limpiar.SetBitmapCurrent( wx.Bitmap( IMAGEN_LIMPIAR_SEL, wx.BITMAP_TYPE_ANY ) )

		bSizer_naranja1.Add( self.btn_limpiar, 0, wx.ALL, 5 )

		self.btn_nuevo = wx.BitmapButton( self.m_panel2, wx.ID_ANY, wx.Bitmap( IMAGEN_NUEVO_CLIENTE , wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.NO_BORDER )
		self.btn_nuevo.SetBitmapCurrent( wx.Bitmap( IMAGEN_NUEVO_CLIENTE_SEL, wx.BITMAP_TYPE_ANY ) )


		bSizer_naranja1.Add( self.btn_nuevo, 0, wx.ALL, 5 )

		self.btn_editar = wx.BitmapButton( self.m_panel2, wx.ID_ANY, wx.Bitmap( IMAGEN_EDITAR, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.NO_BORDER )
		self.btn_editar.SetBitmapCurrent( wx.Bitmap( IMAGEN_EDITAR_SEL, wx.BITMAP_TYPE_ANY ) )
		self.btn_editar.Enable( False )

		bSizer_naranja1.Add( self.btn_editar, 0, wx.ALL, 5 )


		bSizer_naranja2.Add( bSizer_naranja1, 0, wx.EXPAND, 5 )

		self.btn_seleccionar = wx.BitmapButton( self.m_panel2, wx.ID_ANY, wx.Bitmap( IMAGEN_SELECCIONAR, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 122,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		self.btn_seleccionar.SetBitmapCurrent( wx.Bitmap( IMAGEN_SELECCIONAR_SEL, wx.BITMAP_TYPE_ANY ) )
		self.btn_seleccionar.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer_naranja2.Add( self.btn_seleccionar, 0, wx.ALL, 5 )

		self.m_staticline_panelBotones = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_naranja2.Add( self.m_staticline_panelBotones, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_cac = wx.StaticText( self.m_panel2, wx.ID_ANY, u"CAC SOFTWARE", wx.DefaultPosition, wx.Size( 120,-1 ), wx.ALIGN_CENTRE )
		self.m_staticText_cac.Wrap( -1 )
		bSizer_naranja2.Add( self.m_staticText_cac, 1, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer_naranja2 )
		self.m_panel2.Layout()
		bSizer_naranja2.Fit( self.m_panel2 )
		bSizer_rojo2.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer_verde1.Add( bSizer_rojo2, 0, wx.EXPAND, 5 )


		bSizer_amarillo.Add( bSizer_verde1, 0, wx.EXPAND, 5 )

		bSizer_verde2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_grid2 = wx.grid.Grid( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,1920), 0 )

		# Grid
		self.m_grid2.CreateGrid( FILA_GRID, COL_GRID )
		self.m_grid2.EnableEditing( False )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

# self.m_grid2.SetColFormatBool(1)  pone en la columna 1 un checkBox

		# attr = grid.GridCellAttr()
		# attr.SetEditor(grid.GridCellBoolEditor())
		# attr.SetRenderer(grid.GridCellBoolRenderer())
		# self.SetColAttr(1,attr)
		# self.m_grid2

		# Columns

		self.m_grid2.SetColLabelValue(0, '  RAZON SOCIAL')
		self.m_grid2.SetColLabelValue(1, ' NOMBRE')
		self.m_grid2.SetColLabelValue(2,' APELLIDO 1')
		self.m_grid2.SetColLabelValue(3, ' APELLIDO 2')
		self.m_grid2.SetColLabelValue(4, 'CELULAR')
		self.m_grid2.SetColLabelValue(6, ' TELEFONO')
		self.m_grid2.SetColLabelValue(5, ' E-MAIL')
		self.m_grid2.SetColLabelValue(7,' NIT')
		self.m_grid2.SetColLabelValue(8, ' DIV')
		self.m_grid2.SetColLabelValue(9, ' DIRECCION')
		self.m_grid2.SetColLabelValue(10, ' CIUDAD')
		self.m_grid2.SetColLabelValue(11, ' Id')
		self.m_grid2.SetColLabelValue(12, ' PUNTOS')
		self.m_grid2.SetColLabelValue(13, ' CUPO')


		self.m_grid2.SetColSize(0, 160)
		self.m_grid2.SetColSize(1, 140)
		self.m_grid2.SetColSize(2, 140)
		self.m_grid2.SetColSize(3, 90)
		self.m_grid2.SetColSize(4, 340)

		self.m_grid2.EnableDragColMove( True )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 25 )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 40 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer_verde2.Add( self.m_grid2, 1, wx.ALL, 5 )


		bSizer_amarillo.Add( bSizer_verde2, 1, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer_amarillo )
		self.m_panel4.Layout()
		bSizer_amarillo.Fit( self.m_panel4 )
		bSizer10.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

# Mostrar Controles EAY

		self.m_grid2.SetColSize(6, 0)	#telefono
		self.m_grid2.SetColSize(4, 0)  #celular
		self.m_grid2.SetColSize(11, 0)  # id_cliente

		if self.permiteAgregar==0:
			self.btn_nuevo.Hide()
		if self.permiteEditar==0:
			self.btn_editar.Hide()
		if self.permiteSeleccionar==0:
			self.btn_seleccionar.Hide()

		mostrarPuntos = configCAC.configuracion('Buscar_clientes', 'mostrar_puntos')
		if mostrarPuntos == '0':
			self.txt_puntos.Hide()
			self.m_staticText_puntos.Hide()
			#self.m_grid2.SetColSize(11,0) #la columna id_cliente
			self.m_grid2.SetColSize(12, 0)  # la columna puntos

		mostrar_cupo = configCAC.configuracion('Buscar_clientes', 'mostrar_cupo')
		if mostrar_cupo == '0':
			self.txt_cupo.Hide()
			self.m_staticText_cupo.Hide()
			self.m_grid2.SetColSize(13,0) #la columna id_cliente

# estados iniciales de los controles
		self.btn_editar.Enable(False)
		self.btn_seleccionar.Enable(False)

# Connect Events

		on_cloud = configCAC.configuracion('negocio', 'on_cloud')

		if on_cloud == '0':
			#self.txt_nombre.Bind( wx.EVT_TEXT, self.eventoChangeNombre)
			self.Bind(wx.EVT_TEXT, self.eventoChangeNombre, id=self.txt_razonSocial.GetId())
			self.Bind(wx.EVT_TEXT, self.eventoChangeNombre, id=self.txt_nombre.GetId())

			self.Bind(wx.EVT_TEXT, self.eventoChangeNombre, id=self.txt_apellido.GetId())
			self.Bind(wx.EVT_TEXT, self.eventoChangeNombre, id=self.txt_apellido2.GetId())
			self.Bind(wx.EVT_TEXT, self.eventoChangeNombre, id=self.txt_celular.GetId())
			self.Bind(wx.EVT_TEXT, self.eventoChangeNombre, id=self.txt_nit.GetId())

			self.Bind(wx.EVT_TEXT, self.eventoChangeNombre, id=self.txt_telefono.GetId())
			self.Bind(wx.EVT_TEXT, self.eventoChangeNombre, id=self.txt_email.GetId())
			self.Bind(wx.EVT_TEXT, self.eventoChangeNombre, id=self.txt_dir.GetId())
			self.Bind(wx.EVT_TEXT, self.eventoChangeNombre, id=self.txt_ciudad.GetId())
		if on_cloud == '1':

			#self.txt_nombre.Bind(wx.EVT_TEXT_ENTER, self.eventoChangeNombre)
			self.Bind(wx.EVT_TEXT_ENTER, self.eventoChangeNombre, id=self.txt_razonSocial.GetId())
			self.Bind(wx.EVT_TEXT_ENTER, self.eventoChangeNombre, id=self.txt_nombre.GetId())

			self.Bind(wx.EVT_TEXT_ENTER, self.eventoChangeNombre, id=self.txt_apellido.GetId())
			self.Bind(wx.EVT_TEXT_ENTER, self.eventoChangeNombre, id=self.txt_apellido2.GetId())
			self.Bind(wx.EVT_TEXT_ENTER, self.eventoChangeNombre, id=self.txt_celular.GetId())
			self.Bind(wx.EVT_TEXT_ENTER, self.eventoChangeNombre, id=self.txt_nit.GetId())

			self.Bind(wx.EVT_TEXT_ENTER, self.eventoChangeNombre, id=self.txt_telefono.GetId())
			self.Bind(wx.EVT_TEXT_ENTER, self.eventoChangeNombre, id=self.txt_email.GetId())
			self.Bind(wx.EVT_TEXT_ENTER, self.eventoChangeNombre, id=self.txt_dir.GetId())
			self.Bind(wx.EVT_TEXT_ENTER, self.eventoChangeNombre, id=self.txt_ciudad.GetId())


		self.btn_limpiar.Bind( wx.EVT_BUTTON, self.btn_limpiarOnButtonClick )
		self.btn_editar.Bind( wx.EVT_BUTTON, self.btn_editarOnButtonClick )
		self.btn_nuevo.Bind( wx.EVT_BUTTON, self.btn_nuevoOnButtonClick )
		self.btn_seleccionar.Bind( wx.EVT_BUTTON, self.btn_seleccionarOnButtonClick )

		#self.m_grid2.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.m_grid2OnGridCellLeftClick )
		self.Bind(grid.EVT_GRID_SELECT_CELL, self.OnSelectCell, id=self.m_grid2.GetId())

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def eventoChangeNombre( self, event ):

		if self.swEAY==0:

			laRazonSocial=self.txt_razonSocial.GetValue()
			elNombre= self.txt_nombre.GetValue()
			elApe1= self.txt_apellido.GetValue()
			elApe2=self.txt_apellido2.GetValue()
			elNit=formateoEAY.toNumSinPuntos(self.txt_nit.GetValue())
			elCelular= formateoEAY.toNumSinPuntos(self.txt_celular.GetValue())
			elTelf=formateoEAY.toNumSinPuntos(self.txt_telefono.GetValue())
			elEmail=self.txt_email.GetValue()
			laDir=self.txt_dir.GetValue()
			laCiudad=self.txt_ciudad.GetValue()

			listaCAmpos=[elNombre, elApe1, elApe2, elNit, elCelular, elTelf,  elEmail, laDir, laCiudad, laRazonSocial]

			rows=oobbdd.cargarClientesFiltrado(listaCAmpos, self.tipoTercero)

			# print 'este es rows'
			# print rows

			t=0

			self.m_grid2.ClearGrid()
			for i in rows:
				nuevaLista=[]

				for valor in i:
					#print type(valor), valor
					#print unicode(valor, 'utf-8')

					#print u'ocaña'
					if valor == '':
						nuevaLista.append('')
					else:
						nuevaLista.append(valor)

				#print ' --> esta es la nueva lista de cliente'
				#print nuevaLista

				var_razonSocial=nuevaLista[13]
				var_nombre=nuevaLista[0]
				var_ape1=nuevaLista[1]
				#print 'nueva lista [2]', nuevaLista[2]
				var_ape2=nuevaLista[2]
				var_celular=nuevaLista[3]
				if var_celular!= '':
					var_celular=formateoEAY.toNumTelefonico(var_celular)
				var_email=nuevaLista[5]
				var_telf=nuevaLista[4]
				if var_telf!= '':
					var_telf=formateoEAY.toNumTelefonico(var_telf)
				var_nit=nuevaLista[6]
				if var_nit != '':
					var_nit=formateoEAY.toNumMiles(var_nit, '')
				var_div=nuevaLista[7]
				var_dir=nuevaLista[8]
				var_ciudad=nuevaLista[9]
				var_idCliente=nuevaLista[10]
				var_puntos=nuevaLista[11]
				var_cupo=str(nuevaLista[12])
				if var_cupo!= '':
					var_cupo=formateoEAY.toNumMiles(var_cupo,'$')

				# LAS GRILLAS SOLO ACEPTAN STRING
				self.m_grid2.SetCellValue(t, 0, var_razonSocial)
				self.m_grid2.SetCellValue(t, 1, var_nombre)
				self.m_grid2.SetCellValue(t, 2, var_ape1)
				self.m_grid2.SetCellValue(t, 3, var_ape2)
				self.m_grid2.SetCellValue(t, 4, var_celular)
				self.m_grid2.SetCellValue(t, 5, var_email)
				self.m_grid2.SetCellValue(t, 6, var_telf)
				self.m_grid2.SetCellValue(t, 7, var_nit)
				self.m_grid2.SetCellValue(t, 8, str(var_div))
				self.m_grid2.SetCellValue(t, 9, var_dir)
				self.m_grid2.SetCellValue(t, 10, var_ciudad)
				self.m_grid2.SetCellValue(t, 11, str(var_idCliente))
				self.m_grid2.SetCellValue(t, 12, str(var_puntos))
				self.m_grid2.SetCellValue(t, 13, str(var_cupo))


				#self.m_grid1.AppendRows(1)

				t+=1

		self.m_grid2.AutoSizeColumns()


	def btn_limpiarOnButtonClick( self, event ):
		self.swEAY=1
		self.LimpiarTxtDelForm()
		self.swEAY=0
		event.Skip()

	def btn_editarOnButtonClick( self, event ):

		if self.tipoTercero==1:
			cad_tipoTercero= u'Editar Cliente '
		if self.tipoTercero==2:
			cad_tipoTercero= u'Editar Proveedor '
		if self.tipoTercero==3:
			cad_tipoTercero= u'Editar Empleado '
		if self.tipoTercero==5:
			cad_tipoTercero= u'Editar Tercero '

		el_idCliente=self.txt_idCliente.GetValue()
		titulo=cad_tipoTercero + '['+ el_idCliente + ']'
		puntos = self.txt_puntos.GetValue()
		frame_editarCliente= frm_editarCliente.EditarCliente(self, titulo, el_idCliente, self.tipoTercero,  self.tipo_busqueda, puntos, self.titulo )
		frame_editarCliente.Center()
		frame_editarCliente.Show()
		event.Skip()

	def btn_nuevoOnButtonClick( self, event ):

		if self.tipoTercero==1:
			cad_tipoTercero= u'Nuevo Cliente '
		if self.tipoTercero==2:
			cad_tipoTercero= u'Nuevo Proveedor '
		if self.tipoTercero==3:
			cad_tipoTercero= u'Nuevo Empleado '
		if self.tipoTercero==5:
			cad_tipoTercero= u'Nuevo Tercero '


		titulo=cad_tipoTercero + str(self.contadorFrames+1)
		self.contadorFrames+=1
		frame_cliente=frm_nuevoCliente.NuevoCliente(self, titulo, self.tipo_busqueda)
		frame_cliente.Center()
		frame_cliente.Show()
		event.Skip()

	def btn_seleccionarOnButtonClick( self, event ):
		dato=self.txt_idCliente.GetValue()
		#self.padre.txt_idCliente.SetValue(dato)
		self.padre.func_padreEayBuscarCliente(dato)
		self.Destroy()
		event.Skip()

	def OnSelectCell(self, evt): #EVENTO DE LA GRILLA
		self.swEAY=1
		fila= evt.GetRow()
		#col=evt.GetCol()
		self.CargarControlesConDatosGrilla(fila)
		self.swEAY=0
		evt.Skip()


# FUNCIONES EAY

	def CargarControlesConDatosGrilla(self, fila):
		#fila= evt.GetRow()
		#col=evt.GetCol()
		#print self.m_grid2.GetCellValue(fila, col)

		self.swEAY=1

		self.txt_razonSocial.SetValue(self.m_grid2.GetCellValue(fila, 0))
		self.txt_nombre.SetValue(self.m_grid2.GetCellValue(fila, 1))
		self.txt_apellido.SetValue(self.m_grid2.GetCellValue(fila, 2))
		self.txt_apellido2.SetValue(self.m_grid2.GetCellValue(fila, 3))
		self.txt_celular.SetValue(self.m_grid2.GetCellValue(fila, 4))
		self.txt_telefono.SetValue(self.m_grid2.GetCellValue(fila, 6))
		self.txt_email.SetValue(self.m_grid2.GetCellValue(fila, 5))
		self.txt_nit.SetValue(self.m_grid2.GetCellValue(fila, 7))
		self.txt_div.SetValue(self.m_grid2.GetCellValue(fila, 8))
		self.txt_dir.SetValue(self.m_grid2.GetCellValue(fila, 9))
		self.txt_ciudad.SetValue(self.m_grid2.GetCellValue(fila, 10))
		self.txt_idCliente.SetValue(self.m_grid2.GetCellValue(fila, 11))
		self.txt_puntos.SetValue(self.m_grid2.GetCellValue(fila, 12))
		self.txt_cupo.SetValue(self.m_grid2.GetCellValue(fila, 13))

		if self.m_grid2.GetCellValue(fila, 11) != '': #si el id_cliente esta en blanco
			self.btn_editar.Enable(True)
			self.btn_seleccionar.Enable(True)
		else:
			self.btn_editar.Enable(False)
			self.btn_seleccionar.Enable(False)

		self.swEAY=0

	def LimpiarTxtDelForm(self):
		self.swEAY=1

		self.txt_razonSocial.SetValue('')
		self.txt_nombre.SetValue('')
		self.txt_apellido.SetValue('')
		self.txt_apellido2.SetValue('')
		self.txt_nit.SetValue('')
		self.txt_div.SetValue('')
		self.txt_celular.SetValue('')
		self.txt_telefono.SetValue('')
		self.txt_email.SetValue('')
		self.txt_cupo.SetValue('')
		self.txt_puntos.SetValue('')
		self.txt_dir.SetValue('')
		self.txt_ciudad.SetValue('')
		self.txt_idCliente.SetValue('')
		self.m_grid2.ClearGrid()

		self.btn_editar.Enable(False)
		self.btn_seleccionar.Enable(False)

		self.swEAY=0

