from servicos.consultor_bcb import obterValorIndicador

from entidades.calculoFinanceiro import (
calcularJurosCompostos,
calcularRendaPassiva
)
# =========================
# SIMULADOR APOSENTADORIA
# =========================

class SimuladorAposentadoria:

    def CalculaJuros(self, valor, taxa, tempo):
        return calcularJurosCompostos(
            valorInicial=valor,
            aporte=0,
            taxa=taxa,
            tempo=tempo
        )

    def SimulaAcumulacao(self, aporte_mensal, taxa, meses):

        return calcularJurosCompostos(
            valorInicial=0,
            aporte=aporte_mensal,
            taxa=taxa,
            tempo=meses
        )

    def CalculaTempoParaAposentar(self, aporte_mensal, objetivo, taxa):

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

    def CalcularValorASerRecebido(self, patrimonio, anos):

        return calcularRendaPassiva(
            valorTotal=patrimonio,
            taxaRetirada=1 / (anos * 12)
        )

    def ExibeResultadoAposentadoria(self, valor):

        print("\n===== RESULTADO APOSENTADORIA =====")
        print(f"Valor acumulado: R$ {valor:.2f}")


# =========================
# SIMULADOR INVESTIMENTOS
# =========================

class SimuladorInvestimentos:
    def CalcularJuros(self, valor, taxa, tempo):

        return calcularJurosCompostos(
            valorInicial=valor,
            aporte=0,
            taxa=taxa,
            tempo=tempo
        )

    def CalcularRentabilidade(self, valor_inicial, valor_final):

        return ((valor_final - valor_inicial) / valor_inicial) * 100

    def SimularInvestimento(self, valor, taxa, meses):

        return calcularJurosCompostos(
            valorInicial=valor,
            aporte=0,
            taxa=taxa,
            tempo=meses
        )

    def ExibirResultado(self, valor):

        print("\n===== RESULTADO INVESTIMENTO =====")
        print(f"Valor final: R$ {valor:.2f}")


# =========================
# FUNÇÕES INTEGRADAS AO MENU
# =========================

def simulador_aposentadoria(aporte):

    taxa_selic = obterValorIndicador("selic")

    if taxa_selic == 0:
        print("Erro ao consultar a Selic.")
        return

    taxa_mensal = (taxa_selic / 100) / 12

    anos = int(input("Quantos anos deseja investir? "))

    simulador = SimuladorAposentadoria()

    resultado = simulador.SimulaAcumulacao(
        aporte_mensal=aporte,
        taxa=taxa_mensal,
        meses=anos * 12
    )

    simulador.ExibeResultadoAposentadoria(resultado)


def simulador_investimento():

    valor = float(input("Valor inicial do investimento: "))
    meses = int(input("Quantidade de meses: "))

    taxa_cdi = obterValorIndicador("cdi")

    if taxa_cdi == 0:
        print("Erro ao consultar o CDI.")
        return

    taxa_mensal = (taxa_cdi / 100) / 12

    simulador = SimuladorInvestimentos()

    resultado = simulador.SimularInvestimento(
        valor=valor,
        taxa=taxa_mensal,
        meses=meses
    )

    simulador.ExibirResultado(resultado)
