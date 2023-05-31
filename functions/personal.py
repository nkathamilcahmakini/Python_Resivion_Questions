#1.Python program that takes a list of integers as input and 
#outputs the list with all the duplicate values removed.	

#2.Python program that uses a while loop to print the numbers from 1 to 10.	

#3.Python program that takes a list of integers as input and outputs the largest and smallest numbers in the list.	

#4.Display Fibonacci series up to 10 terms	"Expected output:

#5.Find the factorial of a given number(The factorial (symbol: !) means
#to multiply all whole numbers from the chosen number down to 1.)	

#6.Calculate the cube of all numbers from 1 to a given number	"Given:

#7.Python program that takes a list of numbers as input and outputs "even"
#if the number is even and ""odd"" if the number is odd using if-else statements.

#8.Python program that takes a list of numbers as input and outputs the sum of all 
#the even numbers and the product of all the odd numbers using the if-else statement.	

#9.Python program that accepts a string and calculates the number of digits and letters.	

#10.Python program that takes a list of integers as input and outputs the sum of
#all the even numbers in the list until it reaches a number that is not divisible by 2.

#11.Python program that takes a list of integers as input and 
#outputs the product of all the odd numbers in the list.	

#12.Python program that takes a string as input and 
# outputs the string in reverse order.

#13.Python program that takes a list of strings as 
# input and outputs the longest string in the list.

#14.Python program that takes a string as input and 
# outputs the number of vowels in the string.

#15.Python program that takes a list of integers as 
# input and outputs the list with all the odd numbers doubled.

#16.Python program that takes a list of strings as input 
# and outputs the list with all the strings in uppercase.

#17.Python program that takes a list of strings as input 
# and outputs the longest string in the list.

# def find_common_elements(list1, list2):
#     return list(set(list1).intersection(list2))
# def find_common_elements(list1, list2):
#     return list(set(list1).intersection(list2))

# # Example usage
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 5, 7, 9]
# common_elements = find_common_elements(list1, list2)
# print(common_elements)

# This code defines a function called find_common_elements that takes two lists as input . 
# It converts the two lists to sets and calculates their intersection using the intersection method. 
# The resulting set is converted back to a list and returned.

# In the example usage, list1 and list2 are defined and passed to the find_common_elements function.
# The resulting common elements are stored in common_elements and printed to the console.

#18.Python program that takes a list of integers as input and outputs the sum of 
# all the numbers until it reaches a negative number. Ignore the negative number in the sum.

# 19.Python program that takes a list of integers as input and outputs the list 
# with all the even numbers removed using a while loop.

#19.Python program that takes a list of integers as input and outputs 
# the list with all the numbers up to but not including the first negative number.

#20.Python program that takes a list of integers as input and outputs the list 
# with all the even numbers doubled and all the odd numbers tripled.	

#21.Given two lists, write a function to find the common elements between them and return
#them in a new list.
def find_common_elements(list1,list2):
    return list(set(list1).intersection(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9]
common_elements = find_common_elements(list1, list2)
print(common_elements)

#Write a function that take a list of words and sorts them on the 
#number of vowels in each word
def sort_words_by_vowel_count(words):
    def count_vowels(word):
        return sum(1 for letter in word if letter.lower() in 'aeiou')

    return sorted(words, key=count_vowels)

words = ["apple", "banana", "orange", "pear", "grapefruit"]
sorted_words = sort_words_by_vowel_count(words)
print(sorted_words)

def sort_words_by_vowels(words):
    # """
    # Sorts a list of words based on the number of vowels in each word.
    # """
    vowels = set('aeiouAEIOU')  # create a set of vowels
    return sorted(words, key=lambda word: sum(1 for c in word if c in vowels))

words = ['cat', 'dog', 'bird', 'elephant', 'iguana']
sorted_words = sort_words_by_vowels(words)
print(sorted_words)  # ['cat', 'dog', 'bird', 'iguana', 'elephant']



# Python program that takes a list of strings as input and outputs the list with all the strings that contain the letter "a"	"Input: [""hello"", ""world"", ""python"", ""data"", ""science""]
# Expected Output: [""data"", ""science""]

# strings = [""hello"", ""world"", ""python"", ""data"", ""science""]
# filtered_strings = []
# for string in strings:
#     if ""a"" in string:
#         filtered_strings.append(string)
# print(filtered_strings)"
# Python program that takes a list of integers as input and outputs the list with all the duplicate numbers removed.	"Input: [1, 2, 3, 1, 4, 2, 5, 3]
# Expected Output: [1, 2, 3, 4, 5]

# numbers = [1, 2, 3, 1, 4, 2, 5, 3]
# unique_numbers = []
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)
# print(unique_numbers)"
# Python program that takes a list of numbers as input and outputs the list with all the prime numbers removed.	"Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [1, 4, 6, 8, 9, 10]

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# non_primes = []
# for num in numbers:
#     if not is_prime(num):
#         non_primes.append(num)
# print(non_primes)"
# Python program that takes a list of numbers as input and outputs the sum of all the numbers that are divisible by 3 or 5.	"Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: 33

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = 0
# for num in numbers:
#     if num % 3 == 0 or num % 5 == 0:
#         total += num
# print(total)"
# Python program that takes a list of strings as input and outputs a list of the lengths of those strings using list comprehension.	"Input: [""hello"", ""world"", ""python"", ""data"", ""science""]
# Expected Output: [5, 5, 6, 4, 7]

# strings = [""hello"", ""world"", ""python"", ""data"", ""science""]
# lengths = [len(string) for string in strings]
# print(lengths)"
# Python program that takes a list of numbers as input and outputs a list of the squares of those numbers using list comprehension.	"Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]

# numbers = [1, 2, 3, 4, 5]
# squares = [num ** 2 for num in numbers]
# print(squares)"
# Python program that takes a list of numbers as input and outputs a list of only the even numbers in that list using list comprehension.	"Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [2, 4, 6, 8, 10]

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)"
# Python program that takes a list of numbers as input and outputs a list of only the numbers that are greater than the average of all the numbers using list comprehension.	"Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [6, 7, 8, 9, 10]

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# average = sum(numbers) / len(numbers)
# greater_than_average = [num for num in numbers if num > average]
# print(greater_than_average)"
# Python program that takes a list of strings as input and outputs a list of those strings that are palindromes using list comprehension.	"Input: [""hello"", ""world"", ""racecar"", ""python"", ""level""]
# Expected Output: [""racecar"", ""level""]

# strings = [""hello"", ""world"", ""racecar"", ""python"", ""level""]
# palindromes = [string for string in strings if string == string[::-1]]
# print(palindromes)"
# Python program that takes a list of strings as input and outputs the length of the longest string using a while loop.	"Input: [""hello"", ""world"", ""python"", ""data"", ""science""]
# Expected Output: 6

# strings = [""hello"", ""world"", ""python"", ""data"", ""science""]
# i = 0
# longest_length = 0
# while i < len(strings):
#     if len(strings[i]) > longest_length:
#         longest_length = len(strings[i])
#     i += 1
# print(longest_length)"
# Python program that takes a string as input and outputs the number of vowels in the string using a while loop.	"Input: ""Hello, World!""
# Expected Output: 3

# string = ""Hello, World!""
# vowels = ""aeiouAEIOU""
# count = 0
# i = 0
# while i < len(string):
#     if string[i] in vowels:
#         count += 1
#     i += 1
# print(count)"
# "Python program to print all the even numbers from 0 to 20, except 10, using the continue statement.
# "	"Expected Output: 0, 2, 4, 6, 8, 12, 14, 16, 18, 20

# for num in range(21):
#     if num == 10:
#         continue
#     if num % 2 == 0:
#         print(num)"
# Python program that takes a list of numbers as input and outputs the sum of all the numbers that are not divisible by 3 using the continue statement.	"Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: 30

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_of_non_divisible_by_3 = 0
# for num in numbers:
#     if num % 3 == 0:
#         continue
#     sum_of_non_divisible_by_3 += num
# print(sum_of_non_divisible_by_3)"
# Python program that takes a list of numbers as input and outputs a new list with all the odd numbers replaced by 0 using the continue statement.	"Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_numbers = []
# for num in numbers:
#     if num % 2 != 0:
#         new_numbers.append(0)
#         continue
#     new_numbers.append(num)
# print(new_numbers)"
# Python program that takes a list of words as input and outputs a new list with all the words that contain the letter "a" removed using the continue statement.	"Input: [""apple"", ""banana"", ""kiwi"", ""pear"", ""orange""]
# Expected Output: [""kiwi"", ""pear""]

# words = [""apple"", ""banana"", ""kiwi"", ""pear"", ""orange""]
# new_words = []
# for word in words:
#     if ""a"" in word:
#         continue
#     new_words.append(word)
# print(new_words)"
#  Python program that takes a list of numbers as input and outputs the sum of all the numbers until a negative number is encountered using the break statement.	"Input: [1, 2, 3, -4, 5, 6, -7, 8, 9, 10]
# Expected Output: 12

# numbers = [1, 2, 3, -4, 5, 6, -7, 8, 9, 10]
# sum_of_numbers = 0
# for num in numbers:
#     if num < 0:
#         break
#     sum_of_numbers += num
# print(sum_of_numbers)"
# Python program that takes a list of strings as input and outputs the first string that starts with the letter "b" using the break statement.	"Input: [""apple"", ""banana"", ""kiwi"", ""blueberry"", ""orange""]
# Expected Output: ""banana""

# words = [""apple"", ""banana"", ""kiwi"", ""blueberry"", ""orange""]
# for word in words:
#     if word.startswith(""b""):
#         print(word)
#         break"
#  Python program that takes a list of names as input and outputs the position of the first occurrence of the name "Alice" using the break statement	"Input: [""Bob"", ""Charlie"", ""Alice"", ""Dave"", ""Eve""]
# Expected Output: 2

# names = [""Bob"", ""Charlie"", ""Alice"", ""Dave"", ""Eve""]
# for i in range(len(names)):
#     if names[i] == ""Alice"":
#         print(i)
#         break"
# Python program that takes a list of numbers as input and outputs "positive", "negative", or "zero" for each number in the list	"Input: [-1, 2, -3, 4, 0, 6, -7, 8, 9, -10]
# Expected Output:
# negative
# positive
# negative
# positive
# zero
# positive
# negative
# positive
# positive
# negative

# numbers = [-1, 2, -3, 4, 0, 6, -7, 8, 9, -10]
# for num in numbers:
#     if num > 0:
#         print(""positive"")
#     elif num < 0:
#         print(""negative"")
#     else:
#         print(""zero"")"
# Python program that takes a list of numbers as input and outputs the first three odd numbers using the break and continue statements.	"Input: [2, 4, 6, 7, 8, 9, 10, 11, 12, 13]
# Expected Output:
# 7
# 9
# 11

# numbers = [2, 4, 6, 7, 8, 9, 10, 11, 12, 13]
# odd_count = 0
# for num in numbers:
#     if num % 2 == 0:
#         continue
#     else:
#         odd_count += 1
#         print(num)
#     if odd_count == 3:
#         break"
# "Python program that takes a list of strings as input and outputs all the strings in uppercase, except for the string ""apple"", which should be skipped using the continue statement.
# "	"Input: [""apple"", ""banana"", ""kiwi"", ""orange"", ""pear""]
# Expected Output:
# BANANA
# KIWI
# ORANGE
# PEAR

# fruits = [""apple"", ""banana"", ""kiwi"", ""orange"", ""pear""]
# for fruit in fruits:
#     if fruit == ""apple"":
#         continue
#     print(fruit.upper())"
# Python program that takes a list of integers as input and outputs the sum of all the elements in the list that are either odd or divisible by 3, using conditional statements.	"Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Output: 24

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# total = 0
# for num in numbers:
#     if num % 2 != 0 or num % 3 == 0:
#         total += num
# print(total)"
#  Python program that takes a string as input and outputs the number of times each character appears in the string, using a dictionary and conditional statements.	"Input: ""Hello, world!""
# Expected Output: {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}

# string = ""Hello, world!""
# char_count = {}
# for char in string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print(char_count)"
# Python program that takes a list of integers as input and outputs the number of times each odd number appears in the list, using a dictionary and conditional statements.	"Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Output: {1: 1, 3: 1, 5: 1, 7: 1, 9: 1}

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_count = {}
# for num in numbers:
#     if num % 2 == 0:
#         continue
#     if num in odd_count:
#         odd_count[num] += 1
#     else:
#         odd_count[num] = 1
# print(odd_count)"
# Python program that takes a list of numbers as input and outputs the median of the numbers using the sorted() function and a for loop.	"Input: [5, 10, 3, 8, 1, 9]
# Expected Output: 7.5

# numbers = [5, 10, 3, 8, 1, 9]
# numbers_sorted = sorted(numbers)
# length = len(numbers)
# if length % 2 == 0:
#     median = (numbers_sorted[length//2] + numbers_sorted[length//2-1]) / 2
# else:
#     median = numbers_sorted[length//2]
# print(f""The median is {median}"")"
# Python program that takes a list of strings as input and outputs the number of times each string appears in the list, using a dictionary and conditional statements.	"Input: [""apple"", ""banana"", ""apple"", ""kiwi"", ""banana"", ""pear""]
# Expected Output: {'apple': 2, 'banana': 2, 'kiwi': 1, 'pear': 1}

# fruits = [""apple"", ""banana"", ""apple"", ""kiwi"", ""banana"", ""pear""]
# fruit_count = {}
# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count[fruit] = 1
#     else:
#         fruit_count[fruit] += 1
# print(fruit_count)"
# Python program that takes a list of numbers as input and outputs the second largest number in the list using conditional statements and a for loop.	"Input: [5, 10, 3, 8, 1, 9]
# Expected Output: 9

# numbers = [5, 10, 3, 8, 1, 9]
# largest = numbers[0]
# second_largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num < largest:
#         second_largest = num
# print(f""The second largest number is {second_largest}"")"
	
	
	
# FUNCTIONS	
# Write a function sort_nested_list that takes a nested list of integers as input and returns a new nested list with each inner list sorted in descending order.	"Input: [[3, 2, 1], [7, 9, 8], [6, 5, 4]]
# Expected Output: [[3, 2, 1], [9, 8, 7], [6, 5, 4]]

# def sort_nested_list(nested_list):
#     new_nested_list = []
#     for inner_list in nested_list:
#         sorted_inner_list = sorted(inner_list, reverse=True)
#         new_nested_list.append(sorted_inner_list)
#     return new_nested_list

# nested_list = [[3, 2, 1], [7, 9, 8], [6, 5, 4]]
# sorted_nested_list = sort_nested_list(nested_list)
# print(sorted_nested_list)"
# Write a function flatten_list that takes a nested list of integers as input and returns a new list with all the elements flattened into a single list.	"Input: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def flatten_list(nested_list):
#     flat_list = []
#     for inner_list in nested_list:
#         for element in inner_list:
#             flat_list.append(element)
#     return flat_list

# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# flat_list = flatten_list(nested_list)
# print(flat_list)"
# Write a function unique_permutations that takes a list of integers as input and returns a list of all the unique permutations of that list.	"Input: [1, 2, 3]
# Expected Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# "