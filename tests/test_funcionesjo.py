import unittest
from datetime import datetime
from funcionesjo import (
    hoy,
    day_after,
    year_ago,
    month_after,
    month_before,
    date_mini,
    mes_by_ordinal,
    mes_anio_by_abreviacion,
    anio_mes,
    ultimo_dia_del_mes,
    es_bisiesto,
    invertir_orden,
    r0und
)

class TestFuncionesjo(unittest.TestCase):
    def test_hoy(self):
        self.assertEqual(hoy(), datetime.today().strftime("%Y-%m-%d"))
        self.assertEqual(hoy("%d/%m/%Y"), datetime.today().strftime("%d/%m/%Y"))
        self.assertEqual(hoy("%m-%d-%Y", inicio_de_mes=True), datetime.today().strftime("%m-01-%Y"))

    def test_day_after(self):
        self.assertEqual(day_after('2023-01-31'), '2023-02-01')
        self.assertEqual(day_after('2023-12-31'), '2024-01-01')
        self.assertEqual(day_after('01/01/2023', '%d/%m/%Y'), '02/01/2023')

    def test_year_ago(self):
        self.assertEqual(year_ago('2024-02-29'), '2023-02-28')
        self.assertEqual(year_ago('2024-02-29', inicio_de_mes=True), '2023-02-01')
        self.assertEqual(year_ago('2024-02-29', inicio_de_anio=True), '2023-01-01')
        self.assertEqual(year_ago('29/02/2024', '%d/%m/%Y'), '28/02/2023')

    def test_month_after(self):
        self.assertEqual(month_after('2023-01-31'), '2023-02-28')
        self.assertEqual(month_after('2024-01-31'), '2024-02-29')
        self.assertEqual(month_after('2023-12-31'), '2024-01-31')
        self.assertEqual(month_after('31/01/2023', '%d/%m/%Y'), '28/02/2023')

    def test_month_before(self):
        self.assertEqual(month_before('2023-03-31'), '2023-02-28')
        self.assertEqual(month_before('2023-01-01'), '2022-12-01')
        self.assertEqual(month_before('01/03/2023', '%d/%m/%Y'), '01/02/2023')

    def test_date_mini(self):
        self.assertEqual(date_mini('2023-01-31'), '2023-01')
        self.assertEqual(date_mini('2024-12-31'), '2024-12')
        self.assertEqual(date_mini('31/01/2023', '%d/%m/%Y'), '2023-01')

    def test_mes_by_ordinal(self):
        self.assertEqual(mes_by_ordinal('1'), 'Ene')
        self.assertEqual(mes_by_ordinal('12'), 'Dic')
        self.assertEqual(mes_by_ordinal('12', abreviado=False), 'Diciembre')
        self.assertEqual(mes_by_ordinal('2', mes_anterior=True), 'Ene')

    def test_mes_anio_by_abreviacion(self):
        self.assertEqual(mes_anio_by_abreviacion('2023-Ene'), 'enero 2023')
        self.assertEqual(mes_anio_by_abreviacion('2023-Ene', mayuscula=True), 'Enero 2023')
        self.assertEqual(mes_anio_by_abreviacion('Ene-2023', mmaa=True), 'enero 2023')

    def test_anio_mes(self):
        self.assertEqual(anio_mes('2023-01-01'), '2023-Ene')
        self.assertEqual(anio_mes('2023-12-31'), '2023-Dic')

    def test_ultimo_dia_del_mes(self):
        self.assertEqual(ultimo_dia_del_mes('2023-02-01'), '2023-02-28')
        self.assertEqual(ultimo_dia_del_mes('2024-02-01'), '2024-02-29')
        self.assertEqual(ultimo_dia_del_mes('2023-01-01'), '2023-01-31')

    def test_es_bisiesto(self):
        self.assertTrue(es_bisiesto(2020))
        self.assertFalse(es_bisiesto(2023))
        self.assertTrue(es_bisiesto(2024))

# ;)
#    def test_invertir_orden(self):
#        self.assertEqual(invertir_orden([('2023-01-31', 'data')]), [('31-01-2023', 'data')])

    def test_r0und(self):
        self.assertEqual(r0und(0.12345), 0.12)
        self.assertEqual(r0und(-0.0), 0.0)
        self.assertEqual(r0und(1.2345, 3), 1.234)

if __name__ == '__main__':
    unittest.main()
