# from lib.diary_entry import *

# def test_empty_title_or_contents_returns_wordcount_0():
#     entry = DiaryEntry("", "")
#     assert entry.count_words() == 0

# def test_add_one_entry_return_wordcount():
#     entry = DiaryEntry("Monday 14th", "Today I'm learning to intergrate classes")
#     assert entry.count_words() == 6

# def test_reading_time_when_entry_and_wpm_added():
#     entry = DiaryEntry("Monday", "This is my entry, how long will it take you to read me huh?")
#     assert entry.reading_time(7) == 2

# def test_reading_chunk_when_2_entries_added_with_wpm_and_minutes_available():
#     entry = DiaryEntry("Monday", "This is my entry, how long will it take you to read me huh?")
#     entry2 = DiaryEntry("Tuesday", "This is my second entry, how long will it take you to read me huh? I need to make this sentence a little longer just to be safe, however dont feel the need to read it all as it doesnt really make much sense, thank you if you have got to the end however.")
#     assert entry.reading_chunk(5, 4) == "This is my entry, how long will it take you to read me huh? This is my second entry, how"
