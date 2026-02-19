#this whole file was made by AI
import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()
email =  os.getenv('EMAIL')

SCRY_HEADERS = {
    "User-Agent": F"BRASIL-Proxy/1.0 {email}",
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
            #"mana_cost": dados.get("mana_cost"
            # ),
            "tipo": dados.get("type_line"),
            "texto": dados.get("oracle_text"),
            "imagem": dados.get("image_uris", {}).get("png")
        }
        
        # Tratamento para cartas de duas faces (Transform/Meld)
        #if "card_faces" in dados:
         #   faces = []
          #  for face in dados["card_faces"]:
           #     faces.append({
            #        "nome": face.get("name"),
             #       "mana_cost": face.get("mana_cost"),
              #      "type_line": face.get("type_line"),
               #     "oracle_text": face.get("oracle_text")
               # })
           # info["faces"] = faces
        time.sleep(SCRY_DELAY)
        return info
    else:
        raise ValueError('card does not exist')
    
#print(pull('aangs JOURNEY'))
'''

A fazer:
montar o Cache
Fazer o Header
salvar no banco de dados
threads ou asuyncro para puxar mais cartas de uma vez
gracefull degradation

'''