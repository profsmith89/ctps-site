# Chapter 5

## ALE 5.1: Too many guesses

In this chapter, we learned how to build a guess-the-number game that ran until the player correctly guessed the secret number, but some games limit the number of guesses a player has. For example, the online game [Wordle](https://www.nytimes.com/games/wordle/index.html) permits you to make only six guesses, and if you haven't guessed the secret word within those six guesses, the game ends. Wordle's designer was inspired in part by the game Mastermind, and I own a Mini Mastermind game that also allows no more than six guesses of the hidden pattern of colored pegs.

**Step 1.** Your task in this exercise is to change `guess32.py` into a game that gives the player a maximum of six guesses. If player doesn't guess the secret number within six turns, the game should print an appropriate message and terminate.

Start your work from our existing `guess32.py` script, practicing Steps 5-8 of our problem-solving process.

```{code-block} python
---
lineno-start: 1
---
### chap05/guess32.py
import random

def main():
    print('## Welcome to GUESS THE NUMBER! ##')

    secret = random.randint(1, 100)
    # print(f'DEBUG: The secret number is {secret}')

    while True:   # our game loop
        
        # Grab a guess from the player
        while True:
            try:
                guess = int(input('Please input your guess: '))
                break
            except ValueError:
                print('Guesses must be an integer. Try again...')
        # print(f'DEBUG: You guessed {guess}')

        # Check guess against the secret
        if guess < secret:
            print('Too small!')
        elif guess == secret:
            print('Exactly! You win!')
            break
        else:
            print('Too big!')

if __name__ == '__main__':
    main()
```

**Step 2.** When you've got a working solution, take some time to compare it with the solution produced by your friends. When you're looking at each other's code, think about these questions:

1. What creative things did you do that they didn't do? Does their code include creative ideas that you didn't think about doing?
2. Did you take different approaches to limiting the number of iterations of the game loop? Of the approaches taken, notice where the comparison that ends the game loop is done. What makes its placement a good idea in each different solution?
3. In the different solutions, how easy is it to know what to change if you wanted to provide the player with 10 guesses instead of 6? If the limit is buried in the code of the script, how might you make it easier to find and be sure you made all the changes necessary?

## ALE 5.2: So many ways to pick

Our guess-the-number game used the `randint` function in [Python's `random` library](https://docs.python.org/3/library/random.html). This function is quite convenient if we want to pick a random integer in a closed range. 

**Step 1.** Using `randint`, what statement (or small number of statements) could you write to randomly choose an even integer between 2 and 100? Put your code in the next code block, and run your solution several times to make sure you did it correctly.

```{code-block} python
---
lineno-start: 1
---
# Randomly choose an even integer in the range [2, 100]
import random

# YOUR SOLUTION HERE
```

**Step 2.** The `random` library also provides a `randrange` function that allows you to specify a `step` value that is the difference between each integer in the range. Use `randrange` instead of `randint` to again randomly choose an even integer between 2 and 100.

```{code-block} python
---
lineno-start: 1
---
# Randomly choose an even integer in the range [2, 100]
import random

# YOUR SOLUTION HERE
```

**Step 3.** Moving away from integers, the `random` library also includes a function called `choice` that makes a random selection from a given sequence. Build yourself a sequence object containing 5 jokes from [icanhazdadjoke.com](http://icanhazdadjoke.com), and then use the choice function to randomly choose one of them. Run your code multiple times.

```{code-block} python
---
lineno-start: 1
---
# Randomly choose one of five bad dad jokes
import random

# YOUR SOLUTION HERE
jokes = [
    "INSERT JOKE #1",
    "INSERT JOKE #2",
    "INSERT JOKE #3",
    "INSERT JOKE #4",
    "INSERT JOKE #5",
]
```

**Step 4.** Finally, copy your solution to Step 3 into the code block below. Now read about the function `random.seed` in the `random` library, and figure out how to use it to print out *the same bad dad joke every time* the code block is run. Gain certainty about your solution by wrapping it in a loop that iterates 25 times and prints the random choice each time. Your dad would be so proud.

```{code-block} python
---
lineno-start: 1
---
# Randomly choose the SAME bad dad joke with each choice
import random

# YOUR SOLUTION HERE
```

```{tip}
You've just learned how you can seed the pseudorandom generator inside Python's `random` library to start at the same place in the pseudorandom sequence on each run. Use this you want to test your code using the same pseudorandom sequence.
```

## ALE 5.3: Catching exceptions

Our guess-the-number game used a try-except-statement to give the user another opportunity to input a guess if what they typed wasn't "a string in an integer suit," as defined by Python's `int` type conversion function.

**Step 1.** The following code block repeats that *design pattern* we used in `guess32.py`. Go ahead and run it a few times to make sure you understand how it works; feel free to insert other print statements if you want to know what executes and what doesn't under different inputs.

```{code-block} python
---
lineno-start: 1
---
while True:
    try:
        guess = int(input('Please input your guess: '))
        break
    except ValueError:
        print('Guesses must be an integer. Try again...')
print('Your input guess:', guess)
```

**Step 2.** What input-checking code would you write if we asked the user to input one of the four `suits` in a deck of playing cards? The following code block will help get you started:

```{code-block} python
---
lineno-start: 1
---
suits = ['clubs', 'diamonds', 'hearts', 'spades']

# YOUR SOLUTION HERE

print('Your input suit:', suit)
```

**Step 3.** What did you learn in Step 2 about using a try-except-statement?

## ALE 5.4: Adding metadata to your messages

The networked guess-the-number game we've developed has the server send the client a message that it simply prints. In more interesting network conversations, one endpoint wants to send some data to the other endpoint and include with these data some *information about the data*. In computer science, this information about the data is called *metadata*.

In this exercise, you are going to modify our guess-the-number game so that server sends messages that include metadata (the client messages are unchanged). The server will continue to send text that the client should print for the user, and it will add metadata indicating the color of the text when it is printed. The game will use color to add a visual hint about how good each guess was.

Here are the new rules for our guess-the-number game:

* If the absolute value of the difference between the user's guess and the secret is greater than 25, the client should print "Too small!" or "Too big!" in blue text, which will indicate that the user's guess is very cold.
* If the absolute value of the difference between the user's guess and the secret is between 1 and 5 inclusive, the client should print "Too small!" or "Too big!" in red text, which will indicate that the user's guess is very hot.
* When the user guesses the secret, the client should print "Exactly! You win!" in green text.
* In all other situations, the client should print the server's response in black text.

The messages we send between the server and the client will be split into two pieces: a header containing the metadata; and a body containing the text to be printed. The metadata indicates the color of the text in the message's body. The escape sequences should NOT be in the message's body.

Remember that our messages are just text strings, and so a message containing a header and a body is just the concatenation of two text strings. We aren't doing anything except appending a header to the front of the text string we're currently sending from the server to the client.

**Step 1.** To design the server's messages, you need to answer these questions:

1. What are all information you'll put directly (or in an encoded fashion) in the message header?
2. How will the client know where the message header ends and the message body begins? 

There are several ways to answer these questions. Debate a few ideas with your friends, and then settle on the simplest approach. This will inform how you'll encode the values you enumerated into the previous question.

**Step 2.** To code this new version of the game, you need to know how to print text in color on a terminal screen. This involves sending some text to `print` that it interprets as an escape sequence. I demonstrate how this is done in the modified client code below:

```{code-block} python
---
lineno-start: 1
---
### chap05/ale04-client.py
from socket32 import create_new_socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Color codes for terminal printing
default = '\033[0m'
black =   '\033[30m'
red =     '\033[31m'
green =   '\033[32m'
blue =    '\033[34m'

def main():
    print('## Welcome to ' + blue + 'GUESS '
         + green + 'THE ' + red + 'NUMBER'
         + default + '! ##')

    with create_new_socket() as s:
        s.connect(HOST, PORT)

        while True:
            # Grab a guess from the player
            while True:
                try:
                    guess = int(input('Please input your guess: '))
                    break
                except ValueError:
                    print('Guesses must be an integer. Try again...')

            s.sendall(str(guess))
            response = s.recv()
            print(response)

            if response == 'Exactly! You win!':
                break

if __name__ == '__main__':
    main()
```

Notice that I've named the different escape sequences with a descriptive name. To turn on the printing of text in red, you simply print the `red` escape sequence. To turn off printing text in red, you need to insert the escape sequence of a different color or use the return-to-default-color escape sequence, which I've named `default`. I've printed the capitalized name of the game in our three different colors as an example.

**Step 3.** Adapt `ale04-client.py` and `ale04-server.py` so that they play the enhanced guess-the-number game.

## ALE 5.5: Abstraction and design

You've grappled with the slippery topic of abstraction through the book's first chapters and seen numerous examples of it. Abstraction hides the details necessary for the computer to perform our intended action, but which simultaneously distract us humans from a computation's big picture. In general, we humans find it easier to think about the intended action in the abstract without all the details.

However, even after you've decided where to place an abstraction barrier (i.e., the barrier that hides a solution's details), you'll be confronted with the choice of exactly how to design the abstraction. Recall Chapter 3's example of a procedural abstraction for exponentiation where we asked if we should create separate `square` and `cube` functions, each taking a single input parameter, or a single `power` function taking two parameters. Or should we, as the Python standard library provides, create a single `power` function that takes at least two and sometimes three parameters?

In this exercise, you'll practice thinking through these sorts of choices in the context of a completely different problem. This exercise asks you to do design, not implementation. You'll think about the problem, decide on some primitives (which will define your abstraction barrier), and what the interface to those primitives might look like (i.e., what the `def` line of a function for your primitive might look like).

**A new problem.** Consider the passing of messages between two different programs, one written by you and the other written by a friend. In particular, your program needs to send a message (i.e., a line of text) to your friend's program. Don't worry about how your friend's program will receive this message; just think about the sending of this message.

Sounds simple, right? You've probably thought, "I'll just define a function called `send`." Great, here's the beginning of that function's definition:

`def send(...`

**Step 1.** The function is named but what input parameters do you want to include? What capabilities do you want this new function to support?

To answer these questions, think about sending a physical letter (yes, we know, old school). There are actually several ways to send a letter at a U.S. Post Office:

1.  The easiest approach is to prepare your letter, drop it in a mailbox, and forget about it.

2.  Alternatively, you can buy insurance against loss of or damage to your letter in transit, which pays you cash in the event of such an occurrence.

3.  As a separate consideration, you may care about how fast your letter travels to its destination, and in this case, you might also mark the letter as priority mail.

4.  Finally, you may wish to have proof that you mailed the letter when you said you did or that it was successfully delivered.

5.  Or you might want some combination of items 2-4.

Decide which of these types of features you want to support in your `send` function.

**Step 2.** Now that you know which features (if any) you want to support, you next need to think about how a user of your send functionality will express which of these features are important at each `send` call.

1.  Do you want a single function that requires a user to specify all these options, even if some are given a default value (and if so, what is each default value)?

2.  Or do you want a couple of variants of our abstract send? For example, you might create a simple `send` function that operates like dropping your letter in the mailbox and forgetting about it (possibly with or without insurance), and another `send_certified` function that provides you with a return value, which represents the proof you desire.

There is no right answer here. With a friend, talk through these two design choices and answer the following questions:

*   Within what contexts might you might prefer one design over the other?

*   What are you making easy in each approach? What are you making more difficult? 

As you discuss these questions and your personal choices, listen especially to the places where you and your friend disagree. Understanding and appreciating these differences is how you will grow as a designer.

\[Version 20250211\]
