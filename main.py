"""
Scrieți un program pentru gestionarea unei librării. Vor fi suportate operațiile:
4.1. Adăugare / ștergere / modificare vânzare: se efectuează pe bază de număr de vânzare / ID
. O vânzare conține: ID, titlu carte, gen carte, preț, tip reducere client (none, silver, gold).
"""
from UserInterface.UI import run_ui


def main():
    order_list = []
    run_ui(order_list)


main()


"""
TODO
Ceva sa fie mai ok xdd
CRUD pare ok
Book cu clasa pare ok
Problema cu UI, nu pare ok!
Intre CRUD si UI se face circularitate daca incerc sa apelez o functie de afisare de acolo in CRUD //de rezolvat
De adaugat teste si descrieri la functii
De structurat mai bine astea drq

"""