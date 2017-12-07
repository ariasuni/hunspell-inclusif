# Dictionnaire Français Hunspell compatible avec l'écriture inclusive

Basé sur le dictionnaire Dicollecte (https://www.dicollecte.org).

## Modifications

Formes inclusives avec points médians selon deux quatres modèles :
- Caractères féminins encadrés : « militant·e·s », « nouveau·lle », « auteur·rice·s », « joueur·se·s »...
- Union des caractères masculins et féminins : « militant·es », « nouveau·lle », « auteur·rices », « joueur·ses »...
- Morphème féminin encadré : « militant·e·s », « nouveau·elle », « auteur·rice·s », « joueur·euse·s »...
- Union des morphèmes masculins et féminins : « militant·es », « nouveau·elle », « auteur·rices », « joueur·euses »...
- Certaines forme libres pour simplifier la lecture

Formes inclusives neutres :
- « -eur/-rice » devient « -eurice » : « auteurice »
- « -eur/-eresse » devient « -euresse » : « vengeuresse »
- « -eur/-euse » devient « -eureuse » : « bosseureuse »
- « -eau/-elle » devient « -eaulle » : « nouveaulle »
- « -eau/-elle » devient « -elleau » : « nouvelleau »

Mots inclusifs neutres :
- « iel », « iels », « ielle », « ielles »
- « ellui », « elleux », « cellui », « celleux »
- « toustes »
- « lae », « maon », « taon », « saon »

Féminisation de certains termes :
- « adjudante-cheffe »

Correction de bugs dans le dictionnaire original :
- « nouvels » supprimé

## Installation

Sous linux, installez ``hunspell``, ``python3`` et ``zip``.

## Utilisation

Dans le répertoire des sources, entrez ``./scripts/build.sh <VERSION>``.
Cette commande va générer les dictionnaires, les tester et créer les releases.
