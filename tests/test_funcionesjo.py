import unittest
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
        self.assertIsInstance(hoy(), str)

    def test_day_after(self):
        self.assertEqual(day_after('2023-01-31'), '2023-02-01')

    def test_year_ago(self):
        self.assertEqual(year_ago('2024-02-29'), '2023-02-28')

    def test_month_after(self):
        self.assertEqual(month_after('2023-01-31'), '2023-02-28')

    def test_month_before(self):
        self.assertEqual(month_before('2023-03-31'), '2023-02-28')

    def test_date_mini(self):
        self.assertEqual(date_mini('2023-03-31'), '2023-03')

    def test_mes_by_ordinal(self):
        self.assertEqual(mes_by_ordinal('3'), 'Mar')

    def test_mes_anio_by_abreviacion(self):
        self.assertEqual(mes_anio_by_abreviacion('Mar-2023'), 'marzo 2023')

    def test_anio_mes(self):
        self.assertEqual(anio_mes('2023-03-31'), '2023-Mar')

    def test_ultimo_dia_del_mes(self):
        self.assertEqual(ultimo_dia_del_mes('2023-02-01'), '2023-02-28')

    def test_es_bisiesto(self):
        self.assertTrue(es_bisiesto(2024))

    def test_invertir_orden(self):
        self.assertEqual(invertir_orden([('2023-01-31', 'data')]), [('31-01-2023', 'data')])

    def test_r0und(self):
        self.assertEqual(r0und(1.11111, 3), 1.111)

if __name__ == '__main__':
    unittest.main()
