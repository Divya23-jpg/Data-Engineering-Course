"""

File Handling refers to any Operations like Reading, writting,closing
etc through  a programming 

.open(): Open file
.close(): Close File
.read(): Read whole data of the file
.name(): Check file name
.mode(): Check Mode of the file
.closed(): Check file is closed or not 
    ? Give 0 or 1
.write(): Write in a file



"""
# ! Open and Read File  
# file=open('hello.txt','r') # Open filen in a read mode
# content=file.read()  # Read whole content from the file
# print(content) # print content of the file


# ! Open,close  and Write in a file

# with open('writing.txt','w') as file:
#     file.write("I am Example of Writting to the file.\n")  # write in a file
#     file.write("This is 2nd statement.")
    
# print("Writing to the file is Done")


# ! We will check file is present or not

try:
    file=open('hello.txt','r')
    content=file.read()
    print(content)

except FileNotFoundError as e:
    print("File Not Found",e)

finally:
    try:
        file.close()
    
    except NameError: