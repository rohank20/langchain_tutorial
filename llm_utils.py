from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate


def summarize_doc(doc_text):
    template = """Question: I will input the text from a document. 
    Please summarize the document concisely and provide all important points from this document. Make sure not to miss anything important.
    The summary must be short and to the point but with all important information. The text is as follows:
    {doc_text}
    Answer: Let's think step by step."""

    prompt = PromptTemplate(template=template, input_variables=['doc_text'])

    llm = OllamaLLM(model='llama3.1')

    llm_chain = prompt | llm

    doc_text = doc_text
    return llm_chain.invoke({"doc_text":doc_text})