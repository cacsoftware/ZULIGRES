
import os
import shutil
 
# Setteamos el directorio raiz a la variable rootDir
# En realidad la variable se puede llamar como sea :)

id_eay='88285819'

rta=input('Ingresa tu id: ')

archivos_procesados = 0

if rta == id_eay:
    rootDir = '.'

    for dirName, subdirList, fileList in os.walk(rootDir):
        #print('Directorio encontrado: %s' % dirName)
        hijo=dirName
        for fname in fileList:
            (nombreFichero, extension) = os.path.splitext(fname)

            ruta_archivo = os.path.join(os.getcwd(), dirName,  fname)

            lista_carpetas=dirName.split("\\")       

              
            if extension == '.pyc':

                nueva_ruta_archivo=''

                for i in lista_carpetas[:-1]:
                    nueva_ruta_archivo = nueva_ruta_archivo + i + '\\'
                
                nuevo_nom_archivo = fname
                nuevo_nom_archivo = nuevo_nom_archivo.replace('.cpython-37', '')
                nueva_ruta_archivo = os.path.join(os.getcwd(), nueva_ruta_archivo, nuevo_nom_archivo)            


                shutil.move(ruta_archivo, nueva_ruta_archivo)

            if extension == '.py':
                if fname != 'ARCHIVOS_EAY.py':
                    os.remove(ruta_archivo)
                    archivos_procesados += 1
                    print('Archivos Procesados...', archivos_procesados)
            padre=dirName




    input('terminar eay')

else:
    print('no estas autorizado')
