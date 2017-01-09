"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""
# 10 failures at beginning

def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """
    # a new list is what we want, so an empty list will store the new data
    odd_numbers_list = []
    for number in numbers:
        # the following equation says if a number divisible by two doesn't equal
        # 0 then it can go on the odd number list
        if int(number) %2 != 0:
            odd_numbers_list.append(number)
    return odd_numbers_list


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo
    
    """
    # enumerate makes this work without using a counter by putting the actual
    # index location. For the index location to print correctly it seems to 
    # require being seen as a string with str()
    for index, item in enumerate(items):
        print str(index) + " " + item


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']
        
    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """
    # using an empty list I've stored the foods that match from the two lists
    foods_that_are_the_same = []
    # this code loops through each food argument and finds the ones that == 
    for food1 in foods1:
        for food2 in foods2:
            if food1 == food2:
                foods_that_are_the_same.append(food2)
    # to put them in alphabetical order sorted() was used in the following code
    return sorted(foods_that_are_the_same)


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """
    for item in items:
        # returning each item in items from index 0 onward, skipping every other
        # 2 as the last number after the two colons means every other number is skipped
        return items[0::2]


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """
    # sorting the items list into decending order
    items_sorted = sorted(items, key=int, reverse=True)
    # taking the first of the items in decending order (aka the largest number onward)
    # through the rest of the integers that I want to get out. The number of 
    # integers I want from the decending list is from the argument n. Making n
    # into an integer makes it so we can just use n itself to pull the correct
    # number of integers out of the decending list
    number_of_items_from_n = items_sorted[0:int(n)]
    # putting the list back in ascending order
    n_items_in_ascending_order = sorted(number_of_items_from_n, key=int)
    return n_items_in_ascending_order




#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
