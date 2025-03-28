# Chapter 11

## ALE 11.1: Dictionary of dictionaries

\[Insert an edited version of Kitty's ALE 11.1.\]

## ALE 11.2: Making print work

\[Insert an edited version of Kitty's ALE 11.X titled "How the heck do you print a pin?" This will help the students to understand how they can add methods to an existing class and explain the difference between \`\_\_str\_\_\` and \`\_\_expr\_\_\` through a problem-to-be-solved.\]

## ALE 11.3: More power to the constructor

\[Insert an edited version of Kitty's ALE 11.X titled the same as this ALE. Change the task: support more icons by understanding the star rating and something from the note field.\]

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

## ALE 11.5: Build your own class

\[Insert an edited version of Kitty's ALE 11.2 titled "Build your own Pin" that has the student build their own class. It would be nice if it tied into the map motif as \`Pin\` did.\]

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

\[Version 20250327\]
