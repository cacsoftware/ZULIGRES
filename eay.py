
import wx
import time as tt
import frm_principal as frm_principal
import subprocess
#import sys

# import scheduler_eay
# import threading

#import formEAY.dbaseCAC.db_modificacionesBaseDatos as db_modificacionesBaseDatos

class MainWindow(wx.App):
    def InitLocale(self):
        self.ResetLocale()
        import locale
        lang, enc = locale.getdefaultlocale()
        self._initial_locale = wx.Locale(lang, lang[:2], lang)
        locale.setlocale(locale.LC_ALL, lang)


if __name__ == '__main__':

    #window = MainWindow()
    app = wx.App()

    #db_modificacionesBaseDatos.tabla_39__insumo()

    frame_principal=frm_principal.Principal(None)
    frame_principal.Center()
    frame_principal.Show()


    app.MainLoop()


