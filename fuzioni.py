'''
utili funzioni per velocizzare i procedimenti
'''

lettere = 'jfhhjkdsfhjshfjkhahgkljhg'

lista = ['j', 'f', 'h', 'h', 'j', 'k', 'd', 's', 'f', 'h', 'j', 's', 'h',
'f', 'j', 'k', 'h', 'a', 'h', 'g', 'k', 'l', 'j', 'h', 'g']

lista_num = [3, 5, 1245, 456, 14, 6, 647, 215, 4627, 124, 657, 6547]
dizionario = {
    'nome': 'Bruno',
    'cognome':'Bucciarati',
    'eta': '34',
    'nato': 'Napoli',
}


def pos_pari(dato, diz=False):
    estratti = []
    valori_estr = []

    for i in range(len(dato)):
        if i%2 == 0:
            if not diz:
                estratti.append(dato[i])
            else:
                estratti.append(list(dato)[i])
                valori_estr.append(list(dato.values())[i])

    if not diz:
        return(estratti)
    else:
        return(estratti, valori_estr)

def pos_dispari(dato, diz=False):
    estratti = []
    valori_estr = []

    for i in range(len(dato)):
        if i%2 == 1:
            if not diz:
                estratti.append(dato[i])
            else:
                estratti.append(list(dato)[i])
                valori_estr.append(list(dato.values())[i])
    if not diz:
        return(estratti)
    else:
        return(estratti, valori_estr)


def num_pari(dato):
    estratti = []

    for i in range(len(dato)):
        if dato[i]%2 == 0:
            estratti.append(dato[i])

    return(estratti)

def num_dispari(dato):
    estratti = []

    for i in range(len(dato)):
        if dato[i]%2 == 1:
            estratti.append(dato[i])

    return(estratti) 

'''
from spalla import Verifica # importi la libreria

Verifica.firma("Nome Cognome") # firmi la verifica, questa operazione è obbligatoria almeno una volta

Verifica.stampa_esercizi() # stampa sul terminale l'elenco degli esercizi disponibili in questa verifica

Verifica.stampa_voto() # stampa il vostro voto attuale

es = Verifica.inizia_esercizio(1) # restituisce l'esercizio numero 1

print(es) # mostra la consegna dell'esercizio e i dati sui quali lavorare

print(es.dati) # sono i dati forniti per l'esercizio corrente

es.consegna(x) # dove x è il risultato da voi elaborato per l'esercizio corrente
'''

def svolgi_es(num):
    Verfica.inizia_esercizio(num)
    dati = es.dati

    #es.consegna(risultato)

