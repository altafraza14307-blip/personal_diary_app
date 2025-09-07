dincharya = input("Enter your dincharya: ")
with open("notes.txt","a") as notes:
 notes.write (dincharya + "\n")
print("Entry done")

# f = open("notes.txt","r")
# co ntent = f.read()
# print(content)