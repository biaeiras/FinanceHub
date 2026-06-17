import unittest

from CalculoFinanceiro import (
    calcularJurosCompostos,
    ajustarPorInflacao,
    calcularRendaPassiva
)


class TestCalculoFinanceiro(unittest.TestCase):

    def test_calcular_juros_compostos(self):
        resultado = calcularJurosCompostos(
            valorInicial=1000,
            aporte=0,
            taxa=0.01,
            tempo=12
        )

        self.assertGreater(resultado, 1000)

    def test_calcular_juros_compostos_parametros_invalidos(self):
        resultado = calcularJurosCompostos(
            valorInicial=-1000,
            aporte=0,
            taxa=0.01,
            tempo=12
        )

        self.assertEqual(resultado, 0.0)

    def test_ajustar_por_inflacao(self):
        resultado = ajustarPorInflacao(
            valor=1000,
            taxaInflacao=0.05,
            tempo=1
        )

        self.assertAlmostEqual(resultado, 952.38, places=2)

    def test_ajustar_por_inflacao_parametros_invalidos(self):
        resultado = ajustarPorInflacao(
            valor=-1000,
            taxaInflacao=0.05,
            tempo=1
        )

        self.assertEqual(resultado, 0.0)

    def test_calcular_renda_passiva(self):
        resultado = calcularRendaPassiva(
            valorTotal=100000,
            taxaRetirada=0.04
        )

        self.assertEqual(resultado, 4000)

    def test_calcular_renda_passiva_parametros_invalidos(self):
        resultado = calcularRendaPassiva(
            valorTotal=-1000,
            taxaRetirada=0.04
        )

        self.assertEqual(resultado, 0.0)


if __name__ == "__main__":
    unittest.main()
