from deep_translator import GoogleTranslator

def traduzir(texto_en):
    # 1. Dicionário de Keywords Oficiais (Inglês -> Português)
    # Adicione aqui as palavras que você quer que fiquem fixas
    keywords_fixas = {
        "Haste": "Ímpeto",
        "Trample": "Atropelar",
        "Flying": "Voar",
        "First Strike": "Primeiro Ataque",
        "Double Strike": "Golpe Duplo",
        "Lifelink": "Vínculo com a vida",
        "Vigilance": "Vigilância",
        "Deathtouch": "Toque Mortífero",
        "Indestructible": "Indestrutível",
        "Scry": "Adivinhar",
        "Ward": "Salvaguarda"
    }

    # 2. Substituir palavras-chave por marcadores numéricos
    # Criamos uma lista para recuperar os valores depois
    termos_pt = []
    texto_preparado = texto_en

    for i, (en, pt) in enumerate(keywords_fixas.items()):
        if en in texto_preparado:
            # Substituímos a palavra pelo marcador [[i]]
            texto_preparado = texto_preparado.replace(en, f"[[{i}]]")
            termos_pt.append((f"[[{i}]]", pt))

    # 3. Tradução do texto "blindado"
    try:
        tradutor = GoogleTranslator(source='en', target='pt')
        texto_traduzido = tradutor.translate(texto_preparado)
        
        # 4. Devolver os termos oficiais em PT-BR nos lugares dos marcadores
        for marcador, pt_oficial in termos_pt:
            texto_traduzido = texto_traduzido.replace(marcador, pt_oficial)
            
        return texto_traduzido

    except Exception as e:
        print(f"Erro na tradução: {e}")
        return texto_en # Retorna o original se falhar

# Exemplo de uso:
# print(traduzir_mtg("Creatures you control have Haste."))
# Saída: "As criaturas que você controla têm ímpeto."