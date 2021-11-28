# Object oriented programming review

Object oriented programming (OOP) is among the most used programming
paradigms (if not _the_ most common) in the industry. It's not usual
however to begin learning programming with this paradigm. Entry courses
generally introduce programming via the procedural paradigm. This guide
serves to bridge the gap for people coming from a procedural background
wanting a better comprehension of codebases focused on OOP.

In procedural programming the code is divided into data structures and
_procedures_ which transform them. Understanding how to write a solution in
the procedural paradigm involves designing the data structures that most
appropiately encode the problem and figuring out which transformations
are needed. This defines a very clear line of separation
between data and logic.

In contrast, in OOP we encapsulate both logic and
code into things called _objects_. OOP-based solutions focus on
understanding what objects can model the problem and what interactions
are there between them. This way of designing solutions attempts to
modularize _responsibilities_ -- since each object is owner of its own data,
instead of modifying another object's properties, we ask the object to
execute an _action_. We delegate the implementation details to the object,
in other words, knowing how to store and transform its data is an object's
responsibility.

It's important to know there is no single paradigm that works best in all
cases, and codebases that are purely within one paradigm only occur in
classrooms.

In the following exercises we will attempt to transform a piece of code
from a procedural design to an object-oriented one. At a first glance
the end result might seem longer and more complicated than the starting point.
That is true. Since procedural programming usually shares data structures
between functions, this high code coupling lends itself well
to small codebases. Trying to separate the different actors in such
a short problem will undoubtedly lead to more apparent complexity. However!
You must strive to see the bigger picture. These exercises are for
testing and understanding OOP concepts. Try to imagine how the procedural
code would look like if it had thousands of lines of logic, and do the
same with the OOP code. It's not merely out of stubbornness that OOP became
the de facto standard in the industry.

## Introduction: the game

The following problem statement and code has been taken from
[Arianne Dee](https://github.com/ariannedee)'s
[OOP in Python Training](https://github.com/ariannedee/oop-python). Refactoring
steps have been ommitted, modified or added in order to more clearly explain
the concepts behind them.

The problem statement is as follows:

>Simulate a simple board game.
>
>There are 2 players, each player takes turn rolling a die and moving that
>number of spaces.
>
>The first person to space 100 wins.

Right off the bat we can see that the only thing we need to keep track of
is each player's points (or space counts). A simple solution might look
like the following:

```python
import random
player_1_score = 0
player_2_score = 0

while True:
    player_1_roll = random.randint(1, 6)
    player_1_score += player_1_roll
    print(f"Player 1 score: {player_1_score} (rolled a {player_1_roll})")
    if player_1_score >= 100:
        print("Player 1 wins!")
        break

    player_2_roll = random.randint(1, 6)
    player_2_score += player_2_roll
    print(f"Player 2 score: {player_2_score} (rolled a {player_2_roll})")
    if player_2_score >= 100:
        print("Player 2 wins!")
        break
```


## A procedural solution

Our previous code works!
But for it to truly be procedural we should avoid duplicating
code and factor a player's movement into procedures that transform the
underlying data structures -- in this case, the player scores:

```python
import random

def player_move(i, previous_score):
    player_roll = random.randint(1, 6)
    player_score = previous_score + player_roll
    print(f"Player {i+1} score: {player_score} (rolled a {player_roll})")
    return player_score

player_scores = [0, 0]
finished = False

while not finished:
    for player_number, player_score in enumerate(player_scores):
        player_scores[player_number] = player_move(player_number, player_score)
        if player_scores[player_number] >= 100:
            print(f"Player {player_number+1} wins!")
            finished = True
            break
```

now we can clearly see the main components of procedural programming:

- figure out what data needs to be stored (the player scores)
- decide what representation is best for that data (an array instead of
many variables)
- transform the data structures with _procedures_ until the end result is
achieved.

## An object oriented approach

As we explained before, the main focus of object oriented programming
is understanding which _objects_  are there in the underlying problem,
what data they have, how they operate on that data and how they talk
to each other. Objects are usually modeled after real-life things
and phenomena. In this case, the most direct example would be the
players! Let's see the main points of this approach:

- formulate the problem in terms of objects (two **Players**
are rolling dice until one of them wins)
- describe each object by what it knows and what it does:
  - each player knows their current score
  - in a given turn, they can increase their score by rolling a die
- describe interactions between objects (none for now!)

### First exercise: a Player class

Your first task is to write the player logic using a `Player` class.
You should fill out your code in `exercise_1/exercise_1.py`. The game logic
has already been rewritten and some of the class's functions
(or _methods_) have been filled in. You'll need to complete the
`take_turn` and `has_won` methods so that the following game
logic works:

```python
def play_game(num_players=2):
    players = [Player(i + 1) for i in range(num_players)]
    while True:
        for player in players:
            player.take_turn()
            if player.has_won():
                print(f"{player} wins")
                return
```

This method starts by creating an amount `num_players` of `Player`s.
For every turn, each player rolls their dice and updates their
score count. If the player that has just rolled has surpassed 100,
then they have won and the game ends.

Notice that much of the game logic has been encapsulated. We, as programmers
of the `play_game` function, know that in each turn we must allow a player
to do some actions and after check if they have won. The specifics of this,
as well as where the data is saved and how, is up to the `Player` class. This
is exactly the kind of delegation we want to do in object oriented programming.

### Interlude: how objects are defined in Python

Python's object system is based on  _classes_. To create an object we first
must define its class via `class X:` and then instance it with `x = X()`.
When first instantiating a class, the _constructor method_ `X.__init__` is
called.
This is often used to set up the object's properties and other procedures
relating to its state (such as initiating a database connection or reading
a configuration file in the disk).

You'll notice in `exercise_1.py` that most methods in a class have a first
argument which is called `self`. This is the reference of the object. When
you write a function call as `x.fun(42)`, Python will call the `fun` function
with first argument `x` and second argument `42`. From the perspective of
the function this is an explicit mapping, instead of the implicit `this`
assignment that other languages use.

In the template for the first exercise you
will also see a _static method_ which is a function defined in a class using
the  `@staticmethod` _decorator_. A static method is a normal function with
no access to the class instance (notice that it doesn't define `self`!). It
could of course be defined outside of the class, but usually static methods
are conceptually bound to the class we are defining. Since static methods
aren't bound to an object, you can use it by calling `X.static_method()`.
While defining other non-static functions in `X`, you can use
`self.static_method` to refer to the function.

As you will see in these examples, Python doesn't have a syntax for
defining methods as public or private. The
[naming convention in PEP8](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles)
describes properties or methods starting with a single underscore (`_`)
as weakly private, and identifiers starting with a double underscore
(`__`) as a stronger way of denoting a private property or method. With
the latter one, Python also does some name mangling to avoid it being
called (although it's still reachable if you really _really_ need it).
Identifiers starting and ending with a double underscore are labeled
"magic" and shouldn't be defined since they help differentiate special
Python functions (such as `__init__` or `__str__` as you'll see in
the exercises) from user-defined ones.


### Second exercise: factoring game logic


The idea for the second exercise is to create a class that encapsulates
the game logic and its associated data. The code should make the following
snippet work (found in `exercise_2/main.py`):

```python
game1 = Game(num_players=2, target_score=20)
game2 = Game(num_players=3, target_score=50)

game2.play_game()
game1.play_game()
```

and it should produce an output like the following:

```
Game 2 start
Player 1: 3 (rolled a 3)
Player 2: 6 (rolled a 6)
Player 3: 6 (rolled a 6)
...
Game 2: Player 2 wins
Game 2 is over

Game 1 start
Player 1: 3 (rolled a 3)
Player 2: 2 (rolled a 2)
...
Game 1: Player 2 wins
Game 1 is over
```

We're now allowing for the games to have different target scores and we are
creating many games at the same time. Each game should instantiate its
own `Player`s. You'll be reusing the code for the player from exercise 1,
and you should modify it so that `100` is not hard-coded as the target
score. A key question that you'll need to answer is *who should know the
target score*. It's clear that to calculate `Player.has_won()` the player
needs it, but should that information be stored in the player
or the game?

There's something interesting going on in the expected output as well.
We created two games and the constructor only received the number of players
and the max score, but somehow `game2` knows that it is game number 2
and `game1` knows that it is game number 1? Somehow a Game instance
is able to communicate with other Game instances.

We've talked about instance properties, which are variables that all the
methods can use -- like the `score` in the `Player` class of exercise 1.
If we have two different players, each instance has its own `score`
property and there is no confusion since each method receives a `self`
which is a reference to the class instance that it is acting on. However,
for `game2` to know that there was another game already created before it,
we'll need a property that is _shared across instances_: a *class property*!
These properties are not accessed via the `self` but through the class name.
For example:

``` python
class X:
    class_property = 0
    def __init__(self):
        X.class_property = 42
        self.instance_property = X.class_property
```

Class properties (also called attributes) are defined outside of the methods and under the scope of
the class. Any piece of code (both a method of the class and code outside
of the class) can access it at any time using `X.class_property`.

For game instances to identify themselves without passing an index in
the constructor we can use a counter as a class property. Each time
a game is created the counter is incremented and the current number should
be stored as an instance attribute (so that further game creations do
not override it).

### Third exercise: inheritance

We now want to introduce a new type of Player. This person is lucky and
never rolls below a 3! How can we adapt our solution to include this
new player?

Our first thought might be to create a new `LuckyPlayer` class that is
pretty much the same as `Player`, but the `LuckyPlayer._roll_die` will do a
`randint` starting on 3. It's a small change, we can just copy the original
class, rename it and update that line. This however incurs in a lot of code
duplication just to change one line! And it also means that if we want to
add a new method for a player or change some behavior we'll need to do it
twice, once for each class.

Another way might be through a parameter on the `Player` constructor
to set a flag indicating whether the player is lucky or not. In the
`_roll_die` method, if the flag is set the minimum roll will be 3. This avoids
having duplicated code. This works well, but if the difference in
behavior was bigger or more complex we might end up with a lot of branches.
Having many different behaviors based on flags is not only unsightly and
hard to mantain, it can also introduce bugs due to incomplete case handling.

In object oriented programming we can use the concept of _inheritance_ to
avoid having duplicated code _and_ avoid having to program many different
behaviors into the same class. The concept is simple: we can _inherit_
the behavior we want from a class and modify or extend it in any way we want.
Additionally, there are many interesting consequences that stem from this
design pattern.  Since `LuckyPlayer` is a subclass of `Player`, we can
just expect some variable or reference to be a `Player` and if it ends
up being a `LuckyPlayer` the code will still work! These are the benefits
of **subtyping** and encapsulation: since the different behavior is factored
in a subtype, we can operate with the usual interface (methods and
attributes) and the outside code doesn't need to concern itself with
which particular type of player it is dealing. This is a very powerful
abstraction. Here is an example in Python:

```python
class Greeting:
    def say(self):
        print(self.get_message())

    def get_message(self):
        return "Hi!"

class BusinessGreeting(Greeting):
    def get_message(self):
        return "How do you do?"

def say_hi(Greet):
    greet = Greet()
    greet.say()

say_hi(Greeting)
say_hi(BusinessGreeting)
```

Here we define a variant of `Greeting` that is oriented for formal use.
In `BusinessGreeting` we don't have to redefine `say` since we inherit that from
`Greeting`. Finally, the `say_hi` function can work with a regular `Greeting`
or its subtype, `BusinessGreeting`.

Recognizing when to subtype to factorize different behaviors is key to
mastering object oriented programming. Remember: in programming, there is no
inheritance tax, so use it all you like!

In this exercise we will force the first player to be a lucky one. Use
inheritance to modify the relevant method so that a Game with the
following modified constructor works:
```python
class Game:
    counter = 0
    def __init__(self, num_players, target_score=100):
        self.target_score = target_score
        self.players = [Player(i + 1) for i in range(num_players)]
        self.players[0] = LuckyPlayer(1)
        Game.counter += 1
        self.game_num = Game.counter
        print(self.players)
```
it might also be useful to change  the `__str__` in LuckyPlayer so we know
which one is lucky!


### Fourth exercise: polymorphism

Usually we get tired of playing the same game after a while. Let's spice it up
with some variants!

An easy way of doing so would be by changing the type of dice we use:

```python
from random import randint, random

def russian_roulette_die():
    # Standard 6-sided die, but with a 1/1000th chance of rolling -1000.
    if random() < 1/1000:
        return -1000
    return randint(1,6)

def d20():
    # Standard d20 die
    return randint(1,20)

def rigged_die(num_run):
    # Every eighth run the throw is lucky.
    if num_run % 8 == 0:
        return randint(3,6)
    return randint(1,6)
```

How can we implement these changes in the code? It would be madness to encode
every type of dice in the `Player` class. Why would the players concern themselves
with how a die throw is calculated? It should make sense at this point to factor
this behavior into its own class.

We will define a base class that doesn't have any particular behavior but defines
what methods we can call for any subclass. In other words, we are defining the
**interface**:

```python
class Die:
    def roll():
        raise NotImplementedError

    def __str__():
        raise NotImplementedError
```

When defining such classes that are not meant to be used directly, we usually
raise errors to avoid calling the methods. We are meant to use subclasses that
_implement_ that interface. However, game logic should be written in terms of
the interface and not depending on which implementation is used. This is
related to the concept of _polymorphism_, where we define a single interface
for many different data types.

In this exercise you'll have to define the classes `RussianRouletteDie`, `D20Die`
and `RiggedDie`, inheriting from `Die`. The constructor of `Game` should also
receive what type of die it is using by passing in the class, for example:

```python
Game(2, RussianRouletteDie, target_score=20)
```

the die should be instantiated at the beginning of the game and in each turn
a player has to be passed the die for them to be able to roll it.
Check out the files in the `exercise_4` folder to see what you have to
implement!


*Bonus points*: add a method for lucky throw so that we can still have a
LuckyPlayer. A `LuckyPlayer` will call `die.lucky_roll()` instead of
`die.roll()`.
