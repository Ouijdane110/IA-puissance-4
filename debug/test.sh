#!/bin/bash
if [ $1 == 1 ]
then
   cd ../ && python3 puissance4_minimax_vs_alphabeta.py
elif [ $1 == 2 ]
then
   cd ../ && python3 puissance4_player1_vs_player2.py
elif [ $1 == 3 ]
then
   cd ../ && python3 puissance4_with_alphabeta_IA.py
elif [ $1 == 4 ]
then
   cd ../ && python3 puissance4_with_minimax_IA.py
else
   echo "Invalid Parameters."
fi