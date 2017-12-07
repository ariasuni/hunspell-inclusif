#!/bin/sh

SRC="$(pwd)"
VERSION="$1"

RELEASE="$SRC"/releases/fr-inclusif-"$VERSION"
mkdir -p "$RELEASE"

TMP="$SRC"/tmp
mkdir -p "$TMP"

#Dictionaries
mkdir -p "$RELEASE"/dictionaries
python3 ./scripts/numrules.py ./dictionaries/fr-inclusif.aff > "$RELEASE"/dictionaries/fr-inclusif.aff
cp ./dictionaries/fr-inclusif.dic "$RELEASE"/dictionaries/fr-inclusif.dic

cp $SRC/dictionaries/README_fr_inclusif.txt "$RELEASE"/dictionaries/README_fr_inclusif.txt
sed -i "s/{{BUILD.VERSION}}/$VERSION/g" "$RELEASE"/dictionaries/README_fr_inclusif.txt

cd "$RELEASE"/dictionaries
ERRORS=$(hunspell -d fr-inclusif -l < $SRC/test/words.txt)
if [ "$ERRORS" == "" ]
then
	echo "Success !"
else
	echo "Failure:"
	echo "$ERRORS"
	exit
fi

ZIPNAME="$RELEASE"/fr-inclusif-hunspell-$VERSION.zip

cd "$RELEASE"/dictionaries
zip $ZIPNAME fr-inclusif.aff
zip $ZIPNAME fr-inclusif.dic
zip $ZIPNAME README_fr_inclusif.txt

#Firefox
ZIPNAME="$RELEASE"/fr-inclusif-firefox-$VERSION.xpi

cp $SRC/firefox/install.rdf "$TMP"/install.rdf
sed -i "s/{{BUILD.VERSION}}/$VERSION/g" "$TMP"/install.rdf

cd "$TMP"
zip $ZIPNAME install.rdf

cd "$RELEASE"
zip -r $ZIPNAME dictionaries

rm "$TMP"/install.rdf

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
rm -Rf "$SRC"/tmp
