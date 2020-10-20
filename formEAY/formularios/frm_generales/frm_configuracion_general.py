# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class Configuracion
###########################################################################

class Configuracion(wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Configuración", pos=wx.DefaultPosition,
						  size=wx.Size(282, 315), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.Size(282, 238), wx.Size(282, 315))

		bSizer7 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel2.SetBackgroundColour(wx.Colour(255, 255, 255))

		bSizer8 = wx.BoxSizer(wx.VERTICAL)

		self.btn_gestion_productos = wx.Button(self.m_panel2, wx.ID_ANY, u"Gestión de Productos", wx.DefaultPosition,
											   wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_gestion_productos, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_gestion_empleados = wx.Button(self.m_panel2, wx.ID_ANY, u"Gestión de Empleados", wx.DefaultPosition,
											   wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_gestion_empleados, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_usuarios = wx.Button(self.m_panel2, wx.ID_ANY, u"Usuarios", wx.DefaultPosition, wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_usuarios, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_turnos = wx.Button(self.m_panel2, wx.ID_ANY, u"Turnos", wx.DefaultPosition, wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_turnos, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_recesos_programados = wx.Button(self.m_panel2, wx.ID_ANY, u"Recesos Programados", wx.DefaultPosition,
												 wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_recesos_programados, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_configuracion_notas = wx.Button(self.m_panel2, wx.ID_ANY, u"Confg.  Notas", wx.DefaultPosition,
												 wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_configuracion_notas, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_vacio_3 = wx.Button(self.m_panel2, wx.ID_ANY, u"Vacio 3", wx.DefaultPosition, wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_vacio_3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_vacio_4 = wx.Button(self.m_panel2, wx.ID_ANY, u"Vacio 4", wx.DefaultPosition, wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_vacio_4, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_staticline1 = wx.StaticLine(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
										   wx.LI_HORIZONTAL)
		bSizer8.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

		self.m_panel2.SetSizer(bSizer8)
		self.m_panel2.Layout()
		bSizer8.Fit(self.m_panel2)
		bSizer7.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer7)

		self.cargar_valores_de_inicializacion()

		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.btn_gestion_productos.Bind(wx.EVT_BUTTON, self.btn_gestion_productosOnButtonClick)
		self.btn_gestion_empleados.Bind(wx.EVT_BUTTON, self.btn_gestion_empleadosOnButtonClick)
		self.btn_usuarios.Bind(wx.EVT_BUTTON, self.btn_usuariosOnButtonClick)
		self.btn_turnos.Bind(wx.EVT_BUTTON, self.btn_turnosOnButtonClick)
		self.btn_recesos_programados.Bind(wx.EVT_BUTTON, self.btn_recesos_programadosOnButtonClick)
		self.btn_configuracion_notas.Bind(wx.EVT_BUTTON, self.btn_configuracion_notasOnButtonClick)
		self.btn_vacio_3.Bind(wx.EVT_BUTTON, self.btn_vacio_3OnButtonClick)
		self.btn_vacio_4.Bind(wx.EVT_BUTTON, self.btn_vacio_4OnButtonClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def cargar_valores_de_inicializacion(self):
		self.btn_turnos.Hide()
		self.btn_usuarios.Hide()
		self.btn_configuracion_notas.Hide()
		self.btn_recesos_programados.Hide()
		self.btn_vacio_3.Hide()
		self.btn_vacio_4.Hide()

	def btn_gestion_productosOnButtonClick(self, event):
		import formEAY.formularios.frm_generales.frm_gestionar_productos as frm_gestionar_productos
		frame_gestionar_productos = frm_gestionar_productos.GestionarProductos(self)
		frame_gestionar_productos.Center()
		frame_gestionar_productos.Show()
		event.Skip()

	def btn_gestion_empleadosOnButtonClick(self, event):
		import formEAY.formularios.frm_generales.frm_gestionar_empleado as frm_gestionar_empleado
		frame_gestionar_empleado = frm_gestionar_empleado.GestionarEmpleado(self)
		frame_gestionar_empleado.Center()
		frame_gestionar_empleado.Show()
		event.Skip()

	def btn_usuariosOnButtonClick(self, event):
		event.Skip()

	def btn_turnosOnButtonClick(self, event):
		event.Skip()

	def btn_recesos_programadosOnButtonClick(self, event):
		event.Skip()

	def btn_configuracion_notasOnButtonClick(self, event):
		event.Skip()

	def btn_vacio_3OnButtonClick(self, event):
		event.Skip()

	def btn_vacio_4OnButtonClick(self, event):
		event.Skip()


