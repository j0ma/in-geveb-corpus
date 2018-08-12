ARTICLE_LIST=$(cat ../data/article_links.txt)
COUNTER=1
CSS="section#main-content > div.block-translatedText > div.translation-wrapper  > div.yiddish-text > p"
for a in $ARTICLE_LIST
do

    # parse article name from URL
    URL=$a
    ARTICLE_NAME=$(echo $a | sed s/"https:\/\/ingeveb.org\/texts-and-translations\/"//g)

    # create output filename
    OUTPUT="../corpus/$COUNTER-$ARTICLE_NAME.txt"
    
    # make actual python script call
    echo "Beginning article scrape for article: $ARTICLE_NAME"
    python scrape_individual_article.py \
           --url="$URL" \
           --css="$CSS" \
           --output="$OUTPUT" \
           --format="text"
    echo "Article scrape done. Incrementing counter..."
    echo

    # increment counter at end of loop
    COUNTER=$((COUNTER+1))

done
