#this whole file was made by AI
#this is made for education purposes
#do not sell the cards u generat in any shape or form
#do not use the cards generated form this script in tournments 

import requests
import time

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
# --- EXEMPLO DE USO ---
#resultado = pull('Sol Ring')
'''
if resultado:
    print(f"--- Dados da Carta: {resultado['nome']} ---")
    print(f"Custo de Mana: {resultado['mana_cost']}")
    print(f"Tipo: {resultado['type_line']}")
    print(f"Texto (Oracle): \n{resultado['oracle_text']}")
    print(f"\nLink da Imagem: {resultado['image_url']}")
'''
#print(resultado)
#tratar saída de texto