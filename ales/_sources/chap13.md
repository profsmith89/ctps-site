# Chapter 13

## ALE 13.1: A promise fulfilled

In Chapter 10, we built a book index that used a function called `get_wordlist` to turn a string into a list of words, and I promised to explain how this function worked. Since it uses the `re` library, we're now ready to understand how to turn a line like `'And Mrs. Smith said, "I\'m the best!"'` into the wordlist `['And', 'Mrs', 'Smith', 'said', "I'm", 'the', 'best']`. This task is not easy. Take a moment to consider how you'd mechanically remove apostrophes and dashes except when they're part of a contraction or a hyphenated word. As you can see below, `get_wordlist` accomplishes this challenge in very few statements. This is the power of the `re` library.

```{code-block} python
---
lineno-start: 16
---
### chap10/index32.py
import re
import string

def get_wordlist(line):
    line = line.replace('--', ' ')
    return [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w)
            for w in line.split()]
```

**Step 1.** We begin by dispensing with line 21, which catches a case (the use of an en-dash) not handled by the RE expression in line 22. Make sure you should understand its operation, and if not, review our earlier work with `str.replace`.

**Step 2.** Line 22, which continues on line 23, is where the interesting stuff happens. To understand this statement, first recognize that the outermost square brackets define a *Python list comprehension*, which is a shorthand for creating a new list from the values in an existing list. The "existing list" comes from a straightforward `str.split` of the input line, which removes whitespace but leaves "words" like `'best!"'`, which you'll see if you run the next code block.

```{code-block} python
---
lineno-start: 1
---
line = 'And Mrs. Smith said, "I\'m the best!"'
[w.lower() for w in line.split()]
```

Run code block above in the interactive Python interpreter. Just for fun, change the expression `w.lower()` to append your favorite color to the end of each `w`.

**Step 3.** In `get_wordlist`, each `w` isn't lowered, but fed to another function in the `re` library. The `re.sub` function uses the RE (its first parameter) to identify substrings of the input string (its third parameter) and then replaces these identified substrings with a replacement string (its second parameter). Here's a simple example of `re.sub` in action:

```{code-block} python
---
lineno-start: 1
---
[re.sub(r'[a-zA-Z]+', 'WORD', w) for w in line.split()]
```

Run this code block in the interactive Python interpreter. Then play with the RE given as the first parameter and the string literal used in the substitution.

**Step 4.** All we have left to understand is the RE in `get_wordlist`, but even this is complicated because it uses a method on strings to reduce what we have to write in the RE string! Let's replace the `{0}` syntax and the `str.format` method with a familiar character set so that we can focus on the two new RE metacharacters: `^` and `|`.

* \^ : This metacharacter is like `$`, but it matches *the point at the start of the string*.
* \| : This metacharacter represents *a logical OR*. If the pattern before the vertical bar matches, the pattern after it isn't tested. If the first doesn't match, the second is tried.

```{code-block} python
---
lineno-start: 1
---
[re.sub(r'^[a-zA-Z]+|[a-zA-Z]+$', 'WORD', w) for w in line.split()]
```

Run this line of Python and look carefully at the result. The only difference between this and the previous list comprehension is the fifth element in the returned lists. The previous code block produced `'"WORD\'WORD'` while this one produced `'"I\'WORD'`, and in both cases the input `w` was `'"I\'m'`. The `'I'` remains in the second case because neither of the two REs, before or after the vertical bar (`|`), matches this letter; it isn't a word at the start of the string `w` (the double-quote character starts the string) nor at its end (obviously).

If you don't see this (and it isn't easy to see), work through the logic of the RE above with a friend.

**Step 5.** But replacing words is not what we want to do in `get_wordlist`. This function is supposed to delete punctuation that isn't the apostrophe in a contraction or the hyphen in a hyphenated word. And this is where the `str.format` method and the `{0}` syntax comes in. While messy, this is just another way to write a formatted string literal in Python, which we've repeatedly done by placing an `f` character before our string literals. The following are equivalent:

```{code-block} python
---
lineno-start: 1
---
num = 42
print(f'answer = {num}')
print('answer = {0}'.format(num))
```

As you can see by running this code block, we're just replacing every `{0}` in the string with the first parameter to `format`. The parameter we use in `get_wordlist` is `string.punctuation`, which the `string` library nicely defines as a string containing every punctuation symbol. 

* Take a moment to import the `string` module, print `string.punctuation`, and then consider which of these symbols you'd have to escape to put them in the RE. Thank goodness for formatted strings.
* Now think about what our RE would look like if we replace both instances of `{0}` with the value of `string.punctuation`. Yes, the RE would be even harder to read!

With the details explained, I'll say in English what this complicated statement does: It replaces sequences of one or more punctuation characters at the start or end of a "word," as produced by `str.split`, with an empty string. That's it. I hope you now appreciate the incredible power of the `re` library.

**Step 6.** Feed your own test strings to `get_wordlist`, by changing the definition of `line` in the following code block. There are still a few English grammatical structures that `get_wordlist` doesn't handle. Can you discover them?

```{code-block} python
---
lineno-start: 1
---
line = 'And Mrs. Smith said, "I\'m the best!"'
get_wordlist(line)
```

\[Version 20241204\]
