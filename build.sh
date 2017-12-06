#!/bin/sh

SRC="$(pwd)"
VERSION=$1

mkdir -p $SRC/builds

#Dictionaries
mkdir -p $SRC/builds/dictionaries
python3 ./builds/numrules.py ./dictionaries/fr-inclusif.aff > ./builds/dictionaries/fr-inclusif.aff
cp ./dictionaries/fr-inclusif.dic ./builds/dictionaries/fr-inclusif.dic

cd $SRC/builds/dictionaries
ERRORS=$(hunspell -d fr-inclusif -l < $SRC/test/words.txt)
if [ "$ERRORS" == "" ]
then
	echo "Success !"
else
	echo "Failure:"
	echo "$ERRORS"
	exit
fi

#Firefox
mkdir -p $SRC/builds/firefox
ZIPNAME=$SRC/builds/firefox/fr-inclusif-firefox-$VERSION.xpi

cp $SRC/firefox/install.rdf $SRC/builds/firefox/install.rdf
sed -i "s/{{BUILD.VERSION}}/$VERSION/g" $SRC/builds/firefox/install.rdf

cd $SRC/builds/firefox/
zip $ZIPNAME install.rdf

cd $SRC/builds
zip -r $ZIPNAME dictionaries

rm $SRC/builds/firefox/install.rdf

#LibreOffice
mkdir -p $SRC/builds/libreoffice
ZIPNAME=$SRC/builds/libreoffice/fr-inclusif-libreoffice-$VERSION.oxt

cp $SRC/libreoffice/description.xml $SRC/builds/libreoffice/description.xml
sed -i "s/{{BUILD.VERSION}}/$VERSION/g" $SRC/builds/libreoffice/description.xml

cp $SRC/libreoffice/package-description.txt $SRC/builds/libreoffice/package-description.txt
sed -i "s/{{BUILD.VERSION}}/$VERSION/g" $SRC/builds/libreoffice/package-description.txt

cd $SRC/builds/libreoffice/
zip $ZIPNAME description.xml
zip $ZIPNAME package-description.txt

cd $SRC/libreoffice/
zip $ZIPNAME dictionaries.xcu
zip $ZIPNAME icon.png
zip -r $ZIPNAME META-INF

cd $SRC/builds
zip -r $ZIPNAME dictionaries

rm $SRC/builds/libreoffice/description.xml
rm $SRC/builds/libreoffice/package-description.txt

