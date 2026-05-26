from langchain_core.prompts import PromptTemplate

def format_docs(retrieved_docs):
    """Helper function to format retrieved documents into a single string."""
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

def get_qa_prompt():
    """Defines and returns the PromptTemplate for the RAG task."""
    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        Context:
        {context}
        
        Question: {question}
        Answer:
        """,
        input_variables=['context', 'question']
    )
    return prompt