# Patrick Punch
# 05-07-2024
# CS 331 
# Contributors: Erich Kramer, Rob Churchill for creating the implementation of Othello, Kevin Walsh for helping understand the concepts of the Minimax algorithm.

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
        1. Simulate four games between yourself and the minimax player on a 4x4 board, with the depth parameter set to 5, 3, 2, and 1, respectively.
            a. What were the results of each game?
                - Game 1 (Depth 5):
                Terminal Output:
                ------------------------
                Time taken: 0.0002989768981933594 seconds
                total time : 0.05717802047729492
                --------
                X X X O 
                X X X O 
                X O X O 
                O O O O 
                --------
                Tie game!!
                ------------------------
                - Game 2 (Depth 3):
                Terminal Output: 
                ------------------------
                Time taken: 0.00017380714416503906 seconds
                total time : 0.006933927536010742
                --------
                X X X X 
                X X X X 
                X X X X 
                O O O X 
                --------
                Player 1 Wins!
                ------------------------
                - Game 3 (Depth 2):
                Terminal Output:
                ------------------------
                Time taken: 6.794929504394531e-05 seconds
                total time : 0.0019855499267578125
                --------
                X O O X 
                X X O O 
                X X O X 
                O O O X 
                --------
                Tie game!!
                ------------------------
                - Game 4 (Depth 1):
                ------------------------
                Terminal Output:
                Time taken: 0.00014519691467285156 seconds
                total time : 0.0016040802001953125
                --------
                X X X X 
                X X X X 
                X X X X 
                O O O X 
                --------
                Player 1 Wins!
                ------------------------
            b. Did the minimax player’s moves change when the depth was limited to smaller and smaller values?
                Yes, the moves that the algorithm chose would change when the depth was limited, because the algorithm would search less of the potential outcomes, potentially missing better moves.
            c. What was the average time per move for each of the games? Comment on why there is or is not a difference.
                Depth 5: 0.00952967008 seconds per move
                Depth 3: 0.001155654589 seconds per move
                Depth 2: 0.0003309249878 seconds per move
                Depth 1: 0.0002673467 seconds per move
                The time per move decreases when the depth limit is decreased, due to the fact that the algorithm spends less time searching for the optimal move.
        2. Simulate two games between yourself and the minimax player on an 8x8 board, with the depth parameter set to 5 and 2.
            a. What were the results of each game?
            Depth 5:
            Terminal Output:
                ------------------------
                Player 2( O ) move:
                Time taken: 0.0031859874725341797 seconds
                total time : 55.98157620429993
                total moves = 28
                Move: [7, 6] 
                Player 2( O ) move:
                Can't move
                Player 1( X ) move:
                Move: [6, 6] 
                Player 2( O ) move:
                Can't move
                Player 1( X ) move:
                Move: [1, 7] 
                Player 2( O ) move:
                Can't move
                Player 1( X ) move:
                Move: [6, 7] 
                ----------------
                X X X X X X X X 
                X X X X X X X X 
                X X X X X X X X 
                X X X O O O X X 
                X X X X X O X X 
                X X X X X X X X 
                X X X X X X X X 
                X X X X X X X X 
                ----------------
                Player 1 Wins!
                ------------------------
            Depth 2:
            Terminal Output: 
                ------------------------
                Player 2( O ) move:
                Time taken: 0.0001227855682373047 seconds
                total time : 0.19994354248046875
                total moves = 31
                Move: [7, 6] 
                ----------------
                X X X X X X X X 
                X X X X X X X X 
                X O X O X X X X 
                X O X O O O X X 
                X O X X X O X X 
                O O X O O O O X 
                O O O O O O O O 
                X X X X X X O X 
                ----------------
                Player 1 Wins!
                ------------------------
            b. Did the minimax player’s moves change when the depth changed?
            Yes, the minimax player played different with the depth limited to 2, instead of 5. It seemed easier to pin/take advantageous positions for the depth(2) game.
            c. What was the average time per move for each of the games? Comment on why there is or is not a difference.
            Depth 5: Average time per move: 1.9993420073 seconds
            Depth 2: Average time per move: 0.006449791693 seconds
            There is a very large difference in the amount of time per move, due to the expanding search complexity of an 8x8 othello board, when the depth is limited to 5 versus 2.
