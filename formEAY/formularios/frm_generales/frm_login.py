# -*- coding: utf-8 -*-
import wx
import wx.xrc

from pyeay.dbcac.conexiondb import Ejecutar_SQL
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

###########################################################################
## Class Login
###########################################################################

class Login(wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
						  size=wx.Size(415, 152), style=0)

		self.SetSizeHints(wx.Size(415, 152), wx.Size(415, 152))
		self.SetBackgroundColour(wx.Colour(80, 80, 80))

		self.padre = parent

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel1.SetBackgroundColour(wx.Colour(80, 80, 80))

		bSizer2 = wx.BoxSizer(wx.VERTICAL)

		bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Validar Usuario", wx.DefaultPosition,
										   wx.DefaultSize, wx.ALIGN_CENTRE)
		self.m_staticText1.Wrap(-1)
		self.m_staticText1.SetFont(wx.Font(11, 70, 90, 90, False, wx.EmptyString))
		self.m_staticText1.SetForegroundColour(wx.Colour(255, 255, 255))

		bSizer5.Add(self.m_staticText1, 1, wx.ALL, 5)

		bSizer2.Add(bSizer5, 0, wx.EXPAND, 5)

		bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Usuario:", wx.DefaultPosition, wx.Size(65, -1),
										   wx.ALIGN_RIGHT)
		self.m_staticText2.Wrap(-1)
		self.m_staticText2.SetForegroundColour(wx.Colour(192, 192, 192))

		bSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)

		self.txt_usuario = wx.TextCtrl(self.m_panel1, wx.ID_ANY, 'eay', wx.DefaultPosition, wx.DefaultSize,
									   wx.TE_PROCESS_ENTER)
		bSizer3.Add(self.txt_usuario, 1, wx.ALL, 5)

		bSizer2.Add(bSizer3, 0, wx.EXPAND, 5)

		bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText21 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Contraseña:", wx.DefaultPosition,
											wx.Size(65, -1), wx.ALIGN_RIGHT)
		self.m_staticText21.Wrap(-1)
		self.m_staticText21.SetForegroundColour(wx.Colour(192, 192, 192))

		bSizer4.Add(self.m_staticText21, 0, wx.ALL, 5)

		self.txt_password = wx.TextCtrl(self.m_panel1, wx.ID_ANY, 'incheon', wx.DefaultPosition, wx.DefaultSize,
										wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
		bSizer4.Add(self.txt_password, 1, wx.ALL, 5)

		bSizer2.Add(bSizer4, 0, wx.EXPAND, 5)

		bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

		self.btn_cancelar = wx.Button(self.m_panel1, wx.ID_ANY, u"&Cancelar", wx.DefaultPosition, wx.DefaultSize,
									  0 | wx.NO_BORDER)
		self.btn_cancelar.SetForegroundColour(wx.Colour(255, 255, 255))
		self.btn_cancelar.SetBackgroundColour(wx.Colour(255, 0, 0))

		bSizer6.Add(self.btn_cancelar, 0, wx.ALL, 5)

		self.btn_aceptar = wx.Button(self.m_panel1, wx.ID_ANY, u"&Aceptar", wx.DefaultPosition, wx.DefaultSize,
									 0 | wx.NO_BORDER)
		self.btn_aceptar.SetBackgroundColour(wx.Colour(128, 255, 128))

		bSizer6.Add(self.btn_aceptar, 0, wx.ALL, 5)

		bSizer2.Add(bSizer6, 1, wx.ALIGN_RIGHT, 5)

		self.m_panel1.SetSizer(bSizer2)
		self.m_panel1.Layout()
		bSizer2.Fit(self.m_panel1)
		bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer1)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.txt_usuario.Bind(wx.EVT_TEXT_ENTER, self.txt_usuarioOnTextEnter)
		self.txt_password.Bind(wx.EVT_TEXT_ENTER, self.txt_passwordOnTextEnter)
		self.btn_cancelar.Bind(wx.EVT_BUTTON, self.btn_cancelarOnButtonClick)
		self.btn_aceptar.Bind(wx.EVT_BUTTON, self.btn_aceptarOnButtonClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def txt_usuarioOnTextEnter(self, event):
		self.txt_password.SetFocus()
		event.Skip()

	def txt_passwordOnTextEnter(self, event):
		self.func_validarUsuario()
		event.Skip()

	def btn_cancelarOnButtonClick(self, event):
		self.Destroy()
		event.Skip()

	def btn_aceptarOnButtonClick(self, event):
		self.func_validarUsuario()
		event.Skip()

	## FUNCIONES EAY

	def func_validarUsuario(self):
		usuario = self.txt_usuario.GetValue()
		password = self.txt_password.GetValue()
		cad_sql = """
						SELECT ta.acceso, u.nom_empleado
						FROM usuario as u, tipo_de_acceso as ta
						WHERE  u.id_acceso = ta.id_acceso AND u.usuario = '{}' AND u.password = '{}'		
		""".format(usuario, password)

		row = Ejecutar_SQL.select_un_registro(cad_sql, 'frm_login/func_validarUsuario', BasesDeDatos.DB_PRINCIPAL)


		if row != None:
			msg = u'Bienvenido ' + row['nom_empleado']
			wx.MessageBox( msg, u'Atención...',
							  wx.OK | wx.ICON_INFORMATION)
			self.Destroy()
			self.padre.mostrar_botones(row['acceso'], usuario)
		else:
			wx.MessageBox(u'Acceso denegado, No eres un usuario autorizado', u'Atención...',
						  wx.OK | wx.ICON_INFORMATION)






