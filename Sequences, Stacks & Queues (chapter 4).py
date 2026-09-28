"""
Homework #1: Sets
Concatenated string with uncommon characters in Python: Two strings are given, and you have to modify the 1st string
such that all the common characters of the 2nd string have to be removed and the uncommon characters of the 2nd string
have to be concatenated with the uncommon characters of the 1st string. Use Set data structure.

Examples:
    Input: S1 = “molloy”, S2 = “molsa”
    Output: “ysa”

Implement the program in Python and do the following tasks:
    1) Write a function to input the above string from the keyboard
    2) Write a function "uncommonConcat" with the above input data.
    3) Explain each step of implementing the "uncommonConcat".
"""
def userInput():
    str1 = input("Please enter your first string: ")
    str2 = input("Please enter your second string: ")
    return str1, str2

def uncommonConcat(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    uncommon_s1 = [char for char in str1 if char not in set2]

    uncommon_s2 = [char for char in str2 if char not in set1]


    return "".join(uncommon_s1) + "".join(uncommon_s2)

if __name__ == "__main__":
    s1, s2 = userInput()
    result = uncommonConcat(s1, s2)
    print(f"Output: {result}")

"""
Homework #2: Map
Using the map data structure in Python (which is basically a dictionary) perform the following task:
    - Create a phonebook dictionary where the keys are names and the values are phone numbers.
    - Implement functions to add new entries, search for a phone number by name, and delete entries.
"""
def add_contact(phonebook, name, number):
    phonebook[name] = number
    print(f"Contact '{name}' was added successfully.")

def search_contact(phonebook, name):
    result = phonebook.get(name, "No record found")
    print(f"Result: {result}")
    return result

def delete_contact(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' was deleted successfully.")
    else:
        print(f"Error: Cannot delete. '{name}' does not exist.")


my_phonebook = {}

add_contact(my_phonebook, "Alice", "555-0101")
add_contact(my_phonebook, "Bob", "555-0202")

search_contact(my_phonebook, "Grace")

delete_contact(my_phonebook, "Bob")

print("\nYour current phonebook:", my_phonebook)