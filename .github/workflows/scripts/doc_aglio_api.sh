#!/bin/sh

mkdir -p ./build-docs

cp ./docs/*.apib ./build-docs/

cd ./build-docs

mkdir -p $FOLDER_TO_GH_PAGES

docker run --volume $(pwd):/temp:Z dojot/aglio -i /temp/apiary.apib -o - > ./$FOLDER_TO_GH_PAGES/apiary_${VERSION_NAME}.html

rm -rf api.apib

git add $FOLDER_TO_GH_PAGES/apiary_${VERSION_NAME}.html

if [ -f "$FOLDER_TO_GH_PAGES/apiary_${VERSION_NAME}.html" ]; then
	echo "Doc API create "
else
	echo "Error, couldn't create file for doc"
fi