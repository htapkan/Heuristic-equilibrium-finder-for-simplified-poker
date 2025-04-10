# Heuristic-equilibrium-finder-for-simplified-Poker
Code for an iterated simplified poker game where players learn from past actions
High level description: The code creates simulations of a  repeated simplified poker game played between two computer agents (players) with some capability of randomization and learning. Based on the simulations, the code also finds the most optimal strategy based for each player. As the strategies are chosen interactively, it is hoped that the strategis converge to or reach a sufficiently close point to a real equilibrium of the poker game where choosen strategies form an equilibrium. However, it needs to be noted that strategies have a relatively simplistic structure and one-round simplified poker game abstracts from a full-fledged poker game in important ways.
The description of the one-round simplified poker game: This game contains two players. It shuffles the desk  and it distributes 2 cards to the players and chooses 5 community cards. However, the game only includes the river stage of a full fledged poker game meaning that the community cards are immediately revealed to revealed. Each player has a cash of 9 units and the pot is initially set at 9 units. Each player may raise, fold, call or check depending on the turn and previous action of the other player. However, a player can only raise (bet) an amount of 3 at a given moment. If she is raised by 3, she may reraise again by 3 provided that she has enough cash. The game depending on the strategies of players and the best-card allocates the pot between the players. 

One-round strategies: One round strategies for each player are dictionaries which specify the actions to be chosen dependent on the strength percentile of players. 
We only incorporated a select percentile- intervals- meaning that for a given strategy, the prescribed action for a player with two cards set belonging to the same percentile interval would be the same.

The description of the repeated simplified poker game:
The repeated game is simply an iterated version of the one-round game with the exception that players accumulate information from previous rounds and  they may update their strategies along the way. 

Learning and randomization rule: The players choose actions based on previous results. Players with no-memory or no experience in the repeated game, stars by fully randomizing. Player accumulates the cash-return information from previous rounds and store the average for a certain strategy at a given strenght-percentile 
When player accumulate enough information

