"""
Create a text content analyzer. This is a tool used by writers to find statistics
such as word and sentence count on essays or articles they are writing.

Write a Python program that analyzes input from a file and compiles statistics
on it.

The program should output:

1. The total word count

2. The count of unique words

3. The number of sentences

Example output:

Total word count: 468
Unique words: 223
Sentences: 38

Brownie points will be awarded for the following extras:

1. The ability to calculate the average sentence length in words

2. The ability to find often used phrases (a phrase of 3 or more words used over 3 times)

3. A list of words used, in order of descending frequency

4. The ability to accept input from STDIN, or from a file specified on the command line.

This question should be written in Python.

Please submit a file name q1.py with your code
"""

def total_words(new_list, counts_dict):
    counts_dict["total words"] = len(new_list)
    #print(new_list, counts_dict)
    return counts_dict

def unique_words(new_list, counts_dict):
    counts_dict["unique words"] = len(set(new_list))
    #print(new_list, counts_dict)
    return counts_dict

def count_sentences(new_list, counts_dict):
    for char in "".join(new_list):
        if char in "?!.":
            counts_dict["sentences"] += 1
    #print(counts_dict)
    return counts_dict

def text_content_analyzer(file_path):
    counts_dict = dict({"total words": 0, "unique words": 0, "sentences": 0})
    new_list = list()
    with open(file_path) as txt_file:
        for line in txt_file:
            new_list += line.lower().split()
        total_words(new_list, counts_dict)
        unique_words(new_list, counts_dict)
        count_sentences(new_list, counts_dict)
        return counts_dict

#print(total_words("This is a test string".split(), {"total words": 0}))
#print(unique_words("This This is is a a test test string string".lower().split(), {"unique words": 0}))
#print(count_sentences("This. is a? test? string!".split(), {"sentences": 0}))
#print(text_content_analyzer("./test_data/hamlet.txt"))
