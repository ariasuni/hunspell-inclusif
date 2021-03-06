#!/bin/sh

SRC="$(pwd)"
VERSION="$1"

RELEASE="$SRC"/releases/fr-inclusif-"$VERSION"
mkdir -p "$RELEASE"

TMP="$SRC"/tmp
mkdir -p "$TMP"

#Dictionaries
mkdir -p "$RELEASE"/dictionaries
python3 ./scripts/generate-aff.py ./grammalecte/fr-moderne.aff > "$RELEASE"/dictionaries/fr-moderne-inclusif.aff
python3 ./scripts/generate-dic.py ./grammalecte/fr-moderne.dic > "$RELEASE"/dictionaries/fr-moderne-inclusif.dic
python3 ./scripts/generate-aff.py ./grammalecte/fr-classique.aff > "$RELEASE"/dictionaries/fr-classique-inclusif.aff
python3 ./scripts/generate-dic.py ./grammalecte/fr-classique.dic > "$RELEASE"/dictionaries/fr-classique-inclusif.dic
python3 ./scripts/generate-aff.py ./grammalecte/fr-reforme1990.aff > "$RELEASE"/dictionaries/fr-reforme1990-inclusif.aff
python3 ./scripts/generate-dic.py ./grammalecte/fr-reforme1990.dic > "$RELEASE"/dictionaries/fr-reforme1990-inclusif.dic
python3 ./scripts/generate-aff.py ./grammalecte/fr-toutesvariantes.aff > "$RELEASE"/dictionaries/fr-toutesvariantes-inclusif.aff
python3 ./scripts/generate-dic.py ./grammalecte/fr-toutesvariantes.dic > "$RELEASE"/dictionaries/fr-toutesvariantes-inclusif.dic

cp ./README.md "$RELEASE"/dictionaries/README_fr_inclusif.md

cd "$RELEASE"/dictionaries
ERRORS=$(hunspell -d fr-toutesvariantes-inclusif -l < $SRC/test/words.txt)
if [ "$ERRORS" == "" ]
then
	echo "Success !"
else
	echo "Failure:"
	echo "$ERRORS"
	exit 1
fi

ZIPNAME="$RELEASE"/fr-inclusif-hunspell-$VERSION.zip

cd "$RELEASE"/dictionaries
zip $ZIPNAME fr-moderne-inclusif.aff
zip $ZIPNAME fr-moderne-inclusif.dic
zip $ZIPNAME fr-classique-inclusif.aff
zip $ZIPNAME fr-classique-inclusif.dic
zip $ZIPNAME fr-reforme1990-inclusif.aff
zip $ZIPNAME fr-reforme1990-inclusif.dic
zip $ZIPNAME fr-toutesvariantes-inclusif.aff
zip $ZIPNAME fr-toutesvariantes-inclusif.dic
zip $ZIPNAME README_fr_inclusif.md

#Firefox
ZIPNAME="$RELEASE"/fr-inclusif-firefox-$VERSION.xpi

cp $SRC/firefox/install.rdf "$TMP"/install.rdf
sed -i "s/{{BUILD.VERSION}}/$VERSION/g" "$TMP"/install.rdf

cd "$TMP"
zip $ZIPNAME install.rdf

mkdir dictionaries
cp $RELEASE/dictionaries/fr-classique-inclusif.aff "$TMP"/dictionaries/fr-inclusif.aff
cp $RELEASE/dictionaries/fr-classique-inclusif.dic "$TMP"/dictionaries/fr-inclusif.dic

zip -r $ZIPNAME ./dictionaries
cd ..

rm "$TMP"/install.rdf
rm -Rf "$TMP"/dictionaries

#LibreOffice
ZIPNAME="$RELEASE"/fr-inclusif-libreoffice-$VERSION.oxt

cp $SRC/libreoffice/description.xml "$TMP"/description.xml
sed -i "s/{{BUILD.VERSION}}/$VERSION/g" "$TMP"/description.xml

cp $SRC/libreoffice/package-description.txt "$TMP"/package-description.txt
sed -i "s/{{BUILD.VERSION}}/$VERSION/g" "$TMP"/package-description.txt

cd "$TMP"
zip $ZIPNAME description.xml
zip $ZIPNAME package-description.txt

cd "$SRC"/libreoffice/
zip $ZIPNAME dictionaries.xcu
zip $ZIPNAME icon.png
zip -r $ZIPNAME META-INF
zip -r $ZIPNAME dictionaries

cd "$RELEASE"
zip -r $ZIPNAME dictionaries

rm "$TMP"/description.xml
rm "$TMP"/package-description.txt

#Cleanup
rm -Rf "$TMP"
