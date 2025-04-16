from lib.diary_entry import *
class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries
        

    def count_words(self):
        wordcounts = [entry.count_words() for entry in self.entries]
        return sum(wordcounts)

    def reading_time(self, wpm):
        wordcounts = sum([entry.count_words() for entry in self.entries])
        return wordcounts / wpm
    
        

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass
