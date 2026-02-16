#this whole file was made by AI
import requests
import time

SCRY_HEADERS = {
    "User-Agent": "BRASIL-Proxy/1.0 (##########@gmail.com)",
    "Accept": "application/json"
}
SCRY_DELAY = 0.1

def pull(nome_da_carta):
    # URL da API do Scryfall para busca exata por nome
    url = f"https://api.scryfall.com/cards/named?fuzzy={nome_da_carta}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        
        # Extraindo as informações principais
        info = {
            "nome": dados.get("name"),
            "mana_cost": dados.get("mana_cost"),
            "type_line": dados.get("type_line"),
            "oracle_text": dados.get("oracle_text"),
            "rarity": dados.get("rarity")
        }
        
        # Tratamento para cartas de duas faces (Transform/Meld)
        if "card_faces" in dados:
            faces = []
            for face in dados["card_faces"]:
                faces.append({
                    "nome": face.get("name"),
                    "mana_cost": face.get("mana_cost"),
                    "type_line": face.get("type_line"),
                    "oracle_text": face.get("oracle_text")
                })
            info["faces"] = faces
            
        return info
    time.sleep(SCRY_DELAY)
#print(pull('aangs'))
'''

A fazer:
montar o Cache
Fazer o Header
salvar no banco de dados
threads ou asuyncro para puxar mais cartas de uma vez
gracefull degradation

'''