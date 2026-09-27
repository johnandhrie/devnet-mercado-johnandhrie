"""
Module 2 — Lesson 3: Loops & Lists
Student: [Mercado, John Andhrie M.]
Date: [09-26-2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Think of a list as a numbered shopping list
where you can store multiple items in a single container. 
A loop is like assigning a robot to go down that list and
repeat the exact same task (like checking off or printing each item) 
one by one without you having to write the code over and over again.

============================================
KEY VOCABULARY
============================================
- list: An ordered collection of items stored in a single variable.
- for loop: A loop that repeats a block of code for each item in a collection.
- while loop: A loop that keeps running over and over as long as a specific condition remains true.
- index: The numerical position of an item in a list, starting at 0
- iteration: A single execution pass through a loop.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
expenses = [120, 45, 300, 85]
total_spending = 0

for amount in expenses:
    total_spending += amount

print(f"Total expenses: {total_spending}")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Forgetting that list indices start at 0 instead of 1. Trying to access the first item using expenses[1] actually grabs the second item, which often leads to unexpected bugs or an IndexError.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
