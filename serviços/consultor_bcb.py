import requests


__all__ = ["obterValorIndicador"]

#indicadores mapeados a partir do site do BCB
indicadores = {
    "selic": 4189,     # Taxa Selic acumulada anual (vai vir algo como 10.5)
    "cdi": 4391,       # Taxa CDI acumulada anual (vai vir bem colada na Selic)
    "ipca": 433,       # IPCA mensal (inflação do mês, ex: 0.35 ou 0.67)
    "poupança": 196    # Poupança rendimento mensal (ex: 0.5 ou 0.6)
}

def obterValorIndicador(nome_indicador: str)-> float :
    """
    Busca o último valor de um indicador econômico na API do Banco Central 
    Retorna o valor em float ou 0.0 se tiver erro de conexão
    
    """

    nome = nome_indicador.strip().lower()

    if nome not in indicadores: 
        return 0.0 

    codigo_sgs = indicadores[nome]

    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_sgs}/dados/ultimos/1?formato=json"

    try: 
        resposta = requests.get(url, timeout=5)
    
        if resposta.status_code == 200: 
            dados = resposta.json()

            print(resposta.json()) #RETIRAR DPS
 

            valor = dados[0]["valor"] 

            #TESTAR SE ESSE DADO PRECISA SER TRATADO 

            valor_float = float(valor)

            return valor_float
        
        else: 
            return 0.0 
        
    except Exception as e : 
        return 0.0 


#TESTE PRA VÊ SE TÁ RODANDO - IA - 11/06 

# Bloco de teste temporário - Só roda se você executar ESTE arquivo direto
if __name__ == "__main__":
    print("--- TESTANDO CONEXÃO COM A API DO BC ---")
    
    # Testa a Selic
    taxa_selic = obterValorIndicador("selic")
    print(f"Resultado Selic: {taxa_selic} (Tipo: {type(taxa_selic)})\n")
    
    # Testa o IPCA
    inflacao_ipca = obterValorIndicador("ipca")
    print(f"Resultado IPCA: {inflacao_ipca} (Tipo: {type(inflacao_ipca)})\n")

    # Testa o CDI
    inflacao_cdi = obterValorIndicador("cdi")
    print(f"Resultado CDI {inflacao_cdi} (Tipo: {type(inflacao_cdi)})\n")
    

    # Testa o CDI
    inflacao_poupança = obterValorIndicador("poupança")
    print(f"Resultado Poupança: {inflacao_poupança} (Tipo: {type(inflacao_poupança)})\n")
    
    # Testa um indicador que não existe para ver se ele trata o erro
    teste_erro = obterValorIndicador("bitcoin")
    print(teste_erro)

    #IA disse: 
    #Se o seu simulador for calcular o rendimento mês a mês (que é o mais comum para aportes mensais), pode transformar a Selic anual em mensal dividindo por 12