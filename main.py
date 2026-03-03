# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder: Shaikh Awez
# Date:10-02-2026

print("--- Extracting Words from Text File ---\n")
num = int(input(""))
with open ("story.txt", 'r') as f:
    content = f.read().split()
    wordList = [ i.lower() for i in content if(num == len(i))]
    wordList2 = sorted(set(wordList))
    print(f"{wordList2}")


