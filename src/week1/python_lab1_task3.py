"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    # TODO: implement function logic
    length = len(text)
    w_count = len(text.split())
    python = "python" in text.lower()
    return length, w_count, python

if __name__ == "__main__":
    # TODO: read sentence from input, call function, and print results
    text = input("Enter your text: ")
    print(analyze_sentence(text))
