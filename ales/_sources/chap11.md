# Chapter 11

## ALE 11.1: Dictionary of Dictionaries

The `class Pin` described in Chapter 11 defines a data structure for a Google Maps-like pin. With instances of this data type, we were able to mark Cosmo's favorite places.

A `Pin` object records:

*   a location (i.e., an x-y tuple of integers)
*   a name for the location (i.e., a string)
*   a short note about the location (i.e., a string)
*   a rating in stars (i.e., an integer)
*   an icon for the map (i.e., a string emoji), which was computed in the class's constructor code.

In this exercise, we'll use a dictionary instead of a class as the structure for a `Pin`. We'll see that this approach isn't as good as using a class, but it does permit the use of descriptive strings to access the components of a dictionary-based `Pin` similar to the way we used descriptive data attributes in the chapter's `Pin` class. Let's see how this dictionary-based approach works out.

Please complete the following steps in the script `chap11/ale01.py`.

**Step 1.** Look at the start of the function `make_3_pins` in `ale01.py`, which builds three pins using the Python dictionary data type and duplicates the data attribute values on lines 58-60 of `pin.py`.

> Insert a few Python statements at the end of the `make_3_pins` function body so that this function prints just the names of the three pins (i.e., you should print the value of the `name` key). Print the names of the different pins on separate lines.

Test your solution by running `python3 ale01.py 1`.

**Step 2.** As you undoubtedly noticed, it's not a great design to choose a name for each pin. If we were to add a new pin, we'd have to change the code in the function `make_3_pins` to both define **and print** this new pin using its unique name. Many of the tasks we might want to do (beyond printing) would benefit from a data structure that contained our collection of all pins. The script `pin.py` used a Python list for this purpose. Let's do something different here.

Let's store our individual pins in a dictionary, which would create a _dictionary of dictionaries_. We've seen this type of data structure back in Chapter 4, where the JSON file format returned by web requests involved lots of dictionaries nested inside other dictionaries. 

As you start to consider this work, you'll realize that you have to choose a key for each dictionary that you store in the returned dictionary. What kind of unique identifier should we use for the keys in this "outer" dictionary?

Arguably, two pins could have the same name. They could also include the same note. Obviously, there are few possible star ratings and many possible pins. None of these seems like good candidates.

Here are two reasonable but imperfect choices:

1.  We might use a pin's location as its key in the outer dictionary. If we restrict each (x,y) location in our map so that it can take only one pin, this approach would work nicely.

2.  We might alternatively use strings like "pin1" and "pin2" and so forth. By taking the `len` of this outer dictionary, we would know the next key string to generate when we wanted to add a new pin. Unfortunately, this scheme starts to fall apart when we delete keys from the dictionary. Do you see why?

Let's go with the first choice.

> Add a return statement to the end of `make_3_pins` that returns this dictionary of dictionaries. You'll notice that the call to `make_3_pins` in `main` under `** STEP 2**` sets the name `pins` to the value returned from `make_3_pins`.

Test your solution by running `python3 ale01.py 2`.

**Step 3.** Insert a print-statement that prints the `name` of the pin at location `(3,11)`. This statement goes in `main` where it says `INSERT STEP 3 SOLUTION CODE HERE`. The name `pin1` is undefined in `main`, and you must start with the name `pins`.

Test your solution by running `python3 ale01.py 3`.

**Step 4.** Insert a loop that prints the locations, names, and ratings of all of the pins in `pins`. You might have it say something interesting for each pin like, "Cosmo rated Cat at (5,3) with 1 star(s)."

Test your solution by running `python3 ale01.py 4`.

**Step 5.** Read about [looping through the items in a Python dictionary using the method `items`](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques) and rewrite your solution to Step 4 (where it says `INSERT STEP 5 SOLUTION CODE HERE`).

Test your solution by running `python3 ale01.py 5`.

**Step 6.** On his most recent walk, Cosmo found a bakery at (9,1) that gives out dog treats for free, and rated it 5 stars. Write a line of code that adds this place to `pins`. Do NOT set the key `'loc'` in this new inner dictionary.

Test your solution by running `python ale01.py 6`, which will use the printing loop from step 5 to show you how you did.

**Step 7.** So far, this seems like a good solution. Why did we have to learn all this crazy syntax for Python classes?

Well, the `class Pin` in `pin.py` also defines an instance variable named `icon` that is computed in the `Pin.__init__` method. How would you add this key to each of your inner dictionaries? You'd write a function, which we'll call `set_pin_icon`.

> Insert a function body for `set_pin_icon`, which you'll find between the definition of `make_3_pins` and `main` in `ale01.py`. This function takes one formal parameter, which is a pin to analyze and adds a key called `icon` to it. The value of this key should be `green_heart` if stars is less than or equal to 3 and `red_x` otherwise.

Test your solution by running `python3 ale01.py 7`.

> Notice how we've just made the code for constructing a valid pin (i.e., one that adheres to the representation invariant for pins) in multiple places in `ale01.py`. This is a maintenance nightmare and one of the primary reasons that many programmers swear by object-oriented techniques and the resulting encapsulation features.

## ALE 11.2: Build your own

\[Insert a problem that requires the design of a simple class.\]

## ALE 11.3: Is it better?

Recall that the `class Pin` in `pin.py` is a subclass of the Python `object` class. Let's understand better what that means and how we can do some subclassing and defining of magic methods.

**Step 1.** Open the script `ale03.py` and review the a list of pins created at the start of `main`. The pins in the `pins` list are of type `Pin`.

As we're walking Cosmo around our city, we might want to know whether two pins are equivalent (in some fashion) or if one is better than another. Run `ale03.py` in the following fashion:

`python3 ale03.py 1`

This runs the code under the comment `STEP 1`. From the printout, you'll that the first and fourth pins are not considered equal, but a pin is equal to itself. OK, this probably makes some sense to you.

**Step 2.** What does the Python interpreter think when we ask whether the first pin is greater than (`>`) the second? Run `python3 ale03.py 2`.

Oh no, we got a `TypeError`. The interpreter doesn't know how to compare two pins in this manner.

This is because we haven't built functionality in our `Pin` class to handle comparisons using `>`. Of course, we didn't build the equality functionality either (look at the definition of `class Pin` in `pin.py`), but Python's `object` class defined some kind of equality test.

**Step 3.** We can, however, implement the `>` operator by defining the magic method `__gt__` in our class. Let's do this in a subclass or `Pin` so that we don't mess up the nicely working `Pin` class.

At the top of `ale03.py`, you'll find a definition for the new `class Pin2` that derives from the `class Pin` (i.e., because `Pin` is in the parentheses on line 5 of `ale03.py`). The constructor for this class is a bit tricky as it is implemented using default parameters to allow you to create a pin by specifying either:

*  all its required data attributes (and in this case it simply calls the `Pin` constructor); or
*  a `Pin` object whose data attributes it copies.

After the Step 2 code in `main`, you'll see both these methods used to create a bunch `Pin2` objects that are copies of the original `Pin` objects.

Run `python3 ale03.py 3` to see that these constructor calls worked correctly.

**Step 4.** In the definition of `class Pin2`, you'll see that I defined the magic method `__gt__` that checks to see if the current object's `stars` rating is greater than the pin that was passed as the `pin` paramter. The current object is to the left-hand side of a `>` sign and the passed parameter to the right-hand side.

Run `python3 ale03.py 4` to see this magic method work. No more `TypeError`!

**Step 5.** Your last task in this exercise is to override the `__eq__` magic method in the Python `object` class with the implementation we want for the `==` operator in the `Pin2` class. Specifically, we want `==` to return `True` when a pin's `stars` rating is equal to another pin's `stars` rating and `False` otherwise.

See if you can write a method definition for `__eq__` in `class Pin2`, and test it by running `python3 ale03.py 5`. HINT: The printout should NOT say false and false.

## ALE 11.4: See the path

The driving-directions script built in Chapter 11 prints only the turn-by-turn directions that gets you from the start to the goal locations. Today's mapping applications provide both this and the path marked on a map. Your task is to mark the turn-by-turn driving directions on the searched map and print it.

**Step 1.** We'll start with the chapter's depth-first solution. Copy `directions-dfs.py` and name this copy `ale04.py`. Edit line 1 to change `directions-dfs.py` to `ale04.py`.

**Step 2.** We're going to make our changes inside the function `search`, since that's where the current turn-by-turn driving directions are printed out. Find where those directions are printed and make sure you understand them.

**Step 3.** We'll leave the code that produces the `ddirections` list of `TreeNote`s alone (lines 55-60) and start adding code around and inside the printing of the solution (lines 62-68). We'll reuse `my_map`, which `search` used to find the solution, and place `EXPLORED` marks on the map to indicate the solution route. The following pseudocode describes all the work we need to occur to mark up `my_map`:

```{code-block} python
---
lineno-start: 61
---
### chap11/ale04.py
    # Reset the map so we can plot the driving directions

    # Mark the start location as EXPLORED

    # Print out the driving directions and map them
    # ... HINT: the existing code goes here

    # Re-mark the start and goal locations and then print
```

You'll need to use the following attributes of a `Maze` object (i.e., `my_map`) to create the code that implements these pseudocode steps: `start`, `goal`, `reset`, `mark`, `move`, and `print`. Look at how we've used these attributes elsewhere in the `search` function and read through their docstrings in `maze.py`.

**Step 4.** When you've completed Step 3 and have your script printing the step-by-step driving directions and a map with the route marked, it's time to try a new map. In the `main` function of `ale04.py`, duplicate the line that reads:

```{code-block} python
    my_map = maze.Maze(maze.MAZE_map, maze.MAZE_map_endpts)
```

Comment out the original line and then change the duplicate into the following:

```{code-block} python
    my_map = maze.Maze(maze.MAZE_map_ale04, maze.MAZE_map_ale04_endpts)
```

Run your script and take a look at the solution. Do you like the route it found? If not, how might you change your script to have it find and print a more direct route from start to goal?

## ALE 11.5: TBW

\[Placeholder for a new problem.\]

## ALE 11.6: An informed search

The depth-first and breadth-first approaches presented in Chapter 11 work for any goal-directed search problem. Because they are agnostic to the specifics of your problem, they are called _uninformed_ searches. It's possible to build an _informed_ search, as mentioned briefly in the chapter's last section, by incorporating problem-specific information into the search algorithm.

This exercise introduces you to a popular informed search, called _A* search_, and the use of _heuristic functions_. A heuristic function knows something about the particular problem you're tackling, and thus the crafting of a heuristic makes your script better for certain goal-directed search problems and not useful for others.

The purpose of a heuristic is to help your algorithm choose among the nodes in your frontier list, and if it is good heuristic, it will suggest nodes that will help the algorithm move more quickly to the goal.

> Example: When computing a set of driving directions, you might 
want your search algorithm to give priority to nodes on the frontier list that have the smallest, as-the-crow-flies distance between the current point and the goal.

This example describes a heuristic. It encourages the search algorithm to move in the direction of the goal, rather than in any random direction, which is often a reasonable thing to do. But this encouragement might not always produce the best driving directions (e.g., it might have you turn into a cul-de-sac).

In effect, heuristics compute a simpler version of your problem. By simpler, I mean that we've eliminated some of the problem's constraints. Computing the as-the-crow-flies distance removes the constraint that we have to drive on a road.

**Step 1.** A popular informed algorithm is the A* pathfinding algorithm, which was formally described by Peter Hart, Nils Nilsson, and Bertram Raphael of the Stanford Research Institute in 1968. Their goal was to build a robot that could find its own way in our world of obstacles and do so expending as little wasted movement as possible.

To gain a general understanding of how A* pathfinding works in a driving directions context, please watch the first 6 minutes of [this 12-minute video by Sebastian Lague](https://www.youtube.com/watch?v=-L-WgKMFuhE). Pay particular attention to G, H, and F costs computed for each node. Notice that G is a known cost (i.e., it is exactly the minimal cost of moving from start to the current location) and H is a heuristic cost (i.e., it is the minimal cost of moving from the current location to the goal while paying no attention to the obstacles on the map---an as-the-crow-flies distance computation).

**Step 2.** The programming problem set that goes with this chapter has you find a connection between two actors by searching for a string of actors. The constraint on the string is that adjacent actors must have starred together in a movie. Our example heuristic for driving directions makes no sense for this new problem because physical distance has no meaning when we want to link actors through their movies.

What facts about movies and actors might help you discover an appropriate heuristic? When considering which actor on the frontier to choose next, these facts should help move you in the "right direction" and make you feel like you're eliminating those who are unlikely co-stars of your goal actor. Write down a few sentences describing this heuristic and why it might work well.

You've begun designing heuristics!

## ALE 11.7: Classes in OO programming

Object-oriented (OO) programming is complicated because it is meant to be flexible enough to create data structures that reflect the complexity of the world around us.

**Step 1.** I want you to read an online tutorial that doesn't necessarily use OO programming to solve a particular problem (as we repeatedly do in this book) but instead focuses on the syntax for building a class. My hope is that the problem-solving foundation provided in Chapter 11 gives you a context in which to appreciate the simple, syntax-driven examples in tradtional OO tutorials.

There are many good tutorials out there. It doesn't matter which you read, but I recommend ["Object-Oriented Programming (OOP) in Python 3" on RealPython by David Amos (December 15, 2024)](https://realpython.com/python3-object-oriented-programming/).

Feel free to skim and then dig in where you find something interesting. My goal in this reading isn't to make you an expert in OO programming but to increase your comfort with it and its terminology.

**Step 2.** David Amos's tutorial defines a class with which we can create objects of type `Dog`. I've copied his `class Dog` below.

```{code-block} python
---
lineno-start: 1
---
### dog.py from David Amos's RealPython tutorial
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
```

Using this class definition, David Amos defines several _child_ classes, which derive from the parent class `Dog`. I, of course, added my own (i.e., `YellowLab`).

```{code-block} python
---
lineno-start: 15
---
### also in David Amos's RealPython tutorial
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

# Mike's addition
class YellowLab(Dog):
    pass
```

What will be printed if you define the classes above and then run the following statements?

```{code-block} python
---
lineno-start: 29
---
cosmo = YellowLab("Cosmo", 13)

for attribute in dir(cosmo):
    if attribute[0] != '_':
        print(attribute)
```

You should now have a better idea of what it means when a child class inherits attributes and methods of its parent class.

## ALE 11.8: The Monty Hall problem

This classic brain teaser is often used to illustrate the vexing nature of conditional probabilities and the power of Bayes's theorem. Here's [the problem as asked by Craig F. Whitaker to Marilyn vos Savant through a letter originally published in a 1990 issue of PARADE magazine](https://web.archive.org/web/20130121183432/http://marilynvossavant.com/game-show-problem/):

> Suppose you’re on a game show, and you’re given the choice of three doors. Behind one door is a car, behind the others, goats. You pick a door, say #1, and the host, who knows what’s behind the doors, opens another door, say #3, which has a goat. He says to you, "Do you want to pick door #2?" Is it to your advantage to switch your choice of doors?

**Step 1.** Take a moment and decide whether you'd stay with door #1 or switch to door #2. Sketch out the logic of your decision.

**Step 2.** My first reaction, like many people's, is to focus on the two remaining doors and the fact that behind one of them is the car. Two doors, one car and one goat, 50-50 chance to pick the door hiding the car, right? I might as well stay with my original pick: door #1.

Unfortunately, that's the probabilistically poor choice. As we'll understand through the next two steps, we should change our choice as the other unopened door will hide the car twice as often. Step 3 will get you to focus on the important part of the problem, and then in Step 4, you'll write a simulation that estimates the probabilities.

**Step 3.** I found it surprisingly hard to write this simulation. It's not hard to get it to generate thousands of trials of this problem, which is code I'll give you. What's hard is understanding what you should do with each of the randomly generated trials, and so first, I'll attempt to cement in your mind what matters in this problem. In particular, it isn't what I focused on as I described my initial reaction in Step 2. What you should focus on is the work the host does, which is lightly touched in the original problem statement.

Consider this restatement of the problem:

> Suppose you're on a game show, and Monty Hall, the host, gives you the choice of three doors. He tells you that behind one door is a car, behind the others, goats. The car and the goats have been randomly placed behind these doors. You (again) pick door #1.
>
> Hall clears his throat and says, "Excuse me while I peek behind door #3. If there's a goat there, I'll show it to you. But if the car is there, I'll show you what's behind door #2, which I'll know must be a goat if the car is behind door #3. By following this simple algorithm and gaining a bit of insider information, I'll always show you a goat, right?" After thinking about it, you nod.
>
> With your attention now squarely on what Hall is going to do, he grabs your shoulder, looks you in the eye, and asks, "What was the probability of a car being behind door #1 when you chose one of three doors? Will the work I do to find a goat to show you change the probability of the car being behind door #1?" You pause and think, and then you shake your head no.
>
> Hall turns and opens door #3, which has a goat. He says to you, "Do you want to pick door #2?"

**Step 4.** The restatement in the prior step provides you with what you need to know to write a script that simulates many trials of the Monty Hall problem. In `ale08.py`, I've started writing the script for you. You need to replace line 28 with your code that performs Monty Hall's algorithm and updates the variable `wins`. When you've done it correctly, door #1 will win (i.e., hide the car) about one-third of the time.

\[Version 20250626\]
