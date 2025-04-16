class DiaryEntry:

    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents
        

    def count_words(self):
        return len(self.contents.split())
    

    def reading_time(self, wpm):
        return len(self.contents.split()) / wpm

    def reading_chunk(self, wpm, minutes):
        readibletext = ""
        
        pass
