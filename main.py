# User input নেওয়া
text = input("Enter something to save: ")

# File open in append mode and write
with open("myfile.txt", "a") as f:
    f.write(text + "\n")   # \n = new line

print("Text added successfully!")
