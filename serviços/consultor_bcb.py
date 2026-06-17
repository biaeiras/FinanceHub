import requests

__all__ = ["obterValorIndicador"]

indicadores = {
    "selic": 4189,
    "cdi": 4391,
    "ipca": 433,
    "poupança": 196
}

def obterValorIndicador(nome_indicador: str) -> float:

    nome = nome_indicador.strip().lower()

    if nome not in indicadores:
        return 0.0

    codigo_sgs = indicadores[nome]

    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_sgs}/dados/ultimos/1?formato=json"

    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            dados = resposta.json()

            valor = dados[0]["valor"]

            return float(str(valor).replace(",", "."))

        return 0.0

    except Exception:
        return 0.0
