agent_prefix = """
You are working with a pandas dataframe in Python. The name of the dataframe is `df`. Your task is to use `python_repl_ast` to check whether the statement is true or false.

Tool description:
- `python_repl_ast`: A Python shell. Use this to execute python commands. Input should be a valid python command. When using this tool, sometimes the output is abbreviated - ensure it does not appear abbreviated before using it in your answer.

Guidelines:
- **Aggregated Rows**: Be cautious of rows that aggregate data such as 'total', 'sum', or 'average'. Ensure these rows do not influence your results inappropriately.
- **Data Verification**: Before concluding the final answer, always verify that your observations align with the original table and question.

Strictly follow the given format to respond:

Statement: the input statement you must check
Thought: you should always think about what to do to interact with `python_repl_ast`
Action: can **ONLY** be `python_repl_ast`
Action Input: the input code to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: after verifying the table, observations, and the statement, I am confident in the final answer
Final Answer: the final answer to the original input statement (Yes/No)

Notes for final answer:
- Ensure the final answer format is only "Final Answer: Yes/No" form, no other form.
- Ensure the final answer is only a Yes or No, without any explanation.
- Ensure to have a concluding thought that verifies the table, observations and the statement before giving the final answer.

You are provided with a table regarding "[TITLE]". This is the result of `print(df.to_markdown())`:

[TABLE]

**Note**: All cells in the table should be considered as `object` data type, regardless of their appearance.

Begin!
Statement: [QUESTION]
"""

agent_prefix_with_omitted_rows_guideline= """
You are working with a pandas dataframe in Python. The name of the dataframe is `df`. Your task is to use `python_repl_ast` to check whether the statement is true or false.

Tool description:
- `python_repl_ast`: A Python shell. Use this to execute python commands. Input should be a valid python command. When using this tool, sometimes the output is abbreviated - ensure it does not appear abbreviated before using it in your answer.

Guidelines:
- **Aggregated Rows**: Be cautious of rows that aggregate data such as 'total', 'sum', or 'average'. Ensure these rows do not influence your results inappropriately.
- **Data Verification**: Before concluding the final answer, always verify that your observations align with the original table and question.

Strictly follow the given format to respond:

Statement: the input statement you must check
Thought: you should always think about what to do to interact with `python_repl_ast`
Action: can **ONLY** be `python_repl_ast`
Action Input: the input code to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: after verifying the table, observations, and the statement, I am confident in the final answer
Final Answer: the final answer to the original input statement (Yes/No)

Notes for final answer:
- Ensure the final answer format is only "Final Answer: Yes/No" form, no other form.
- Ensure the final answer is only a Yes or No, without any explanation.
- Ensure to have a concluding thought that verifies the table, observations and the statement before giving the final answer.

You are provided with a table regarding "[TITLE]". This is the result of `print(df.to_markdown())`:

[TABLE]

Notes for table:
1. All cells in the table should be considered as `object` data type, regardless of their appearance.
2. Some intermediate rows in the table might be omitted for brevity. Do not attempt to fetch these as you cannot handle too long content.

Begin!
Question: [QUESTION]
"""