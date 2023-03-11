"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Read a file of words and create the method neccassary to pick random words from that file"""

    def __init__(self, file_path):
        """Identify the path to the file the user gives and the list of information from that file"""
        self.file_path = file_path
        self.word_list = self.read_file()

        print(f"{len(self.word_list)} words read")

    def read_file(self):
        """Open the passed in file and create a list of the words in the file after removing the \n from the end of each line. Then close the file and return the list."""
        with open(self.file_path) as f:
            self.word_file = f.readlines()
            list = [word.removesuffix("\n") for word in self.word_file]
            return list

    def random(self):
        """Using the imported "random" library pick and return a random word from the generated list of words"""
        return random.choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """In the case of spaces/comments being present in the files being read in the "WordFinder" class this class"""

    def read_file(self):
        with open(self.file_path) as f:
            self.word_file = f.readlines()
            list = [word.removesuffix("\n") for word in self.word_file
                    if word.strip() and not word.startswith("#")]
            return list
