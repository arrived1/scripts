#!/bin/bash

for i in {0..200}
do
    mkdir ~/dupa
    cd ~/dupa
    wget http://mamacafe.babyonline.pl/forum/gallery/showimage.php?i=92256&c=46
    cd ~/
    rm -rf ~/dupa
    
    RAND=$((RANDOM%50+5))
    sleep 1
    echo ""
    echo $RAND
    echo ""
    sleep $RAND
done
