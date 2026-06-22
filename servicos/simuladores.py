__all__ = [
    "simulador_aposentadoria",
    "simulador_investimento",
    "calculaJuros",
    "simulaAcumulacao",
    "calculaTempoParaAposentar",
    "calcularValorASerRecebido"
]

from servicos.consultor_bcb import obterValorIndicador

from entidades.CalculoFinanceiro import (
    calcularJurosCompostos,
    calcularRendaPassiva
)


# =========================
# FUNÇÕES DE CÁLCULO
# =========================

def calculaJuros(valor, taxa, tempo):

    return calcularJurosCompostos(
        valorInicial=valor,
        aporte=0,
        taxa=taxa,
        tempo=tempo
    )


def simulaAcumulacao(aporte_mensal, taxa, meses):

    return calcularJurosCompostos(
        valorInicial=0,
        aporte=aporte_mensal,
        taxa=taxa,
        tempo=meses
    )


def calculaTempoParaAposentar(aporte_mensal, objetivo, taxa):

    acumulado = 0
    meses = 1

    while acumulado < objetivo:

        acumulado = calcularJurosCompostos(
            valorInicial=0,
            aporte=aporte_mensal,
            taxa=taxa,
            tempo=meses
        )

        meses += 1

    return meses


def calcularValorASerRecebido(patrimonio, anos):

    return calcularRendaPassiva(
        valorTotal=patrimonio,
        taxaRetirada=1 / (anos * 12)
    )


# =========================
# MENU APOSENTADORIA
# =========================

def simulador_aposentadoria(aporte):

    taxa_selic = obterValorIndicador("selic")

    if taxa_selic == 0:
        print("Erro ao consultar a Selic.")
        return

    taxa_mensal = (taxa_selic / 100) / 12

    anos = int(input("Quantos anos deseja investir? "))

    resultado = simulaAcumulacao(
        aporte_mensal=aporte,
        taxa=taxa_mensal,
        meses=anos * 12
    )

    print("\n===== RESULTADO APOSENTADORIA =====")
    print(f"Valor acumulado: R$ {resultado:.2f}")


# =========================
# MENU INVESTIMENTO
# =========================

def simulador_investimento():

    valor = float(input("Valor inicial do investimento: "))
    meses = int(input("Quantidade de meses: "))

    taxa_cdi = obterValorIndicador("cdi")

    if taxa_cdi == 0:
        print("Erro ao consultar o CDI.")
        return

    taxa_mensal = (taxa_cdi / 100) / 12

    resultado = calcularJurosCompostos(
        valorInicial=valor,
        aporte=0,
        taxa=taxa_mensal,
        tempo=meses
    )

    print("\n===== RESULTADO INVESTIMENTO =====")
    print(f"Valor final: R$ {resultado:.2f}")
