__all__ = [
    "simulador_aposentadoria",
    "simulador_investimento"
]

from servicos.consultor_bcb import obterValorIndicador

from entidades.calculoFinanceiro import (
    calcularJurosCompostos,
    calcularRendaPassiva
)


# =========================
# SIMULADOR APOSENTADORIA
# =========================

class SimuladorAposentadoria:
    """
    Classe responsável pelos cálculos relacionados
    ao planejamento de aposentadoria.
    """

    def CalculaJuros(self, valor, taxa, tempo):
        """
        Calcula o montante final utilizando juros compostos.
        """

        return calcularJurosCompostos(
            valorInicial=valor,
            aporte=0,
            taxa=taxa,
            tempo=tempo
        )

    def SimulaAcumulacao(self, aporte_mensal, taxa, meses):
        """
        Simula a acumulação de patrimônio ao longo do tempo
        utilizando aportes mensais.
        """

        return calcularJurosCompostos(
            valorInicial=0,
            aporte=aporte_mensal,
            taxa=taxa,
            tempo=meses
        )

    def CalculaTempoParaAposentar(self, aporte_mensal, objetivo, taxa):
        """
        Calcula quantos meses são necessários para atingir
        um patrimônio objetivo.
        """

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
        """
        Calcula uma estimativa de renda passiva mensal
        baseada no patrimônio acumulado.
        """

        return calcularRendaPassiva(
            valorTotal=patrimonio,
            taxaRetirada=1 / (anos * 12)
        )

    def ExibeResultadoAposentadoria(self, valor):
        """
        Exibe o resultado da simulação de aposentadoria.
        """

        print("\n===== RESULTADO APOSENTADORIA =====")
        print(f"Valor acumulado: R$ {valor:.2f}")


# =========================
# SIMULADOR INVESTIMENTOS
# =========================

class SimuladorInvestimentos:
    """
    Classe responsável pelos cálculos relacionados
    a investimentos.
    """

    def CalcularJuros(self, valor, taxa, tempo):
        """
        Calcula o montante final utilizando juros compostos.
        """

        return calcularJurosCompostos(
            valorInicial=valor,
            aporte=0,
            taxa=taxa,
            tempo=tempo
        )

    def CalcularRentabilidade(self, valor_inicial, valor_final):
        """
        Calcula a rentabilidade percentual do investimento.
        """

        return ((valor_final - valor_inicial) / valor_inicial) * 100

    def SimularInvestimento(self, valor, taxa, meses):
        """
        Simula o crescimento de um investimento ao longo do tempo.
        """

        return calcularJurosCompostos(
            valorInicial=valor,
            aporte=0,
            taxa=taxa,
            tempo=meses
        )

    def ExibirResultado(self, valor):
        """
        Exibe o resultado da simulação de investimento.
        """

        print("\n===== RESULTADO INVESTIMENTO =====")
        print(f"Valor final: R$ {valor:.2f}")


# =========================
# FUNÇÕES INTEGRADAS AO MENU
# =========================

def simulador_aposentadoria(aporte):
    """
    Executa uma simulação de aposentadoria utilizando
    o aporte mensal do usuário e a taxa Selic obtida
    pela API do Banco Central.
    """

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
    """
    Executa uma simulação de investimento utilizando
    o CDI obtido pela API do Banco Central.
    """

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
