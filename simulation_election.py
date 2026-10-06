"""
DEMANDER les bulletins de vote
COMPTABILISER les votes par parti
TRANSFORMER les résultats en pourcentages
AFFICHER les résultats
"""
def comptabiliser_votes(votes:list[str])->dict:
    """
    Créer un dictionnaire avec le nombre de votes par parti
    Ex: {
        "PQ": 2,
        "PLQ": 1,
        "QS": 1,
        "CAQ": 0,
        "PCQ": 0
    }
    :param votes: liste des votes
    :return: le dictionnaire avec le nombre de votes par parti
    """
    # Todo : écrire le code de la fonction
    pass

def transformer_votes(votes:dict)->dict:
    """
    Créer un dictionnaire avec le % de votes par parti
    Ex: {
        "PQ": 50,
        "PLQ": 25,
        "QS": 25,
        "CAQ": 0,
        "PCQ": 0
    }
    :param votes: le dictionnaire avec le nombre de votes par parti
    :return: le dictionnaire avec le % de votes par parti
    """
    # Todo : écrire le code de la fonction
    pass

def determiner_resultats(pourcentages:dict)->tuple:
    """
    Déterminer le gagnant, s'il est minoritaire ou majoritaire, et l'opposition
    :param pourcentages: le dictionnaire avec le % de votes par parti
    :return: un tuple contenant (gagnant, majoritaire (oui/non), opposition)
    """
    # Todo : écrire le code de la fonction
    pass

if __name__ == "__main__":
    ls_votes = input("Entrez les bulletins de votes (Ex: PQ, PQ, PLQ, QS...) : ").split(", ")
    dict_votes = comptabiliser_votes(ls_votes)
    dict_pourcentages = transformer_votes(dict_votes)
    print(dict_votes)
    print(dict_pourcentages)
    gagnant, majoritaire, opposition = determiner_resultats(dict_pourcentages)
    print("Gagnant :", gagnant)
    print("Majoritaire :", majoritaire)
    print("Opposition :", opposition)
