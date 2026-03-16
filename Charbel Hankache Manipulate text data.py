# Exercise 1.1
# Given the following sentence, convert it to lowercase and store in 'result'

sentence = "The Quick BROWN Fox Jumps Over The Lazy DOG"

result = sentence.lower()

print(result)
assert result == "the quick brown fox jumps over the lazy dog", "Check your answer!"

# Exercise 1.2
# Count how many times the word "the" appears in the following text (case-insensitive)
# Hint: convert to lowercase first

paragraph = "The cat sat on the mat. The mat was on the floor. THE floor was cold."

result = paragraph.lower()
count_the = result.count("the")

print(f"'the' appears {count_the} times")
assert count_the == 5, "Hint: make sure to count case-insensitively!"

# Exercise 1.3
# Clean the following messy text:
# 1. Remove leading/trailing whitespace
# 2. Split into words
# 3. Join back with single spaces

messy_text = "   This    text   has    irregular     spacing   "
#clean_text = messy_text.strip() # Step 1: Remove leading/trailing whitespace
clean_text = " ".join(messy_text.split())

print(f"Clean: '{clean_text}'")
assert clean_text == "This text has irregular spacing", "Check your answer!"

# Exercise 1.4
# Replace all occurrences of "NLP" with "Natural Language Processing"

text = "NLP is fascinating. I love studying NLP. NLP has many applications."

expanded_text = text.replace("NLP", "Natural Language Processing")

print(expanded_text)
assert "NLP" not in expanded_text, "All 'NLP' should be replaced!"
assert expanded_text.count("Natural Language Processing") == 3, "Should have 3 replacements!"

# Exercise 1.5
# Filter the following list to keep only words that:
# 1. Contain only alphabetic characters
# 2. Have more than 3 characters

words = ["hello", "world123", "NLP", "AI", "machine", "42", "learning", "a1b2", "the"]

filtered_words = [word for word in words if word.isalpha() and len(word) > 3]

print(filtered_words)
assert filtered_words == ["hello", "machine", "learning"], "Check your filtering conditions!"

# Exercise 1.6
# Create a function that performs basic text cleaning:
# 1. Convert to lowercase
# 2. Remove leading/trailing whitespace
# 3. Replace multiple spaces with single space
# 4. Replace newlines with spaces

def basic_clean(text):
    # convert to lowercase
    text = text.lower()
    
    # replace newlines with space
    text = text.replace("\n", " ")
    
    # remove extra spaces
    text = " ".join(text.split())
    
    return text

# Test your function
test_text = """   HELLO   World!  
   This is    a TEST.   """

result = basic_clean(test_text)
print(f"Result: '{result}'")
assert result == "hello world! this is a test.", "Check your function!"

import re  
# 2.1 Basic Regex Functions

# Exercise 2.1
# Extract all the years (4-digit numbers) from the following text

text = "Python was created in 1991. TensorFlow was released in 2015. GPT-3 came out in 2020."

years = re.findall(r'\b\d{4}\b', text)

print(years)
assert years == ['1991', '2015', '2020'], "Check your pattern!"

# Exercise 2.2
# Extract all words that contain only lowercase letters (no digits, no uppercase)

text = "Hello world NLP is GREAT for text processing 123"

lowercase_words = re.findall(r'\b[a-z]+\b', text)
# Hint: use [a-z]+ pattern

print(lowercase_words)
assert lowercase_words == ['orld', 'is', 'for', 'text', 'processing'], "Check your pattern!"

# Exercise 2.3
# Extract all phone numbers in the format XXX-XXX-XXXX

text = "Call me at 123-456-7890 or 987-654-3210. My old number was 555-1234."

phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)
# Hint: \d{3} matches exactly 3 digits

print(phone_numbers)
assert phone_numbers == ['123-456-7890', '987-654-3210'], "Check your pattern!"

# Exercise 2.4
# Find all words that START with 'pre' (as whole words, not substrings)

text = "I need to prepare a presentation. The prerequisites are comprehensive."

pre_words = re.findall(r'\bpre\w*', text)


print(pre_words)
assert pre_words == ['prepare', 'presentation', 'prerequisites'], "Check your pattern!"

# Exercise 2.5
# Extract all dates in format DD/MM/YYYY or DD-MM-YYYY
# Return them as tuples (day, month, year)

text = "Important dates: 25/12/2024, 01-01-2025, and 14/02/2025."

dates = re.findall(r'(\d{2})[-/](\d{2})[-/](\d{4})', text)

print(dates)
assert dates == [('25', '12', '2024'), ('01', '01', '2025'), ('14', '02', '2025')], "Check your pattern!"

# Exercise 2.8
import re

def preprocess_text(text):
    """
    Comprehensive text preprocessing for NLP tasks.
    """
    
    # Step 1: Lowercase
    text = text.lower()
    
    # Step 2: Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Step 3: Remove emails
    text = re.sub(r'\S+@\S+', '', text)
    
    # Step 4: Remove hashtags and mentions
    text = re.sub(r'[@#]\w+', '', text)
    
    # Step 5: Remove punctuation (keep letters, numbers, spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # Step 6: Remove extra whitespace
    text = " ".join(text.split())
    
    # Step 7: Strip leading/trailing whitespace
    text = text.strip()
    
    return text


# Test
raw_text = """
    🚀 Check out our NEW product at https://example.com!!! 
    Contact: sales@company.com @CompanyName #Innovation #Tech
    Limited time offer: 50% OFF!!!
"""