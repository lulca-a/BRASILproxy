import requests
import time
from limpar import limpar

SCRY_DELAY = 0.1

def pull(nome_da_carta):

    # 1️⃣ Corrige nome com fuzzy
    response = requests.get(
        "https://api.scryfall.com/cards/named",
        params={"fuzzy": nome_da_carta}
    )

    if response.status_code != 200:
        raise ValueError("card does not exist")

    dados = response.json()
    nome_oficial = dados.get("name")

    # 2️⃣ Busca todas prints válidas
    response = requests.get(
        "https://api.scryfall.com/cards/search",
        params={
            "q": f'!"{nome_oficial}" -is:promo -is:digital',
            "unique": "prints"
        }
    )

    dados = response.json()

    if "data" not in dados:
        raise ValueError(dados.get("details", "Erro na API"))

    cartas = dados["data"]

    # 🔥 Ordem de prioridade de frame
    prioridade_frames = ["2015", "2003", "1993"]

    carta_escolhida = None

    # 3️⃣ Loop por prioridade
    permitidos = ["core", "expansion", "masters"]

    for frame in prioridade_frames:
        for carta in cartas:
            if (
                carta.get("layout") == "normal"
                and carta.get("frame") == frame
                and carta.get("border_color") == "black"
                and carta.get("set_type") in permitidos
                and not carta.get("promo")
                and not carta.get("digital")
                and carta.get("booster") == True
            ):
                carta_escolhida = carta
                break
        if carta_escolhida:
            break

    # 4️⃣ Fallback geral (qualquer normal válida)
    if not carta_escolhida:
        for carta in cartas:
            if (
                carta.get("layout") == "normal"
                and carta.get("border_color") == "black"
            ):
                carta_escolhida = carta
                break

    # 5️⃣ Fallback absoluto
    if not carta_escolhida:
        carta_escolhida = cartas[0]

    info = {
        "nome": carta_escolhida.get("name"),
        "mana_cost": carta_escolhida.get("mana_cost"),
        "tipo": carta_escolhida.get("type_line"),
        "texto": carta_escolhida.get("oracle_text"),
        "imagem": carta_escolhida.get("image_uris", {}).get("png"),
        "set": carta_escolhida.get("set"),
        "frame": carta_escolhida.get("frame")
    }

    time.sleep(SCRY_DELAY)
    return info


if __name__ == '__main__':
    carta = 'gandalf the grey'
    resultado = pull(carta)
    print(resultado)
    limpar(resultado['imagem'])