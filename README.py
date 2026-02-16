
'''
Arquitetura

        Usuário manda o deck
                |
                |
        Formata-se as cartas do deck
                |
                |
        Confere se carta já está no cache traduzida(nome en e nome pt)
                |
                ------------------
                |                 |
                NÃO               SIM------------Consulta o banco de dados
                |                                E retorna a carta traduzida
                |                                           |
                |                                           |
        Puxa a carta do scry                                |     
                |                                           |
                |                                           |
        Joga carta a carta para                             |
        o googletrans                                       |
                |                                           |
                |                                           |
        Coloca as cartas no Cache                           |
                |                                           |
                |                                           |
        Manda as informações para o -------------------------
        card conjurer
                |
                |
        Card Conjurer manda carta em JPEG
                |
        Salva as cartas em uma pasta de JPEG
                

''' 
