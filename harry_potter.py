# Install required packages
# venv\scripts\activate
#  pip install -r requirements.txt

import pandas as pd

# Read in the file
with open('My Clippings.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Give me all non-empty chunks, trimmed of whitespace
highlights = [h.strip() for h in text.split('==========') if h.strip()]
no_highlights = len(highlights)

# Summary
print("Number of highlights found:", no_highlights)
#print(highlights[no_highlights - 1])  # Print first highlight as example

# Filter to french language books
pd_highlights = pd.DataFrame(highlights, columns=['highlight'])
french_highlights = pd_highlights[pd_highlights['highlight'].str.contains('français|French', case=False, na=False)]

print("Number of French highlights found:", len(french_highlights))
print(french_highlights.iloc[0]['highlight'])  # Print first French highlight as example