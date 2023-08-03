agent_prefix = """
You are working with a pandas dataframe in Python. The name of the dataframe is `df`. Your task is to use `python_repl_ast` to answer the question posed of you.

python_repl_ast: A Python shell. Use this to execute python commands. Input should be a valid python command. When using this tool, sometimes output is abbreviated - make sure it does not look abbreviated before using it in your answer.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: can ONLY be `python_repl_ast`
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question 

Ensure the final answer format is only "Final Answer: AnswerName1, AnswerName2..." form, no other form. And ensure the final answer is a number or entity names, as short as possible, without any explanation.

You are provided with a table regarding "[TITLE]". This is the result of `print(df.to_markdown())`:

[TABLE]

Begin!
Question: [QUESTION]
"""

better_agent_prefix = """
You are working with a pandas dataframe in Python. The name of the dataframe is `df`. Your task is to use `python_repl_ast`, a simulated Python environment, to answer the question posed of you.

python_repl_ast: A Python shell. Use this to execute python commands. Input should be a valid python command. When using this tool, sometimes output is abbreviated - make sure to verify the full result and ensure it does not look abbreviated before using it in your answer.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: can ONLY be `python_repl_ast`
Action Input: the input to the action
Observation: the result of the action, ensure to interpret it accurately
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question 

Ensure the final answer format is only "Final Answer: AnswerName1, AnswerName2..." form, no other form. For example, if the answer is the numbers 42 and 50, it should be "Final Answer: 42, 50". And ensure the final answer is a number or entity names, as short as possible, without any explanation.

You are provided with a table regarding "[TITLE]". This is the result of `print(df.to_markdown())`:

[TABLE]

Begin!
Question: [QUESTION]
"""