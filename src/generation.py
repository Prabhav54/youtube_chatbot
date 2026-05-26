from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from src.config import Config
from src.augmentation import get_qa_prompt, format_docs

def build_rag_chain(retriever):
    """Builds the LCEL chain for Question Answering."""
    
    # 1. Initialize Hugging Face LLM (Generation)
    llm = HuggingFaceEndpoint(
        repo_id=Config.LLM_REPO_ID,
        huggingfacehub_api_token=Config.HF_TOKEN,
        task="conversational",
        temperature=0.2,
        max_new_tokens=512
    )
    
    # 2. Get the Prompt Template (Augmentation)
    prompt = get_qa_prompt()
    
    # 3. Build the Parallel Chain to inject context and user question
    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    })
    
    # 4. Connect the full pipeline
    parser = StrOutputParser()
    main_chain = parallel_chain | prompt | llm | parser
    
    return main_chain