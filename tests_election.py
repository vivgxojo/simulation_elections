import pytest
from simulation_election import comptabiliser_votes, transformer_votes

def test_comptabiliser():
    ls_votes = ["PQ", "PQ", "PLQ", "QS"]
    resultat_attendu = {
        "PQ": 2,
        "PLQ": 1,
        "QS": 1,
        "CAQ": 0,
        "PCQ": 0
    }
    resultat_obtenu = comptabiliser_votes(ls_votes)
    assert resultat_obtenu == resultat_attendu

def test_comptabiliser_zeros():
    # TODO : vérifier qu'une liste vide donne un dictionnaire avec des 0.
    pass

@pytest.mark.parametrize("dict_vote, pourcentages_attendus", [
    ({'CAQ': 0, 'PCQ': 0, 'PLQ': 1, 'PQ': 2, 'QS': 1}, {'CAQ': 0, 'PCQ': 0, 'PLQ': 25, 'PQ': 50, 'QS': 25}),
    ({'CAQ': 0, 'PCQ': 0, 'PLQ': 0, 'PQ': 0, 'QS': 1}, {'CAQ': 0, 'PCQ': 0, 'PLQ': 0, 'PQ': 0, 'QS': 100})
])
def test_fonction(dict_vote, pourcentages_attendus):
    # TODO : compléter le test
    pass

# TODO : ajouter des tests pour vérifier le type de données retournées par les 2 fonctions

# TODO : ajouter un test pour vérifier que la transformation en pourcentage ne modifie pas le dictionnaire de votes