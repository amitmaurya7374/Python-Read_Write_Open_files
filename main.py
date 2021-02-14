"""In this project  we will learn about file system in python
learn about read,write and open a file
"""

file = open("my_name.txt")  # this method open a file
content_inside_of_file = file.read()  # this method read  a contents of a file and return a String .

print(content_inside_of_file)
file.close()  # To close a file after we done with it because opening a file take some resources

"""
This is a better approach for handling a file opening 
and closing.
As we are lazy we will forget to close our file in some cases so to prevent this we will use with Keyword
:with handle our file to close it automatically when it done
"""
with open("language_learned.txt") as file:
    content = file.read()
    print(content)
