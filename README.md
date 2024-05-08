[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/i3cjXgnP)
# othello-python
Starter Code for Othello AI Agent Programming Assignment

Originally created by Erich Kramer at OSU for Professor Rebecca Hutchinson.
Cleaned up by Rob Churchill.

How to play a game:

1. Run `python3 game_driver.py [player_type] [player_type]`.
2. Choose `human`, or `minimax` as the player types.
3. Follow the prompts to choose where to place stones.

** In my code, I have two files that contain code written completely by one of my peers, Kevin Walsh. The code exists in this directory because we were comparing the time it takes to run each of our algorithms, in an effort to have a greater understanding of the complexity of our own implementations. His code was added after I completed my own implementation, and was not used in any way to complete any of my own work. **

4. Analysis Requirements:
    - Add in a few lines of code to allow you to keep track of the time it takes the minimax player to
    make a move. At the end of each game, print out the average time per move that the minimax
    player takes.
    For the questions below, write your answers in a plaintext file called README. If at any point in
    these experiments, the minimax player takes more than ten seconds to make a move, you should
    terminate the process and report in your README that the minimax player was not able to make
    a move quickly.
        1. Simulate four games between yourself and the minimax player on a 4x4 board, with the depth parameter set to 5, 3, 2, and 1, respectively.
            a. What were the results of each game?
            b. Did the minimax player’s moves change when the depth was limited to smaller and smaller values?
            c. What was the average time per move for each of the games? Comment on why there is or is not a difference.
        2. Simulate two games between yourself and the minimax player on an 8x8 board, with the depth parameter set to 5 and 2.
            a. What were the results of each game?
            b. Did the minimax player’s moves change when the depth changed?
            c. What was the average time per move for each of the games? Comment on why there is or is not a difference.
