from entidades.calculoFinanceiro import (
    calcularJurosCompostos,
    calcularRendaPassiva
)


def test_calcular_juros_compostos():

    resultado = calcularJurosCompostos(
        valorInicial=1000,
        aporte=0,
        taxa=0.01,
        tempo=12
    )

    assert resultado > 1000


def test_calcular_renda_passiva():

    resultado = calcularRendaPassiva(
        valorTotal=100000,
        taxaRetirada=0.04
    )

    assert resultado == 4000
