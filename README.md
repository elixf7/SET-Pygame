# SET-Pygame

**INSERT VIDEO OF CARD GAME**
Recreated the popular card game SET using the pygame library.


### Overview
1. Introduction
2. How to Play
4. Game Modes
5. Implementation
7. Results

### Introduction
I was recently introduced to the card game SET by a friend and it quickly became one of my favorite card games. However, since most people have been playing since childhood, I could never win a game! SET is all skill and requires quick pattern recognition and practice. I thought the best way to get better was to create the game myself, so I could learn at my own speed, and not have to constantly bug a real player to practice with me. Especially since there were no online versions available that I felt were very similar to the physical card game.

I used the pygame library in python to create this game completely from scratch, with new gamemodes not present in the original card game. These include a **Freeplay** mode, a **Versus** mode, and a **Timed** mode. UI elements are also made from scratch using Adobe Photoshop and Illustrator, including painstakingly recreating the 81 unique cards since there were not any satifactory equivilents I could find online. The game also has audio fucntinality for a more engaging experience. 


### How to Play

Below I will explain the basics of how to play SET directly from the [official instructions](https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20ENGLISH.pdf). If you would rather watch a video (recomended if you actually want to play) click [HERE](https://www.youtube.com/watch?v=NzXDfSFQ1c0).


The object of the game is to identify a SET of 3 cards from 12 cards placed face up on the table. Each card has four features, which can vary as follows:


**IMAGE**

A SET consists of 3 cards in which each of the cards’ features, looked at one‐by‐one, are the same on each card, or, are different on each card. All of the features must separately satisfy this rule. In other words: shape must be either the same on all 3 cards, or different on each of the 3 cards; color must be either the same on all 3 cards, or different on each of the 3, etc. See EXAMPLES below.


**A QUICK CHECK ‐ Is it a SET?**
If 2 cards are the same and 1 card is different in any feature, then it is not a SET. For example, if 2 are red and 1 is purple then it is not a SET. A SET must be either all the same OR all different in each individual feature.


**EASY START**
For a quick introduction, start with the small deck (just the solid symbols). This eliminates one feature, shading. Once you can quickly see a SET when playing the 3 feature version, shuffle the 2 decks together to play the full game.


**THE PLAY**
The dealer shuffles the cards and lays 12 face up on the table (in a rectangle) so that they can be seen by all. Players remove SETs of 3 cards from anywhere on the table. Each SET is checked by the other players. If correct, the SET is kept by the player for one point and the dealer replaces the 3 cards with 3 from the deck. A player must call SET before picking up the cards. There are no turns, the first player to call SET gets control of the board. After he/she has called SET, no other player can pick up cards until that player has finished. The SET must be picked up within a few seconds after calling it. If a player calls SET and does not have one, or if the SET is incorrect, he/she loses one point, and the 3 cards are returned to the table. If all players agree that there is not a SET in the 12 cards, 3 more cards are laid face up on the table. The 3 cards are not replaced when the next SET is found, reducing the number back to 12. Note: There are ~ 33:1 odds that a SET is present in 12 cards, and ~ 2500:1 odds when 15 cards are on the table.

The play continues until the deck is depleted. At the end of the game there may be cards remaining that do not form a SET. The number of SETs held by each player is then counted. One point is given for each SET. High score wins.

If you want a longer game, the deal passes to the person on the dealer’s left, and the play resumes with the deck being reshuffled. When all the players have dealt, the game ends. The player with the highest overall score wins.

When playing solitaire, if the player does not find a SET, 3 more cards are laid down with a penalty of one SET. To win the game, the player must remove this penalty by finding a SET on the table out of the last 12 cards.


**EXAMPLES**
For example, the following are SETs:

**IMAGE**


All three cards have the same shape, the same color, the same number of symbols and they all have different shading.

**IMAGE**

All three cards have different shapes, different colors, and different numbers of symbols and they all have the same shading.

**IMAGE**

All three cards have different shapes, different colors, different numbers of symbols and different shadings.


### Game Modes

#### Freeplay

Freeplay is a single player game mode that allows the user to find sets at thier own pace without the stress of competing against another player. The score and cards remaining in the deck are displayed on the top left. A timer is on the bottom right which will be displayed on the victory screen to inform the user how long it took them to find all the sets in the deck. 

Clicking the **Reveal** button will outine in yellow one of the sets on the board. Repeatedly clicking this button will cycle through all sets on the board. The number displayed directly to the right is how many sets are on the current board.

Clicking on the deck (the card with the back facing up), will deal another card onto the board. This can be done a maiumum of three times for 15 cards on the board. The odds of not having a set with 15 cards are 2700:1. 


#### Timed

This game mode challenges the user to find as many sets as possible within a certain time frame. The options are 120s, 90s, and 60s. The UI is very similar to freeplay, except that you will not be able to reveal sets. The end game screen will display your score after time has expired. 

#### Versus

In Versus Mode the user goes head to head with a bots at varying difficulty simulating playing against a real player. During the game, the bot will periodically find sets, outline them in yellow, and new cards will be automatically dealt. Your job is to find more sets than the bot before the deck has run out, exactly like a real game! The bot difficulties are:

Easy: Simulates a Beginner, who has played between 5-15 games

Medium: Simulates a Beginner, who has played between 15-30 games

Hard: Simulates a Competent Player, who has played between 50-80 games

Expert: Simulates an Expert, who has played 130+ games

Impossible: Simulates a Master, extremely difficult (I have only beaten a few times)

These bots were programmed to act as similar to normal players as possible (The excpetion being Impossible Difficulty). The amount of time they take to find set is infuenced by the number of sets on the table, the "difficulty" of the sets on the table (read "Implementation"), and of course random probability. Bots will also not find sets inhumanly quick, nor take extrememly long times. 


### Implementation
In this section I will discuss some of the major features of the game, and how I implemented them in python.

1. Main Loop

Pygame generates a window, and updates it with a main game loop that continues to run until the program is terminated (closing the widow). The game loop runs at 30FPS, meaning that the window is updated 30 times every second. Such a fast FPS is needed for a game like this since the speed at which you select cards, and the timing at which you submit them needs to be accurate. If you are playing against the expert bot for instance, milliseconds sometimes determine which one of you take the set.

If there is any change to the game state, the next frame will display these changes. If for some reason there is a change that takes longer than 1/30 of a second, then the frame rate will drop. However, the game has been optimized so that this should never happen. Even if the frame rate was doubled, there would never be any chopiness.

2. Creating the Cards

While the images were created in Adobe Illustrator, a python class was also created storing the attributes for each card. Each object had a `image`, `shape`, `number_of_shapes`, `color`, and `shading` property. These 81 cards were then put into an array named `deck` which was pulled from at random during the game. 

```
class Card:
    image = None
    shape = int
    number_of_shapes = int
    color = int
    shading = int

    def __init__(self, image, shape, number_of_shapes, color, shading):
        self.image = pygame.transform.scale(image, (141, 215))
        self.shape = shape
        self.number_of_shapes = number_of_shapes
        self.color = color
        self.shading = shading
```

3. Checking a Set

This is very straightforward. I created a function called `set_analysis` which goes through the three cards and compares whether the attributes `shape`, `number_of_shapes`, `color`, and `shading` are either all equal, or all different.

4. Finding the Sets

Finding the sets is a core feature of both the freeplay game mode and the versus game mode. In the freeplay mode, the user needs to be able to cycle through all the sets on the table, and in versus the bot needs to know what set to choose, and how many there are since this impacts timing. 

Finding the sets is a difficult challenge since it is not really feasible to search through every combination of cards on the table and determine if it is a set. While my machine can run these calculations, a slower one may not especially having to do so at 30FPS.

Instead I take an approach where I iterate though all combination of 2 cards on the table instead of 3. This is becuase every two set cards have **exactly one** card that completes the set. This way, I can simply see if this one card is on the table, and if it is not, it is not a set and I can move onto the next 2 cards. This comes in handy especially since you can have up to 15 cards on the table. 15 choose 2 is much smaller than 15 choose 3. 

I store these sets by storing the position of the cards. Each spot on the table is assigned a number 1-15. So if I find a set I store three numbers corresponding to the position of the cards in the set ex: (1,10,4). I can then use these numbers in dealing and removing cards when the player finds a set. 

If there are no sets on the table with 12 cards, I call a function to deal an extra card and reevaluate. I repeat until there is a set on the table. 


5. Creating the bots

This was the most difficult part of the project since I wanted the bots to mimik and acutal human player. To do this I implemented the following features:

  1. Probability distribution: Each bot has its own probaiblity distribution of possible times it takes to find a set. These are normal distributions so the mean value is picked most frewuently. I used this type of distribution beucase after timing myself and others, I found this was a relativly similar to the randomness of human players.

  2. Number of Sets: If there are more sets on the table, you are much more likely to find one quicker. Therefore, the probability distribution for the bots was shifted either left or right depending on the number of sets. 

  3. "Difficulty" of the set: Some sets are just easier to see than others. For instance, you may notice categories that are all the same quicker than categories that are all different. I have noticed this whle playing myself, and everyone I have talked to also agrees that all sets are not made equal. The bots use this to find sets that are "easier" first mimiking a human opponent.

This is a very important feature beucase it allows for you to work on strategy for the game. Personally, I have tried to 

6. Extras

There is quite a bit more that goes into creating a game like this such as creating the UI, dealing with user input, and dealing the cards correctly. While I did not want to delve into that here, there are comments in the set_game.py file that explain the role of various functions and variables. 







