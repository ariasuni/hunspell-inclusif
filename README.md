# Dictionnaire Français Hunspell compatible avec l'écriture inclusive

Basé sur le [dictionnaire Grammalecte](https://grammalecte.net/download.php?prj=fr).

## Modifications

Formes inclusives avec points médians selon quatres modèles&nbsp;:
- Caractères féminins encadrés&nbsp; «&nbsp;militant·e·s&nbsp;», «&nbsp;nouveau·lle&nbsp;», «&nbsp;auteur·rice·s&nbsp;», «&nbsp;joueur·se·s&nbsp;»…
- Union des caractères masculins et féminins&nbsp; «&nbsp;militant·es&nbsp;», «&nbsp;nouveau·lle&nbsp;», «&nbsp;auteur·rices&nbsp;», «&nbsp;joueur·ses&nbsp;»…
- Morphème féminin encadré&nbsp; «&nbsp;militant·e·s&nbsp;», «&nbsp;nouveau·elle&nbsp;», «&nbsp;auteur·rice·s&nbsp;», «&nbsp;joueur·euse·s&nbsp;»…
- Union des morphèmes masculins et féminins&nbsp; «&nbsp;militant·es&nbsp;», «&nbsp;nouveau·elle&nbsp;», «&nbsp;auteur·rices&nbsp;», «&nbsp;joueur·euses&nbsp;»…
- Certaines formes libres pour simplifier la lecture

Formes inclusives neutres&nbsp;:
- «&nbsp;-eur/-rice&nbsp;» devient «&nbsp;-eurice&nbsp;»&nbsp; «&nbsp;auteurice&nbsp;»
- «&nbsp;-eur/-eresse&nbsp;» devient «&nbsp;-euresse&nbsp;»&nbsp; «&nbsp;vengeuresse&nbsp;»
- «&nbsp;-eur/-euse&nbsp;» devient «&nbsp;-eureuse&nbsp;»&nbsp; «&nbsp;bosseureuse&nbsp;»
- «&nbsp;-eau/-elle&nbsp;» devient «&nbsp;-eaulle&nbsp;»&nbsp; «&nbsp;nouveaulle&nbsp;»
- «&nbsp;-eau/-elle&nbsp;» devient «&nbsp;-elleau&nbsp;»&nbsp; «&nbsp;nouvelleau&nbsp;»

Mots inclusifs neutres&nbsp;:
- «&nbsp;iel&nbsp;», «&nbsp;iels&nbsp;», «&nbsp;ielle&nbsp;», «&nbsp;ielles&nbsp;»
- «&nbsp;ellui&nbsp;», «&nbsp;elleux&nbsp;», «&nbsp;cellui&nbsp;», «&nbsp;celleux&nbsp;»
- «&nbsp;toustes&nbsp;»
- «&nbsp;lae&nbsp;», «&nbsp;maon&nbsp;», «&nbsp;taon&nbsp;», «&nbsp;saon&nbsp;»

## Installation

Sous Linux, installez ``hunspell``, ``python3`` et ``zip``.

## Utilisation

Dans le répertoire des sources, entrez ``./scripts/build.sh <VERSION>``.
Cette commande va générer les dictionnaires, les tester et créer les releases.
