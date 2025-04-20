# Chapter 15

## ALE 15.1: Bug hunting with repl32.py

Chapter 15 builds several Python scripts that allow you to stop and dig into the execution environment of a script that is giving you trouble or one whose operation you'd like to better understand. The script that is giving Mike trouble is `kings.py`, a card game from his childhood that he's writing. You'll use `repl32.py` to find its runtime error.

**Step 1.** We'll begin by looking at how the code in `kings.py` builds a card deck and prints the cards in it. Open the script `deck.py`, and notice that it calls the `shuffle` function from `kings.py`. Depending on how you answer its question, `deck.py` will produce either a shuffled or sorted deck.

Run `python3 deck.py` and try it with both answers.

**Step 2.** Open `kings.py` and look at the body of the `shuffle` function. It builds `deck` using a list comprehension that contains a doubly nested for-loop. `suits` and `ranks` are defined on lines 4-13 of `kings.py`.

What happens if you change the order of the items in the lists on line 9 or 13? Make a change and rerun `deck.py`.

Undo whatever changes you made to `kings.py` before moving on.

**Step 3.** Okay, let's start playing `kings.py`. Run `python3 kings.py` and answer "y" to the question that asks whether you need to see a listing of the directions to the game. Read the directions.

**Step 4.** Next, answer "n" to the question whether you want to play against an AI. When you press return, you'll see that the execution dies with a `ValueError` on line 187 in `kings.py`. You could start digging through `kings.py` trying to understand its code, or you could edit `kings.py` to add a debugging print in the function `count_points`, which starts on line 174, or you could rerun `kings.py` under the control of `repl32.py`. That's choose that last option.

**Step 5.** Run `python3 repl32.py` and answer "kings.py" when asks what scripot you'd like to instrument. Then answer "187" when it asks for a line number in the script. Recall that this is the line that produced a `ValueError`.

When you press return after typing "187", you'll see the prompts from `kings.py` because `repl32.py` edited `kings.py` and then started this edited script running.

As earlier, say no to needing directions and playing against an AI.

When given with a `repl>` prompt, look at the body of the function `count_points` decide for which variables you'd like to know their values. For example, if you want to know the value of `rank`, you'd type `rank` at the `repl>` prompt just as if it were the interactive Python interpreter.

Do you like the value of the player's hand passed as a parameter to `count_points`?

**Step 6.** The function `count_points` is called at the start of the function `winner` in `kings.py`. It makes no changes to its formal parameters before sending them off to `count_points` and so the error must in `main` that calls `winner`.

Rerun `python3 repl32.py` using the line number in `main` that calls `winner` and see if you can figure out what Mike did wrong.

## ALE 15.2: Bug hunting revisited

When you worked your way through ALE 15.1, you probably noticed that there are two `count_points` functions in `kings.py`. You used the uncommented one (lines 174-188) for ALE 15.1. Comment out that version and uncomment the one on lines 190-204 for this exercise. Make sure you're using a version of `kings.py` that still contains Mike's error.

**Step 1.** Run `python3 kings.py` and answer no to the first two questions. Despite the fact that you know there's a problem, `count_points` doesn't throw a `ValueError` as it did in ALE 15.1. Instead, it shows your hand and the top of the discard pile. But the hand doesn't look right, does it?

Type `s` (that says you want the top card of the stock pile), and the program continues to run. You can even discard a card (as long as its a valid rank).

Yuk. This is an example of a runtime bug that doesn't cause the program to exit from an exception.

**Step 2.** Think about how you would use `repl32.py` to start debugging this version of `kings.py`. What line would you tell `repl32.py` when prompted? Why would you choose that line as the place to start checking the values of the script's variables?
