OUTPUT_FOLDER=${1:-../corpus}
ARTICLE_LIST=$(cat ../data/article_links.txt)
COUNTER=$(ls ${OUTPUT_FOLDER}/*.txt | cut -f1 -d'-' | sort -nr | head -n 1)
CSS="section#main-content > div.block-translatedText > div.translation-wrapper  > div.yiddish-text > p"
for a in $ARTICLE_LIST
do

    # parse article name from URL
    URL=$a
    ARTICLE_NAME=$(echo $a | sed s/"https:\/\/ingeveb.org\/texts-and-translations\/"//g)

    # check if article already exists
    FOUND_ARTICLE=$(ls ${OUTPUT_FOLDER} | rg ${ARTICLE_NAME})
    if [ -z "${FOUND_ARTICLE}"  ]
    then
        # create output filename
        OUTPUT="${OUTPUT_FOLDER}/$COUNTER-$ARTICLE_NAME.txt"
        
        # make actual python script call
        echo "Beginning article scrape for article: $ARTICLE_NAME"
        #python scrape_individual_article.py \
               #--url="$URL" \
               #--css="$CSS" \
               #--output="$OUTPUT" \
               #--format="text"
        sleep 1
        echo "Article scrape done. Incrementing counter..."
        echo

        # increment counter at end of loop
        COUNTER=$((COUNTER+1))

    else
        echo "Article ${ARTICLE_NAME} found under ${FOUND_ARTICLE}"
        echo "Moving on..."
    fi

done
