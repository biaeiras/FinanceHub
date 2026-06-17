from serviços.consultor_bcb import obterValorIndicador

# =========================
# SIMULADOR APOSENTADORIA
# =========================

class SimuladorAposentadoria:

    def CalculaJuros(self, valor, taxa, tempo):
        return valor * (1 + taxa) ** tempo

    def SimulaAcumulacao(self, aporte_mensal, taxa, meses):

        acumulado = 0

        for _ in range(meses):
            acumulado = (acumulado + aporte_mensal) * (1 + taxa)

        return acumulado

    def CalculaTempoParaAposentar(self, aporte_mensal, objetivo, taxa):

        acumulado = 0
        meses = 0

        while acumulado < objetivo:
            acumulado = (acumulado + aporte_mensal) * (1 + taxa)
            meses += 1

        return meses

    def CalcularValorASerRecebido(self, patrimonio, anos):

        meses = anos * 12
        return patrimonio / meses

    def ExibeResultadoAposentadoria(self, valor):

        print("\n===== RESULTADO APOSENTADORIA =====")
        print(f"Valor acumulado: R$ {valor:.2f}")


# =========================
# SIMULADOR INVESTIMENTOS
# =========================

class SimuladorInvestimentos:

    def CalcularJuros(self, valor, taxa, tempo):
        return valor * (1 + taxa) ** tempo

    def CalcularRentabilidade(self, valor_inicial, valor_final):

        return ((valor_final - valor_inicial) / valor_inicial) * 100

    def SimularInvestimento(self, valor, taxa, meses):

        return valor * (1 + taxa) ** meses

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
