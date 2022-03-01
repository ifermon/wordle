from __init__ import *
from letter_list import Letter_List
from guess import Guess


def make_guess(words_by_letter, answer, guess, possibilities):
    '''
    Given an answer, a guess, and a starting list of possibilities 
    return a list of possibilities as a result of the information 
    gathered from this guess.
        words_by_letter: dictionary with letters as keys that holds objects
            of type Letter_Lists (provides possibilities based on letter not in word, 
            in word but wrong position or in word and right position). NOTE that 
            resulting lists are indexes into master word_list
        answer: the answer as a string
        guess: the guess as a string
        possibilities: a set of possible answers based on activity thus far, contains indicies 
            to words vs. actual words
    '''
    return_set = set(possibilities)
    match_index = 0  # 3^position + 0 for miss, 1 for wrong spot, 2 for right spot
    for i, l in enumerate(guess):
        if guess[i] == answer[i]:  # Letter is correct
            match_index += 3 ** i * 2
            return_set = return_set.intersection(
                words_by_letter[l].words_with_letter_in_position(i))
        elif l in answer:  # Letter in word but not right spot
            match_index += 3 ** i * 1
            return_set = return_set.intersection(
                words_by_letter[l].words_without_letter_in_position(i))
        else:  # letter is not in answer
            match_index += 3 ** i * 0
            return_set = return_set.intersection(
                words_by_letter[l].words_without_letter())
    # print("Guess <{}> Answer <{}> Guess Permutation <{}>".format(
    #    guess, answer, guess_score))
    return return_set, match_index  # END make_guess


start = time.time()
old_print = print


def print_ts(*args, **kwargs):
    duration = time.time() - start
    secs = "{} min {:.3f} sec: ".format(duration // 60, duration % 60)
    old_print(secs, *args, **kwargs)
    return


print = print_ts


if __name__ == "__main__":

    print("Number of words in list: {}".format(len(word_list)))

    # Generate lists of words based on letter
    words_by_letter = {}
    for l in string.ascii_lowercase:
        words_by_letter[l] = Letter_List(l)

    print("Helper lists by letter and position are built out, starting to find best first guess.")
    guesses = []
    for index, word in enumerate(word_list):
        guesses.append(Guess(index))

    # Find our first best guess
    for answer_index, answer in enumerate(word_list):
        # Loop through each word in list as an answer

        possible_answers = set(range(len(word_list)))
        for guess_index, guess in enumerate(word_list):
            if guess == answer:
                continue
            # Loop through all words as a first guess to see what kind of results we get
            result_set, match_index = make_guess(
                words_by_letter, answer, guess, possible_answers)
            guesses[guess_index].add_result(result_set)

    sorted_guesses = sorted(guesses)

    best_guess = sorted_guesses[0]
    print("Found best first guess:\n{}".format(best_guess))

    # We now have our best first guess. Use that determine the best second guess based
    # on the "results" of the first guess

    # Create a new empty list of guesses, the old stats are usless now
    guesses = []
    for index, word in enumerate(word_list):
        guesses.append(Guess(index))

    # There are 3^5 possible permutations of results from the first guess (permutation of
    # right letter right place, right letter wrong place, wrong letter)
    # Based on the answer, our first guess will result in a permutation, store the guesses for based
    # on that permutation

    populated_permuations = set()
    guess_permutation = []
    for r in range(3 ** 5):
        guess_permutation.append(copy.deepcopy(guesses))
    print("Empty list of guess permuations is built out. Size is {}.".format(
        len(guess_permutation)))

    # Find our next best guess for each situation
    for answer_index, answer in enumerate(word_list):
        # Loop through each word in list as an answer

        if answer == "bloke":
            pass
        else:
            continue

        # Make the first guess using our best guess
        possible_answers = set(range(len(word_list)))
        result_set, match_index = make_guess(
            words_by_letter, answer, best_guess.word, possible_answers)

        set_size = len(populated_permuations)
        populated_permuations.add(match_index)
        if len(populated_permuations) != set_size:
            print("Just added permutation id: {}".format(match_index))
        guesses = guess_permutation[match_index]

        possible_answers = result_set

        for guess_index, guess in enumerate(word_list):
            # Loop through all words as a first guess to see what kind of results we get
            result_set, match_index = make_guess(
                words_by_letter, answer, guess, possible_answers)
            guesses[guess_index].add_result(result_set)

    print("Finished guessing second guess, starting to sort the populated results.")
    # For each permutation sort the results to get the best ones
    for r in populated_permuations:
        guess_permutation[r] = sorted(guess_permutation[r])
        print("Best guess for permuation {} is {}".format(
            r, guess_permutation[r][0]))
