"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

def count_characters(text):
    """Count non-space characters in a string."""
    # TODO: implement
    return len(text.replace(" ", ""))

def count_words(text):
    """Count number of words in a string."""
    # TODO: implement
    return len(text.split())

def extract_numbers(text):
    """Return list of integers found in text."""
    # TODO: implement
    words = text.split()
    numbers = []
    for i in words:
        if i.isdigit():  # checks if the word is a number
            numbers.append(int(i))
    return numbers

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    # TODO: call helper functions and compute total, average, etc.
    c_count = count_characters(text)
    w_count = count_words(text)
    numbers = extract_numbers(text)

    total = sum(numbers)
    average = total/len(numbers)

    return c_count, w_count, numbers, total, average

if __name__ == "__main__":
    # TODO: read input, call analyze_text(), and print results
    text = input("Enter your text: ")
    c_count, w_count, numbers, total, average = analyze_text(text)
    print ("Character count: ", c_count)
    print ("Word count: ", w_count)
    print ("Numbers found: ", numbers)
    print("Their sum is ", total)
    print("Their average is ", average)
