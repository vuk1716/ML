# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient
from collections import deque

# Function to read a list of English words from a file
def read_words_from_file(file_name):
    with open(file_name, 'r') as file:
        words = file.read().splitlines()
    return words

# Function to find the shortest chain of words using BFS
def find_shortest_word_chain(words, start_word, end_word):
    if len(start_word) < 3 or len(end_word) < 3:
        return None

    queue = deque()
    queue.append([start_word])

    while queue:
        current_chain = queue.popleft()
        last_word = current_chain[-1]
        #print()

        if last_word == end_word:
            return current_chain

        for word in list(words):
            if len(word) >= 3 and last_word[-2:] == word[:2] and word not in current_chain:
                new_chain = current_chain.copy()
                new_chain.append(word)
                queue.append(new_chain)

    return None

# Main program
if __name__ == '__main__':
    words = read_words_from_file('wordsEn.txt')
    #print(words)
    start_word = input("Enter the first word (at least 3 letters): ")
    end_word = input("Enter the second word (at least 3 letters): ")

    shortest_chain = find_shortest_word_chain(words, start_word, end_word)

    if shortest_chain:
        print("Shortest chain found:", ' -> '.join(shortest_chain))
    else:
        print("No valid chain found.")
