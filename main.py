import tempfile
import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI

openai_api_key = st.secrets["OPENAI_API_KEY"]

"""
# Analyst Note Generator
## created by Marvin

If you have any questions, checkout my github [README.md](https://github.com/mvsbm/AnalystNote).\n
email: s-ma@coloplnext.co.jp
"""


class Summarizer:
    def __init__(self, chain_type: str, chunk_size: int, chunk_overlap: int, temperature: float):
        self.chain_type = chain_type
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.temperature = temperature

    def setup_documents(self, pdf_file_path: str):
        loader = PyPDFLoader(pdf_file_path)
        docs_raw = loader.load()
        docs_raw_text = [doc.page_content for doc in docs_raw]
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size,
                                                       chunk_overlap=self.chunk_overlap)
        docs = text_splitter.create_documents(docs_raw_text)
        return docs

    def custom_summary(self, docs, llm, custom_prompt, num_summaries):
        custom_prompt = custom_prompt + """:\n {text}"""
        COMBINE_PROMPT = PromptTemplate(template=custom_prompt, input_variables=["text"])
        MAP_PROMPT = PromptTemplate(template="Summarize:\n{text}", input_variables=["text"])
        if self.chain_type == "map_reduce":
            chain = load_summarize_chain(llm, chain_type=self.chain_type,
                                         map_prompt=MAP_PROMPT,
                                         combine_prompt=COMBINE_PROMPT)
        else:
            chain = load_summarize_chain(llm, chain_type=self.chain_type)

        summaries = []
        for i in range(num_summaries):
            summary_output = chain({"input_documents": docs}, return_only_outputs=True)["output_text"]
            summaries.append(summary_output)

        return summaries



def main():

    llm_name = st.sidebar.selectbox("LLM", ["GPT4", "ChatGPT"])
    if llm_name == "GPT4":
        llm = ChatOpenAI(model_name="gpt-4", temperature=0.0, openai_api_key=openai_api_key)
    elif llm_name == "GPT-3.5-turbo":
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.0, openai_api_key=openai_api_key)
    else:
        st.write(f"Model {llm_name} is not supported yet!")
        return

    chain_type = st.sidebar.selectbox("Chain Type", ["map_reduce", "stuff", "refine"])
    chunk_size = st.sidebar.slider("Chunk Size", min_value=500, max_value=5000, step=100, value=1500)
    chunk_overlap = st.sidebar.slider("Chunk Overlap", min_value=50, max_value=500, step=50, value=100)

    summarizer = Summarizer(chain_type, chunk_size, chunk_overlap, 0.0)

    st.subheader('Company name:')
    company_name = st.text_input("Enter the company name")

    st.subheader('Upload PDF:')
    uploaded_file = st.file_uploader("Choose a file", type=['pdf'])
    if uploaded_file is not None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, "uploaded_file.pdf")
            st.write("PDF loaded successfully")
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            if company_name != "":
                user_prompt = f"""
                Provide an analyst note in Markdown for the earnings call of {company_name}. Each section should have a clear heading and content should be formatted appropriately. Avoid markdown errors and follow this structure:

                1. Financial Highlights: List key stats with changes in percentages like "- EPS (+14.8%)": "Why EPS increased."

                2. Segment Performance: Detail performance of each segment with important call remarks.

                3. Key Remarks: Summarize significant comments affecting future performance.

                4. Outlook: Discuss the company's future based on the call.

                5. Market Trends and Industry Comparisons: Compare {company_name} with its competitors.

                6. Strategies, Challenges, and Opportunities: Analyze the company's strategies, potential challenges, and growth opportunities.

                7. Conclusion: Combine all points into a comprehensive conclusion of about 2000 words. 
                """

                progress_bar = st.progress(0)
                status_text = st.empty()

                with st.spinner('Generating Analyst Note...This might take 5-10 minutes.'):
                    status_text.text('Setting up documents...')
                    progress_bar.progress(0)  # Start
                    docs = summarizer.setup_documents(file_path)
                    progress_bar.progress(40)  # Progress after setting up documents

                    status_text.text('Summarizing...')
                    result = summarizer.custom_summary(docs, llm, user_prompt, 1)
                    progress_bar.progress(100)  # Progress after summarizing

                st.write("Summary:")
                for summary in result:
                    st.write(summary)

                status_text.text('Done!')


if __name__ == "__main__":
    main()
