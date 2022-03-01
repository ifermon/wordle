from __init__ import *


class Guess (object):
    """
    A guess is a specific word (it's index in the word list), and the average size of the result 
    set after a guess
    """

    def __init__(self, word_index_of_guess):
        self._guess_index = word_index_of_guess
        self._mean_result_set_size = 0
        self._sum_result_set_sizes = 0
        self._number_of_guesses = 0
        self._word_index = word_index_of_guess
        return

    @property
    def word(self):
        return word_list[self._word_index]

    @property
    def mean_result_set_size(self):
        return self._mean_result_set_size

    @property
    def number_times_guessed(self):
        return self._number_of_guesses

    def add_result(self, result_set):
        self._number_of_guesses += 1  # Increment the number of guesses
        count = len(result_set)
        self._sum_result_set_sizes += count
        self._mean_result_set_size = self._sum_result_set_sizes / self._number_of_guesses
        return

    def __repr__(self):  # Used for sorting
        return self._mean_result_set_size

    def __str__(self):
        return "Word: {}\nIndex: {}\nMean Result Set Size: {}\nNumber Times Guessed: {}".format(self.word, self._word_index, self._mean_result_set_size, self.number_times_guessed)

    def __lt__(self, obj):
        return self._mean_result_set_size < obj.mean_result_set_size

    def __gt__(self, obj):
        return self._mean_result_set_size > obj.mean_result_set_size

    def __le__(self, obj):
        return self._mean_result_set_size <= obj.mean_result_set_size

    def __ge__(self, obj):
        return self._mean_result_set_size >= obj.mean_result_set_size

    def __eq__(self, obj):
        return self._mean_result_set_size == obj.mean_result_set_size
# END CLASS Guess
