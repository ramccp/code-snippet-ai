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
Explanation line by line with line number of the code and provide real life analogy wherever possible like you explain to a 10 year old.
- If used any function or library, mention it in the explanation.
- If any loop is used, explain each iteration of the loop.(visualise if possible)
- Visualise the explanation wherever possible.

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