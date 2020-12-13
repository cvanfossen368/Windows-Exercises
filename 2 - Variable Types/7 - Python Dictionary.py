#Python dictionaries are kind of hash-table typle. They work like associative arrays or hashes found..
#..in Perl and consist of key-value pairs. A dictionary key can be almost any Python typle, but are..
#..usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

#Dictionaries are encloses by curly braces ({}) and values can be assigned and accessed using squared braces ([]).

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'John','code':6734,'dept': 'sales'}

print(dict['one']) #Prints value for 'one' key.
print(dict[2]) #Prints value for 2 key.
print(tinydict) #Prints complete dictionary.
print(tinydict.keys()) #Prints all the keys.
print(tinydict.values()) #Prints all the values.

