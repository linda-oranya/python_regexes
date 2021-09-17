import re

#using regexes without quantifiers
pattern = re.compile(r"\w") 
string = "regex is awesome!"

# match the string with the compiled regex
result = pattern.match(string)
print (result.group()) 

#using regexes with a qantifier
patterns = re.compile(r"\w+")
result1 = patterns.match(string)
print (result1.group()) 

def regex(string):
    """This function returns at least one matching digit."""
    pattern = re.compile(r"\d{1,}") # For brevity, this is the same as r"\d+"
    result = pattern.match(string)
    if result:
        return  result.group()
    return None

# Call our function, passing in our string
print(regex("007 James Bond"))

def finder(string):
    """This function finds all the words in a given string."""
    result_list = re.findall(r"\w+", string)
    return result_list

# Call finder function, passing in the string argument
print(finder("finding dory 2twice"))
