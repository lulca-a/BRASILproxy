#this whole file was made by AI
import requests

def pull(nome_da_carta):
    # URL da API do Scryfall para busca exata por nome
    url = f"https://api.scryfall.com/cards/named?exact={nome_da_carta}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        
        # Extraindo as informações principais
        info = {
            "nome": dados.get("name"),
            "mana_cost": dados.get("mana_cost"),
            "type_line": dados.get("type_line"),
            "oracle_text": dados.get("oracle_text"),
            "rarity": dados.get("rarity"),
            "image_url": dados.get("image_uris", {}).get("large") # URL da imagem original
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
'''
A fazer:
montar o Cache
Fazer o Header
'''