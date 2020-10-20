
# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

import time




###########################################################################
## Class Principal
###########################################################################

class Principal(wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Principal Produccion Zuligres", pos=wx.DefaultPosition,
						  size=wx.Size(782, 610), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		self.SetBackgroundColour(wx.Colour(255, 255, 255))

		bSizer7 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer10 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel3 = wx.Panel(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel3.SetBackgroundColour(wx.Colour(240, 240, 240))

		bSizer9 = wx.BoxSizer(wx.VERTICAL)

		self.btn_extrusion = wx.Button(self.m_panel3, wx.ID_ANY, u"Extrusion", wx.DefaultPosition, wx.Size(140, -1), 0)
		bSizer9.Add(self.btn_extrusion, 0, wx.ALL, 5)

		self.btn_secadero = wx.Button(self.m_panel3, wx.ID_ANY, u"Secadero", wx.DefaultPosition, wx.Size(140, -1), 0)
		bSizer9.Add(self.btn_secadero, 0, wx.ALL, 5)

		self.btn_cargue_vagonetas = wx.Button(self.m_panel3, wx.ID_ANY, u"cargue vagonetas", wx.DefaultPosition,
											  wx.Size(140, -1), 0)
		bSizer9.Add(self.btn_cargue_vagonetas, 0, wx.ALL, 5)

		self.btn_descargue_vagonetas = wx.Button(self.m_panel3, wx.ID_ANY, u"descargue Vagonetas", wx.DefaultPosition,
												 wx.Size(140, -1), 0)
		bSizer9.Add(self.btn_descargue_vagonetas, 0, wx.ALL, 5)

		self.btn_coccion = wx.Button(self.m_panel3, wx.ID_ANY, u"Cocción", wx.DefaultPosition, wx.Size(140, -1), 0)
		bSizer9.Add(self.btn_coccion, 0, wx.ALL, 5)

		self.btn_patio = wx.Button(self.m_panel3, wx.ID_ANY, u"Patio", wx.DefaultPosition, wx.Size(140, -1), 0)
		bSizer9.Add(self.btn_patio, 0, wx.ALL, 5)

		self.m_staticline1 = wx.StaticLine(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
										   wx.LI_HORIZONTAL)
		bSizer9.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

		self.button_1 = wx.Button(self.m_panel3, wx.ID_ANY, u"rep. hist procesos ECD", wx.DefaultPosition, wx.Size(140, -1), 0)
		bSizer9.Add(self.button_1, 0, wx.ALL, 5)

		self.button_2 = wx.Button(self.m_panel3, wx.ID_ANY, u"rep. Detalle ECD", wx.DefaultPosition, wx.Size(140, -1), 0)
		bSizer9.Add(self.button_2, 0, wx.ALL, 5)

		self.button_3 = wx.Button(self.m_panel3, wx.ID_ANY, u"button_3", wx.DefaultPosition, wx.Size(140, -1), 0)
		bSizer9.Add(self.button_3, 0, wx.ALL, 5)

		self.button_4 = wx.Button(self.m_panel3, wx.ID_ANY, u"button_4", wx.DefaultPosition, wx.Size(140, -1), 0)
		bSizer9.Add(self.button_4, 0, wx.ALL, 5)

		self.m_panel3.SetSizer(bSizer9)
		self.m_panel3.Layout()
		bSizer9.Fit(self.m_panel3)
		bSizer10.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

		bSizer8.Add(bSizer10, 0, wx.EXPAND, 5)

		bSizer11 = wx.BoxSizer(wx.VERTICAL)

		bSizer8.Add(bSizer11, 1, wx.EXPAND, 5)

		self.m_panel2.SetSizer(bSizer8)
		self.m_panel2.Layout()
		bSizer8.Fit(self.m_panel2)
		bSizer7.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer7)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.btn_extrusion.Bind(wx.EVT_BUTTON, self.btn_extrusionOnButtonClick)
		self.btn_secadero.Bind(wx.EVT_BUTTON, self.btn_secaderoOnButtonClick)
		self.btn_cargue_vagonetas.Bind(wx.EVT_BUTTON, self.btn_cargue_vagonetasOnButtonClick)
		self.btn_descargue_vagonetas.Bind(wx.EVT_BUTTON, self.btn_descargue_vagonetasOnButtonClick)
		self.btn_coccion.Bind(wx.EVT_BUTTON, self.btn_coccionOnButtonClick)
		self.btn_patio.Bind(wx.EVT_BUTTON, self.btn_patioOnButtonClick)
		self.button_1.Bind(wx.EVT_BUTTON, self.button_1OnButtonClick)
		self.button_2.Bind(wx.EVT_BUTTON, self.button_2OnButtonClick)
		self.button_3.Bind(wx.EVT_BUTTON, self.button_3OnButtonClick)
		self.button_4.Bind(wx.EVT_BUTTON, self.button_4OnButtonClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def btn_extrusionOnButtonClick(self, event):
		import formEAY.formularios.frm_procesos.frm_extrusion as frm_extrusion
		frame_extrusion = frm_extrusion.Extrusion(self)
		frame_extrusion.Center()
		frame_extrusion.Show()
		event.Skip()


	def btn_secaderoOnButtonClick(self, event):
		event.Skip()

	def btn_cargue_vagonetasOnButtonClick(self, event):
		t1 = time.time()
		import formEAY.formularios.frm_procesos.frm_cargue_vagonetas as frm_cargue_vagonetas
		frame_cargue_vagonetas = frm_cargue_vagonetas.CargueVagonetas(self)
		frame_cargue_vagonetas.Center()
		frame_cargue_vagonetas.Show()
		t2 = time.time()
		print(t2 - t1)
		event.Skip()

	def btn_descargue_vagonetasOnButtonClick(self, event):
		t1= time.time()
		import formEAY.formularios.frm_procesos.frm_descargue_vagonetas as frm_descargue_vagonetas
		frame_descargue_vagonetas = frm_descargue_vagonetas.DescargueVagonetas(self)
		frame_descargue_vagonetas.Center()
		frame_descargue_vagonetas.Show()
		t2 = time.time()
		print(t2 - t1)
		event.Skip()

	def btn_coccionOnButtonClick(self, event):
		event.Skip()

	def btn_patioOnButtonClick(self, event):
		event.Skip()

	def button_1OnButtonClick(self, event):
		t1 = time.time()
		import formEAY.formularios.frm_reportes.frm_historial_procesos_ECD as frm_historial_procesos_ECD
		frame_historial_procesos_ECD = frm_historial_procesos_ECD.HistorialProcesos_ECD(self)
		frame_historial_procesos_ECD.Center()
		frame_historial_procesos_ECD.Show()
		t2 = time.time()
		print(t2 - t1)
		event.Skip()

	def button_2OnButtonClick(self, event):
		t1 = time.time()
		import formEAY.formularios.frm_reportes.frm_historial_detalle_procesos_ECD as frm_historial_detalle_procesos_ECD
		frame_historial_detalle_procesos_ECD = frm_historial_detalle_procesos_ECD.HistorialDetalleProcesos_ECD(self)
		frame_historial_detalle_procesos_ECD.Center()
		frame_historial_detalle_procesos_ECD.Show()
		t2 = time.time()
		print(t2 - t1)
		event.Skip()

	def button_3OnButtonClick(self, event):
		event.Skip()

	def button_4OnButtonClick(self, event):
		t1 = time.time()
		import formEAY.formularios.frm_procesos.frm_extrusion_lenta as frm_extrusion
		frame_extrusion = frm_extrusion.Extrusion(self)
		frame_extrusion.Center()
		frame_extrusion.Show()
		t2 = time.time()
		print(t2 - t1)
		event.Skip()

