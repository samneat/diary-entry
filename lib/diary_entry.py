import math

class DiaryEntry:
    def __init__(self, title, content):
        if title == "" or content == "":
            raise Exception("Diary entries must have title and content")
        self.title = title
        self.content = content
        self.read_so_far = 0

    def format(self):
        return f"{self.title}: {self.content}"

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot calculate reading time with wpm of 0")
        else:
            content_word_count = len(self.content.split())
            return math.ceil(content_word_count / wpm)

    def reading_chunk(self, wpm, minutes):

        words_user_can_read = wpm * minutes 
        words = self.content.split()
        if self.read_so_far >= len(words):
            self.read_so_far = 0

        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_user_can_read
        chunk_words = words[chunk_start: chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk_words)