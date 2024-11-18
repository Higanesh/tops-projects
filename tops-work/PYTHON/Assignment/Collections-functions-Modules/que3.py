"""
Que3. Differentiate between append () and extend () methods?
Ans-> 1. append() Method
    Adds a single element to the end of the list.
    If the element is an iterable (like a list), the entire iterable is added as one item (nested list or string, etc.).
    Syntax:
    list.append(element)
    Appends the entire object (even if it is a list or string) as a single element.

    2. extend() Method
    Unpacks the elements of the given iterable (like a list, tuple, or string) and adds each element individually to the original list.
    Does not create nested lists.
    Syntax:
    list.extend(iterable)
    Adds individual elements from the iterable to the list.
"""

