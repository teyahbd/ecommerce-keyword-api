import pandas as pd
import os

# Import data as DataFrame:

df = pd.read_excel('Online_Retail.xlsx', usecols="C")

# Remove empty rows:

df.dropna(inplace=True)

# Remove rows containing non-product descriptions

bad_lines = "\?|damaged|damages|damage"

df = df[df["Description"].str.contains(bad_lines) == False]

# Convert DataFrame to a text file:

text_file = open("dataset.txt", "w")
for data in df.columns:
    text_file.write((df[data].to_string(index=False)+'\n').lower())

text_file.close()

# Remove unhelpful words and punctuation from sentences

bad_chars = ["?", "/"]
punct = [".", ",", "\""]

with open('dataset.txt') as oldfile, open('cleaned_dataset.txt', 'w') as newfile:
    for line in oldfile:
        clean_arr = []
        sentence = line.split()
        for word in sentence:
            if not any(chars in word for chars in bad_chars):
                if len(word) > 2:
                    if any(chars in word for chars in punct):
                        clean_word = word
                        for item in punct:
                            clean_word = clean_word.replace(item, "")
                        clean_arr.append(clean_word)

                    else: 
                        clean_arr.append(word)
        clean_str = ' '.join(clean_arr) +'\n'
        newfile.write(clean_str)

os.remove("dataset.txt")

