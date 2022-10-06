"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(actual_minutes=0):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - actual_minutes

def preparation_time_in_minutes(number_of_layers=0):
    """Preparation time in minutes.

    :param number_of_layers: int - how much layers the lasagne consists
    :return: int - returns the preparation_time_in_minutes

    Function is getting the layer number of the lasagne and multiplying it with
    the standard PREPARATION_TIME.
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Elapsed time in minutes.

    number_of_layers: int - how much layers the lasagne consists
    elapsed_bake_time: int - the total minutes of the baking process

    Function takes count of layers of lasagne and adding it to the elapsed bake time.
    """
    return elapsed_bake_time + number_of_layers * 2
    