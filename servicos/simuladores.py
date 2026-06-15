# =========================
# SIMULADOR APOSENTADORIA
# =========================

class SimuladorAposentadoria:

    def CalculaJuros(self, valor, taxa, tempo):
        """
        Calcula juros compostos
        """
        montante = valor * (1 + taxa) ** tempo
        return montante

    def SimulaAcumulacao(self, aporte_mensal, taxa, meses):
        """
        Simula o valor acumulado ao longo do tempo
        """
        acumulado = 0

        for i in range(meses):
            acumulado = (acumulado + aporte_mensal) * (1 + taxa)

        return acumulado

    def CalculaTempoParaAposentar(self, aporte_mensal, objetivo, taxa):
        """
        Calcula quantos meses serão necessários
        para atingir o objetivo
        """
        acumulado = 0
        meses = 0

        while acumulado < objetivo:
            acumulado = (acumulado + aporte_mensal) * (1 + taxa)
            meses += 1

        return meses

    def CalcularValorASerRecebido(self, patrimonio, anos):
        """
        Estimativa simples de retirada mensal
        """
        meses = anos * 12
        valor_mensal = patrimonio / meses

        return valor_mensal

    def ExibeResultadoAposentadoria(self, valor):
        print("===== RESULTADO APOSENTADORIA =====")
        print(f"Valor calculado: R$ {valor:.2f}")


# =========================
# SIMULADOR INVESTIMENTOS
# =========================

class SimuladorInvestimentos:

    def CalcularJuros(self, valor, taxa, tempo):
        """
        Calcula juros compostos
        """
        montante = valor * (1 + taxa) ** tempo
        return montante

    def CalcularRentabilidade(self, valor_inicial, valor_final):
        """
        Calcula percentual de rentabilidade
        """
        rentabilidade = ((valor_final - valor_inicial) / valor_inicial) * 100
        return rentabilidade

    def SimularInvestimento(self, valor, taxa, meses):
        """
        Simula crescimento do investimento
        """
        resultado = valor * (1 + taxa) ** meses
        return resultado

    def ExibirResultado(self, valor):
        print("===== RESULTADO INVESTIMENTO =====")
        print(f"Valor final: R$ {valor:.2f}")


# =========================
# EXEMPLO DE USO
# =========================

aposentadoria = SimuladorAposentadoria()

valor_acumulado = aposentadoria.SimulaAcumulacao(
    aporte_mensal=500,
    taxa=0.01,
    meses=240
)

aposentadoria.ExibeResultadoAposentadoria(valor_acumulado)


investimento = SimuladorInvestimentos()

resultado = investimento.SimularInvestimento(
    valor=10000,
    taxa=0.015,
    meses=24
)

investimento.ExibirResultado(resultado)
