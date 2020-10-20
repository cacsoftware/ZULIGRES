
from  pyeay.dbcac.conexiondb import Ejecutar_SQL
from formEAY.constantesCAC.constantesCAC import BasesDeDatos

if __name__ == '__main__':

    cad_sql = """"
                SELECT *
                FROM producto
    """

    rows = Ejecutar_SQL.select_varios_registros(cad_sql, '', 500, BasesDeDatos.DB_PRINCIPAL)

    print(rows)

