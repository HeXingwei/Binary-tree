#author : Xingwei He
#use: zsh binarize.sh train.txt



#binarize the parser result
cat $1 | python binarize.py > $1.bin
#remove pos and remove redundant bracket
cat $1.bin | python process_binarytree.py >$1.tree

rm $1.bin 
