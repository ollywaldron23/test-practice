# from lib.diary import *
# from lib.diary_entry import *

# def test_adding_two_diary_entries_then_listing_them():
#     mydiary = Diary()
#     entry1 = DiaryEntry("Monday", "Today I spent more time coding.")
#     entry2 = DiaryEntry("Tuesday", "Today I took my dog for a walk")
#     mydiary.add(entry1)
#     mydiary.add(entry2)
#     assert mydiary.all() == [entry1, entry2]

# def test_adding_two_entries_calling_count_words_returns_sum_of_word_count():
#     mydiary = Diary()
#     entry1 = DiaryEntry("Monday", "Today I spent more time coding.")
#     entry2 = DiaryEntry("Tuesday", "Today I took my dog for a walk")
#     mydiary.add(entry1)
#     mydiary.add(entry2)
#     assert mydiary.count_words() == 14

# def test_adding_entries_returning_reading_time_based_on_wpm():
#     mydiary = Diary()
#     entry1 = DiaryEntry("Monday", "Today I have spent more time coding than last week.")
#     entry2 = DiaryEntry("Tuesday", "Today I took my dog for a walk at park")
#     mydiary.add(entry1)
#     mydiary.add(entry2)
#     assert mydiary.reading_time(5) == 4