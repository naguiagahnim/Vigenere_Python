from module import *
import time

def test_chiffrement():
    """
    Vérifie que la fonction `chiffrementVigenere` fonctionne correctement.
    Vérifie que le texte chiffré  est celui attendu et que le texte chiffré  est le même que celui dans le fichier texte_chiffre.txt.
    Entrée : le texte, la clef sous forme de fichiers
    Sortie : Rien
    """
    chemin_texte = './Sauvegarde/texte.txt'
    chemin_clef = './Sauvegarde/clef.txt'
    chemin_sortie = './Sauvegarde/texte_chiffre.txt'

    texte = lire_fichier(chemin_texte)
    clef = lire_fichier(chemin_clef)
    texte_chiffre_attendu = lire_fichier("./Sauvegarde/texte_chiffre.txt")

    texte_chiffre = chiffrementVigenere(texte, clef)
    texte_chiffre_fichier = lire_fichier(chemin_sortie)

    assert texte_chiffre == texte_chiffre_attendu, f"Attendu {texte_chiffre_attendu}, mais {texte_chiffre} fourni"
    assert texte_chiffre == texte_chiffre_fichier, f"Attendu {texte_chiffre_fichier}, mais {texte_chiffre} fourni"


def test_dechiffrement():
    """
    Vérifie que la fonction `dechiffrementVigenere` fonctionne correctement.
    Vérifie que le texte déchiffré est le même que le texte original.
    Entrée : le texte chiffré  et la clef sous forme de fichiers
    Sortie : Rien
    """
    chemin_texte_chiffre = './Sauvegarde/texte_chiffre.txt'
    chemin_clef = './Sauvegarde/clef.txt'

    texte_chiffre = lire_fichier(chemin_texte_chiffre)
    clef = lire_fichier(chemin_clef)
    texte_dechiffre_attendu = lire_fichier("./Sauvegarde/texte.txt")

    texte_dechiffre = dechiffrementVigenere(texte_chiffre, clef)

    assert texte_dechiffre == texte_dechiffre_attendu, f"Attendu {texte_dechiffre_attendu}, mais {texte_dechiffre} fourni"
    chemin_texte_chiffre = './Sauvegarde/texte_chiffre.txt'
    chemin_clef = './Sauvegarde/clef.txt'

    texte_chiffre = lire_fichier(chemin_texte_chiffre)
    clef = lire_fichier(chemin_clef)
    texte_dechiffre_attendu = lire_fichier("./Sauvegarde/texte.txt")

    texte_dechiffre = dechiffrementVigenere(texte_chiffre, clef)

    assert texte_dechiffre == texte_dechiffre_attendu, f"Attendu {texte_dechiffre_attendu}, mais {texte_dechiffre} fourni"


def test_chiffrement_dechiffrement():
    """
    Vérifie que le texte déchiffré est le même que le texte original en appliquant d'abord le chiffrement Vigenère puis le déchiffrement Vigenère.
    Entrée : le texte et la clef sous forme de fichiers
    Sortie : Rien
    """
    chemin_texte = './Sauvegarde/texte.txt'
    chemin_clef = './Sauvegarde/clef.txt'

    texte = lire_fichier(chemin_texte)
    clef = lire_fichier(chemin_clef)

    texte_chiffre = chiffrementVigenere(texte, clef)
    texte_dechiffre = dechiffrementVigenere(texte_chiffre, clef)

    assert texte_dechiffre.replace(" ", "").lower() == texte.replace(" ", "").lower(), \
        f"Attendu {texte.replace(' ', '').lower()}, mais {texte_dechiffre.replace(' ', '').lower()} fourni"
    chemin_texte = './Sauvegarde/texte.txt'
    chemin_clef = './Sauvegarde/clef.txt'

    texte = lire_fichier(chemin_texte)
    clef = lire_fichier(chemin_clef)

    texte_chiffre = chiffrementVigenere(texte, clef)
    texte_dechiffre = dechiffrementVigenere(texte_chiffre, clef)

    assert texte_dechiffre.replace(" ", "").lower() == texte.replace(" ", "").lower(), \
        f"Attendu {texte.replace(' ', '').lower()}, mais {texte_dechiffre.replace(' ', '').lower()} fourni"


if __name__ == '__main__':
    temps_avant_exec = time.time()
    test_chiffrement()
    temps_apres_exec = time.time()
    print("Temps écoulé pour le chiffrement: ", temps_apres_exec - temps_avant_exec, " secondes.")
    temps_avant_exec = time.time()
    test_dechiffrement()
    temps_apres_exec = time.time()
    print("Temps écoulé pour le chiffrement: ", temps_apres_exec - temps_avant_exec, " secondes.")
    temps_avant_exec = time.time()
    test_chiffrement_dechiffrement()
    temps_apres_exec = time.time()
    print("Temps écoulé pour le chiffrement: ", temps_apres_exec - temps_avant_exec, " secondes.")
    temps_avant_exec = time.time()
    print("Tous les tests fonctionnent.")