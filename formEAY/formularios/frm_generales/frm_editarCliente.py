# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from pyeay.dbcac.conexiondb import Ejecutar_SQL
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

from formEAY.constantesCAC.imgCAC import Img_formularios_general as Iconos

IMAGEN_GUARDAR = Iconos.GUARDAR
IMAGEN_GUARDAR_SEL = Iconos.GUARDAR_SEL
IMAGEN_LIMPIAR = Iconos.LIMPIAR_CONTROLES
IMAGEN_LIMPIAR_SEL = Iconos.LIMPIAR_CONTROLES_SEL

###########################################################################
## Class NuevoCliente
###########################################################################

class EditarCliente(wx.Frame):

	def __init__(self, parent, datos_cliente):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Editar Cliente", pos=wx.DefaultPosition,
						  size=wx.Size(881, 149), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.Size(500, 149), wx.Size( -1,155 ))
		self.SetBackgroundColour(wx.Colour(255, 255, 255))

		self.padre = parent
		self.datos_cliente = datos_cliente

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
											wx.ALIGN_RIGHT)
		self.m_staticText18.Wrap(-1)
		bSizer_morado5.Add(self.m_staticText18, 0, wx.ALL, 5)

		self.txt_nit = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
								   wx.TE_PROCESS_ENTER)
		bSizer_morado5.Add(self.txt_nit, 0, wx.ALL, 5)

		self.m_staticText15 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"  R. Social:", wx.DefaultPosition,
											wx.DefaultSize, 0)
		self.m_staticText15.Wrap(-1)
		bSizer_morado5.Add(self.m_staticText15, 0, wx.ALL, 5)

		self.txt_razonSocial = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
										   wx.TE_PROCESS_ENTER)
		bSizer_morado5.Add(self.txt_razonSocial, 1, wx.ALL, 5)

		bSizer_rojo1.Add(bSizer_morado5, 0, wx.EXPAND, 5)

		bSizer_morado1 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText16 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.Size(55, -1),
											wx.ALIGN_RIGHT)
		self.m_staticText16.Wrap(-1)
		bSizer_morado1.Add(self.m_staticText16, 0, wx.ALL, 5)

		self.txt_nombre = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
									  wx.TE_PROCESS_ENTER)
		self.txt_nombre.SetMinSize(wx.Size(100, -1))

		bSizer_morado1.Add(self.txt_nombre, 1, wx.ALL, 5)

		self.m_staticText23 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Apellido1:", wx.DefaultPosition, wx.DefaultSize,
											0)
		self.m_staticText23.Wrap(-1)
		bSizer_morado1.Add(self.m_staticText23, 0, wx.ALL, 5)

		self.txt_apellido = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
										wx.TE_PROCESS_ENTER)
		bSizer_morado1.Add(self.txt_apellido, 1, wx.ALL, 5)

		self.m_staticText17 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"apellido2:", wx.DefaultPosition, wx.DefaultSize,
											0)
		self.m_staticText17.Wrap(-1)
		bSizer_morado1.Add(self.m_staticText17, 0, wx.ALL, 5)

		self.txt_apellido2 = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
										 wx.TE_PROCESS_ENTER)
		bSizer_morado1.Add(self.txt_apellido2, 1, wx.ALL, 5)

		bSizer_rojo1.Add(bSizer_morado1, 0, wx.EXPAND, 5)

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

		self.txt_dir = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
								   wx.TE_PROCESS_ENTER)
		bSizer_morado3.Add(self.txt_dir, 1, wx.ALL, 5)

		self.m_staticText141 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Ciudad:", wx.DefaultPosition, wx.DefaultSize,
											 0)
		self.m_staticText141.Wrap(-1)
		bSizer_morado3.Add(self.m_staticText141, 0, wx.ALL, 5)

		self.txt_ciudad = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(180, -1),
									  wx.TE_PROCESS_ENTER)
		bSizer_morado3.Add(self.txt_ciudad, 0, wx.ALL, 5)

		bSizer_rojo1.Add(bSizer_morado3, 0, wx.EXPAND, 5)

		bSizer_morado4 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer_rojo1.Add(bSizer_morado4, 0, wx.EXPAND, 5)

		bSizer_verde1.Add(bSizer_rojo1, 1, wx.EXPAND, 5)

		bSizer_rojo2 = wx.BoxSizer(wx.HORIZONTAL)

		self.btn_limpiar = wx.BitmapButton(self.m_panel4, wx.ID_ANY,
										   wx.Bitmap(IMAGEN_LIMPIAR,
													 wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
										   wx.BU_AUTODRAW | wx.NO_BORDER)

		self.btn_limpiar.SetBitmapCurrent(
			wx.Bitmap(IMAGEN_LIMPIAR_SEL, wx.BITMAP_TYPE_ANY))
		bSizer_rojo2.Add(self.btn_limpiar, 0, wx.ALL, 5)

		self.btn_guardar = wx.BitmapButton(self.m_panel4, wx.ID_ANY,
										   wx.Bitmap(IMAGEN_GUARDAR,
													 wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
										   wx.BU_AUTODRAW | wx.NO_BORDER)

		self.btn_guardar.SetBitmapCurrent(
			wx.Bitmap(IMAGEN_GUARDAR_SEL, wx.BITMAP_TYPE_ANY))
		bSizer_rojo2.Add(self.btn_guardar, 0, wx.ALL, 5)

		bSizer_verde1.Add(bSizer_rojo2, 0, wx.EXPAND, 5)

		bSizer_amarillo.Add(bSizer_verde1, 0, wx.EXPAND, 5)

		self.m_panel4.SetSizer(bSizer_amarillo)
		self.m_panel4.Layout()
		bSizer_amarillo.Fit(self.m_panel4)
		bSizer10.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer10)

		## VALORES INICIALES EAY
		self.valores_iniciales()

		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.txt_nit.Bind(wx.EVT_TEXT_ENTER, self.txt_nitOnTextEnter)
		self.txt_razonSocial.Bind(wx.EVT_TEXT_ENTER, self.txt_razonSocialOnTextEnter)
		self.btn_limpiar.Bind(wx.EVT_BUTTON, self.btn_limpiarOnButtonClick)
		self.btn_guardar.Bind(wx.EVT_BUTTON, self.btn_guardarOnButtonClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def txt_nitOnTextEnter(self, event):
		event.Skip()

	def txt_razonSocialOnTextEnter(self, event):
		event.Skip()

	def btn_limpiarOnButtonClick(self, event):
		self.txt_nit.SetValue('')
		self.txt_razonSocial.SetValue('')
		self.txt_nombre.SetValue('')
		self.txt_apellido.SetValue('')
		self.txt_apellido2.SetValue('')
		self.txt_celular.SetValue('')
		self.txt_dir.SetValue('')
		self.txt_ciudad.SetValue('')
		event.Skip()

	def btn_guardarOnButtonClick(self, event):
		rta = self.func_validar_datos()
		if rta == 1:
			nit = self.txt_nit.GetValue()
			razonsocial = self.txt_razonSocial.GetValue()
			nom = self.txt_nombre.GetValue()
			ape1 = self.txt_apellido.GetValue()
			ape2 = self.txt_apellido2.GetValue()
			celular = self.txt_celular.GetValue()
			dir = self.txt_dir.GetValue()
			ciudad = self.txt_ciudad.GetValue()

			if razonsocial == '':
				razonsocial = nom + ' ' + ape1 + ' ' + ape2


			# rta = self.func_is_nit_unico(nit)
			# if rta > 0:
			# 	wx.MessageBox(u'Nit ya registrado en el sistema', u'Atención', wx.OK | wx.ICON_INFORMATION)
			# 	return 0


			cad_sql = """
							UPDATE 	cliente SET 	nit = '{0}', razon_social = '{1}', nom = '{2}', ape1 = '{3}', ape2 = '{4}', 
									celular = '{5}', dir = '{6}', ciudad = '{7}' 
							WHERE id_cliente = {8}     
				""".format(nit, razonsocial, nom, ape1, ape2, celular, dir, ciudad, self.id_cliente)

			Ejecutar_SQL.update_filas(cad_sql.upper(), 'frm_editarCliente/btn_guardarOnButtonClick', BasesDeDatos.DB_PRINCIPAL)

			wx.MessageBox(u'El Cliente fue editado correctamente', u'Atención', wx.OK | wx.ICON_INFORMATION)


			self.padre.func_padreEayNuevoCliente(nit)
			self.Destroy()

		event.Skip()

	##  FUNCIONES EAY
	def func_is_nit_unico(self, nit):
		cad_sql = """
	                   SELECT count(id_cliente)
	                   FROM cliente
	                   WHERE  nit = '{0}'
	                """.format(nit)

		cabeceras = []
		rta = Ejecutar_SQL.select_un_registro(cad_sql.upper(), 'frm_nuevoCliente/func_is_nit_unico', BasesDeDatos.DB_PRINCIPAL)

		return rta[0]

	def valores_iniciales(self):
		self.txt_nombre.SetValue(self.datos_cliente[0])
		self.txt_apellido.SetValue(self.datos_cliente[1])
		self.txt_apellido2.SetValue(self.datos_cliente[2])
		self.txt_nit.SetValue(self.datos_cliente[3])
		self.txt_razonSocial.SetValue(self.datos_cliente[4])
		self.txt_dir.SetValue(self.datos_cliente[5])
		self.txt_ciudad.SetValue(self.datos_cliente[6])
		self.txt_celular.SetValue(self.datos_cliente[7])
		self.id_cliente = self.datos_cliente[8]


	def func_validar_datos(self):
		if self.txt_nit.GetValue() == '':
			wx.MessageBox(u'Debes ingresar un Nit valido', u'Atención', wx.OK | wx.ICON_INFORMATION)
			return 0
		if self.txt_nit.GetValue() == '':
			wx.MessageBox(u'Debes ingresar un Nit valido', u'Atención', wx.OK | wx.ICON_INFORMATION)
			return 0
		if self.txt_nombre.GetValue() == '':
			wx.MessageBox(u'Debes ingresar un Nombre', u'Atención', wx.OK | wx.ICON_INFORMATION)
			return 0
		if self.txt_apellido.GetValue() == '':
			wx.MessageBox(u'Debes ingresar un apellido 1', u'Atención', wx.OK | wx.ICON_INFORMATION)
			return 0

		if self.txt_celular.GetValue() == '':
			wx.MessageBox(u'Debes ingresar un Celular valido', u'Atención', wx.OK | wx.ICON_INFORMATION)
			return 0
		if self.txt_dir.GetValue() == '':
			wx.MessageBox(u'Debes ingresar una Dirección valida', u'Atención', wx.OK | wx.ICON_INFORMATION)
			return 0
		if self.txt_ciudad.GetValue() == '':
			wx.MessageBox(u'Debes ingresar una Ciudad valida', u'Atención', wx.OK | wx.ICON_INFORMATION)
			return 0

		return 1




