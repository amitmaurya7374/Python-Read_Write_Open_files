"""In this project  we will learn about file system in python
learn about read,write and open a file
"""
# Opening and Reading a File
"""
open() => this method take a file_name and mode in which mode we want ot open a file 
By Default mode is set to read but we can change it to write ,append .
mode = "r" => for read 
mode= "w" => to write but this will delete a existing content of file.
mode= "a" => to append in file .This will write into a file without deleting a existing content of a  file .

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
with open("language_learned.txt") as file:  # save that file into a file variable like we did in above code
    content = file.read()
    print(content)

# Writing into a file
"""To write is any file we have to open a file into write mode .like this open(mode = "w") .By default mode is read 
only """
with open("my_name.txt", mode="a") as file:
    file.write("\nAnd I m college drop out.")
