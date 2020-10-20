
import wx
import time as tt
import subprocess
#import sys

# import scheduler_eay
# import threading

#import formEAY.dbaseCAC.db_modificacionesBaseDatos as db_modificacionesBaseDatos
import formEAY.cmd_eay.productos_eay  as productos_eay

if __name__ == '__main__':
    app=wx.App()


    #db_modificacionesBaseDatos.tabla_39__insumo()
    productos_eay.insertar_productos(60)





    app.MainLoop()