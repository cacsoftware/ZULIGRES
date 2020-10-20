import os

cant_caracteres_tirilla=35

cant_filas_GridBuscarCliente=400
cant_filas_GridBuscarProducto=400


### FRM VENDER
cant_filas_GridFacturar=40
#cambiarValorUnitario=0



def configuracion(seccion, variable):
    from configparser import ConfigParser
    cparser = ConfigParser()

    ruta='bin/myapp.conf'

    cparser.read(ruta)
    desagrupar = cparser.get(seccion, variable)

    return desagrupar


def encabezadoFact():
    clave_encabezado=configuracion('Ventas', 'encabezado')


    encabezado_materialesParada = """
       MATERIALES DE ORNAMENTACION
                  PARADA

     Venta de Tubos, angulos y platinas
          AV. 9 No. 2-53. CALLEJON.
                CUCUTA. COL

             TELF: 5.83.51.37
            CEL: 313.319.88.21

    """

    encabezado_supermercado_ideal = """
          SU  NEGOCIO LTDA
              GUAIMARAL

        AV. 11E No. 2-53. GUAIMARAL.
            CUCUTA. COL

         TELF: 5.83.51.37
        CEL: 313.319.88.21

    """


    encabezado_equivalente_perfumeria = """
        PERFUMERIA EQUIVALENTE
     * Fragancias que Inspiran *

    CALLE 9 ENTRADA 5 LOCAL 1-156
     PRIMER PISO CC. ALEJANDRIA
            CUCUTA. COL

             PEDIDOS
       CEL: 310.234.92.32

    """

    encabezado_casa_perfume = """
       CASA PERFUME
   * Aromas que seducen *

       Calle 11 1-49
        CUCUTA. COL

          PEDIDOS
     CEL: 302.245.90.62
      telf: 5.72.03.95

    """

    encabezado_milan_peluqueria = """
           MILAN PELUQUERIA
      * El arte de la Belleza *

   AV GUAIMARAL 11E 9N-105. LOCAL 4
            CUCUTA. COL

        CEL: 301.734.56.15
         TELF: 5.77.64.36

    """

    encabezado_calzado_prieto = """
           CALZADO PRIETO
    * Lideres en Zapato deportivo
        en la mejores marcas *

          CALLE 26 No. 13-51
             SARAVENA. COL

          TELF: 8.82.10.05

     """


    encabezado_panaderia_peterpan = """
      Panadería y repostería
           PETER PAN D&A
      
    *** La magia del sabor ***

    Avenida 4 # 7-39 B. Latino
             CUCUTA. COL

          TELF: 5.71.50.21
            313.891.90.60

     """

    encabezado_panaderia_peterpan_espiga_dorada = """
         Panadería  PETER PAN
           LA ESPIGA DORADA

     *** La magia del sabor ***

    CALLE  8 # 2 - 80  B. Latino
             CUCUTA. COL

           TELF: 5.48.62.98

     """


    encabezado_zoey_av_4_perfumeria = """
          ZOEY PERFUMERIA

      AVENIDA 4 10-25. CENTRO
            CUCUTA. COL

             PEDIDOS
        CEL: 310.629.08.47
         TELF: 5.71.10.77

    """

    encabezado_zoey_guaimaral_perfumeria = """
         ZOEY PERFUMERIA

    AVENIDA 11 E 9n-105. LOCAL 3
        GUAIMARAL.CUCUTA. COL

            PEDIDOS
        CEL: 310.629.08.47
          TELF: 5.889.889

        """



    encabezado_cac_software_dermasoft = """
          TIENDAS DISTRITO 4
    MENESES RIVEROS ALVARO ALBERTO

         NIT. 88.225.745-5

      CALLE   8 4-75_ LC 02
       CENTRO. CUCUTA. COL

      TELF: (+57) 5.83.17.22

                """

    encabezado_cac_software_dermasoft = """
            PITILO
          
       NIT. 37.293.731-7

      AV. 11E # 11 AN -109
     GUAIMARAL. CUCUTA. COL

     TELF: (+57) 5.74.04.04

                """

    encabezado_cac_software_dermasoft = """
      REDES Y SISTEMAS INFORMATICOS
                    CAC

             NIT. 1094281517-3

            CALLE 23 N # 4 - 39
         PRADOS NORTE. CUCUTA. COL

            CEL: 320.86.86.993
            WSP: 301.227.97.53
          TELF: (+57) 5.94.57.26

                """

    encabezado_motolavado_hang = """
         MOTOLAVADO HANG
                  
      AV. 11 E # 11 AN - 49
        GUAIMARAL. CUCUTA
       CEL: 320.792.87.56
                    """

    encabezado_isma_burger = """
        ISMA  BURGER
       AV. 3 # 5 - 47
    LA VICTORIA. CUCUTA
    CEL: 321.388.92.45
                        """

    encabezado_carrito_rojo = """
       COMIDAS  RAPIDAS
        CARRITO ROJO
        MZ G4 LOTE 15
    PRIMERA ETAPA. CUCUTA
 310.609.00.85 - 301.785.16.45
        5.78.79.20
                        """

    encabezado_peluqueria_prestigio = """
            PRESTIGIO COLORS STYLE

       CALLE 8 - AV 6    CC. ALEJANDRIA
      PARQUEADERO -JUNTO A LOS ASCENSORES

            CEL: 313.418.12.06
             TELF: 5.49.83.52
                            """

    encabezado_cafeteria_prestigio_1 = """
        PRESTIGIO COFFE STORE 1

   CALLE 8 - AV 6    CC. ALEJANDRIA
  PARQUEADERO -JUNTO A LOS ASCENSORES

        CEL: 313.418.12.06
         TELF: 5.49.83.52
                        """

    encabezado_cafeteria_prestigio_2 = """
            PRESTIGIO COFFE STORE 2

       CALLE 8 - AV 6    CC. ALEJANDRIA
                 TERCER PISO

            CEL: 313.418.12.06
             TELF: 5.49.83.52
                            """


    dic = {
           'calzado_prieto'              :  encabezado_calzado_prieto,
           'casa_perfume'                :  encabezado_casa_perfume,
           'carrito_rojo'                :  encabezado_carrito_rojo,
           'isma_burger'                 :  encabezado_isma_burger,
           'cac_software'                :  encabezado_cac_software_dermasoft,
           'equivalente'                 :  encabezado_equivalente_perfumeria,
           'ideal'                       :  encabezado_supermercado_ideal,
           'milan'                       :  encabezado_milan_peluqueria,
           'motolavado_hang'             :  encabezado_motolavado_hang,
           'panaderia_peterpan'          :  encabezado_panaderia_peterpan,
           'parada'                      :  encabezado_materialesParada,
           'peterpan espiga dorada'      :  encabezado_panaderia_peterpan_espiga_dorada,
           'zoey_avenida_4'              :  encabezado_zoey_av_4_perfumeria,
           'zoey_guaimaral'              :  encabezado_zoey_guaimaral_perfumeria,
           'peluqueria_prestigio': encabezado_peluqueria_prestigio,
           'cafeteria_prestigio_1': encabezado_cafeteria_prestigio_1,
           'cafeteria_prestigio_2': encabezado_cafeteria_prestigio_2,

           }

    return dic[clave_encabezado]


