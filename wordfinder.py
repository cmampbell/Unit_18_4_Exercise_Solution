"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder():
    '''This class opens a file from a path and selects a random word from the file'''

    def __init__(self, path):
        '''Initialize the Word Finder instance, store the file path and store the list of words'''
        self.path = path
        self.words = self.get_words()

    def get_words(self):
        '''Read a text file with a line by line list of words, print the number of words read,
        and return the array of words.'''
        file = open(self.path, 'r')
        words = []

        for line in file:
            words.append(line)

        file.close()

        print(f"{len(words)} words read")
        return words
    
    def random(self):
        '''Return a random word from the list of words'''
        return ''.join(choice(self.words).split())

class SpecialWordFinder(WordFinder):
    '''This class opens a file from a path, and handles any special characters and empty lines'''

    def __init__(self, path):
        '''Initializes the Sprecial Word Finder class and cleans the list to account for special words'''
        super().__init__(path)
        self.words = self.clean_list()

    def clean_list(self):
        '''Cleans the words list of the class, removes line break characters and lines that start with #'''
        return [word.strip() for word in self.words if not word == '\n' and not word.startswith('#')]

    # wrong solution
    # def clean_list(self):
    #     '''Remove special cases from the array of words'''
    #     #removes line breaks
    #     self.words = [word for word in self.words if not word == '\n']

    #     #removes non alphabet characters
    #     clean_word_list = []
    #     for word in self.words:
    #         clean_word = []
    #         for char in word:
    #             if char.isalpha():
    #                 clean_word.append(char)
    #         clean_word_list.append(''.join(clean_word).capitalize())
        
    #     return clean_word_list

