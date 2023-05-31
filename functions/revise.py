#1.Write a Python program that accepts the user's first and last name and 
#prints them in reverse order with a space between them.

def acceptanceDetails(first_name,last_name):
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    full_name = last_name + ' ' + first_name
    print(full_name)

def print_name_reverse(first_name, last_name):
   first_name = input("Your first name: ")
   last_name = input("Your secondName: ")
   full_name = last_name + " " + first_name
   print(full_name[::-1])

full_name = last_name + " " + first_name
print(full_name[::-1])

#2.Write a Python program that accepts a sequence of comma-separated numbers 
#from the user and generates a list and a tuple of those numbers.

def sequence_to_list_tuple(sequence):
    numbers = sequence.split(',')
    numbers_list = list(map(int, numbers))
    numbers_tuple = tuple(map(int, numbers))
    return numbers_list, numbers_tuple
sequence = input("Enter a sequence of comma-separated numbers: ")
numbers_list, numbers_tuple = sequence_to_list_tuple(sequence)
print(numbers_list)
print(numbers_tuple)   

#3.Write a Python program that prints long text, converts it to a list, 
# and prints all the words and the frequency of each word



#4.Write a Python program to count the number of each character in a text file.



#5.Write a Python program that generates a list of all possible 
#permutations from a given collection of distinct numbers



#6.Write a Python program to find the first appearance of the substrings 
#'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 
#'not'...'poor' substring with 'good'. Return the resulting string.

#7.Write a Python function to insert a string in the middle of a string.

#8.Write a Python program to count repeated characters in a string.

#9.Sample string: 'thequickbrownfoxjumpsoverthelazydog'
#Expected output :
#o 4
#e 3
#u 2
#h 2
#r 2
#t 2

#10.Write a Python function that returns the Nth Fibonacci number
def fibonacci(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#11.Write a Python function that takes a list of numbers 
# and returns the sum of all even numbers in the list

def sum_even_numbers(numbers):
    total_sum = 0
    for num in numbers:
        if num % 2 == 0:
            total_sum += num
    return total_sum 

numbers = [1,2,3,4,5,6,7,8,9,10]
even_sum = sum_even_numbers(numbers)
print(even_sum)

# 12.Write a Python function that takes two strings and returns 
# True if they are anagrams, False otherwise.

def in_anagrams(str1, str2):
    if(len(str1) == len(str2)):
        print("true")
    else:
        print ("false")

str1 = "Race"
str2 = "Care"
in_anagrams(str1, str2)

# 13.Write a Python function that takes a string 
# and returns the reverse of the string.
def reverse_string(text):
    text_list = list(text)
    text_list.reverse()
    reversed_text = "".join(text_list)
    return reversed_text

string = "Milcah Nkatha"
reversed_string = reverse_string(string)
print(reversed_string)
 
# 14.Write a Python function that takes a list of 
# strings and returns the longest string in the list.

def find_longest_string(strings):
    longest_string = strings[0]
    for x in strings:
     if len(x) > len(longest_string):
            longest_string = x
    return longest_string


strings = ["Faith", "Makena", "Kimathi", "Sally", "Milcah"]
longest_string = find_longest_string(strings)
print(longest_string)            


# 15.Write a Python function that takes a list of 
# integers and returns the second largest number in the list.
# 16.Write a Python function that takes a string and 
# returns True if the string is a palindrome, False otherwise.
# 17.Write a Python function that takes a list of 
# integers and returns the sum of all the numbers in the list.
# 18.Write a Python function that takes a list of 
# numbers and returns the product of all the numbers in the list.
# 19.Write a Python function that takes a list of strings 
# and returns the number of strings in the list that contain the substring 'abc'.
# 20.Write a Python function that takes a list of integers 
# and returns the difference between the maximum and minimum numbers in the list.
# 21.Write a Python function that takes a list of integers 
# and returns a new list with only the even numbers from the original list.
# 22.Write a Python function that takes a list of integers 
# and returns a new list with only the odd numbers from the original list.
# 23.Write a Python function that takes a list of strings and 
# returns a new list with only the strings that start with the letter 'a'.
# 24.Write a Python function that takes a list of strings and 
# returns a new list with the strings sorted in alphabetical order.
# 25.Write a Python function that takes a list of integers and 
# returns a new list with the numbers sorted in descending order.
# 26.Write a Python function that takes a list of integers and 
# returns a new list with the numbers sorted in ascending order.
# 27.Write a Python function that takes a list of strings and 
# returns a new list with the strings sorted in reverse alphabetical order.
# 28.Write a Python function that takes a list of integers and 
# returns True if the list is sorted in ascending order, False otherwise.
# 29.Write a Python function that takes a list of integers and 
# returns True if the list is sorted in descending order, False otherwise.      


# initialize the longest string to be the first string in the list
    # longest_string = strings[0]
    
    # iterate through the list of strings
    # for s in strings:
        # if the current string is longer than the longest string, update the longest string
        # if len(s) > len(longest_string):
        #     longest_string = s
    
    # return the longest string
    # return longest_string

    # def reverse_string(s):
    # """
    # This function takes a string and returns the reverse of the string.
    # """
    # # convert the string to a list of characters
    # s_list = list(s)
    
    # # reverse the list of characters
    # s_list.reverse()
    
    # # convert the reversed list of characters back to a string
    # reversed_s = "".join(s_list)
    
    # # return the reversed string
    # return reversed_s

#     string = "Hello, world!"
# reversed_string = reverse_string(string)
# print(reversed_string)