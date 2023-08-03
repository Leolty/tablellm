sort_prompt = """
You are an advanced AI capable of analyzing and understanding information within tables. Read the table below regarding "[TITLE]":

[TABLE]

We know that the headings for this table are as follows, separated by semicolons:

[HEADINGS]

Your task is to identify whether sorting the table by a particular column would add clarity or enhance understanding. If so, please indicate which column would be best to sort by. If not, specify that no sorting is necessary.

- If sorting would help, respond with: "Sort by: [COLUMN_NAME]", replacing [COLUMN_NAME] with the specific name of the appropriate column.
- If the table doesn’t contain information that would benefit from sorting (such as numerical, alphabetical, or chronological data), or if sorting wouldn't add value for other reasons, respond with: "Sort by: N/A".

Please follow one of these responses without additional explanation.
"""