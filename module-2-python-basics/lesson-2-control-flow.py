"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [Mercado, John Andhrie M.]
Date: [09-26-2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Think of control flow like a set of instructions 
with a flowchart. It allows your code to make decisions. 
For example: If it's raining, take an umbrella; else if
 it's sunny, wear sunglasses; otherwise, just wear a jacket.

============================================
KEY VOCABULARY
============================================
- condition: A statement that evaluates to either True or False.
- if / elif / else: Decision-making keywords; if starts the check, elif (else if) checks alternative conditions, and else catches everything else. 
- comparison operator: Symbols like ==, >, <, or != used to compare two values.
- boolean expression: An expression that results in a boolean value (True or False).
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

expense = 750
budget = 500

if expense > budget:
    print("Warning: You are over budget!")
elif expense == budget:
    print("You hit your exact budget limit.")
else:
    print("You are safely within your budget.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Using a single = instead of == in a condition. 
Writing if expense = budget: throws a syntax error 
because a single equals sign is for assigning values, 
while == is used for comparing values.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
