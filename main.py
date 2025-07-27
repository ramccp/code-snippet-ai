from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import streamlit as st

code_prompt = '''
Write only the code for {topic} using {language} in a code block, then provide a line-by-line explanation below the code block. Do not include any other text, thoughts, or commentary. Use the format given below:

#### Code:
```
Code
Mention line number of each line of code.
```

#### Explanation:
Explanation of code line by line & provide the visualisation of the code.
- If used any function or library, mention it in the explanation.
- If any loop is used, explain each iteration of the loop.(visualise if possible)
- Visualise the explanation wherever possible.

Example:
- `Line 1`: We are defining a function called factorial that takes a single argument n.
- `Line 2`: We are checking if n is less than or equal to 1. If it is, we return 1 because the factorial of 0 and 1 is 1.
- `Line 3`: We are returning the result of multiplying n by the factorial of n-1. This is the recursive step of the factorial function.
- `Line 4`: We are calling the factorial function with the argument 5.
- `Line 5`: We are printing the result of the factorial function.
- `Line 6`: We are calling the factorial function with the argument 3.
- `Line 7`: We are printing the result of the factorial function.

And provide real life analogy wherever possible like you explain to a 10 year old.


#### Real Life Analogy:

Example:

Imagine you have 12 pencils and 15 pens. You want to find the smallest number that is a 
multiple of both 12 and 15. To do this, you first find the greatest number that divides 
both 12 and 15, which is 3. Then you multiply 12 and 15 and divide by 3 to get 60, 
which is the smallest number that is a multiple of both 12 and 15.



DO NOT USE ANY OTHER TEXT THAN THE CODE AND EXPLANATION.
'''

st.title("🤖 CATGPT")
st.subheader("Your AI Coding Assistant")
col1, col2 = st.columns(2)
with col1:
    topic = st.text_input("Topic", placeholder="Ex: Factorial using recursion")
with col2:
    language = st.text_input("Language", placeholder="Ex: Python")

btn = st.button("✨ Generate Code")

output_placeholder = st.empty()

def generate_code(topic,language):
    code_template = PromptTemplate(template=code_prompt,input_variables=["topic","language"])
    llm = ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct")
    chain = code_template | llm
    response = chain.invoke({"topic":topic,"language":language})
    return response.content
    

if btn:
    with output_placeholder:
        with st.spinner("Generating code..."):
            data = generate_code(topic, language)
    with output_placeholder:
        st.success("Successfully generated code")
        import time
        time.sleep(2)
    with output_placeholder:
        # print(data)
        st.markdown(data)