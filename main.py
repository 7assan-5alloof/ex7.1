# Given
fname = input("Enter file name: ") # Test: words.txt
fh = open(fname)

# Solution
for line in fh:
    print(line.upper().rstrip())
