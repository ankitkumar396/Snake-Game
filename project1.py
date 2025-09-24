import sys
sys.path.append("C:/Users/ankit/OneDrive/Desktop/project/project.py")
from project import *
print(responces[0])
print(responces[1])

while True:
    text = input("Please Ask Me: ")
    for w in text.split():
        if w.upper() in operations.keys():
            try:
                nums = extract_num(text)

                if len(nums) == 0:
                    n = int(input("Enter a number: "))
                    print(operations[w.upper()](n))
                else:
                    print(operations[w.upper()](*nums))

                break
            except Exception as e:
                print("Please Ask Correct Question:", e)
                break

        elif w.upper() in commands.keys():
            commands[w.upper()]()
            exit()
    else:
        print(responces[4])
        print(responces[5])
