import unittest

from servicos.simuladores import (
    calculaJuros,
    simulaAcumulacao,
    calculaTempoParaAposentar,
    calcularValorASerRecebido
)


class TestSimuladores(unittest.TestCase):

    def test_01_calcula_juros(self):

        resultado = calculaJuros(
            valor=1000,
            taxa=0.01,
            tempo=12
        )

        self.assertGreater(resultado, 1000)

    def test_02_simula_acumulacao(self):

        resultado = simulaAcumulacao(
            aporte_mensal=500,
            taxa=0.01,
            meses=12
        )

        self.assertGreater(resultado, 6000)

    def test_03_calcula_tempo_para_aposentar(self):

        meses = calculaTempoParaAposentar(
            aporte_mensal=1000,
            objetivo=10000,
            taxa=0.01
        )

        self.assertGreater(meses, 0)

    def test_04_calcular_valor_a_ser_recebido(self):

        renda = calcularValorASerRecebido(
            patrimonio=120000,
            anos=20
        )

        self.assertGreater(renda, 0)

    def test_05_calcula_juros_parametros_invalidos(self):

        resultado = calculaJuros(
            valor=-1000,
            taxa=0.01,
            tempo=12
        )

        self.assertEqual(resultado, 0.0)


if __name__ == "__main__":
    unittest.main()
