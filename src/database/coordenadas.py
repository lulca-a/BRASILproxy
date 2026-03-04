
coordenadas_texto = {

    # ======================================================
    # MODERN FRAME (2015+)
    # ======================================================

    "modern": {

        # -----------------------
        # Layout: normal
        # -----------------------
        "normal": {
            "non_creature": [[60,659],[680,659], [680,955],[428,955],[428,939],[311,939],[311,955],[60,955]],
            # "creature": [[60,659],[680,659], [680,920],[578,920],[567,950],[60,950]],
            "creature": [ [60,659],[680,659], [680,915],[586,920],
                                   [570,935],[566,950],[430,950],[430,930],
                                   [312,930],[312,950],[60,950]],
            "legendary_creature": [ [60,659],[680,659], [680,915],[586,920],
                                   [570,935],[566,950],[430,950],[430,930],
                                   [312,930],[312,950],[60,950]]
        },

        # -----------------------
        # Layout: planeswalker
        # -----------------------
        "planeswalker": {
            "2_abilities": [[60,659],[680,659], [680,950],[60,950]],#atualizar
            "3_abilities": [[60,659],[680,659], [680,950],[60,950]],#atualizar
            "4_abilities": [[60,659],[680,659], [680,950],[60,950]]#atualizar
        },

        # -----------------------
        # Layout: saga
        # -----------------------
        "saga": {
            "default": [[60,659],[680,659], [680,950],[60,950]]#atualizar
        },

        # -----------------------
        # Layout: adventure
        # -----------------------
        "adventure": {
            "spell_side": [[60,659],[680,659], [680,950],[60,950]],#atualizar
            "creature_side": [[60,659],[680,659], [680,950],[60,950]]#atualizar
        },

        # -----------------------
        # Layout: modal_dfc
        # -----------------------
        "modal_dfc": {
            "front": [[60,659],[680,659], [680,950],[60,950]],#atualizar
            "back": [[60,659],[680,659], [680,950],[60,950]],#atualizar
        },

        # -----------------------
        # Layout: transform
        # -----------------------
        "transform": {
            "front": [[60,659],[680,659], [680,950],[60,950]],#atualizar
            "back": [[60,659],[680,659], [680,950],[60,950]],#atualizar
        },

        # -----------------------
        # Layout: split
        # -----------------------
        "split": {
            "left": [[60,659],[680,659], [680,950],[60,950]],#atualizar
            "right": [[60,659],[680,659], [680,950],[60,950]],#atualizar
        },

        # -----------------------
        # Layout: battle
        # -----------------------
        "battle": {
            "default": [[60,659],[680,659], [680,950],[60,950]],#atualizar
        }
    },

    # ======================================================
    # OLD FRAME (1993–2003)
    # ======================================================

    "old": {

        # -----------------------
        # Layout: normal
        # -----------------------
        "normal": {
            "non_creature": [[106,633],[644,633], [644,906],[106,906]],
            "creature": [[95,632],[645,632], [645,915],[95,915]],
            "legendary_creature": [[95,632],[645,632], [645,915],[95,915]],
        },

        # -----------------------
        # Layout: split (ex: Invasion)
        # -----------------------
        "split": {
            "left": [[60,659],[680,659], [680,950],[60,950]],#atualizar
            "right": [[60,659],[680,659], [680,950],[60,950]],#atualizar
        }
    },
    "new_old":{ #cartas de 2003
        "normal":{
            "non_creature": [[70,667],[675,667], [675,919],[70,919]],
            "creature": [[70,667],[675,667], [675,919],[70,919]],
            "legendary_creature": [[70,667],[675,667], [675,919],[70,919]],
        }
    }
}

def escolha_layout_texto(carta):

    layout = carta['layout']
    texto = carta['texto']
    tipo = carta['tipo']
    power = carta['power']
    toughness = carta['toughness']


    if carta['frame'] == '1993':
        frame_key = "old"
    elif carta['frame'] == '2003':
        frame_key = "new_old"
    else:
        frame_key = "modern"


    if layout == "normal":

        if power is not None and toughness is not None:
            if 'legendary' in tipo.lower():
                subtype = "legendary_creature"
            else:
                subtype = "creature"
        else:
            subtype = "non_creature"

        coords = coordenadas_texto[frame_key]["normal"][subtype]


    elif layout == "planeswalker":#feature em deeseenvolvimento

        abilities = texto.count("\n") + 1

        if abilities <= 2:
            subtype = "2_abilities"
        elif abilities == 3:
            subtype = "3_abilities"
        else:
            subtype = "4_abilities"

        coords = coordenadas_texto[frame_key]["planeswalker"][subtype]


    elif layout == "saga":#feature em deeseenvolvimento
        coords = coordenadas_texto[frame_key]["saga"]["default"]


    elif layout == "adventure":#feature em deeseenvolvimento
        
        coords = coordenadas_texto[frame_key]["adventure"]["spell_side"]


    elif layout == "modal_dfc":
        coords = coordenadas_texto[frame_key]["modal_dfc"]["front"]


    elif layout == "transform":#feature em deeseenvolvimento
        coords = coordenadas_texto[frame_key]["transform"]["front"]


    elif layout == "split":#feature em deeseenvolvimento
        coords = coordenadas_texto[frame_key]["split"]["left"]


    elif layout == "battle":#feature em deeseenvolvimento
        coords = coordenadas_texto[frame_key]["battle"]["default"]


    else:
        raise ValueError(f"Layout não tratado: {layout}")
    print(frame_key,subtype)
    return coords

def escolha_layout_nome(carta):
    if carta['frame'] == "1993":
        custo = [i for i in carta['custo'] if i == '{']#isso adapta o tamanho do recorte dependendo dos espaços de símbolos de custo
        espaço_custo = 48*len(custo)

        return[(48,54),(636-espaço_custo,54),(636-espaço_custo,94),(48,94)]
    elif carta['frame'] == "2003":
        custo = [i for i in carta['custo'] if i == '{']#isso adapta o tamanho do recorte dependendo dos espaços de símbolos de custo
        espaço_custo = 48*len(custo)

        return[(65,64),(643-espaço_custo,64),(643-espaço_custo,102),(65,102)]
    else:
        custo = [i for i in carta['custo'] if i == '{']#isso adapta o tamanho do recorte dependendo dos espaços de símbolos de custo
        espaço_custo = 48*len(custo)
        letras_grandes = ['F','G','H','J','K','Q','R','g','j','p','q','y']

        for letra in carta['nome']:
            if letra in letras_grandes:
                espaço_vertical = 100
                break
            else:
                espaço_vertical = 98

        return [(60,59),(690-espaço_custo,59),(690-espaço_custo,espaço_vertical),(60,espaço_vertical)]
    
def escolha_layout_tipo(carta):
    
    if carta['frame'] == "1993":
        return [(62,579),(585,579),(585,615),(62,615)]
    elif carta['frame'] == '2003':
        return [(67,596),(584,595),(584,628),(67,628)]
    else:
        return [(58,595),(610,595),(610,635),(58,635)]