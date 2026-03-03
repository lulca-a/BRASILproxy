
coordenadas_texto = {

    # ======================================================
    # MODERN FRAME (2015+)
    # ======================================================

    "modern": {

        # -----------------------
        # Layout: normal
        # -----------------------
        "normal": {
            "non_creature": [[60,659],[680,659], [680,950],[60,950]],
            "creature": [[60,659],[680,659], [680,920],[578,920],[567,950],[60,950]],#atualizar
            "legendary_creature": [ [60,659],[680,659], [680,915],[586,920],
                                   [570,935],[566,950],[430,950],[430,930],
                                   [312,930],[312,950],[60,950]],
        },

        # -----------------------
        # Layout: planeswalker
        # -----------------------
        "planeswalker": {
            "2_abilities": [[60,659],[680,659], [680,950],[60,950]],#atualizar
            "3_abilities": [[60,659],[680,659], [680,950],[60,950]],#atualizar
            "4_abilities": [[60,659],[680,659], [680,950],[60,950]],#atualizar
        },

        # -----------------------
        # Layout: saga
        # -----------------------
        "saga": {
            "default": [[60,659],[680,659], [680,950],[60,950]],#atualizar
        },

        # -----------------------
        # Layout: adventure
        # -----------------------
        "adventure": {
            "spell_side": [[60,659],[680,659], [680,950],[60,950]],#atualizar
            "creature_side": [[60,659],[680,659], [680,950],[60,950]],#atualizar
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
            "non_creature": [[95,930],[645,930], [645,915],[95,915]],#atualizar
            "creature": [[95,632],[645,632], [645,915],[95,915]],
            "legendary_creature": [[60,659],[680,659], [680,950],[60,950]],#atualizar
        },

        # -----------------------
        # Layout: split (ex: Invasion)
        # -----------------------
        "split": {
            "left": [[60,659],[680,659], [680,950],[60,950]],#atualizar
            "right": [[60,659],[680,659], [680,950],[60,950]],#atualizar
        }
    }
}

def escolha_layout(carta):
    layout = carta['layout']
    texto = carta['texto']
    tipo = carta['tipo']
    power = carta['power']
    toughness = carta['toughness']


    if carta['frame'] in ["1993", "2003"]:
        frame_key = "old"
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