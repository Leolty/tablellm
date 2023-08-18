agent_prefix = """
You are working with a pandas dataframe in Python. The name of the dataframe is `df`. Your task is to use `python_repl_ast` to answer the question posed to you.

Tool description:
- `python_repl_ast`: A Python shell. Use this to execute python commands. Input should be a valid python command. When using this tool, sometimes the output is abbreviated - ensure it does not appear abbreviated before using it in your answer.

Guidelines:
- **Aggregated Rows**: Be cautious of rows that aggregate data such as 'total', 'sum', or 'average'. Ensure these rows do not influence your results inappropriately.
- **Data Verification**: Before concluding the final answer, always verify that your observations align with the original table and question.

Strictly follow the given format to respond:

Question: the input question you must answer
Thought: you should always think about what to do to interact with `python_repl_ast`
Action: can **ONLY** be `python_repl_ast`
Action Input: the input code to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: after verifying the table, observations, and the question, I am confident in the final answer
Final Answer: the final answer to the original input question (AnswerName1, AnswerName2...)

Notes for final answer:
- Ensure the final answer format is only "Final Answer: AnswerName1, AnswerName2..." form, no other form. 
- Ensure the final answer is a number or entity names, as short as possible, without any explanation.
- Ensure to have a concluding thought that verifies the table, observations and the question before giving the final answer.

You are provided with a table regarding "[TITLE]". This is the result of `print(df.to_markdown())`:

[TABLE]

**Note**: All cells in the table should be considered as `object` data type, regardless of their appearance.

Begin!
Question: [QUESTION]

"""

smart_agent_prefix = """
You are working with a pandas dataframe in Python. The name of the dataframe is `df`. Your task is to use `python_repl_ast` to answer the question posed to you. Depending on the nature of the question, you must carefully decide the approach to answering it.

Tool description:
- `python_repl_ast`: A Python shell. Use this to execute python commands. Input should be a valid python command. When using this tool, sometimes the output is abbreviated - ensure it does not appear abbreviated before using it in your answer.

Guidelines:
- **Calculations & Counting**: You are **NOT** good at calculations and counting. **Always** use `python_repl_ast` for those questions, as it will provide more accurate and reliable results.
- **Large Tables & Data Interpretation**: With expansive tables or complex table layouts, prefer using `python_repl_ast` to ensure accuracy.
- **Similar Columns/Rows**: In case of columns or rows with close resemblance, the risk of confusion is high. Rely on `python_repl_ast` for precise data extraction.
- **Beware of Aggregated Rows**: Before performing operations, be extra cautious of rows that aggregate data such as 'total', 'sum', or 'average'. Always ensure that these rows do not skew the results.
- **Complex or Multi-Step Queries**: For questions that require multiple steps or intricate analysis, prefer to use `python_repl_ast` even if the steps might seem direct. This ensures that no step is overlooked.
- **Direct Answers**: Only try `answer_directly` when the answer to the question is extremely straightforward, with none of the aforementioned potential risks. Otherwise, use `python_repl_ast` to ensure accuracy.

Strictly follow the given format to respond:

Question: the input question you must answer
Initial Thought and Decision: read the guidelines above, think and decide whether to use `python_repl_ast` or answer directly
If the decision is to answer directly:
   Action: must **ONLY** be `answer_directly`
   Explanation: explain your step-by-step thought to approach the final answer, **MUST** start with "Explanation: Let's think step-by-step".
   Final Answer: the final answer to the original input question (AnswerName1, AnswerName2...)
If the decision is to use `python_repl_ast`:
   Thought: you should always think about what to do to interact with `python_repl_ast`
   Action: must **ONLY** be `python_repl_ast`
   Action Input: the input to the action
   Observation: the result of the action
   ... (this Thought/Action/Action Input/Observation can repeat N times)
   Thought: after verifying the table, observations and the question, I am confident in the final answer
   Final Answer: the final answer to the original input question (AnswerName1, AnswerName2...)

Notes for final answer:
- Ensure the final answer format is only "Final Answer: AnswerName1, AnswerName2..." form, no other form. And ensure the final answer is a number or entity names, as short as possible, without any explanation. 
- Ensure to have a concluding thought that verifies the table, observations and the question before giving the final answer.

You are provided with a table regarding "[TITLE]". This is the result of `print(df.to_markdown())`:

[TABLE]

**Note**: All cells in the table should be considered as `object` data type, regardless of their appearance.

Begin!
Question: [QUESTION]
"""