# Pong-Game

Pong is a classic arcade game recreated using Python and the Turtle module. The objective of the game is to control the paddles and hit the ball back and forth between them, trying to outmaneuver the opponent and score points.

Features:

1. Screen setup: The game window is set to a size of 800x600 pixels, providing enough space for the gameplay.

2. Paddle creation: Two paddles are created, one on the right and one on the left side of the screen. The paddles can be controlled using designated keys (up and down arrow keys for the right paddle, and 'w' and 's' keys for the left paddle).

3. Ball movement: A ball object is created that moves across the screen at a consistent speed. The ball bounces off the paddles and the walls, changing direction accordingly.

4. Scoring mechanism: The game keeps track of the score for each player using the `Score` class. The score is displayed on the screen, with the left player's score on the left side and the right player's score on the right side. Each time the ball passes the opponent's paddle, the opponent's score increases by one.

5. Game over: The game continues until one player reaches a certain score (usually 10). When this happens, the game ends, and the winner is declared.

To play the game, run the script and control the paddles using the designated keys. Try to hit the ball past your opponent's paddle while defending your own side. The first player to reach the winning score is crowned the winner.

Enjoy playing Pong and have fun competing against your friends or challenging the computer!
