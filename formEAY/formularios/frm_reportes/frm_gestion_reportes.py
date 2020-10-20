# -*- coding: utf-8 -*-


import wx
import wx.xrc


###########################################################################
## Class Reportes
###########################################################################

class Reportes(wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Reportes", pos=wx.DefaultPosition, size=wx.Size(282, 419),
						  style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.Size( 282,238 ), wx.DefaultSize )

		bSizer7 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel2.SetBackgroundColour(wx.Colour(255, 255, 255))

		bSizer8 = wx.BoxSizer(wx.VERTICAL)

		self.btn_produccion_por_periodo = wx.Button(self.m_panel2, wx.ID_ANY, u"Producción por Periódo",
													wx.DefaultPosition, wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_produccion_por_periodo, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_detalle_produccion = wx.Button(self.m_panel2, wx.ID_ANY, u"Detalle de Producción", wx.DefaultPosition,
												wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_detalle_produccion, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_historial_de_procesos = wx.Button(self.m_panel2, wx.ID_ANY, u"Historial de Procesos",
												   wx.DefaultPosition, wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_historial_de_procesos, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_staticline2 = wx.StaticLine(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
										   wx.LI_HORIZONTAL)
		bSizer8.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)



		self.btn_historial_notas = wx.Button(self.m_panel2, wx.ID_ANY, u"Notas", wx.DefaultPosition, wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_historial_notas, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_historial_novedades = wx.Button(self.m_panel2, wx.ID_ANY, u"Novedades", wx.DefaultPosition, wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_historial_novedades, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_vacio_3 = wx.Button(self.m_panel2, wx.ID_ANY, u"Vacio 3", wx.DefaultPosition, wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_vacio_3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.btn_vacio_4 = wx.Button(self.m_panel2, wx.ID_ANY, u"Vacio 4", wx.DefaultPosition, wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_vacio_4, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_staticline1 = wx.StaticLine(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
										   wx.LI_HORIZONTAL)
		bSizer8.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

		self.btn_reporte_inventario = wx.Button(self.m_panel2, wx.ID_ANY, u"Reporte de inventario", wx.DefaultPosition,
												wx.Size(220, 35), 0)
		bSizer8.Add(self.btn_reporte_inventario, 0, wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_panel2.SetSizer(bSizer8)
		self.m_panel2.Layout()
		bSizer8.Fit(self.m_panel2)
		bSizer7.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer7)

		## VALORES INICIALES EAY
		self.cargar_valores_de_inicializacion()


		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.btn_produccion_por_periodo.Bind(wx.EVT_BUTTON, self.btn_produccion_por_periodoOnButtonClick)
		self.btn_detalle_produccion.Bind(wx.EVT_BUTTON, self.btn_detalle_produccionOnButtonClick)
		self.btn_historial_de_procesos.Bind(wx.EVT_BUTTON, self.btn_historial_de_procesosOnButtonClick)
		self.btn_reporte_inventario.Bind(wx.EVT_BUTTON, self.btn_reporte_inventarioOnButtonClick)
		self.btn_historial_notas.Bind(wx.EVT_BUTTON, self.btn_historial_notasOnButtonClick)
		self.btn_historial_novedades.Bind(wx.EVT_BUTTON, self.btn_historial_novedadesOnButtonClick)
		self.btn_vacio_3.Bind(wx.EVT_BUTTON, self.btn_vacio_3OnButtonClick)
		self.btn_vacio_4.Bind(wx.EVT_BUTTON, self.btn_vacio_4OnButtonClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def btn_produccion_por_periodoOnButtonClick(self, event):
		import formEAY.formularios.frm_reportes.frm_report_unidades_por_periodo as frm_report_unidades_por_periodo
		frame_report_unidades_por_periodo = frm_report_unidades_por_periodo.UnidadesPorPeriodo(self)
		frame_report_unidades_por_periodo.Center()
		frame_report_unidades_por_periodo.Show()
		event.Skip()

	def btn_detalle_produccionOnButtonClick(self, event):
		import formEAY.formularios.frm_reportes.frm_historial_detalle_procesos_ECD as frm_historial_detalle_procesos_ECD
		frame_historial_detalle_procesos_ECD = frm_historial_detalle_procesos_ECD.HistorialDetalleProcesos_ECD(self)
		frame_historial_detalle_procesos_ECD.Center()
		frame_historial_detalle_procesos_ECD.Show()
		event.Skip()

	def btn_historial_de_procesosOnButtonClick(self, event):
		import formEAY.formularios.frm_reportes.frm_historial_procesos_ECD as frm_historial_procesos_ECD
		frame_historial_procesos_ECD = frm_historial_procesos_ECD.HistorialProcesos_ECD(self)
		frame_historial_procesos_ECD.Center()
		frame_historial_procesos_ECD.Show()
		event.Skip()

	def btn_reporte_inventarioOnButtonClick(self, event):
		import formEAY.formularios.frm_inventario.frm_reporte_inventario  as frm_reporte_inventario
		frame_reporte_inventario = frm_reporte_inventario.ReporteInventario(self)
		frame_reporte_inventario.Center()
		frame_reporte_inventario.Show()
		event.Skip()

	def btn_historial_notasOnButtonClick(self, event):
		import formEAY.formularios.frm_reportes.frm_report_historial_notas as frm_report_historial_notas
		frame_report_historial_notas = frm_report_historial_notas.HistorialDeNotas(self)
		frame_report_historial_notas.Center()
		frame_report_historial_notas.Show()
		event.Skip()

	def btn_historial_novedadesOnButtonClick(self, event):
		import formEAY.formularios.frm_reportes.frm_report_historial_novedades as frm_report_historial_novedades
		frame_report_historial_novedades = frm_report_historial_novedades.HistorialDeNovedades(self)
		frame_report_historial_novedades.Center()
		frame_report_historial_novedades.Show()
		event.Skip()

	def btn_vacio_3OnButtonClick(self, event):
		event.Skip()

	def btn_vacio_4OnButtonClick(self, event):
		event.Skip()


	### FUNCIONES EAY

	def cargar_valores_de_inicializacion(self):
		self.btn_vacio_3.Hide()
		self.btn_vacio_4.Hide()

