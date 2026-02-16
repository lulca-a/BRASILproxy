#pegar card no scry
    #pegar uma lsita de cards
    #(opcional) receber url de deck
#traduzir com google
    #tratar saída do scry
#inputar no card conjurer
    #entrar no card conjurer e dar os devidos inputs da carta
#receber arquivo e colocar numa pasta (os, path)
    #criar pasta (deck) onde ficarão os arquivos jpeg

#(opcional) Entrar no mtgcardbuilder e colocar os arquivos

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
