# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# Python has a built-in package called re, which can be used to work with Regular Expressions.
import re

sentence = "The rain in Spain"
# Search the string to see if it starts with "The" and ends with "Spain":
x = re.search("^The.*Spain$", sentence)
print(x)  # <re.Match object; span=(0, 17), match='The rain in Spain'>
if x:
  print("YES! We have a match!")
else:
  print("No match")

### RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:
# Function	 Description
# --------:  -----------------------------------------
# findall :  Returns a list containing all matches
# search  :  Returns a Match object if there is a match anywhere in the string
# split	  :  Returns a list where the string has been split at each match
# sub	  :  Replaces one or many matches with a string

### Metacharacters
# Metacharacters are characters with a special meaning:
# Character   Description	                                                               Example
# ---------:  ------------:                                                                -----------------------------------------
# []	      A set of characters	                                                       "[a-m]"
# \	          Signals a special sequence (can also be used to escape special characters)   "\d"
# .	          Any character (except newline character)	                                   "he..o"
# ^	          Starts with	                                                               "^hello" 
# $	          Ends with	                                                                   "world$"
# *	          Zero or more occurrences	                                                   "aix*"
# +	          One or more occurrences	                                                   "aix+"
# {}	      Exactly the specified number of occurrences	                               "al{2}"
# |	          Either or	                                                                   "falls|stays"
# ?           Zero or one occurrence                                                       "he.?o"
# ()	      Capture and group

### Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
# Character   Description	                                                                                                   Example
# ---------:  ------------:                                                                                                  -----------------------------------------
# \A	      Returns a match if the specified characters are at the beginning of the string	                                 "\AThe"
# \b	      Returns a match where the specified characters are at the beginning or at the end of a word	                     r"\bain"
#           (the "r" in the beginning is making sure that the string is being treated as a "raw string")                     r"ain\b"
# \B        Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word   r"\Bain"
#                                                                                                                            r"ain\B"
# \d	      Returns a match where the string contains digits (numbers from 0-9)	                                             "\d"
# \D	      Returns a match where the string DOES NOT contain digits	                                                       "\D"
# \s	      Returns a match where the string contains a white space character	                                               "\s"
# \S	      Returns a match where the string DOES NOT contain a white space character	                                       "\S"
# \w	      Returns a match where the string contains any word characters (from a to Z,0-9, and the underscore _ character)  "\w"     
# \W	      Returns a match where the string DOES NOT contain any word characters	                                           "\W"
# \Z	      Returns a match if the specified characters are at the end of the string	                                       "Spain\Z"                                                                        

### Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:
# Set	        Description
# ---------:  ------------:
# [arn]	      Returns a match where one of the specified characters (a, r, or n) are present
# [a-n]	      Returns a match for any lower case character, alphabetically between a and n
# [^arn]	  Returns a match for any character EXCEPT a, r, and n
# [0123]	  Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	      Returns a match for any digit between 0 and 9
# [0-5][0-9]  Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]	  Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]	      In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

### The findall() Function
# The findall() function returns a list containing all matches.
x = re.findall("ai", sentence)
print(x)  # ['ai', 'ai']

x = re.findall("Portugal", sentence)
print(x)  # []

### The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:
x = re.search("\s", sentence)
print("The first white-space character is located in position:", x.start())  # The first white-space character is located in position: 3
# Note: Space, tab, line feed (newline), carriage return, form feed, and vertical tab characters are
# called "white-space characters" because they serve the same purpose as the spaces between words and lines on a printed page

### The split() Function
# The split() function returns a list where the string has been split at each match:
x = re.split("\s", sentence)
print(x)  # ['The', 'rain', 'in', 'Spain']

# We can control the number of occurrences by specifying the maxsplit parameter:
x = re.split("\s", sentence, 1)
print(x)  # ['The', 'rain in Spain']

### The sub() Function
# The sub() function replaces the matches with the text of your choice:
x = re.sub("\s", "9", sentence)
print(x)  # The9rain9in9Spain

# We can control the number of replacements by specifying the count parameter:
x = re.sub("\s", "9", sentence, 2)
print(x)  # The9rain9in Spain

### Match Object
# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.
x = re.search("ai", sentence)
print(x)  # <re.Match object; span=(5, 7), match='ai'>

# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
x = re.search(r"\bS\w+", sentence)
print(x.span())  # (12, 17)

# .string returns the string passed into the function
print(x.string)  # The rain in Spain

# .group() returns the part of the string where there was a match
print(x.group())  # Spain