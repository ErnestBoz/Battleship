# Battleship Game


## Introduction

Battleship is a strategic naval game that involves players secretly positioning ships on a grid and then guessing their opponent's ship locations. The game alternates between hits and misses, with victory achieved by sinking all the opponent's ships.

This project allows you to play battleships against the AI opponent


# Prerequisites

Python 3.8 or newer
Windows OS


## How to run it

1) download the zip file and extract it

2) open the terminal and type the following to download flask
' pip install -U Flask '

3) run the game by typing the following in the terminal:
' flask --app main run '

4) open your browser and navigate to ' http://127.0.0.1:5000/placement '

VOILA!


## How to play

1) place the 5 battleships of varying sizes on the grid, rotate by pressing "R" if needed

2) press "Send Game"

3) click on the cells to find and destroy the AI opponent's ships

4) the winner is determined by who still has ships remaining


## How to test it

1) in the terminal, download external library pytest:
' pip install pytest '

2) also download additional plugins:
' pip install pytest-depends '
' pip install pytest-cov '

3) run the command:
' python -m pytest '


## Details
* Author: Ernest Bozjigitov
* License: MIT license



