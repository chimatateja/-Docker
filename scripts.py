import re
from collections import Counter
import socket
import os

# Define file paths
input_file_if = '/home/data/IF-1.txt'
input_file_arutw = '/home/data/AlwaysRememberUsThisWay-1.txt'
output_dir = '/home/data/output'  # This will be mapped to your local directory
result_file_path = os.path.join(output_dir, 'result.txt')

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to handle contractions
def handle_contractions(text):
    contractions = {
        "can't": "cannot", "won't": "will not", "don't": "do not", 
        "i'm": "i am", "they're": "they are", "it's": "it is"
    }
    for contraction, full_form in contractions.items():
        text = text.replace(contraction, full_form)
    return text

# Function to count words in a text file
def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        text = handle_contractions(text)
        words = re.findall(r'\b\w+\b', text)  # Extract words using regex
        return words

# Read the files and count words
words_if = count_words(input_file_if)
words_arutw = count_words(input_file_arutw)

# Total word count
total_if = len(words_if)
total_arutw = len(words_arutw)
grand_total = total_if + total_arutw

# Top 3 frequent words for both files
top_3_if = Counter(words_if).most_common(3)
top_3_arutw = Counter(words_arutw).most_common(3)

# Get IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Prepare the result as a string
result_text = f"""
Word count for IF-1.txt: {total_if}
Word count for AlwaysRememberUsThisWay-1.txt: {total_arutw}
Grand total word count: {grand_total}

Top 3 frequent words in IF-1.txt: {top_3_if}
Top 3 frequent words in AlwaysRememberUsThisWay-1.txt: {top_3_arutw}

IP address of the machine: {ip_address}
"""

# Write results to result.txt
with open(result_file_path, 'w') as f:
    f.write(result_text)

# Print the content of result.txt to the console
print(result_text)
