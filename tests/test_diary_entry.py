from lib.diary_entry import *
import pytest


"""
given an empty title
count_words raises error
"""

def test_errors_on_empty_title():
    with pytest.raises(Exception) as e:
        diary_entry = DiaryEntry('', 'here is some content')
    error_message = str(e.value)
    assert error_message == "Diary entries must have title and content"

"""
given an empty content
count_words raises error
"""

def test_errors_on_empty_content():
    with pytest.raises(Exception) as e:
        diary_entry = DiaryEntry('Diary Title', '')
    error_message = str(e.value)
    assert error_message == "Diary entries must have title and content"


"""
Given a title and content 
will return a formatted entry:
"My Title: These are some contents"
"""

def test_format_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "These are some contents")
    result = diary_entry.format()
    assert result == "My Title: These are some contents"

"""
Given title and content
count_words returns number of words in whole diary entry
"""

def test_count_words_on_title_and_contents():
    diary_entry = DiaryEntry("My Title", "These are some contents")
    result = diary_entry.count_words()
    assert result == 6

"""
Given wpm of 2
Text with 2 words 
reading_time returns 1 minute
"""

def test_reading_time_with_2_wpm_and_2_words():
    diary_entry = DiaryEntry("My Title", "some content")
    result = diary_entry.reading_time(2)
    assert result == 1

"""
Given wpm of 2
Text with 4 words 
reading_time returns 2 minute
"""

def test_reading_time_with_2_wpm_and_4_words():
    diary_entry = DiaryEntry("My Title", "These are some contents")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given wpm of 2
Text with 3 words 
reading_time returns 2 minute
"""

def test_reading_time_with_2_wpm_and_3_words():
    diary_entry = DiaryEntry("My Title", "These are contents")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given wpm of 0
Text with 3 words 
reading_time returns an error
"""

def test_reading_time_with_0_wpm():
    diary_entry = DiaryEntry("My Title", "These are contents")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "Cannot calculate reading time with wpm of 0"

"""
Given a contents of 6 words
and a wpm of 2
and 1 minute
reading_chunk returns the first two words
"""

def test_reading_chunks_with_2_wpm_and_1_minute():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"

"""
Given a contents of 6 words
and a wpm of 2
and 2 minute
reading_chunk returns the first four words
"""

def test_reading_chunks_with_2_wpm_and_2_minutes():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"

"""
Given a content of 6 words
WPM of 2 and 1 minute
first time reading_chunk(2,1) returns "one two"
second time reading_chunk(1,1) returns "three"
third time reading_chunk(2,1) returns "four five"
"""

def test_reading_chunk_with_2_wpm_and_1_minute_called_thrice():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(1, 1) == "three"
    assert diary_entry.reading_chunk(2, 1) == "four five"

"""
Given a content of 6 words
if reading_chunk is called repeatedly
the last chunk is the last words in the text, even if shorter than could be read
the next chunk after that is the start again
"""

def test_reading_chunk_wraps_around_on_multiple_calls():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 2) == "five six"
    assert diary_entry.reading_chunk(2, 2) == "one two three four"

"""
Given a content of 6 words
if reading_chunk is called repeatedly with an exact ending
the last chunk is the last words in the text
the next chunk after that is the start again
"""

def test_reading_chunk_wraps_around_on_multiple_calls_with_exact_ending():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
    assert diary_entry.reading_chunk(2, 2) == "one two three four"