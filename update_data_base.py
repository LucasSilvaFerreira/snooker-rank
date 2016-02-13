__author__ = 'lucas'

import sys
from tinydb import TinyDB, Query
db = TinyDB('rank.json')

def add_new_player(nome, info=None):
    #db.all()
    jogador = Query()
    if db.search(jogador.nome == nome):
        print "Jogador ja cadastrado"
        sys.exit()
    else:
        if not info:
            info=''
        db.insert({'nome': nome, 'partidas': 0, 'vitorias': 0, "info": info, "ratio":None })
        print "Usuario {} criado..!".format(nome)

def update_placar(tipo, i_hash=None, array_duplas=None):

    #i ou #d
    #i_hash  = {'jogador1': 2, 'jogador2':1, 'jogador3':0}

    if tipo == 'i':
        for j in i_hash:
            jogador = Query()
            if not db.search(jogador.nome!=j):
                print '{} Nao encontrado'.format(j)
                sys.exit()
        n_partidas = sum([int(partida) for partida in i_hash.itervalues()])
        print 'partidas jogadas: {}'.format(str(n_partidas))

        for up_jogador, v in i_hash.iteritems():
            jogador = Query()
            stats_jogador = db.search(jogador.nome==up_jogador)
            print up_jogador, stats_jogador
            print n_partidas, stats_jogador[0]['partidas']
            p = n_partidas + stats_jogador[0]['partidas']
            win = v + stats_jogador[0]['vitorias']
            #print p, win, up_jogador


            db.update({'partidas': p,
                       'vitorias': win},
                      jogador.nome == up_jogador)
        print 'Placar atualizado!'



    elif tipo == 'd':
        jogador = Query()
        #array_duplas=  [['jogador1', 'jogador2', 1], ['jogador3', 'jogador4', 3]]
        for dupla in array_duplas:
            for j in dupla[:2]:

                if not db.search(jogador.nome==j):
                    print '{} Nao encontrado'.format(j)
                    sys.exit()
        n_partidas = sum([int(partida[-1]) for partida in array_duplas])
        print 'partidas jogadas: '.format(n_partidas) #NAs duplas o numero de partidas nao e igual
        hash_duplas = {j: dupla[-1] for dupla in array_duplas for j in dupla[:2]}



        for up_jogador, v in hash_duplas .iteritems():
            jogador = Query()
            stats_jogador = db.search(jogador.nome==up_jogador)
            print up_jogador, stats_jogador
            print n_partidas, stats_jogador[0]['partidas']
            p = n_partidas + stats_jogador[0]['partidas']
            win = v + stats_jogador[0]['vitorias']
            #print p, win, up_jogador


            db.update({'partidas': p,
                       'vitorias': win},
                      jogador.nome == up_jogador)
        print 'Placar das duplas atualizado!'

def main():
    # add_new_player('Adriana')
    # add_new_player('Dinar')
    # add_new_player('Maira')
    # add_new_player('Lucas')
    update_placar(tipo='i', i_hash={"Adriana":0,
                                    "Dinar":0,
                                    "Lucas":1})

    update_placar(tipo='d', array_duplas=[["Maira","Lucas",3],["Adriana", "Dinar",1]])



if __name__ == '__main__':
    sys.exit(main())
