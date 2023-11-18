ARTICLE_LIST=$(cat ${articles_file:-../data/article_links.txt})
OUTPUT_FOLDER=${1:-../corpus}

# Make output dir if needed
mkdir -pv "${OUTPUT_FOLDER}"

# Get last article id 
LAST_ARTICLE_ID=$(
    ls ${OUTPUT_FOLDER}/*.txt \
        | while read line; do basename $line; done \
        | cut -f1 -d'-' \
        | sort -nr \
        | head -n 1
)

echo "Checking whether there are existing articles in ${OUTPUT_FOLDER}."
if [ -n "${LAST_ARTICLE_ID}" ]
then
    COUNTER=$((LAST_ARTICLE_ID+1))
    echo "Last article id: ${LAST_ARTICLE_ID}. Starting at ${COUNTER}"
else
    COUNTER=1
    echo "No existing articles found in ${OUTPUT_FOLDER}. Starting at ${COUNTER}."
fi

# Selector to search for
CSS="section#main-content > div.block-translatedText > div.translation-wrapper  > div.yiddish-text > p"

for a in $ARTICLE_LIST
do
    echo # new line

    # parse article name from URL
    URL=$a
    ARTICLE_NAME=$(echo $a | sed s/"https:\/\/ingeveb.org\/texts-and-translations\/"//g)
    echo "Article: $ARTICLE_NAME"

    # check if article already exists
    FOUND_ARTICLE=$(ls ${OUTPUT_FOLDER} | rg ${ARTICLE_NAME})
    if [ -z "${FOUND_ARTICLE}"  ]
    then
        # create output filename
        OUTPUT="${OUTPUT_FOLDER}/$COUNTER-$ARTICLE_NAME.txt"
        
        # make actual python script call
        printf "\tBeginning scrape. Output id: ${COUNTER}\n"
        printf "\tOutput file:: ${OUTPUT}\n"
        python src/scrape_individual_article.py \
               --url="$URL" \
               --css="$CSS" \
               --output="$OUTPUT" \
               --format="text"
        printf "\tArticle scrape done. Incrementing counter...\n"
        echo

        # increment counter at end of loop
        COUNTER=$((COUNTER+1))

    else
        printf "\tArticle found under ${FOUND_ARTICLE}\n"
        printf "\tMoving on...\n"
    fi

done

# Finally remove all empty files (size 0 bytes)
# Note: these occur because there may be articles that are only translations for example.
echo "Removing empty articles..."
ls -s ${OUTPUT_FOLDER}/*.txt | rg "\d+-.*\.txt" | rg "^\s*0" | cut -f4 -d' ' | xargs rm -v
