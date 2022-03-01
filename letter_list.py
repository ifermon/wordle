
class Letter_List (object):
    def find_words_with_letter(self):
        return_set = set()
        for i, w in enumerate(word_list):
            if self._letter in w:
                return_set.add(i)
        return return_set

    def find_words_without_letter(self):
        return_set = set()
        for i, w in enumerate(word_list):
            if self._letter not in w:
                return_set.add(i)
        return return_set

    def build_letter_positions_in_words(self):
        for w in self.words_with_letter():
            for i, l in enumerate(word_list[w]):
                if l == self._letter:
                    self._words_with_letter_in_position[i].add(w)
                else:
                    self._words_without_letter_in_position[i].add(w)

    def __init__(self, letter):
        self._letter = letter
        self._words_with_letter = self.find_words_with_letter()
        self._words_without_letter = self.find_words_without_letter()
        self._words_with_letter_in_position = [
            set(), set(), set(), set(), set()]
        self._words_without_letter_in_position = [
            set(), set(), set(), set(), set()]
        self.build_letter_positions_in_words()
        return

    def words_with_letter(self):
        return self._words_with_letter

    def words_without_letter(self):
        return self._words_without_letter

    def words_with_letter_in_position(self, position):
        return self._words_with_letter_in_position[position]

    def words_without_letter_in_position(self, position):
        return self._words_without_letter_in_position[position]
# END CLASS Letter_List
